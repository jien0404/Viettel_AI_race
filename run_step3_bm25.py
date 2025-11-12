import os
import re
import pandas as pd
import torch
import sqlite3
import json
import base64
import numpy as np
from PIL import Image
from rank_bm25 import BM25Okapi
from unsloth import FastLanguageModel
from transformers import AutoProcessor
from typing import List, Dict, Any
import subprocess

def get_free_gpu():
    """
    Tìm và trả về ID của GPU có nhiều bộ nhớ trống nhất.
    Sử dụng nvidia-smi để truy vấn.
    """
    try:
        # Lệnh nvidia-smi để lấy index và bộ nhớ trống, định dạng csv, không có header và đơn vị
        command = "nvidia-smi --query-gpu=index,memory.free --format=csv,noheader,nounits"
        
        # Thực thi lệnh và lấy output
        output = subprocess.check_output(command, shell=True, text=True)
        
        # Xử lý output
        gpus = []
        for line in output.strip().split('\n'):
            index, memory_free = line.split(', ')
            gpus.append((int(index), int(memory_free)))
        
        # Sắp xếp các GPU theo bộ nhớ trống giảm dần và chọn GPU đầu tiên
        if not gpus:
            print("Cảnh báo: Không tìm thấy GPU nào. Sẽ sử dụng CPU hoặc cài đặt mặc định.")
            return "auto" # Fallback về "auto"
            
        best_gpu_index = max(gpus, key=lambda item: item[1])[0]
        best_device = f"cuda:{best_gpu_index}"
        print(f"Đã tìm thấy {len(gpus)} GPUs. GPU có nhiều bộ nhớ trống nhất là: {best_device} ({max(gpus, key=lambda item: item[1])[1]} MiB).")
        return best_device

    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Cảnh báo: Không thể chạy `nvidia-smi`. Sẽ sử dụng cài đặt mặc định 'auto'.")
        return "auto" # Fallback nếu nvidia-smi không hoạt động
    
# --- CẤU HÌNH ---
DB_FILE_PATH = "bm25_database_private.sqlite"
QUESTIONS_FILE_PATH = "data/raw/private_test_data/input/question.csv"
SUBMISSION_DIR = "private_submission"
OUTPUT_FILE_PATH = "private_submission/answer.md"

VLM_MODEL_NAME = "unsloth/Qwen3-VL-4B-Instruct-unsloth-bnb-4bit"
TOP_K_BM25 = 3

def load_vlm_model_and_processor(device: str): # Unsloth tự xử lý device, nên tham số này không còn cần thiết
    """
    Tải mô hình VLM đã được tối ưu bằng Unsloth và processor của nó.
    """
    print(f"Đang tải mô hình VLM với Unsloth: {VLM_MODEL_NAME}...")
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=VLM_MODEL_NAME,
        max_seq_length=16384, 
        dtype=None, 
        load_in_4bit=True,
    )
    
    # Processor vẫn tải từ model gốc của Qwen
    processor = AutoProcessor.from_pretrained("Qwen/Qwen3-VL-4B-Instruct")

    # Cấu hình padding cho tokenizer (quan trọng cho batching)
    tokenizer.padding_side = "left"
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
            
    print("Tải mô hình VLM hoàn tất.")
    # Trả về cả tokenizer để sử dụng
    return model, tokenizer, processor

def encode_image_to_base64_uri(image_path):
    try:
        with open(image_path, "rb") as image_file:
            base64_data = base64.b64encode(image_file.read()).decode('utf-8')
            return f"data:image/jpeg;base64,{base64_data}"
    except Exception as e:
        print(f"  - Lỗi khi encode ảnh {image_path}: {e}")
        return None

class BM25_VLM_QA:
    def __init__(self, db_path, vlm_model, tokenizer, processor):
        self.device = vlm_model.device
        print(f"Sử dụng thiết bị: {self.device}")

        self.vlm_model = vlm_model
        self.tokenizer = tokenizer # Thêm tokenizer
        self.processor = processor

        print("Đang kết nối tới SQLite và tải corpus cho BM25...")
        self.corpus = self._load_corpus_from_sqlite(db_path)
        if not self.corpus:
            raise ValueError("Không thể tải corpus từ database.")
        
        print("Đang xây dựng chỉ mục BM25...")
        # --- SỬA DÒNG NÀY ---
        tokenized_corpus = [
            (
                doc['metadata'].get('doc_name', '') + " " + 
                doc.get('searchable_original_content', '') + " " + 
                doc['enriched_content']
            ).split() for doc in self.corpus
        ]
        # --- KẾT THÚC SỬA ---
        self.bm25 = BM25Okapi(tokenized_corpus)
        print("Xây dựng chỉ mục BM25 hoàn tất.")

    def _load_corpus_from_sqlite(self, db_path: str) -> List[Dict[str, Any]]:
        """
        Đọc toàn bộ các chunk từ file SQLite, lấy tất cả các cột cần thiết
        và trích xuất cả original_blocks.
        """
        corpus_data = []
        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT doc_name, chunk_type, enriched_content, metadata FROM chunks")
                for row in cursor.fetchall():
                    doc_name, chunk_type, enriched_content, metadata_str = row
                    metadata = json.loads(metadata_str)
                    
                    metadata['doc_name'] = doc_name
                    metadata['chunk_type'] = chunk_type
                    
                    # === SỬA ĐỔI Ở ĐÂY ===
                    # Trích xuất original_blocks từ metadata
                    original_blocks = metadata.get('original_blocks', [])
                    
                    searchable_original_content = ""
                    for block in original_blocks:
                        block_type = block.get('type')
                        if block_type == 'paragraph':
                            searchable_original_content += block.get('content', '') + " "

                    # Thêm original_blocks vào cấp cao nhất của dictionary
                    corpus_data.append({
                        'enriched_content': enriched_content,
                        'original_blocks': original_blocks,
                        'searchable_original_content': searchable_original_content.strip(), # <<< Lưu lại
                        'metadata': metadata
                    })
                    # === KẾT THÚC SỬA ĐỔI ===
        except Exception as e:
            print(f"LỖI: không thể đọc file database '{db_path}': {e}")
        return corpus_data

    def retrieve_bm25(self, question: str, top_k: int) -> List[Dict[str, Any]]:
        print(f"  - Đang truy xuất top {top_k} ngữ cảnh bằng BM25...")
        tokenized_query = question.split()
        doc_scores = self.bm25.get_scores(tokenized_query)
        top_k_indices = np.argsort(doc_scores)[::-1][:top_k]
        return [self.corpus[i] for i in top_k_indices]

    # === HÀM GENERATE_ANSWER VIẾT LẠI HOÀN TOÀN THEO LOGIC ĐÃ THÀNH CÔNG ===
    # Thay thế toàn bộ hàm này trong class BM25_VLM_QA

    def generate_answer(self, retrieved_chunks: List[Dict], question: str, options: Dict[str, str]) -> str:
        """
        Tạo prompt và sinh câu trả lời, bao gồm cả original_blocks và enriched_content.
        """
        print("  - Đang chuẩn bị prompt và ngữ cảnh cho VLM (Unsloth)...")
        
        context_str = ""
        vlm_content_list = []

        # Xây dựng context từ tất cả các chunk được truy xuất
        for i, chunk in enumerate(retrieved_chunks):
            # === BẮT ĐẦU SỬA ĐỔI ===
            enriched_content = chunk['enriched_content']
            original_blocks = chunk.get('original_blocks', [])
            metadata = chunk['metadata']
            doc_name = metadata.get('doc_name', 'N/A')
            chunk_type = metadata.get('chunk_type')

            # Định dạng original_blocks để dễ đọc
            original_content_str = ""
            for block in original_blocks:
                block_type = block.get('type')
                if block_type == 'paragraph':
                    original_content_str += block.get('content', '') + "\n"
                elif block_type == 'html_table':
                    # Có thể dùng lại hàm linearize_html_table nếu muốn,
                    # hoặc chỉ hiển thị HTML gốc
                    original_content_str += f"[Bảng HTML gốc]:\n{block.get('raw_html', '')}\n"
                # Thêm các loại block khác nếu cần
            
            # Thêm cả hai loại nội dung vào context_str
            context_str += f"--- Ngữ cảnh tham khảo {i+1} (Từ tài liệu: {doc_name}) ---\n"
            context_str += f"**NỘI DUNG GỐC:**\n{original_content_str.strip()}\n\n"
            context_str += f"**NỘI DUNG ĐÃ LÀM GIÀU (để tham khảo thêm):**\n{enriched_content}\n\n"
            # === KẾT THÚC SỬA ĐỔI ===
            
            if chunk_type == 'image_context':
                image_path_relative = metadata.get('image_path')
                if image_path_relative:
                    image_path_full = os.path.join(SUBMISSION_DIR, doc_name, image_path_relative)
                    image_uri = encode_image_to_base64_uri(image_path_full)
                    if image_uri:
                        # Thêm ảnh vào vlm_content_list theo đúng format
                        vlm_content_list.append({"type": "image", "image": image_uri})
                        print(f"    - Đã tìm thấy và sẽ sử dụng ảnh: {image_path_full}")
                        # Chỉ lấy ảnh đầu tiên để tránh phức tạp
                        break

        options_str = "\n".join([f"{key}: {value}" for key, value in options.items()])
        prompt_template = f"""
Bạn là một **trợ lý QA tiếng Việt chuyên nghiệp**, được huấn luyện đặc biệt để xử lý **câu hỏi trắc nghiệm nhiều đáp án đúng**.

QUY TẮC BẮT BUỘC:
0. Câu trả lời cuối cùng **BẮT BUỘC** phải được đặt trong cặp thẻ `[ANSWER]` và `[/ANSWER]`. **Đây là quy tắc quan trọng nhất.**
1. Bạn **chỉ** được sử dụng thông tin trong phần NGỮ CẢNH bên dưới.
2. Đáp án **chỉ** là chuỗi ký tự gồm các lựa chọn đúng, viết hoa, phân tách bằng dấu phẩy **(không có khoảng trắng)**. Ví dụ: `A` hoặc `A,C,D`
3. **Không** viết thêm lời giải thích.
4. Nếu không có thông tin, vẫn phải chọn đáp án bạn cho là đúng nhất.

--- VÍ DỤ ---
**VÍ DỤ 1:**
NGỮ CẢNH: Công thức hóa học của nước là H2O.
CÂU HỎI: Các nguyên tố hóa học nào tạo nên phân tử nước?
LỰA CHỌN: A: A, H | B: H, O | C: A, O | D: H, 2
ĐÁP ÁN: [ANSWER]B[/ANSWER]

**VÍ DỤ 2:**
NGỮ CẢNH: Sản phẩm hỗ trợ kết nối qua cả Wi-Fi và Bluetooth. Cổng USB-C dùng để sạc.
CÂU HỎI: Sản phẩm hỗ trợ những kết nối không dây nào?
LỰA CHỌN: A: Wi-Fi | B: Cổng USB-C | C: Bluetooth | D: NFC
ĐÁP ÁN: [ANSWER]A,C[/ANSWER]

**VÍ DỤ 3:**
NGỮ CẢNH: Yêu cầu kỹ thuật cho bộ phận C là phải có chứng chỉ "A D M".
CÂU HỎI: Bộ phận nào cần chứng chỉ "A D M"?
CÁC LỰA CHỌN:
A: Bộ phận C | B: Bộ phận D | C: Bộ phận A | D: Bộ phận B
ĐÁP ÁN: [ANSWER]A[/ANSWER]
--- KẾT THÚC VÍ DỤ ---

--- BẮT ĐẦU NHIỆM VỤ ---
NGỮ CẢNH TỔNG HỢP:
{{context_str}}

CÂU HỎI: {{question}}

CÁC LỰA CHỌN:
{{options_str}}

ĐÁP ÁN:"""

        final_prompt_text = prompt_template.format(context_str=context_str, question=question, options_str=options_str)
        
        # === BẮT ĐẦU SỬA LỖI THEO CODE MẪU ===
        
        # Bước 1: Xây dựng content list, đặt text làm item đầu tiên
        final_content_list = [{"type": "text", "text": final_prompt_text}]
        # Nối danh sách ảnh đã tìm thấy vào sau
        final_content_list.extend(vlm_content_list)
        
        # Bước 2: Tạo messages batch (dù chỉ có 1 item)
        messages_batch = [[{"role": "user", "content": final_content_list}]]
        
        print("  - Đang sinh câu trả lời bằng VLM (Unsloth)...")
        try:
            # Bước 3: Luôn sử dụng PROCESSOR để áp dụng template
            inputs = self.processor.apply_chat_template(
                messages_batch,
                tokenize=True,
                add_generation_prompt=True,
                return_dict=True,
                padding=True,
                return_tensors="pt"
            ).to(self.device)

            # Bước 4: Gọi generate bằng cách unpack dictionary inputs (**)
            outputs = self.vlm_model.generate(**inputs, max_new_tokens=20)
            
            # Bước 5: Giải mã và trích xuất output như trong code mẫu
            response_full = self.processor.batch_decode(outputs, skip_special_tokens=True)[0]
            prompt_text_only = self.processor.decode(inputs['input_ids'][0], skip_special_tokens=True)
            
            if response_full.startswith(prompt_text_only):
                return response_full[len(prompt_text_only):].strip()
            else:
                last_occurrence = response_full.rfind("ĐÁP ÁN:")
                if last_occurrence != -1:
                    return response_full[last_occurrence + len("ĐÁP ÁN:"):].strip()
                return response_full
            
        except Exception as e:
            print(f"  - LỖI khi generate: {e}. Có thể do prompt quá dài hoặc lỗi khác.")
            return "[GENERATION_ERROR]"
        # === KẾT THÚC SỬA LỖI ===


    def process_question(self, question_row: pd.Series) -> str:
        # ... (Hàm này giữ nguyên, không cần thay đổi) ...
        question = question_row['Question']
        options = {'A': question_row['A'], 'B': question_row['B'], 'C': question_row['C'], 'D': question_row['D']}
        retrieved_chunks = self.retrieve_bm25(question, top_k=TOP_K_BM25)
        raw_answer = self.generate_answer(retrieved_chunks, question, options)
        print(f"  - Phản hồi thô từ VLM: '{raw_answer}'")
        answer_content = raw_answer
        match = re.search(r'\[ANSWER\](.*?)\[/ANSWER\]', raw_answer, re.DOTALL)
        if match:
            answer_content = match.group(1).strip()
            print(f"  - Đã tìm thấy thẻ [ANSWER]. Nội dung: '{answer_content}'")
        else:
            print("  - Cảnh báo: Không tìm thấy thẻ [ANSWER]. Sử dụng toàn bộ phản hồi.")
        found_answers = re.findall(r'[A-D]', answer_content.upper())
        valid_answers = sorted(list(set(found_answers)))
        num_correct = len(valid_answers)
        answers_str = ",".join(valid_answers)
        if num_correct > 1: return f'{num_correct},"{answers_str}"'
        elif num_correct == 1: return f'1,{answers_str}'
        else: return '0,""'

# Thay thế hàm main cũ bằng hàm này

def main():
    """
    Hàm chính điều khiển toàn bộ pipeline.
    Đã sửa đổi để luôn ghi một section TASK QA mới vào cuối file output.
    """
    print("======================================================")
    print("===   BẮT ĐẦU PIPELINE: BM25 RETRIEVAL & VLM QA   ===")
    print("======================================================")
    
    # Unsloth tự quản lý device, không cần get_free_gpu nữa
    vlm_model, tokenizer, processor = load_vlm_model_and_processor(device="auto")
    qa_pipeline = BM25_VLM_QA(
        db_path=DB_FILE_PATH, 
        vlm_model=vlm_model, 
        tokenizer=tokenizer, 
        processor=processor
    )
    
    try:
        questions_df = pd.read_csv(QUESTIONS_FILE_PATH)
        print(f"\nĐã đọc thành công {len(questions_df)} câu hỏi từ '{QUESTIONS_FILE_PATH}'.")
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file câu hỏi tại '{QUESTIONS_FILE_PATH}'.")
        return

    # === BẮT ĐẦU SỬA ĐỔI LOGIC GHI FILE ===
    
    # 1. Tạo thư mục nếu chưa tồn tại
    os.makedirs(os.path.dirname(OUTPUT_FILE_PATH), exist_ok=True)
    
    # 2. Luôn mở file ở chế độ nối tiếp ('a' - append)
    with open(OUTPUT_FILE_PATH, 'a', encoding='utf-8') as f:
        
        # 3. Luôn ghi một bộ header mới vào cuối file để bắt đầu một section mới
        print(f"Sẽ ghi một section TASK QA mới vào cuối file '{OUTPUT_FILE_PATH}'.")
        f.write("### TASK QA\n")
        f.write("num_correct,answers\n")

        # 4. Bắt đầu vòng lặp xử lý và ghi các câu trả lời
        total_questions = len(questions_df)
        for index, row in questions_df.iterrows():
            print(f"\n--- Xử lý câu hỏi {index + 1}/{total_questions} ---")
            print(f"Câu hỏi: {row['Question']}")
            
            final_answer_line = qa_pipeline.process_question(row)
            
            print(f"  - Kết quả cuối cùng: {final_answer_line}")
            f.write(final_answer_line + "\n")
            f.flush()
            
    # === KẾT THÚC SỬA ĐỔI LOGIC GHI FILE ===

    print("\n======================================================")
    print("===      HOÀN TẤT TOÀN BỘ PIPELINE QA      ===")
    print(f"Kết quả đã được ghi vào file: '{OUTPUT_FILE_PATH}'")
    print("======================================================")

if __name__ == '__main__':
    main()