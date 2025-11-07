import chromadb
import numpy as np
from typing import List, Dict, Any
import time
import traceback

class VectorStoreHandler:
    def __init__(self, persist_directory: str):
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.persist_directory = persist_directory
        print(f"Khởi tạo ChromaDB client. Dữ liệu sẽ được lưu tại: '{persist_directory}'", flush=True)

    def create_or_get_collection(self, collection_name: str):
        try:
            collection = self.client.get_or_create_collection(name=collection_name)
            print(f"Đã tải/tạo thành công collection: '{collection_name}'", flush=True)
            return collection
        except Exception as e:
            print(f"Lỗi khi tạo hoặc lấy collection: {e}", flush=True)
            return None

    def add_chunks_to_collection(self, collection, chunks: List[Dict[str, Any]]):
        if not chunks:
            print("Không có chunk nào để thêm.", flush=True)
            return

        batch_size = 100 
        doc_name = chunks[0].get('doc_name', 'unknown_doc')

        for start in range(0, len(chunks), batch_size):
            batch_chunks = chunks[start:start+batch_size]
            
            ids = [f"{doc_name}_{start+j}" for j in range(len(batch_chunks))]
            embeddings = [chunk['embedding_vector'].tolist() if hasattr(chunk['embedding_vector'], 'tolist') else chunk['embedding_vector'] for chunk in batch_chunks]
            metadatas = [chunk['metadata'] for chunk in batch_chunks]

            try:
                t0 = time.time()
                print(f"Adding batch to collection (doc={doc_name}) start={start} size={len(batch_chunks)} ...", flush=True)
                collection.add(
                    embeddings=embeddings,
                    metadatas=metadatas,
                    ids=ids
                )
                print(f"Đã thêm thành công batch từ {start} đến {start+len(batch_chunks)} trong {time.time()-t0:.2f}s.", flush=True)
            except Exception as e:
                print(f"Lỗi khi thêm batch vào collection: {e}", flush=True)
                traceback.print_exc()