import torch
from transformers import Qwen3VLForConditionalGeneration, AutoProcessor
from typing import List, Dict, Any
import os
import base64

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

class ContextEnricher:
    def __init__(self, model_name: str = "Qwen/Qwen3-VL-4B-Instruct"):
        print(f"Đang tải mô hình Vision-Language: {model_name}...")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        self.model = Qwen3VLForConditionalGeneration.from_pretrained(
            model_name, 
            dtype="auto", 
            device_map="auto"
        )
        self.processor = AutoProcessor.from_pretrained(model_name)
        print(f"Tải mô hình hoàn tất. Sử dụng thiết bị: {self.device}")

    # Sửa đổi hàm generate để xử lý batch
    def _generate_batch_response(self, messages_batch: List[List[Dict]]) -> List[str]:
        try:
            # `apply_chat_template` có thể xử lý một list các conversation
            inputs = self.processor.apply_chat_template(
                messages_batch,
                tokenize=True,
                add_generation_prompt=True,
                return_dict=True,
                padding=True, # Thêm padding để các chuỗi có cùng độ dài
                return_tensors="pt"
            ).to(self.model.device)

            generated_ids = self.model.generate(**inputs, max_new_tokens=1024)
            
            # Giải mã kết quả cho cả batch
            output_texts = self.processor.batch_decode(
                generated_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
            )
            
            # Cần loại bỏ phần prompt khỏi output
            # Đây là một cách xử lý đơn giản, có thể cần tinh chỉnh
            final_outputs = []
            for i, full_text in enumerate(output_texts):
                # Lấy lại prompt đã được format
                prompt_text_only = self.processor.decode(inputs['input_ids'][i], skip_special_tokens=True)
                # Loại bỏ prompt khỏi output
                if full_text.startswith(prompt_text_only):
                    final_outputs.append(full_text[len(prompt_text_only):].strip())
                else: # Fallback
                     final_outputs.append(full_text)
            
            return final_outputs

        except Exception as e:
            print(f"Lỗi trong quá trình generate batch của model: {e}")
            return ["[Lỗi xử lý]" for _ in messages_batch]

    # Viết lại hoàn toàn hàm enrich_chunks_with_llm để sử dụng batching
    def enrich_chunks_with_llm(self, chunks: List[Dict[str, Any]], 
                               doc_folder_path: str, 
                               batch_size: int = 8) -> List[Dict[str, Any]]:
        
        enriched_chunks_data = []
        
        # Gom các chunk thành các lô để xử lý
        for i in range(0, len(chunks), batch_size):
            batch_chunks = chunks[i:i+batch_size]
            print(f"  > Đang xử lý batch {i//batch_size + 1}/{(len(chunks) + batch_size - 1)//batch_size}...")

            messages_batch = []
            for chunk in batch_chunks:
                content_to_enrich = chunk.get('content_for_enrichment', '')
                chunk_type = chunk.get('chunk_type')

                # Tạo prompt cho từng chunk trong batch
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
                        messages_batch.append([
                            {"role": "user", "content": [
                                {"type": "text", "text": prompt_text},
                                {"type": "image", "image": image_uri}
                            ]}
                        ])
                    else:
                        messages_batch.append([{"role": "user", "content": "File ảnh không tồn tại."}])

                elif chunk_type == 'text':
                    prompt_text = (
                        "BẠN LÀ TRỢ LÝ AI. HÃY TRẢ LỜI BẰNG TIẾNG VIỆT.\n\n"
                        f"**Nội dung cần làm giàu:**\n{content_to_enrich}\n\n"
                        "**YÊU CẦU:** Thực hiện các bước sau:\n"
                        "1. Diễn giải và mở rộng nội dung.\n"
                        "2. Liệt kê 5-10 từ khóa.\n"
                        "3. Đặt ra 3 câu hỏi giả định."
                    )
                    messages_batch.append([{"role": "user", "content": [{"type": "text", "text": prompt_text}]}])
                else:
                    messages_batch.append([{"role": "user", "content": f"Loại chunk không được hỗ trợ."}])
            
            # Gọi model để xử lý cả batch
            enriched_contents = self._generate_batch_response(messages_batch)

            # Gán kết quả trả về cho các chunk tương ứng
            for j, chunk in enumerate(batch_chunks):
                enriched_chunks_data.append({
                    'doc_name': chunk['doc_name'],
                    'chunk_type': chunk['chunk_type'],
                    'enriched_content': enriched_contents[j],
                    'metadata': chunk['metadata']
                })
        
        return enriched_chunks_data