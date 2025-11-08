from llama_cpp import Llama
from typing import List, Dict, Any
import os
import base64

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

class ContextEnricher:
    # --- SỬA ĐỔI QUAN TRỌNG NHẤT NẰM Ở ĐÂY ---
    def __init__(self, 
                 repo_id: str = "unsloth/Qwen3-VL-4B-Instruct-GGUF", 
                 filename: str = "Qwen3-VL-4B-Instruct-Q5_K_M.gguf"): # Dùng Q5_K_M cho ổn định
        
        print(f"Đang tải mô hình GGUF: {repo_id}/{filename}...")
        
        # Đơn giản hóa việc khởi tạo, đặc biệt là n_gpu_layers
        self.llm = Llama.from_pretrained(
            repo_id=repo_id,
            filename=filename,
            
            # GIỮ LẠI: Tham số này rất quan trọng để model hiểu prompt VLM
            chat_format="qwen-vl",  
            
            # THAY ĐỔI QUAN TRỌNG:
            # Thay vì -1 (tất cả), hãy offload một số lượng lớn layer nhưng không phải tất cả.
            # 50 là một con số an toàn cho model 4B. Điều này thường tránh được lỗi
            # với các layer không tương thích.
            n_gpu_layers=50,
            
            # Bật verbose để có thêm thông tin chi tiết nếu lỗi vẫn xảy ra
            verbose=True
        )
        print("Tải mô hình GGUF hoàn tất.")

    # --- THAY ĐỔI LỚN 2: HÀM GENERATE ĐƠN GIẢN HƠN ---
    def _generate_response(self, messages: List[Dict]) -> str:
        """Hàm gọi model cho một yêu cầu duy nhất."""
        try:
            response = self.llm.create_chat_completion(
                messages=messages,
                max_tokens=1024, # Giới hạn token đầu ra
            )
            if response and 'choices' in response and response['choices']:
                return response['choices'][0]['message']['content'].strip()
            return "[Không nhận được phản hồi hợp lệ từ model]"
        except Exception as e:
            print(f"Lỗi trong quá trình generate của model: {e}")
            return f"[Lỗi xử lý: {e}]"

    # --- THAY ĐỔI LỚN 3: LOGIC LẶP TUẦN TỰ (NHƯNG VẪN NHANH) ---
    def enrich_chunks_with_llm(self, chunks: List[Dict[str, Any]], 
                               doc_folder_path: str) -> List[Dict[str, Any]]:
        
        enriched_chunks_data = []
        num_chunks = len(chunks)

        # Lặp qua từng chunk một cách tuần tự.
        # llama.cpp sẽ tự động batch các yêu cầu này ở backend.
        for i, chunk in enumerate(chunks):
            print(f"  > Đang xử lý chunk {i+1}/{num_chunks} (loại: {chunk['chunk_type']})...")
            
            content_to_enrich = chunk.get('content_for_enrichment', '')
            chunk_type = chunk.get('chunk_type')
            messages = []

            # Tạo prompt cho từng chunk
            if chunk_type == 'image_context':
                image_path_relative = chunk['metadata'].get('image_path', '')
                image_path_full = os.path.join(doc_folder_path, image_path_relative)
                
                if os.path.exists(image_path_full):
                    image_uri = f"data:image/jpeg;base64,{encode_image_to_base64(image_path_full)}"
                    prompt_text = (
                        "BẠN LÀ TRỢ LÝ AI. HÃY TRẢ LỜI BẰNG TIẾNG VIỆT.\n\n"
                        f"**Ngữ cảnh:**\n{content_to_enrich}\n\n"
                        "**YÊU CẦU:** Dựa vào hình ảnh và ngữ cảnh, hãy:\n"
                        "1. Mô tả chi tiết hình ảnh.\n"
                        "2. Trích xuất (OCR) toàn bộ văn bản trong ảnh.\n"
                        "3. Diễn giải ý nghĩa của ảnh."
                    )
                    # QUAN TRỌNG: llama-cpp-python sử dụng format 'image_url'
                    messages = [{
                        "role": "user", "content": [
                            {"type": "text", "text": prompt_text},
                            {"type": "image_url", "image_url": {"url": image_uri}}
                        ]
                    }]
                else:
                    messages = [{"role": "user", "content": [{"type": "text", "text": "File ảnh không tồn tại."}]}]

            elif chunk_type == 'text':
                prompt_text = (
                    "BẠN LÀ TRỢ LÝ AI. HÃY TRẢ LỜI BẰNG TIẾNG VIỆT.\n\n"
                    f"**Nội dung cần làm giàu:**\n{content_to_enrich}\n\n"
                    "**YÊU CẦU:** Thực hiện các bước sau:\n"
                    "1. Diễn giải và mở rộng nội dung.\n"
                    "2. Liệt kê 5-10 từ khóa.\n"
                    "3. Đặt ra 3 câu hỏi giả định."
                )
                messages = [{"role": "user", "content": [{"type": "text", "text": prompt_text}]}]
            
            # Xử lý các trường hợp khác
            if not messages:
                enriched_content = f"[Loại chunk '{chunk_type}' không được hỗ trợ hoặc có lỗi]"
            else:
                # Gọi model để xử lý chunk hiện tại
                enriched_content = self._generate_response(messages)

            # Gán kết quả trả về
            enriched_chunks_data.append({
                'doc_name': chunk['doc_name'],
                'chunk_type': chunk['chunk_type'],
                'enriched_content': enriched_content,
                'metadata': chunk['metadata']
            })
        
        return enriched_chunks_data