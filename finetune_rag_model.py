import os
import re
import pandas as pd
import torch
import chromadb
from sentence_transformers import SentenceTransformer
from sentence_transformers.cross_encoder import CrossEncoder
from datasets import Dataset
from tqdm import tqdm
from unsloth import FastLanguageModel
from transformers import TrainingArguments
from trl import SFTTrainer

# ==============================================================================
# --- 1. CẤU HÌNH CHO TOÀN BỘ PIPELINE HUẤN LUYỆN ---
# ==============================================================================

# --- Cấu hình đường dẫn ---
DB_PATH = "all_documents_train"
QUESTIONS_PATH = "data/raw/input/question.csv"
ANSWERS_PATH = "data/raw/output/answer.md"
OUTPUT_MODEL_PATH = "models/qwen2-3b-rag-finetuned"

# (SỬA ĐỔI) Khai báo tên cho cả 2 collection
TEXT_COLLECTION_NAME = "text_chunks_collection"
IMAGE_COLLECTION_NAME = "image_chunks_collection"

# --- Cấu hình Model ---
BASE_MODEL_NAME = "unsloth/Qwen2-3B-Instruct-bnb-4bit" 
EMBEDDING_MODEL_NAME = 'bkai-foundation-models/vietnamese-bi-encoder' 
RERANKER_MODEL_NAME = "thanhtantran/Vietnamese_Reranker"

# --- Cấu hình Retrieval ---
NUM_RETRIEVED_CHUNKS = 50 
TOP_N_AFTER_RERANK = 3    

# --- Cấu hình Huấn luyện (Hyperparameters) ---
LORA_R = 16
LORA_ALPHA = 32
LORA_DROPOUT = 0.05
LEARNING_RATE = 5e-5
NUM_TRAIN_EPOCHS = 3
PER_DEVICE_TRAIN_BATCH_SIZE = 2
GRADIENT_ACCUMULATION_STEPS = 4
MAX_SEQ_LENGTH = 4096


# ==============================================================================
# --- 2. CÁC LỚP VÀ HÀM TIỆN ÍCH ---
# ==============================================================================

def load_and_prepare_data(questions_path, answers_path):
    """(Giữ nguyên không đổi)"""
    print("--- Bước 1: Đang tải và chuẩn bị dữ liệu câu hỏi-trả lời ---")
    try:
        df_questions = pd.read_csv(questions_path)
        with open(answers_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        start_index = -1
        for i, line in enumerate(lines):
            if "### TASK QA" in line:
                start_index = i + 2
                break
        
        if start_index == -1:
            raise ValueError("Không tìm thấy '### TASK QA' trong file answer.md")

        df_answers = pd.read_csv(pd.io.common.StringIO(''.join(lines[start_index:])), header=None, names=['num_correct', 'answers'])
        
        if len(df_questions) != len(df_answers):
            raise ValueError(f"Số lượng câu hỏi ({len(df_questions)}) và câu trả lời ({len(df_answers)}) không khớp!")

        df_full = pd.concat([df_questions, df_answers], axis=1)
        print(f"Tải thành công {len(df_full)} cặp câu hỏi-trả lời.")
        return df_full
    except Exception as e:
        print(f"Lỗi nghiêm trọng khi tải dữ liệu: {e}")
        return None

# (SỬA ĐỔI) Toàn bộ lớp Retriever đã được nâng cấp
class Retriever:
    """Lớp chuyên trách việc truy xuất và rerank ngữ cảnh từ 2 collection (text và image)."""
    def __init__(self, db_path, text_collection_name, image_collection_name, embedding_model, reranker_model):
        print("--- Bước 2: Khởi tạo Retriever cho 2 collection ---")
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        
        # Kết nối DB và lấy cả 2 collection
        db_client = chromadb.PersistentClient(path=db_path)
        self.text_collection = db_client.get_collection(name=text_collection_name)
        self.image_collection = db_client.get_collection(name=image_collection_name)
        print(f"Đã kết nối thành công tới collections: '{text_collection_name}' và '{image_collection_name}'")

        # Tải models (dùng chung cho cả 2)
        self.embedding_model = SentenceTransformer(embedding_model, device=self.device)
        self.reranker_model = CrossEncoder(reranker_model, max_length=512, device=self.device)
        print("Retriever đã sẵn sàng.")

    def retrieve_context(self, question, n_results, top_n_rerank):
        """Thực hiện truy xuất từ cả 2 collection, gộp lại và rerank để lấy ngữ cảnh tốt nhất."""
        question_embedding = self.embedding_model.encode(question, convert_to_tensor=False).tolist()
        
        # 1. Truy xuất song song từ cả hai collection
        text_results = self.text_collection.query(
            query_embeddings=[question_embedding], n_results=n_results, include=["metadatas"]
        )
        image_results = self.image_collection.query(
            query_embeddings=[question_embedding], n_results=n_results, include=["metadatas"]
        )
        
        # 2. Gộp kết quả từ cả hai nguồn
        all_retrieved_docs = text_results['metadatas'][0] + image_results['metadatas'][0]
        if not all_retrieved_docs: 
            return ""

        # 3. Rerank trên tập hợp ứng viên đã gộp
        # Với ảnh, dùng 'text_context'. Với text, dùng 'original_content' để rerank.
        pairs = []
        for doc in all_retrieved_docs:
            content_for_rerank = doc.get('text_context') or doc.get('original_content', '')
            pairs.append([question, content_for_rerank])

        scores = self.reranker_model.predict(pairs, show_progress_bar=False)
        doc_scores = sorted(zip(all_retrieved_docs, scores), key=lambda x: x[1], reverse=True)
        
        # 4. Tạo chuỗi ngữ cảnh từ các kết quả tốt nhất sau khi rerank
        final_docs = [doc for doc, score in doc_scores[:top_n_rerank]]
        context_str = ""
        for i, metadata in enumerate(final_docs):
            # Với ảnh, hiển thị text context. Với text, hiển thị nội dung gốc.
            content = metadata.get('text_context') or metadata.get('original_content', '')
            headings = metadata.get('context_headings', 'N/A')
            context_str += f"--- Ngữ cảnh tham khảo {i+1} (Context: {headings}) ---\nNội dung: {content}\n\n"
        return context_str.strip()


def create_training_prompt(context, question, options, golden_answer):
    """(Giữ nguyên không đổi)"""
    options_str = "\n".join([f"{key}: {value}" for key, value in options.items()])
    answer_letters = str(golden_answer).strip('"')
    prompt_template = f"""Bạn là một trợ lý QA tiếng Việt chuyên nghiệp... (dán prompt few-shot dài của bạn vào đây)
--- BẮT ĐẦU NHIỆM VỤ ---
NGỮ CẢNH:
{context}

CÂU HỎI: {question}

CÁC LỰA CHỌN:
{options_str}

ĐÁP ÁN:"""
    messages = [
        {"role": "user", "content": prompt_template},
        {"role": "assistant", "content": answer_letters}
    ]
    return messages

# ==============================================================================
# --- 3. HÀM CHÍNH ĐIỀU KHIỂN PIPELINE HUẤN LUYỆN ---
# ==============================================================================

def main():
    training_data = load_and_prepare_data(QUESTIONS_PATH, ANSWERS_PATH)
    if training_data is None: return

    # (SỬA ĐỔI) Khởi tạo Retriever với cả 2 tên collection
    retriever = Retriever(
        DB_PATH, 
        TEXT_COLLECTION_NAME, 
        IMAGE_COLLECTION_NAME, 
        EMBEDDING_MODEL_NAME, 
        RERANKER_MODEL_NAME
    )
    
    # --- Các bước còn lại (3, 4, 5, 6) giữ nguyên hoàn toàn ---
    print("\n--- Bước 3: Đang xây dựng tập dữ liệu huấn luyện (Mô phỏng RAG) ---")
    formatted_training_data = []
    for _, row in tqdm(training_data.iterrows(), total=len(training_data), desc="Processing data"):
        question = row['Question']
        options = {'A': row['A'], 'B': row['B'], 'C': row['C'], 'D': row['D']}
        golden_answer = row['answers']
        
        context = retriever.retrieve_context(question, NUM_RETRIEVED_CHUNKS, TOP_N_AFTER_RERANK)
        
        formatted_prompt = create_training_prompt(context, question, options, golden_answer)
        formatted_training_data.append(formatted_prompt)

    dataset = Dataset.from_list([{"messages": data} for data in formatted_training_data])
    print(f"Đã tạo thành công {len(dataset)} mẫu dữ liệu huấn luyện.")

    print(f"\n--- Bước 4: Đang tải model cơ sở: {BASE_MODEL_NAME} ---")
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=BASE_MODEL_NAME, max_seq_length=MAX_SEQ_LENGTH, dtype=None, load_in_4bit=True
    )
    
    model = FastLanguageModel.get_peft_model(
        model, r=LORA_R, lora_alpha=LORA_ALPHA, lora_dropout=LORA_DROPOUT, bias="none",
        use_gradient_checkpointing="unsloth", random_state=42,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    )
    print("Tải model và cấu hình LoRA thành công.")

    print("\n--- Bước 5: Bắt đầu quá trình huấn luyện ---")
    trainer = SFTTrainer(
        model=model, tokenizer=tokenizer, train_dataset=dataset, dataset_format="chatml",
        max_seq_length=MAX_SEQ_LENGTH, packing=True,
        args=TrainingArguments(
            per_device_train_batch_size=PER_DEVICE_TRAIN_BATCH_SIZE,
            gradient_accumulation_steps=GRADIENT_ACCUMULATION_STEPS,
            warmup_steps=10, num_train_epochs=NUM_TRAIN_EPOCHS, learning_rate=LEARNING_RATE,
            fp16=not torch.cuda.is_bf16_supported(), bf16=torch.cuda.is_bf16_supported(),
            logging_steps=1, optim="adamw_8bit", weight_decay=0.01, lr_scheduler_type="linear",
            seed=42, output_dir="outputs",
        ),
    )
    trainer.train()

    print(f"\n--- Bước 6: Huấn luyện hoàn tất. Đang lưu model vào '{OUTPUT_MODEL_PATH}' ---")
    model.save_pretrained(OUTPUT_MODEL_PATH)
    tokenizer.save_pretrained(OUTPUT_MODEL_PATH)
    print("Lưu model thành công!")

if __name__ == "__main__":
    main()