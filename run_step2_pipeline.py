import os
import sys
import time

sys.path.append(os.getcwd())

from src.step2_chunking_embedding.parser import parse_document
from src.step2_chunking_embedding.chunker import create_chunks
from src.step2_chunking_embedding.embedder import Embedder
from src.step2_chunking_embedding.vector_store_handler import VectorStoreHandler

INPUT_DIRECTORY = "submission" 
DB_OUTPUT_DIRECTORY = "chroma_database" 
MASTER_COLLECTION_NAME = "all_documents"

def run_full_pipeline():
    
    doc_folders = [f.path for f in os.scandir(INPUT_DIRECTORY) if f.is_dir()]
    
    if not doc_folders:
        print(f"LỖI: Không tìm thấy thư mục tài liệu nào bên trong '{INPUT_DIRECTORY}'.")
        return

    total_docs = len(doc_folders)
    print(f"Tìm thấy tổng cộng {total_docs} tài liệu để xử lý.")
    
    print("\nKhởi tạo các công cụ xử lý (Embedder, Vector Store)...")
    embedder = Embedder()

    vector_store = VectorStoreHandler(persist_directory=DB_OUTPUT_DIRECTORY)
    master_collection = vector_store.create_or_get_collection(collection_name=MASTER_COLLECTION_NAME)
    print("Khởi tạo hoàn tất.\n")
    
    start_time_full = time.time()

    for i, folder_path in enumerate(doc_folders):
        doc_name = os.path.basename(os.path.normpath(folder_path))
        print(f"--- Đang xử lý tài liệu {i+1}/{total_docs}: {doc_name} ---")
        try:
            md_file_path = os.path.join(folder_path, 'main.md')
            parsed_blocks = parse_document(md_file_path)
            if not parsed_blocks:
                print(f"Cảnh báo: File rỗng hoặc không phân tích được. Bỏ qua.")
                continue
            
            chunks = create_chunks(parsed_blocks, doc_name=doc_name)
            
            chunks_with_embeddings = embedder.embed_chunks(chunks)
            
            vector_store.add_chunks_to_collection(master_collection, chunks_with_embeddings)

        except Exception as e:
            print(f"\n!!!! GẶP LỖI khi xử lý tài liệu '{doc_name}' !!!!")
            print(f"Lỗi chi tiết: {e}")
            print("Tiếp tục với tài liệu tiếp theo...\n")
            continue
        print(f"--- Hoàn tất xử lý {doc_name} ---\n")

    end_time_full = time.time()
    print("\n=====================================================")
    print(f"===   HOÀN TẤT TOÀN BỘ PIPELINE BƯỚC 2   ===")
    print(f"Đã xử lý {total_docs} tài liệu trong {end_time_full - start_time_full:.2f} giây.")
    print(f"Tất cả dữ liệu đã được lưu vào collection '{MASTER_COLLECTION_NAME}'")
    print(f"Trong cơ sở dữ liệu tại: '{DB_OUTPUT_DIRECTORY}'")
    print("=====================================================")

if __name__ == '__main__':
    run_full_pipeline()