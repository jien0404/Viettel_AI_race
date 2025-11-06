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
DB_PATH = "all_documents_training"
QUESTIONS_PATH = "data/raw/input/question.csv"
ANSWERS_PATH = "data/raw/output/answer.md"
OUTPUT_MODEL_PATH = "models/qwen2-3b-rag-finetuned" # Thư mục lưu model đã fine-tune

# --- Cấu hình Model ---
BASE_MODEL_NAME = "unsloth/Qwen2-3B-Instruct-bnb-4bit"
EMBEDDING_MODEL_NAME = 'bkai-foundation-models/vietnamese-bi-encoder' 
RERANKER_MODEL_NAME = "thanhtantran/Vietnamese_Reranker"

# --- Cấu hình Retrieval ---
NUM_RETRIEVED_CHUNKS = 50 # Số lượng ứng viên lấy ra ban đầu
TOP_N_AFTER_RERANK = 3    # Số lượng ngữ cảnh tốt nhất giữ lại để đưa vào prompt

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
    """Đọc câu hỏi từ CSV và câu trả lời từ Markdown, sau đó gộp chúng lại."""
    print("--- Bước 1: Đang tải và chuẩn bị dữ liệu câu hỏi-trả lời ---")
    try:
        # Đọc câu hỏi
        df_questions = pd.read_csv(questions_path)

        # Đọc và xử lý file câu trả lời
        with open(answers_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Tìm dòng bắt đầu của dữ liệu
        start_index = -1
        for i, line in enumerate(lines):
            if "### TASK QA" in line:
                start_index = i + 2 # Bỏ qua header 'num_correct,answers'
                break
        
        if start_index == -1:
            raise ValueError("Không tìm thấy '### TASK QA' trong file answer.md")

        # Đọc dữ liệu câu trả lời bằng pandas
        df_answers = pd.read_csv(pd.io.common.StringIO(''.join(lines[start_index:])), header=None)
        df_answers.columns = ['num_correct', 'answers']
        
        # Gộp câu hỏi và câu trả lời
        if len(df_questions) != len(df_answers):
            raise ValueError(f"Số lượng câu hỏi ({len(df_questions)}) và câu trả lời ({len(df_answers)}) không khớp!")

        df_full = pd.concat([df_questions, df_answers], axis=1)
        print(f"Tải thành công {len(df_full)} cặp câu hỏi-trả lời.")
        return df_full

    except Exception as e:
        print(f"Lỗi nghiêm trọng khi tải dữ liệu: {e}")
        return None


class Retriever:
    """Lớp chuyên trách việc truy xuất và rerank ngữ cảnh từ ChromaDB."""
    def __init__(self, db_path, collection_name, embedding_model, reranker_model):
        print("--- Bước 2: Khởi tạo Retriever ---")
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        
        # Kết nối DB
        self.collection = chromadb.PersistentClient(path=db_path).get_collection(name=collection_name)
        
        # Tải models
        self.embedding_model = SentenceTransformer(embedding_model, device=self.device)
        self.reranker_model = CrossEncoder(reranker_model, max_length=512, device=self.device)
        print("Retriever đã sẵn sàng.")

    def retrieve_context(self, question, n_results, top_n_rerank):
        """Thực hiện truy xuất và rerank để lấy ngữ cảnh tốt nhất."""
        # 1. Truy xuất ban đầu
        question_embedding = self.embedding_model.encode(question, convert_to_tensor=False).tolist()
        results = self.collection.query(
            query_embeddings=[question_embedding], n_results=n_results, include=["metadatas"]
        )
        retrieved_docs = results['metadatas'][0]
        if not retrieved_docs: return ""

        # 2. Rerank
        pairs = [[question, doc.get('original_content', '')] for doc in retrieved_docs]
        scores = self.reranker_model.predict(pairs, show_progress_bar=False)
        doc_scores = sorted(zip(retrieved_docs, scores), key=lambda x: x[1], reverse=True)
        
        # 3. Tạo chuỗi ngữ cảnh
        final_docs = [doc for doc, score in doc_scores[:top_n_rerank]]
        context_str = ""
        for i, metadata in enumerate(final_docs):
            content = metadata.get('original_content', '')
            headings = metadata.get('context_headings', 'N/A')
            context_str += f"--- Ngữ cảnh tham khảo {i+1} ---\nNội dung: {content}\n\n"
        return context_str.strip()


def create_training_prompt(context, question, options, golden_answer):
    """Tạo prompt hoàn chỉnh cho việc huấn luyện, theo định dạng few-shot."""
    options_str = "\n".join([f"{key}: {value}" for key, value in options.items()])
    
    # Lấy phần đáp án chữ cái từ chuỗi "num_correct,answers"
    # Ví dụ: '2,"A,C"' -> 'A,C'
    answer_letters = str(golden_answer).strip('"')

    prompt_template = f"""Bạn là một trợ lý QA tiếng Việt... (prompt few-shot dài của bạn ở đây) ...
--- BẮT ĐẦU NHIỆM VỤ ---
NGỮ CẢNH:
{context}

CÂU HỎI: {question}

CÁC LỰA CHỌN:
{options_str}

ĐÁP ÁN:"""
    
    # Đối với SFTTrainer, chúng ta cần định dạng theo template chat của model
    # và nối câu trả lời vào cuối cùng.
    messages = [
        {"role": "user", "content": prompt_template},
        {"role": "assistant", "content": answer_letters}
    ]
    return messages

# ==============================================================================
# --- 3. HÀM CHÍNH ĐIỀU KHIỂN PIPELINE HUẤN LUYỆN ---
# ==============================================================================

def main():
    # Bước 1: Tải và gộp dữ liệu
    training_data = load_and_prepare_data(QUESTIONS_PATH, ANSWERS_PATH)
    if training_data is None:
        return

    # Bước 2: Khởi tạo Retriever
    # Lưu ý: ChromaDB thường tự đặt tên collection là 'chroma-collection' nếu không chỉ định.
    # Hãy kiểm tra tên collection bằng script check_collections.py nếu gặp lỗi.
    retriever = Retriever(DB_PATH, 'document_chunks', EMBEDDING_MODEL_NAME, RERANKER_MODEL_NAME)
    
    # Bước 3: Xây dựng tập dữ liệu huấn luyện bằng cách mô phỏng RAG
    print("\n--- Bước 3: Đang xây dựng tập dữ liệu huấn luyện (Mô phỏng RAG) ---")
    formatted_training_data = []
    for _, row in tqdm(training_data.iterrows(), total=len(training_data), desc="Processing data"):
        question = row['Question']
        options = {'A': row['A'], 'B': row['B'], 'C': row['C'], 'D': row['D']}
        golden_answer = row['answers']
        
        # Lấy ngữ cảnh y như khi inference
        context = retriever.retrieve_context(question, NUM_RETRIEVED_CHUNKS, TOP_N_AFTER_RERANK)
        
        # Tạo prompt hoàn chỉnh
        formatted_prompt = create_training_prompt(context, question, options, golden_answer)
        formatted_training_data.append(formatted_prompt)

    # Chuyển đổi sang định dạng Dataset của Hugging Face
    dataset = Dataset.from_list([{"messages": data} for data in formatted_training_data])
    print(f"Đã tạo thành công {len(dataset)} mẫu dữ liệu huấn luyện.")

    # Bước 4: Tải model và tokenizer
    print(f"\n--- Bước 4: Đang tải model cơ sở: {BASE_MODEL_NAME} ---")
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=BASE_MODEL_NAME,
        max_seq_length=MAX_SEQ_LENGTH,
        dtype=None,
        load_in_4bit=True,
    )
    
    # Kích hoạt PEFT/LoRA
    model = FastLanguageModel.get_peft_model(
        model,
        r=LORA_R,
        lora_alpha=LORA_ALPHA,
        lora_dropout=LORA_DROPOUT,
        bias="none",
        use_gradient_checkpointing="unsloth",
        random_state=42,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    )
    print("Tải model và cấu hình LoRA thành công.")

    # Bước 5: Huấn luyện model
    print("\n--- Bước 5: Bắt đầu quá trình huấn luyện ---")
    trainer = SFTTrainer(
        model=model,
        tokenizer=tokenizer,
        train_dataset=dataset,
        dataset_format="chatml", # Sử dụng định dạng chat cho cột "messages"
        max_seq_length=MAX_SEQ_LENGTH,
        packing=True, # Đóng gói các mẫu ngắn lại để tăng hiệu quả
        args=TrainingArguments(
            per_device_train_batch_size=PER_DEVICE_TRAIN_BATCH_SIZE,
            gradient_accumulation_steps=GRADIENT_ACCUMULATION_STEPS,
            warmup_steps=10,
            num_train_epochs=NUM_TRAIN_EPOCHS,
            learning_rate=LEARNING_RATE,
            fp16=not torch.cuda.is_bf16_supported(),
            bf16=torch.cuda.is_bf16_supported(),
            logging_steps=1,
            optim="adamw_8bit",
            weight_decay=0.01,
            lr_scheduler_type="linear",
            seed=42,
            output_dir="outputs",
        ),
    )
    trainer.train()

    # Bước 6: Lưu model
    print(f"\n--- Bước 6: Huấn luyện hoàn tất. Đang lưu model vào '{OUTPUT_MODEL_PATH}' ---")
    model.save_pretrained(OUTPUT_MODEL_PATH)
    tokenizer.save_pretrained(OUTPUT_MODEL_PATH)
    print("Lưu model thành công!")

if __name__ == "__main__":
    main()