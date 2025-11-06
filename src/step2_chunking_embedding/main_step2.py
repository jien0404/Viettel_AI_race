import os
import time

from .parser import parse_document
from .chunker import create_chunks
from .embedder import Embedder
from .vector_store_handler import VectorStoreHandler

def process_document_pipeline(doc_folder_path: str, db_path: str):
    start_time = time.time()
    
    doc_name = os.path.basename(os.path.normpath(doc_folder_path))
    print(f"--- BẮT ĐẦU XỬ LÝ TÀI LIỆU: {doc_name} ---")

    md_file_path = os.path.join(doc_folder_path, 'main.md')
    print(f"[1/4] Phân tích file: {md_file_path}...")
    parsed_blocks = parse_document(md_file_path)
    if not parsed_blocks:
        print(f"Cảnh báo: Phân tích thất bại hoặc file '{md_file_path}' rỗng. Bỏ qua tài liệu này.")
        return
    print(f">>> Hoàn tất. Tìm thấy {len(parsed_blocks)} khối nội dung.")

    print("[2/4] Tạo chunks...")
    chunks = create_chunks(parsed_blocks, doc_name=doc_name)
    print(f">>> Hoàn tất. Tạo ra {len(chunks)} chunks.")

    print("[3/4] Tạo vector embeddings...")
    embedder = Embedder() 
    chunks_with_embeddings = embedder.embed_chunks(chunks)
    print(">>> Hoàn tất.")

    print("[4/4] Lưu trữ vào Vector Store...")
    vector_store = VectorStoreHandler(persist_directory=db_path)
    collection = vector_store.create_or_get_collection(collection_name=doc_name)
    if collection:
        vector_store.add_chunks_to_collection(collection, chunks_with_embeddings)
    print(">>> Hoàn tất.")

    end_time = time.time()
    print(f"--- HOÀN TẤT {doc_name} TRONG {end_time - start_time:.2f} GIÂY ---\n")
