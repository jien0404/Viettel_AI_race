import torch
from sentence_transformers import SentenceTransformer
from PIL import Image
from typing import List, Dict, Any

class Embedder:
    def __init__(self):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print(f"Sử dụng thiết bị: {self.device}")

        print("Đang tải mô hình text embedding (AITeamVN/Vietnamese-Sentence-RoBERTa)...")
        # Sử dụng model chuyên cho tiếng Việt để có chất lượng tốt 
        self.text_model = SentenceTransformer(
            'bkai-foundation-models/vietnamese-bi-encoder', 
            device=self.device
        )

        print("Đang tải mô hình image embedding (clip-ViT-B-32)...")
        # CLIP là một mô hình mạnh mẽ để tạo embedding cho cả ảnh và text
        self.image_model = SentenceTransformer(
            'clip-ViT-B-32', 
            device=self.device
        )
        print("Tải mô hình hoàn tất.")

    def embed_chunks(self, chunks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        text_based_chunks_content = []
        text_based_chunks_indices = []
        
        image_chunks_paths = []
        image_chunks_indices = []

        for i, chunk in enumerate(chunks):
            chunk_type = chunk.get('chunk_type')
            if chunk_type in ['text', 'table', 'formula']:
                text_based_chunks_content.append(chunk.get('content_for_embedding', ''))
                text_based_chunks_indices.append(i)
            elif chunk_type == 'image':
                dummy_image_path = chunk.get('content_for_embedding', '')
                try:
                    Image.new('RGB', (60, 30), color = 'red').save(dummy_image_path)
                except FileNotFoundError:
                    pass
                image_chunks_paths.append(dummy_image_path)
                image_chunks_indices.append(i)

        if text_based_chunks_content:
            print(f"Đang tạo embedding cho {len(text_based_chunks_content)} chunk văn bản...")
            text_embeddings = self.text_model.encode(
                text_based_chunks_content, 
                convert_to_tensor=True, 
                show_progress_bar=True
            )
            for i, embedding in zip(text_based_chunks_indices, text_embeddings):
                chunks[i]['embedding_vector'] = embedding.cpu().numpy()

        if image_chunks_paths:
            print(f"Đang tạo embedding cho {len(image_chunks_paths)} chunk hình ảnh...")
            image_pil_objects = [Image.open(path) for path in image_chunks_paths if path]
            image_embeddings = self.image_model.encode(
                image_pil_objects, 
                convert_to_tensor=True, 
                show_progress_bar=True
            )
            for i, embedding in zip(image_chunks_indices, image_embeddings):
                chunks[i]['embedding_vector'] = embedding.cpu().numpy()
        
        return chunks


# --- MAIN ĐỂ KIỂM THỬ ---
if __name__ == '__main__':
    sample_chunks = [
        {"doc_name": "Public_Test_001", "metadata": {"context_headings": "Đây là Tiêu đề chính", "original_content": "Đây là đoạn văn bản giới thiệu đầu tiên. Nó mô tả nội dung của tài liệu."}, "chunk_type": "text", "content_for_embedding": "Ngữ cảnh: Đây là Tiêu đề chính. Nội dung: Đây là đoạn văn bản giới thiệu đầu tiên. Nó mô tả nội dung của tài liệu."},
        {"doc_name": "Public_Test_001", "metadata": {"context_headings": "Đây là Tiêu đề chính > Một Tiêu đề phụ", "original_content": "Đây là đoạn văn bản thứ hai, nằm dưới tiêu đề phụ."}, "chunk_type": "text", "content_for_embedding": "Ngữ cảnh: Đây là Tiêu đề chính > Một Tiêu đề phụ. Nội dung: Đây là đoạn văn bản thứ hai, nằm dưới tiêu đề phụ."},
        {"doc_name": "Public_Test_001", "metadata": {"context_headings": "Đây là Tiêu đề chính > Một Tiêu đề phụ", "original_content": "image_1", "image_path": "images/image_1.jpg", "text_context": "Đây là đoạn văn bản thứ hai, nằm dưới tiêu đề phụ."}, "chunk_type": "image", "content_for_embedding": "images/image_1.jpg"},
        {"doc_name": "Public_Test_001", "metadata": {"context_headings": "Đây là Tiêu đề chính > Một Tiêu đề phụ", "original_content": "<table>...</table>"}, "chunk_type": "table", "content_for_embedding": "Ngữ cảnh: Đây là Tiêu đề chính > Một Tiêu đề phụ. Bảng: Nội dung bảng: Bảng kết quả. Một hàng trong bảng chứa: Hàng 1, Cột 1, Hàng 1, Cột 2."},
        {"doc_name": "Public_Test_001", "metadata": {"context_headings": "Đây là Tiêu đề chính > Một Tiêu đề phụ", "original_content": "$$\\nE = mc^2\\n$$"}, "chunk_type": "formula", "content_for_embedding": "Ngữ cảnh: Đây là Tiêu đề chính > Một Tiêu đề phụ. Nội dung là một công thức toán học."},
    ]
    
    import os
    if not os.path.exists('images'):
        os.makedirs('images')
        
    embedder = Embedder()
    
    chunks_with_embeddings = embedder.embed_chunks(sample_chunks)
    
    print("\n--- Embedding hoàn tất. Kiểm tra kết quả: ---")
    for chunk in chunks_with_embeddings:
        if 'embedding_vector' in chunk:
            print(f" - Loại chunk: '{chunk['chunk_type']}', "
                  f"Đã thêm vector embedding với shape: {chunk['embedding_vector'].shape}")
        else:
            print(f" - Loại chunk: '{chunk['chunk_type']}', LỖI: Không có vector embedding!")