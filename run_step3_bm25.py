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
from transformers import Qwen3VLForConditionalGeneration, AutoProcessor
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
DB_FILE_PATH = "bm25_database.sqlite"
QUESTIONS_FILE_PATH = "data/raw/public_test_data/question.csv"
SUBMISSION_DIR = "submission"
OUTPUT_FILE_PATH = "submission/answer_final_stable_top5_instruct.md"

VLM_MODEL_NAME = "Qwen/Qwen3-VL-4B-Instruct"
TOP_K_BM25 = 5

def load_vlm_model_and_processor(device: str):
    """
    Tải mô hình VLM và processor, cấu hình theo cách đã hoạt động thành công.
    """
    print(f"Đang tải mô hình VLM: {VLM_MODEL_NAME}...")
    model = Qwen3VLForConditionalGeneration.from_pretrained(
        VLM_MODEL_NAME, 
        torch_dtype=torch.bfloat16,
        device_map=device
    )
    processor = AutoProcessor.from_pretrained(VLM_MODEL_NAME)
    
    # --- ÁP DỤNG CHÍNH XÁC LOGIC TỪ CODE MẪU ---
    if hasattr(processor, "tokenizer"):
        processor.tokenizer.padding_side = "left"
        if processor.tokenizer.pad_token is None:
            processor.tokenizer.pad_token = processor.tokenizer.eos_token
            
    print("Tải mô hình VLM hoàn tất.")
    return model, processor

def encode_image_to_base64_uri(image_path):
    try:
        with open(image_path, "rb") as image_file:
            base64_data = base64.b64encode(image_file.read()).decode('utf-8')
            return f"data:image/jpeg;base64,{base64_data}"
    except Exception as e:
        print(f"  - Lỗi khi encode ảnh {image_path}: {e}")
        return None

class BM25_VLM_QA:
    def __init__(self, db_path, vlm_model, processor):
        self.device = vlm_model.device
        print(f"Sử dụng thiết bị: {self.device}")

        self.vlm_model = vlm_model
        self.processor = processor

        print("Đang kết nối tới SQLite và tải corpus cho BM25...")
        self.corpus = self._load_corpus_from_sqlite(db_path)
        if not self.corpus:
            raise ValueError("Không thể tải corpus từ database.")
        
        print("Đang xây dựng chỉ mục BM25...")
        tokenized_corpus = [doc['enriched_content'].split() for doc in self.corpus]
        self.bm25 = BM25Okapi(tokenized_corpus)
        print("Xây dựng chỉ mục BM25 hoàn tất.")

    def _load_corpus_from_sqlite(self, db_path: str) -> List[Dict[str, Any]]:
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
                    corpus_data.append({'enriched_content': enriched_content, 'metadata': metadata})
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
    def generate_answer(self, retrieved_chunks: List[Dict], question: str, options: Dict[str, str]) -> str:
        """
        Tạo prompt và sinh câu trả lời theo logic ổn định từ code mẫu.
        """
        print("  - Đang chuẩn bị prompt và ngữ cảnh cho VLM...")
        
        context_str = ""
        vlm_content_list = []

        # Xây dựng context từ tất cả các chunk được truy xuất
        for i, chunk in enumerate(retrieved_chunks):
            content = chunk['enriched_content']
            metadata = chunk['metadata']
            doc_name = metadata.get('doc_name', 'N/A')
            chunk_type = metadata.get('chunk_type')
            context_str += f"--- Ngữ cảnh tham khảo {i+1} (Từ tài liệu: {doc_name}) ---\n{content}\n\n"
            
            if chunk_type == 'image_context':
                image_path_relative = metadata.get('image_path')
                if image_path_relative:
                    image_path_full = os.path.join(SUBMISSION_DIR, doc_name, image_path_relative)
                    image_uri = encode_image_to_base64_uri(image_path_full)
                    if image_uri:
                        # Thêm cả text và image vào list theo đúng format VLM
                        vlm_content_list.append({"type": "text", "text": f"\nẢnh tham khảo từ ngữ cảnh {i+1}:\n"})
                        vlm_content_list.append({"type": "image", "image": image_uri})

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
        
        # Thêm prompt text vào đầu danh sách content
        vlm_content_list.insert(0, {"type": "text", "text": final_prompt_text})
        
        # Tạo messages với batch size là 1
        messages_batch = [[{"role": "user", "content": vlm_content_list}]]
        
        print("  - Đang sinh câu trả lời bằng VLM...")
        try:
            # --- ÁP DỤNG CHÍNH XÁC LOGIC TỪ CODE MẪU ---
            inputs = self.processor.apply_chat_template(
                messages_batch,
                tokenize=True,
                add_generation_prompt=True,
                return_dict=True,
                padding=True,
                return_tensors="pt"
            ).to(self.device)

            generated_ids = self.vlm_model.generate(**inputs, max_new_tokens=20)
            
            # Giải mã output
            response = self.processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
            
            # Trích xuất phần trả lời sau prompt
            prompt_text_only = self.processor.decode(inputs['input_ids'][0], skip_special_tokens=True)
            if response.startswith(prompt_text_only):
                return response[len(prompt_text_only):].strip()
            else:
                # Fallback: Trả về phần cuối của response nếu không match
                # (Đôi khi model thêm/bớt ký tự làm prompt không khớp 100%)
                # Tìm vị trí "ĐÁP ÁN:" cuối cùng và lấy phần sau đó
                last_occurrence = response.rfind("ĐÁP ÁN:")
                if last_occurrence != -1:
                    return response[last_occurrence + len("ĐÁP ÁN:"):].strip()
                return response # Trả về toàn bộ nếu không tìm thấy
            # --- KẾT THÚC ÁP DỤNG ---
            
        except Exception as e:
            print(f"  - LỖI khi generate: {e}. Có thể do prompt quá dài hoặc lỗi khác.")
            return "[GENERATION_ERROR]"


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

def main():
    # ... (Hàm này giữ nguyên, không cần thay đổi) ...
    print("======================================================")
    print("===   BẮT ĐẦU PIPELINE: BM25 RETRIEVAL & VLM QA   ===")
    print("======================================================")
    best_device = get_free_gpu()
    vlm_model, processor = load_vlm_model_and_processor(device=best_device)
    qa_pipeline = BM25_VLM_QA(db_path=DB_FILE_PATH, vlm_model=vlm_model, processor=processor)
    try:
        questions_df = pd.read_csv(QUESTIONS_FILE_PATH)
        print(f"\nĐã đọc thành công {len(questions_df)} câu hỏi từ '{QUESTIONS_FILE_PATH}'.")
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file câu hỏi tại '{QUESTIONS_FILE_PATH}'.")
        return
    os.makedirs(os.path.dirname(OUTPUT_FILE_PATH), exist_ok=True)
    with open(OUTPUT_FILE_PATH, 'w', encoding='utf-8') as f:
        f.write("### TASK QA\n")
        f.write("num_correct,answers\n")
    print(f"Đã tạo và ghi header cho file output tại '{OUTPUT_FILE_PATH}'.")
    with open(OUTPUT_FILE_PATH, 'a', encoding='utf-8') as f:
        total_questions = len(questions_df)
        for index, row in questions_df.iterrows():
            print(f"\n--- Xử lý câu hỏi {index + 1}/{total_questions} ---")
            print(f"Câu hỏi: {row['Question']}")
            final_answer_line = qa_pipeline.process_question(row)
            print(f"  - Kết quả cuối cùng: {final_answer_line}")
            f.write(final_answer_line + "\n")
            f.flush()
    print("\n======================================================")
    print("===      HOÀN TẤT TOÀN BỘ PIPELINE QA      ===")
    print(f"Kết quả đã được ghi vào file: '{OUTPUT_FILE_PATH}'")
    print("======================================================")

if __name__ == '__main__':
    main()