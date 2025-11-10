import torch
from transformers import Qwen3VLForConditionalGeneration, AutoProcessor
from typing import List, Dict, Any
import os
import base64

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

class ContextEnricher:
    def __init__(self, model_name: str = "Qwen/Qwen3-VL-4B-Thinking"):
        print(f"Đang tải mô hình Vision-Language: {model_name}...")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.model = Qwen3VLForConditionalGeneration.from_pretrained(
            model_name,
            dtype="auto",
            device_map="auto"
        )

        # 👇 Sửa ở đây
        self.processor = AutoProcessor.from_pretrained(model_name)
        if hasattr(self.processor, "tokenizer"):
            self.processor.tokenizer.padding_side = "left"
            if self.processor.tokenizer.pad_token is None:
                self.processor.tokenizer.pad_token = self.processor.tokenizer.eos_token

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
                               batch_size: int = 4) -> List[Dict[str, Any]]:
        
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
                            "Bạn là một chuyên gia phân tích hình ảnh kỹ thuật. Nhiệm vụ của bạn là phân tích hình ảnh được cung cấp trong ngữ cảnh văn bản xung quanh.\n"
                            "HÃY TRẢ LỜI HOÀN TOÀN BẰNG TIẾNG VIỆT. Bắt đầu câu trả lời ngay lập tức, không dùng lời chào hay câu dẫn.\n\n"
                            f"--- NGỮ CẢNH VĂN BẢN ---\n{content_to_enrich}\n\n"
                            "--- YÊU CẦU ---\n"
                            "Hãy phân tích hình ảnh và trả về kết quả theo đúng cấu trúc Markdown sau:\n\n"
                            "### MÔ TẢ HÌNH ẢNH\n"
                            "(Mô tả một cách khách quan và chi tiết tất cả các đối tượng, biểu đồ, và thành phần trong ảnh.)\n\n"
                            "### VĂN BẢN TRONG ẢNH (OCR)\n"
                            "(Trích xuất TOÀN BỘ văn bản, chữ số, ký hiệu có trong ảnh, không bỏ sót. Nếu không có, ghi rõ 'Không có văn bản'.)\n\n"
                            "### PHÂN TÍCH & KẾT NỐI\n"
                            "(Diễn giải ý nghĩa của hình ảnh và mối liên hệ của nó với ngữ cảnh văn bản được cung cấp.)"
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
                        "Bạn là một chuyên gia làm giàu dữ liệu cho hệ thống tìm kiếm (search engine). Nhiệm vụ của bạn là phân tích và mở rộng đoạn văn bản dưới đây.\n"
                        "HÃY TRẢ LỜI HOÀN TOÀN BẰNG TIẾNG VIỆT. Bắt đầu câu trả lời ngay lập tức, không dùng các câu dẫn như 'Dưới đây là phần trả lời...'\n\n"
                        f"--- DỮ LIỆU GỐC ---\n{content_to_enrich}\n\n"
                        "--- YÊU CẦU ---\n"
                        "Hãy tạo ra một phiên bản làm giàu của dữ liệu gốc theo đúng cấu trúc Markdown sau:\n\n"
                        "### TÓM TẮT & MỞ RỘNG\n"
                        "(Tóm tắt lại ý chính và diễn giải, mở rộng nó với các chi tiết bổ sung để làm rõ ngữ cảnh.)\n\n"
                        "### TỪ KHÓA CHÍNH\n"
                        "- (Liệt kê 5-7 từ khóa quan trọng nhất, mỗi từ khóa một dòng)\n\n"
                        "### THUẬT NGỮ LIÊN QUAN\n"
                        "- (Liệt kê các từ đồng nghĩa hoặc thuật ngữ kỹ thuật có liên quan chặt chẽ.)\n\n"
                        "### CÂU HỎI TIỀM NĂNG\n"
                        "- (Tạo ra 3 câu hỏi mà đoạn văn này có thể trả lời trực tiếp.)"
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