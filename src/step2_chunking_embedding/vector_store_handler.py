import chromadb
import numpy as np
from typing import List, Dict, Any

class VectorStoreHandler:
    def __init__(self, persist_directory: str):
        self.client = chromadb.PersistentClient(path=persist_directory)
        print(f"Khởi tạo ChromaDB client. Dữ liệu sẽ được lưu tại: '{persist_directory}'")

    def create_or_get_collection(self, collection_name: str):
        try:
            collection = self.client.get_or_create_collection(name=collection_name)
            print(f"Đã tải/tạo thành công collection: '{collection_name}'")
            return collection
        except Exception as e:
            print(f"Lỗi khi tạo hoặc lấy collection: {e}")
            return None

    def add_chunks_to_collection(self, collection, chunks: List[Dict[str, Any]]):
        if not chunks:
            print("Không có chunk nào để thêm.")
            return

        batch_size = 100 
        doc_name = chunks[0].get('doc_name', 'unknown_doc')

        for i in range(0, len(chunks), batch_size):
            batch_chunks = chunks[i:i+batch_size]
            
            ids = [f"{doc_name}_{i+j}" for j in range(len(batch_chunks))]
            embeddings = [chunk['embedding_vector'].tolist() for chunk in batch_chunks]
            
            metadatas = [chunk['metadata'] for chunk in batch_chunks]

            try:
                collection.add(
                    embeddings=embeddings,
                    metadatas=metadatas,
                    ids=ids
                )
                print(f"Đã thêm thành công batch từ {i} đến {i+len(batch_chunks)}.")
            except Exception as e:
                print(f"Lỗi khi thêm batch vào collection: {e}")

if __name__ == '__main__':
    sample_chunks_with_embeddings = [
        {'doc_name': 'Public_Test_001', 'metadata': {'context_headings': 'Tiêu đề chính', 'original_content': 'Nội dung văn bản 1'}, 'chunk_type': 'text', 'embedding_vector': np.random.rand(768)},
        {'doc_name': 'Public_Test_001', 'metadata': {'context_headings': 'Tiêu đề phụ', 'original_content': 'Nội dung văn bản 2'}, 'chunk_type': 'text', 'embedding_vector': np.random.rand(768)},
        {'doc_name': 'Public_Test_001', 'metadata': {'context_headings': 'Tiêu đề phụ', 'image_path': 'images/image_1.jpg'}, 'chunk_type': 'image', 'embedding_vector': np.random.rand(512)},
        {'doc_name': 'Public_Test_001', 'metadata': {'context_headings': 'Tiêu đề phụ', 'original_content': '<table>...</table>'}, 'chunk_type': 'table', 'embedding_vector': np.random.rand(768)}
    ]

    DB_PATH = "./chroma_db_storage"
    vector_store = VectorStoreHandler(persist_directory=DB_PATH)

    collection = vector_store.create_or_get_collection(collection_name="Public_Test_001")

    if collection:
        print("\n--- Bắt đầu thêm chunks vào vector store ---")
        vector_store.add_chunks_to_collection(collection, sample_chunks_with_embeddings)
        print("--- Thêm chunks hoàn tất ---")
        
        print("\n--- Kiểm tra bằng cách truy vấn thử ---")
        results = collection.query(
            query_embeddings=[sample_chunks_with_embeddings[0]['embedding_vector'].tolist()],
            n_results=2 
        )
        
        print("Kết quả truy vấn:")
        import json
        print(json.dumps(results['metadatas'], indent=2, ensure_ascii=False))