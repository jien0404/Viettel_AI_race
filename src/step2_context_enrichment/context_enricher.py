import torch
from transformers import Qwen3VLForConditionalGeneration, AutoProcessor
from typing import List, Dict, Any
import os
import base64
from PIL import Image

# Hàm trợ giúp để encode ảnh sang base64
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

    def _generate_response(self, messages: List[Dict]) -> str:
        """Hàm chung để gọi model và lấy kết quả."""
        try:
            inputs = self.processor.apply_chat_template(
                messages,
                tokenize=True,
                add_generation_prompt=True,
                return_dict=True,
                return_tensors="pt"
            ).to(self.model.device)

            generated_ids = self.model.generate(**inputs, max_new_tokens=512)
            
            generated_ids_trimmed = [
                out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
            ]
            output_text = self.processor.batch_decode(
                generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
            )
            return output_text[0] if output_text else ""
        except Exception as e:
            print(f"Lỗi trong quá trình generate của model: {e}")
            return "[Lỗi xử lý]"

    def enrich_chunks_with_llm(self, chunks: List[Dict[str, Any]], doc_folder_path: str) -> List[Dict[str, Any]]:
        enriched_chunks = []
        num_chunks = len(chunks)

        for i, chunk in enumerate(chunks):
            print(f"  > Đang xử lý chunk {i+1}/{num_chunks} (loại: {chunk['chunk_type']})...")
            
            # Lấy ngữ cảnh: chunk trước và sau
            context_before = chunks[i-1]['metadata'].get('original_content', '') if i > 0 else "Đây là phần đầu tiên của tài liệu."
            context_after = chunks[i+1]['metadata'].get('original_content', '') if i < num_chunks - 1 else "Đây là phần cuối cùng của tài liệu."
            
            current_content = chunk['metadata'].get('original_content', '')
            
            enriched_content = ""

            if chunk['chunk_type'] == 'image':
                image_path_relative = chunk['metadata'].get('image_path', '')
                image_path_full = os.path.join(doc_folder_path, image_path_relative)
                
                if not os.path.exists(image_path_full):
                    enriched_content = "Không thể xử lý ảnh do không tìm thấy file."
                else:
                    try:
                        base64_image = encode_image_to_base64(image_path_full)
                        image_uri = f"data:image/jpeg;base64,{base64_image}"

                        #+ Sửa đổi prompt cho ảnh
                        prompt_text = (
                            "BẠN LÀ MỘT TRỢ LÝ AI CHUYÊN PHÂN TÍCH TÀI LIỆU KHOA HỌC VÀ KỸ THUẬT.\n"
                            "HÃY TRẢ LỜI HOÀN TOÀN BẰNG TIẾNG VIỆT.\n\n"
                            f"**Ngữ cảnh văn bản phía trước ảnh:**\n{context_before}\n\n"
                            f"**Ngữ cảnh văn bản phía sau ảnh:**\n{context_after}\n\n"
                            "**YÊU CẦU:** Dựa vào hình ảnh được cung cấp và ngữ cảnh trên, hãy thực hiện các nhiệm vụ sau theo đúng thứ tự:\n"
                            "1. **Mô tả chi tiết:** Mô tả hình ảnh một cách chi tiết, dễ hiểu.\n"
                            "2. **Trích xuất văn bản (OCR):** Liệt kê TOÀN BỘ các ký tự, từ, số, nhãn có trong ảnh. Đây là nhiệm vụ quan trọng nhất, không được bỏ sót.\n"
                            "3. **Diễn giải ý nghĩa:** Giải thích mục đích và ý nghĩa của hình ảnh trong bối cảnh của tài liệu.\n\n"
                            "**LƯU Ý:** Câu trả lời của bạn phải được viết hoàn toàn bằng tiếng Việt."
                        )

                        messages = [{
                            "role": "user",
                            "content": [
                                {"type": "text", "text": prompt_text},
                                {"type": "image_url", "image_url": {"url": image_uri}}
                            ],
                        }]
                        enriched_content = self._generate_response(messages)
                    except Exception as e:
                        print(f"    Lỗi khi xử lý ảnh {image_path_full}: {e}")
                        enriched_content = f"Lỗi khi xử lý ảnh: {e}"

            else: # Xử lý text, table, formula
                #+ Sửa đổi prompt cho văn bản
                prompt_text = (
                    "BẠN LÀ MỘT TRỢ LÝ AI CHUYÊN LÀM GIÀU DỮ LIỆU. HÃY TRẢ LỜI HOÀN TOÀN BẰNG TIẾNG VIỆT.\n\n"
                    "**Nhiệm vụ:** Làm giàu nội dung chính dưới đây để tối ưu hóa cho việc tìm kiếm thông tin.\n\n"
                    f"**Ngữ cảnh (đoạn trước):**\n{context_before}\n\n"
                    f"**NỘI DUNG CHÍNH CẦN LÀM GIÀU:**\n{current_content}\n\n"
                    f"**Ngữ cảnh (đoạn sau):**\n{context_after}\n\n"
                    "**YÊU CẦU:** Thực hiện các bước sau:\n"
                    "1. **Diễn giải và Mở rộng:** Viết lại nội dung chính bằng cách diễn giải, giải thích các thuật ngữ, và thêm các thông tin liên quan dựa vào ngữ cảnh.\n"
        "2. **Từ khóa:** Liệt kê 5-10 từ khóa quan trọng nhất từ nội dung chính.\n"
                    "3. **Câu hỏi giả định:** Đặt ra 3 câu hỏi mà nội dung chính này có thể trả lời trực tiếp.\n\n"
                    "**LƯU Ý:** Câu trả lời của bạn phải được viết hoàn toàn bằng tiếng Việt."
                )
                messages = [{"role": "user", "content": [{"type": "text", "text": prompt_text}]}]
                enriched_content = self._generate_response(messages)
            
            new_chunk_data = {
                'doc_name': chunk['doc_name'],
                'chunk_type': chunk['chunk_type'],
                'enriched_content': enriched_content,
                'metadata': chunk['metadata'] 
            }
            enriched_chunks.append(new_chunk_data)

        return enriched_chunks