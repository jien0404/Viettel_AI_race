import os
import re
import pandas as pd
import torch
import chromadb
from sentence_transformers import SentenceTransformer
from sentence_transformers.cross_encoder import CrossEncoder
from datasets import Dataset, load_from_disk # (BỔ SUNG) Thêm load_from_disk
from tqdm import tqdm
from unsloth import FastLanguageModel
from transformers import TrainingArguments
from trl import SFTTrainer

# ==============================================================================
# --- 1. CẤU HÌNH CHO TOÀN BỘ PIPELINE HUẤN LUYỆN ---
# ==============================================================================

# --- Cấu hình đường dẫn ---
DB_PATH = "chroma_database"
QUESTIONS_PATH = "data/raw/input/question.csv"
ANSWERS_PATH = "data/raw/output/answer.md"
OUTPUT_MODEL_PATH = "models/qwen2-3b-rag-finetuned"
PROCESSED_DATA_PATH = "data/processed/rag_finetuning_dataset"

# Khai báo tên cho cả 2 collection
TEXT_COLLECTION_NAME = "text_chunks_collection"
IMAGE_COLLECTION_NAME = "image_chunks_collection"

# --- Cấu hình Model ---
BASE_MODEL_NAME = "unsloth/Qwen2.5-3B-Instruct-bnb-4bit" 
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
# (Phần này không có thay đổi, giữ nguyên như cũ)
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

class Retriever:
    """(Giữ nguyên không đổi)"""
    def __init__(self, db_path, text_collection_name, image_collection_name, embedding_model, reranker_model, image_embedding_model_name="clip-ViT-B-32"):
        print("--- Bước 2: Khởi tạo Retriever cho 2 collection ---")
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        
        db_client = chromadb.PersistentClient(path=db_path)
        self.text_collection = db_client.get_collection(name=text_collection_name)
        self.image_collection = db_client.get_collection(name=image_collection_name)
        print(f"Đã kết nối thành công tới collections: '{text_collection_name}' và '{image_collection_name}'")

        self.text_embedding_model = SentenceTransformer(embedding_model, device=self.device)
        self.image_embedding_model = SentenceTransformer(image_embedding_model_name, device=self.device)
        self.reranker_model = CrossEncoder(reranker_model, max_length=512, device=self.device)
        print("Retriever đã sẵn sàng.")

    def retrieve_context(self, question, n_results, top_n_rerank):
        q_emb_text = self.text_embedding_model.encode(question, convert_to_tensor=False).tolist()
        q_emb_image = self.image_embedding_model.encode(question, convert_to_tensor=False).tolist()
        
        text_results = self.text_collection.query(
            query_embeddings=[q_emb_text], n_results=n_results, include=["metadatas"]
        )
        image_results = self.image_collection.query(
            query_embeddings=[q_emb_image], n_results=n_results, include=["metadatas"]
        )
        
        all_retrieved_docs = text_results.get('metadatas', [[]])[0] + image_results.get('metadatas', [[]])[0]
        if not all_retrieved_docs:
            return ""

        pairs = []
        for doc in all_retrieved_docs:
            content_for_rerank = doc.get('text_context') or doc.get('original_content', '')
            pairs.append([question, content_for_rerank])

        scores = self.reranker_model.predict(pairs, show_progress_bar=False)
        doc_scores = sorted(zip(all_retrieved_docs, scores), key=lambda x: x[1], reverse=True)
        
        final_docs = [doc for doc, score in doc_scores[:top_n_rerank]]
        context_str = ""
        for i, metadata in enumerate(final_docs):
            content = metadata.get('text_context') or metadata.get('original_content', '')
            headings = metadata.get('context_headings', 'N/A')
            context_str += f"--- Ngữ cảnh tham khảo {i+1} (Context: {headings}) ---\nNội dung: {content}\n\n"
        return context_str.strip()


def create_training_prompt(context, question, options, golden_answer):
    """(Giữ nguyên không đổi)"""
    options_str = "\n".join([f"{key}: {value}" for key, value in options.items()])
    answer_letters = str(golden_answer).strip('"')
    prompt_template = f"""Bạn là một trợ lý QA tiếng Việt chuyên nghiệp, chuyên xử lý các câu hỏi trắc nghiệm **nhiều đáp án đúng**.  
Bạn sẽ chỉ sử dụng **chính xác** các thông tin trong phần NGỮ CẢNH được cung cấp, và **không được sử dụng kiến thức bên ngoài**.  

--- HƯỚNG DẪN TRẢ LỜI ---
1. Dựa vào ngữ cảnh, xác định **TẤT CẢ** các lựa chọn (A, B, C, D) mà bạn cho là đúng.
2. Đáp án của bạn **chỉ** là một chuỗi ký tự đại diện đáp án đúng, cách nhau bằng dấu phẩy, không có khoảng trắng. Ví dụ: `A,C` hoặc `B`.
3. **Không** kèm lời giải, lý do, hoặc bất kỳ văn bản nào khác.

--- VÍ DỤ ---

**VÍ DỤ 1: Trường hợp nhiều đáp án đúng**
NGỮ CẢNH: Sản phẩm mới hỗ trợ kết nối qua cả Wi-Fi và Bluetooth. Cổng USB-C dùng để sạc.
CÂU HỎI: Sản phẩm hỗ trợ những kết nối không dây nào?
CÁC LỰA CHỌN:
A: Wi-Fi
B: Cổng USB-C
C: Bluetooth
D: NFC
ĐÁP ÁN: A,C

**VÍ DỤ 2: Trường hợp nội dung lựa chọn chứa ký tự có thể gây nhiễu**
NGỮ CẢNH: Yêu cầu kỹ thuật cho bộ phận C là phải có chứng chỉ "A D M".
CÂU HỎI: Bộ phận nào cần chứng chỉ "A D M"?
CÁC LỰA CHỌN:
A: Bộ phận A
B: Bộ phận B
C: Bộ phận C
D: Bộ phận D
ĐÁP ÁN: C

--- KẾT THÚC VÍ DỤ ---

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

    # (SỬA ĐỔI) Logic kiểm tra, tải hoặc tạo mới dữ liệu đã xử lý
    if os.path.exists(PROCESSED_DATA_PATH):
        print(f"\n--- Bước 3: Tìm thấy dữ liệu đã xử lý tại '{PROCESSED_DATA_PATH}'. Đang tải từ cache... ---")
        dataset = load_from_disk(PROCESSED_DATA_PATH)
        print(f"Tải thành công {len(dataset)} mẫu dữ liệu từ cache.")
    else:
        print("\n--- Bước 3: Không tìm thấy cache. Đang xây dựng tập dữ liệu huấn luyện (Mô phỏng RAG) ---")
        
        # Chỉ khởi tạo Retriever khi cần xử lý dữ liệu
        retriever = Retriever(
            DB_PATH, 
            TEXT_COLLECTION_NAME, 
            IMAGE_COLLECTION_NAME, 
            EMBEDDING_MODEL_NAME, 
            RERANKER_MODEL_NAME
        )
        
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

        # (BỔ SUNG) Lưu dataset đã xử lý ra đĩa để sử dụng lại
        print(f"--- Đang lưu dataset đã xử lý vào '{PROCESSED_DATA_PATH}'... ---")
        os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True) # Đảm bảo thư mục tồn tại
        dataset.save_to_disk(PROCESSED_DATA_PATH)
        print("Lưu thành công!")


    # Chia dữ liệu thành tập huấn luyện và tập đánh giá (validation)
    split_dataset = dataset.train_test_split(test_size=0.1, seed=42)
    train_dataset = split_dataset['train']
    eval_dataset = split_dataset['test']
    print(f"Đã chia dữ liệu: {len(train_dataset)} mẫu huấn luyện, {len(eval_dataset)} mẫu đánh giá.")

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

    # (SỬA LỖI) Đơn giản hóa hàm định dạng để xử lý một ví dụ tại một thời điểm
    # và trả về một danh sách chứa chuỗi đã định dạng.
    def formatting_prompts_func(examples):
        texts = []
        for messages in examples["messages"]:
            # đảm bảo luôn là list
            if isinstance(messages, dict):
                messages = [messages]
            if not isinstance(messages, list):
                continue

            # chỉ lấy sample có "assistant"
            if not any(m["role"] == "assistant" for m in messages):
                continue

            try:
                rendered = tokenizer.apply_chat_template(
                    messages,
                    tokenize=False,
                    add_generation_prompt=False
                )
            except Exception as e:
                print("⚠️ Lỗi khi xử lý message:", e)
                continue

            if isinstance(rendered, str) and len(rendered.strip()) > 0:
                texts.append(rendered)

        # bảo vệ nếu batch trống
        if len(texts) == 0:
            texts = ["<no valid text>"]

        return texts


    print("\n--- Bước 5: Bắt đầu quá trình huấn luyện ---")
    trainer = SFTTrainer(
        model=model,
        tokenizer=tokenizer,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        # (SỬA LỖI) Sử dụng formatting_func thay vì dataset_format
        formatting_func=formatting_prompts_func, 
        max_seq_length=MAX_SEQ_LENGTH,
        packing=True,
        args=TrainingArguments(
            per_device_train_batch_size=PER_DEVICE_TRAIN_BATCH_SIZE,
            gradient_accumulation_steps=GRADIENT_ACCUMULATION_STEPS,
            warmup_steps=10,
            num_train_epochs=NUM_TRAIN_EPOCHS,
            learning_rate=LEARNING_RATE,
            fp16=not torch.cuda.is_bf16_supported(),
            bf16=torch.cuda.is_bf16_supported(),
            optim="adamw_8bit",
            weight_decay=0.01,
            seed=42,
            output_dir="outputs",
            eval_strategy="epoch",
            save_strategy="epoch",
            logging_strategy="epoch",
            save_total_limit=2,
            load_best_model_at_end=True,
            metric_for_best_model="loss",
            greater_is_better=False,
            max_grad_norm=0.3,
            lr_scheduler_type="cosine",
        ),
    )
    
    trainer_stats = trainer.train()
    
    print("\n--- KẾT QUẢ HUẤN LUYỆN ---")
    print(f"Training Loss cuối cùng: {trainer_stats.training_loss}")

    print(f"\n--- Bước 6: Huấn luyện hoàn tất. Đang lưu model tốt nhất vào '{OUTPUT_MODEL_PATH}' ---")
    model.save_pretrained(OUTPUT_MODEL_PATH)
    tokenizer.save_pretrained(OUTPUT_MODEL_PATH)
    print("Lưu model thành công!")

if __name__ == "__main__":
    main()