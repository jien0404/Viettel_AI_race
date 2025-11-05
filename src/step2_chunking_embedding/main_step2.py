import os
import time

from parser import parse_document
from chunker import create_chunks
from embedder import Embedder
from vector_store_handler import VectorStoreHandler

def process_document_pipeline(doc_folder_path: str, db_path: str):
    start_time = time.time()
    
    doc_name = os.path.basename(os.path.normpath(doc_folder_path))
    print(f"--- BẮT ĐẦU XỬ LÝ TÀI LIỆU: {doc_name} ---")

    # ----- Giai đoạn 1: Parsing -----
    md_file_path = os.path.join(doc_folder_path, 'main.md')
    print(f"\n[1/4] Đang phân tích file: {md_file_path}...")
    parsed_blocks = parse_document(md_file_path)
    if not parsed_blocks:
        print("Phân tích thất bại hoặc file rỗng. Dừng pipeline.")
        return
    print(f">>> Phân tích hoàn tất. Tìm thấy {len(parsed_blocks)} khối nội dung.")

    # ----- Giai đoạn 2: Chunking -----
    print("\n[2/4] Đang tạo chunks từ các khối nội dung...")
    chunks = create_chunks(parsed_blocks, doc_name=doc_name)
    print(f">>> Tạo chunk hoàn tất. Tạo ra {len(chunks)} chunks.")

    # ----- Giai đoạn 3: Embedding -----
    print("\n[3/4] Đang tạo vector embeddings...")
    embedder = Embedder()
    chunks_with_embeddings = embedder.embed_chunks(chunks)
    print(">>> Tạo embedding hoàn tất.")

    # ----- Giai đoạn 4: Lưu vào Vector Store -----
    print("\n[4/4] Đang lưu trữ vào Vector Store...")
    vector_store = VectorStoreHandler(persist_directory=db_path)
    collection = vector_store.create_or_get_collection(collection_name=doc_name)
    if collection:
        vector_store.add_chunks_to_collection(collection, chunks_with_embeddings)
    print(">>> Lưu trữ hoàn tất.")

    end_time = time.time()
    print(f"\n--- HOÀN TẤT XỬ LÝ TÀI LIỆU {doc_name} TRONG {end_time - start_time:.2f} GIÂY ---")

# --- MAIN ĐỂ KIỂM THỬ ---
if __name__ == '__main__':
    DUMMY_DOC_FOLDER = "dummy_document"
    DUMMY_IMAGES_FOLDER = os.path.join(DUMMY_DOC_FOLDER, "images")
    DB_STORAGE_PATH = "final_chroma_db"

    os.makedirs(DUMMY_IMAGES_FOLDER, exist_ok=True)

    dummy_md_content = """
# Tiêu đề Thử nghiệm
Một đoạn văn bản.
|<image_1>|
"""
    with open(os.path.join(DUMMY_DOC_FOLDER, "main.md"), "w", encoding="utf-8") as f:
        f.write(dummy_md_content)

    process_document_pipeline(
        doc_folder_path=DUMMY_DOC_FOLDER, 
        db_path=DB_STORAGE_PATH
    )

    if os.path.exists(DB_STORAGE_PATH):
        print(f"\nKiểm tra thành công: Thư mục Vector Store đã được tạo tại '{DB_STORAGE_PATH}'")