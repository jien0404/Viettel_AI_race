import time
import torch
from sentence_transformers import SentenceTransformer
from PIL import Image
from typing import List, Dict, Any
import os

class Embedder:
    def __init__(self):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print(f"Sử dụng thiết bị: {self.device}", flush=True)

        # Tùy biến batch để tránh OOM / block lâu
        self.text_batch_size = 64
        self.image_batch_size = 8

        print("Đang tải mô hình text embedding (AITeamVN/Vietnamese-Sentence-RoBERTa)...", flush=True)
        self.text_model = SentenceTransformer(
            'bkai-foundation-models/vietnamese-bi-encoder', 
            device=self.device
        )

        print("Đang tải mô hình image embedding (clip-ViT-B-32)...", flush=True)
        self.image_model = SentenceTransformer(
            'clip-ViT-B-32', 
            device=self.device
        )
        print("Tải mô hình hoàn tất.", flush=True)

    def embed_chunks(self, chunks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        start_all = time.time()
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
                image_path = chunk.get('content_for_embedding', '')
                if image_path and os.path.exists(image_path):
                    image_chunks_paths.append(image_path)
                    image_chunks_indices.append(i)
                else:
                    print(f"!! CẢNH BÁO: Không tìm thấy ảnh tại '{image_path}'. Bỏ qua embedding cho chunk ảnh (index={i}).", flush=True)

        # Text embeddings (batch)
        if text_based_chunks_content:
            t0 = time.time()
            print(f"Đang tạo embedding cho {len(text_based_chunks_content)} chunk văn bản (batch={self.text_batch_size})...", flush=True)
            text_embeddings = self.text_model.encode(
                text_based_chunks_content, 
                batch_size=self.text_batch_size,
                convert_to_tensor=False, 
                show_progress_bar=False
            )
            for idx, embedding in zip(text_based_chunks_indices, text_embeddings):
                chunks[idx]['embedding_vector'] = embedding if hasattr(embedding, 'tolist') else embedding
            print(f"-> Text embedding xong trong {time.time()-t0:.2f}s", flush=True)

        # Image embeddings (open + maybe resize + batch)
        if image_chunks_paths:
            t0 = time.time()
            print(f"Đang tạo embedding cho {len(image_chunks_paths)} chunk hình ảnh (batch={self.image_batch_size})...", flush=True)
            image_pil_objects = []
            valid_image_indices = []
            for idx, path in zip(image_chunks_indices, image_chunks_paths):
                try:
                    img = Image.open(path).convert('RGB')
                    # giảm kích thước nếu quá lớn để tránh OOM / slow encode
                    img.thumbnail((1024, 1024))
                    image_pil_objects.append(img)
                    valid_image_indices.append(idx)
                except Exception as e:
                    print(f"!! Lỗi mở ảnh '{path}': {e}. Bỏ qua chunk (index={idx}).", flush=True)

            if image_pil_objects:
                image_embeddings = self.image_model.encode(
                    image_pil_objects,
                    batch_size=self.image_batch_size,
                    convert_to_tensor=False,
                    show_progress_bar=False
                )
                for idx, embedding in zip(valid_image_indices, image_embeddings):
                    chunks[idx]['embedding_vector'] = embedding if hasattr(embedding, 'tolist') else embedding
            print(f"-> Image embedding xong trong {time.time()-t0:.2f}s", flush=True)

        print(f"Tổng thời gian embed cho document: {time.time()-start_all:.2f}s", flush=True)
        return chunks