import os
import re
import pandas as pd
import torch
import chromadb
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer
from unsloth import FastLanguageModel
from typing import List, Dict, Any

# --- CẤU HÌNH ---
DB_PATH = "chroma_database"
COLLECTION_NAME = "document_chunks" # Tên collection mặc định, có thể cần thay đổi nếu bạn đặt tên khác ở bước 2
QUESTIONS_FILE_PATH = "question.csv"
OUTPUT_FILE_PATH = "submission/answer.md"

# Model dùng cho embedding câu hỏi (PHẢI GIỐNG model ở bước 2)
EMBEDDING_MODEL_NAME = 'bkai-foundation-models/vietnamese-bi-encoder'

# Model ngôn ngữ lớn để sinh câu trả lời (Qwen tối ưu bởi Unsloth)
LLM_MODEL_NAME = "unsloth/Qwen2.5-3B-Instruct-bnb-4bit"

# Số lượng context chunk sẽ truy xuất cho mỗi câu hỏi
NUM_RETRIEVED_CHUNKS = 5


def load_llm_model_and_tokenizer():
    """
    Tải mô hình ngôn ngữ lớn (LLM) và tokenizer đã được tối ưu hóa bằng Unsloth.
    """
    print(f"Đang tải mô hình LLM: {LLM_MODEL_NAME}...")
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=LLM_MODEL_NAME,
        max_seq_length=2048,
        dtype=None,  # Để Unsloth tự chọn dtype tốt nhất
        load_in_4bit=True,
    )
    print("Tải mô hình LLM hoàn tất.")
    return model, tokenizer


class RetrieverQA:
    def __init__(self, db_path, collection_name, embedding_model_name, llm_model, tokenizer):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print(f"Sử dụng thiết bị: {self.device}")

        # 1. Khởi tạo ChromaDB client
        print("Đang kết nối tới ChromaDB...")
        self.db_client = chromadb.PersistentClient(path=db_path)
        self.collection = self.db_client.get_collection(name=collection_name)
        print(f"Kết nối thành công tới collection '{collection_name}'.")

        # 2. Tải mô hình embedding
        print(f"Đang tải mô hình embedding: {embedding_model_name}...")
        self.embedding_model = SentenceTransformer(embedding_model_name, device=self.device)
        print("Tải mô hình embedding hoàn tất.")
        
        # 3. Lưu trữ mô hình LLM và tokenizer
        self.llm_model = llm_model
        self.tokenizer = tokenizer

    def retrieve_context(self, question: str, n_results: int) -> str:
        """
        Từ một câu hỏi, embedding nó và truy xuất các chunk ngữ cảnh liên quan nhất từ ChromaDB.
        """
        print(f"  - Đang truy xuất ngữ cảnh cho câu hỏi...")
        question_embedding = self.embedding_model.encode(question, convert_to_tensor=False).tolist()
        
        results = self.collection.query(
            query_embeddings=[question_embedding],
            n_results=n_results,
            include=["metadatas"]
        )
        
        context_str = ""
        for i, metadata in enumerate(results['metadatas'][0]):
            content = metadata.get('original_content', '')
            headings = metadata.get('context_headings', 'N/A')
            context_str += f"--- Ngữ cảnh tham khảo {i+1} ---\n"
            context_str += f"Tiêu đề liên quan: {headings}\n"
            context_str += f"Nội dung: {content}\n\n"
            
        return context_str.strip()

    def generate_answer(self, context: str, question: str, options: Dict[str, str]) -> str:
        """
        Tạo prompt, đưa vào mô hình LLM và sinh câu trả lời.
        """
        print("  - Đang sinh câu trả lời bằng LLM...")
        
        # Xây dựng phần lựa chọn trong prompt
        options_str = "\n".join([f"{key}: {value}" for key, value in options.items()])
        
        # Prompt được thiết kế cẩn thận để hướng dẫn model trả lời đúng định dạng
        prompt = f"""
Dựa vào các ngữ cảnh được cung cấp dưới đây, hãy trả lời câu hỏi trắc nghiệm sau.

--- NGỮ CẢNH ---
{context}
--- HẾT NGỮ CẢNH ---

--- CÂU HỎI VÀ LỰA CHỌN ---
Câu hỏi: {question}

Các lựa chọn:
{options_str}

Nhiệm vụ: Chỉ dựa vào ngữ cảnh đã cho, hãy xác định TẤT CẢ các lựa chọn (A, B, C, D) đúng cho câu hỏi trên.
Câu trả lời của bạn phải là một chuỗi chỉ chứa các ký tự đáp án đúng, được phân tách bằng dấu phẩy.
Ví dụ: nếu A và C đúng, trả lời là 'A,C'. Nếu chỉ có B đúng, trả lời là 'B'.

Đáp án:
"""
        
        # Sử dụng template chat của Qwen
        messages = [
            {"role": "system", "content": "Bạn là một trợ lý AI hữu ích, chuyên trả lời câu hỏi dựa trên văn bản được cung cấp."},
            {"role": "user", "content": prompt}
        ]
        
        input_ids = self.tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            return_tensors="pt"
        ).to(self.device)
        
        outputs = self.llm_model.generate(
            input_ids=input_ids, 
            max_new_tokens=50,
            pad_token_id=self.tokenizer.eos_token_id # Thêm pad_token_id để tránh warning
        )
        
        response = self.tokenizer.batch_decode(outputs[:, input_ids.shape[1]:], skip_special_tokens=True)[0]
        return response.strip()

    def process_question(self, question_row: pd.Series) -> str:
        """
        Thực hiện toàn bộ pipeline cho một câu hỏi: retrieve -> generate -> format.
        """
        question = question_row['Question']
        options = {
            'A': question_row['A'],
            'B': question_row['B'],
            'C': question_row['C'],
            'D': question_row['D']
        }
        
        # Bước 1: Truy xuất ngữ cảnh
        context = self.retrieve_context(question, n_results=NUM_RETRIEVED_CHUNKS)
        
        # Bước 2: Sinh câu trả lời thô từ LLM
        raw_answer = self.generate_answer(context, question, options)
        print(f"  - Phản hồi thô từ LLM: '{raw_answer}'")
        
        # Bước 3: Chuẩn hóa và định dạng output
        # Chỉ lấy các ký tự A, B, C, D từ câu trả lời của model
        valid_answers = sorted(list(set(re.findall(r'[A-D]', raw_answer.upper()))))
        
        num_correct = len(valid_answers)
        answers_str = ",".join(valid_answers)
        
        # Định dạng cuối cùng: 1,A hoặc 2,"A,B"
        if num_correct > 1:
            formatted_answer = f'{num_correct},"{answers_str}"'
        elif num_correct == 1:
            formatted_answer = f'1,{answers_str}'
        else:
            # Trường hợp model không tìm thấy đáp án nào
            formatted_answer = '0,""' 
            
        print(f"  - Kết quả cuối cùng: {formatted_answer}")
        return formatted_answer


def main():
    """
    Hàm chính điều khiển toàn bộ pipeline của bước 3.
    """
    print("================================================")
    print("===   BẮT ĐẦU PIPELINE BƯỚC 3: RETRIEVAL & QA   ===")
    print("================================================")
    
    # Tải các mô hình
    llm_model, tokenizer = load_llm_model_and_tokenizer()
    
    # Khởi tạo pipeline
    qa_pipeline = RetrieverQA(
        db_path=DB_PATH,
        collection_name=COLLECTION_NAME,
        embedding_model_name=EMBEDDING_MODEL_NAME,
        llm_model=llm_model,
        tokenizer=tokenizer
    )
    
    # Đọc file câu hỏi
    try:
        questions_df = pd.read_csv(QUESTIONS_FILE_PATH)
        print(f"Đã đọc thành công {len(questions_df)} câu hỏi từ '{QUESTIONS_FILE_PATH}'.")
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file câu hỏi tại '{QUESTIONS_FILE_PATH}'. Vui lòng kiểm tra lại.")
        return

    # Chuẩn bị file output
    # Tạo thư mục nếu chưa tồn tại
    os.makedirs(os.path.dirname(OUTPUT_FILE_PATH), exist_ok=True)
    # Ghi header nếu file chưa có hoặc trống
    if not os.path.exists(OUTPUT_FILE_PATH) or os.path.getsize(OUTPUT_FILE_PATH) == 0:
        with open(OUTPUT_FILE_PATH, 'w', encoding='utf-8') as f:
            f.write("### TASK QA\n")
            f.write("num_correct,answers\n")
        print(f"Đã tạo và ghi header cho file output tại '{OUTPUT_FILE_PATH}'.")

    # Mở file ở chế độ ghi tiếp (append)
    with open(OUTPUT_FILE_PATH, 'a', encoding='utf-8') as f:
        total_questions = len(questions_df)
        for index, row in questions_df.iterrows():
            print(f"\n--- Xử lý câu hỏi {index + 1}/{total_questions} ---")
            print(f"Câu hỏi: {row['Question']}")
            
            final_answer_line = qa_pipeline.process_question(row)
            
            # Ghi kết quả vào file
            f.write(final_answer_line + "\n")
            f.flush() # Đảm bảo dữ liệu được ghi ngay lập tức
            
    print("\n================================================")
    print("===   HOÀN TẤT TOÀN BỘ PIPELINE BƯỚC 3   ===")
    print(f"Kết quả đã được ghi vào file: '{OUTPUT_FILE_PATH}'")
    print("================================================")


if __name__ == '__main__':
    main()