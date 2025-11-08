# Còn 2 vấn đề là: thêm các ví dụ các đáp án là các chữ cái, chỉ dẫn trả lời cho đúng (check lại xem đã truyền đáp án vào đúng kiểu A: abc chưa)
#                 xử lý các trường hợp đầu vào của model bị quá max length, thêm cơ chế nếu vượt quá thì giảm dần số lượng context đến khi vừa

import os
import re
import pandas as pd
import torch
import chromadb
from sentence_transformers import SentenceTransformer
from sentence_transformers.cross_encoder import CrossEncoder
from transformers import AutoTokenizer
from unsloth import FastLanguageModel
from typing import List, Dict, Any

# --- CẤU HÌNH ---
DB_PATH = "chroma_database"
COLLECTION_NAME = "all_documents"
QUESTIONS_FILE_PATH = "data/raw/public_test_data/question.csv"
OUTPUT_FILE_PATH = "submission/answer2.md"

# Model dùng cho embedding câu hỏi (PHẢI GIỐNG model ở bước 2)
EMBEDDING_MODEL_NAME = 'bkai-foundation-models/vietnamese-bi-encoder'

# Model ngôn ngữ lớn để sinh câu trả lời (Qwen tối ưu bởi Unsloth)
# LLM_MODEL_NAME = "unsloth/Qwen2.5-3B-Instruct-bnb-4bit"
LLM_MODEL_NAME = "unsloth/Qwen3-4B-Instruct-2507"
RERANKER_MODEL_NAME = "thanhtantran/Vietnamese_Reranker"

# Số lượng context chunk sẽ truy xuất cho mỗi câu hỏi
NUM_RETRIEVED_CHUNKS = 50
TOP_N_AFTER_RERANK = 5 


def load_llm_model_and_tokenizer():
    """
    Tải mô hình ngôn ngữ lớn (LLM) và tokenizer đã được tối ưu hóa bằng Unsloth.
    """
    print(f"Đang tải mô hình LLM: {LLM_MODEL_NAME}...")
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=LLM_MODEL_NAME,
        max_seq_length= 16384,
        dtype=None, 
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
        
        # 3. (THÊM MỚI) Tải mô hình Reranker
        print(f"Đang tải mô hình Reranker: {RERANKER_MODEL_NAME}...")
        self.reranker_model = CrossEncoder(RERANKER_MODEL_NAME, max_length=512, device=self.device)
        print("Tải mô hình Reranker hoàn tất.")
        
        # 4. Lưu trữ mô hình LLM và tokenizer (Giữ nguyên, chỉ số thứ tự thay đổi)
        self.llm_model = llm_model
        self.tokenizer = tokenizer

    def retrieve_context(self, question: str, n_results: int, top_n_rerank: int) -> str:
        """
        Từ một câu hỏi, truy xuất ban đầu, sau đó rerank để lấy ngữ cảnh chính xác nhất.
        """
        # Bước 1: Truy xuất ban đầu để lấy ra một lượng lớn ứng viên (30 chunks)
        print(f"  - Đang truy xuất {n_results} ngữ cảnh ứng viên...")
        question_embedding = self.embedding_model.encode(question, convert_to_tensor=False).tolist()
        
        results = self.collection.query(
            query_embeddings=[question_embedding],
            n_results=n_results,
            include=["metadatas"]
        )
        
        retrieved_docs = results['metadatas'][0]
        if not retrieved_docs:
            print("  - Không tìm thấy ngữ cảnh nào.")
            return ""

        # Bước 2: Chuẩn bị các cặp [câu hỏi, nội dung chunk] cho reranker
        pairs = []
        for doc in retrieved_docs:
            content = doc.get('original_content', '')
            pairs.append([question, content])

        # Bước 3: Dùng Reranker để chấm điểm các cặp
        print(f"  - Đang Rerank {len(pairs)} ứng viên để chọn ra top {top_n_rerank}...")
        scores = self.reranker_model.predict(pairs, show_progress_bar=False)

        # Bước 4: Kết hợp document với điểm số, sắp xếp và lấy ra top N tốt nhất
        doc_scores = list(zip(retrieved_docs, scores))
        doc_scores.sort(key=lambda x: x[1], reverse=True) # Sắp xếp điểm từ cao đến thấp
        
        final_docs = [doc for doc, score in doc_scores[:top_n_rerank]]

        # Bước 5: Tạo chuỗi ngữ cảnh từ các document đã được rerank
        context_str = ""
        for i, metadata in enumerate(final_docs):
            content = metadata.get('original_content', '')
            headings = metadata.get('context_headings', 'N/A')
            context_str += f"--- Ngữ cảnh tham khảo {i+1} ---\n"
            context_str += f"Tiêu đề liên quan: {headings}\n"
            context_str += f"Nội dung: {content}\n\n"
            
        return context_str.strip()

    def generate_answer(self, context: str, question: str, options: Dict[str, str]) -> str:
        """
        Tạo prompt chi tiết (có hướng dẫn và few-shot), đưa vào mô hình LLM và sinh câu trả lời.
        (Phiên bản cải tiến với thẻ [ANSWER])
        """
        print("  - Đang sinh câu trả lời bằng LLM (với prompt nâng cao)...")
        
        # Xây dựng phần lựa chọn trong prompt
        options_str = "\n".join([f"{key}: {value}" for key, value in options.items()])
        
        # --- PROMPT MỚI VỚI HƯỚNG DẪN CHI TIẾT VÀ THẺ ĐÁP ÁN ---
        prompt = f"""
Bạn là một **trợ lý QA tiếng Việt chuyên nghiệp**, được huấn luyện đặc biệt để xử lý **câu hỏi trắc nghiệm nhiều đáp án đúng**.

QUY TẮC BẮT BUỘC:
0. Câu trả lời cuối cùng **BẮT BUỘC** phải được đặt trong cặp thẻ `[ANSWER]` và `[/ANSWER]`. **Đây là quy tắc quan trọng nhất.**
1. Bạn **chỉ** được sử dụng thông tin trong phần NGỮ CẢNH bên dưới.
2. **Tuyệt đối** không được liệt kê lại danh sách các đáp án được cung cấp, câu trả lời chỉ được phép nhắc đến đáp án mà bạn chọn.
3. Đáp án **chỉ** là chuỗi ký tự gồm các lựa chọn đúng, viết hoa, phân tách bằng dấu phẩy **(không có khoảng trắng)**.
   - Ví dụ: `A` hoặc `A,C,D`
4. **Tuyệt đối không** viết thêm lời giải thích, nhận xét, hay ký tự ngoài đáp án.
5. Nếu không có bất kì thông tin nào từ ngữ cảnh thì vẫn phải chọn (các) đáp án nào mà bạn cho là đúng, không cần giải thích thêm.

--- VÍ DỤ ---

**VÍ DỤ 1: Trường hợp chỉ có 1 đáp án đúng**
NGỮ CẢNH: Công thức hóa học của nước là H2O
CÂU HỎI: Các nguyên tố hóa học nào tạo nên phân tử nước?
CÁC LỰA CHỌN:
A: A, H
B: H, O
C: A, O
D: H, 2
ĐÁP ÁN: [ANSWER]B[/ANSWER]

**VÍ DỤ 2: Trường hợp nhiều đáp án đúng**
NGỮ CẢNH: Sản phẩm mới hỗ trợ kết nối qua cả Wi-Fi và Bluetooth. Cổng USB-C dùng để sạc.
CÂU HỎI: Sản phẩm hỗ trợ những kết nối không dây nào?
CÁC LỰA CHỌN:
A: Wi-Fi
B: Cổng USB-C
C: Bluetooth
D: NFC
ĐÁP ÁN: [ANSWER]A,C[/ANSWER]

**VÍ DỤ 3: Trường hợp nội dung lựa chọn chứa ký tự có thể gây nhiễu**
NGỮ CẢNH: Yêu cầu kỹ thuật cho bộ phận C là phải có chứng chỉ "A D M".
CÂU HỎI: Bộ phận nào cần chứng chỉ "A D M"?
CÁC LỰA CHỌN:
A: Bộ phận C
B: Bộ phận D
C: Bộ phận A
D: Bộ phận B
ĐÁP ÁN: [ANSWER]A[/ANSWER]

--- KẾT THÚC VÍ DỤ ---

--- BẮT ĐẦU NHIỆM VỤ ---
NGỮ CẢNH:
{context}

CÂU HỎI: {question}

CÁC LỰA CHỌN:
{options_str}

ĐÁP ÁN:"""
        
        # Sử dụng template chat của Qwen
        messages = [
            {"role": "user", "content": prompt}
        ]
        
        input_ids = self.tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            return_tensors="pt"
        ).to(self.device)
        
        outputs = self.llm_model.generate(
            input_ids=input_ids, 
            max_new_tokens=2048, # Chỉ cần token cho đáp án (A,B,C,D) nên không cần nhiều
            pad_token_id=self.tokenizer.eos_token_id
        )
        
        response = self.tokenizer.batch_decode(outputs[:, input_ids.shape[1]:], skip_special_tokens=True)[0]
        return response.strip()

    def process_question(self, question_row: pd.Series) -> str:
        """
        Thực hiện toàn bộ pipeline cho một câu hỏi: retrieve -> generate -> format.
        (Phiên bản cải tiến với logic trích xuất thông minh)
        """
        question = question_row['Question']
        options = {
            'A': question_row['A'],
            'B': question_row['B'],
            'C': question_row['C'],
            'D': question_row['D']
        }
        
        # Bước 1: Truy xuất và Rerank ngữ cảnh
        context = self.retrieve_context(
            question, 
            n_results=NUM_RETRIEVED_CHUNKS,
            top_n_rerank=TOP_N_AFTER_RERANK
        )
        
        # Bước 2: Sinh câu trả lời thô từ LLM
        raw_answer = self.generate_answer(context, question, options)
        print(f"  - Phản hồi thô từ LLM: '{raw_answer}'")
        
        # --- LOGIC XỬ LÝ CÂU TRẢ LỜI MỚI ---
        answer_content = ""
        # Bước 3.1: Ưu tiên tìm kiếm câu trả lời trong thẻ [ANSWER]
        # re.DOTALL cho phép '.' khớp với cả ký tự xuống dòng
        match = re.search(r'\[ANSWER\](.*?)\[/ANSWER\]', raw_answer, re.DOTALL)
        
        if match:
            # Nếu tìm thấy, chỉ lấy nội dung bên trong thẻ
            answer_content = match.group(1).strip()
            print(f"  - Đã tìm thấy thẻ [ANSWER]. Nội dung: '{answer_content}'")
        else:
            # Bước 3.2: Nếu không có thẻ, sử dụng toàn bộ phản hồi (phương án dự phòng)
            # Đồng thời cảnh báo để chúng ta biết LLM không tuân thủ
            print("  - Cảnh báo: Không tìm thấy thẻ [ANSWER]. Sử dụng toàn bộ phản hồi để phân tích.")
            answer_content = raw_answer

        # Bước 3.3: Trích xuất các ký tự A, B, C, D hợp lệ từ nội dung đã được xác định
        # Regex này đơn giản hơn vì ta đã thu hẹp phạm vi tìm kiếm.
        # Nó tìm tất cả các ký tự A, B, C, D (không phân biệt hoa thường)
        found_answers = re.findall(r'[A-D]', answer_content.upper())

        # Bước 4: Chuẩn hóa kết quả đã trích xuất
        # Đưa tất cả về chữ hoa, loại bỏ các đáp án trùng lặp và sắp xếp lại.
        valid_answers = sorted(list(set(found_answers)))
        
        # Bước 5: Định dạng output cuối cùng theo yêu cầu
        num_correct = len(valid_answers)
        answers_str = ",".join(valid_answers)
        
        if num_correct > 1:
            formatted_answer = f'{num_correct},"{answers_str}"'
        elif num_correct == 1:
            formatted_answer = f'1,{answers_str}'
        else:
            # Trường hợp không trích xuất được đáp án nào
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