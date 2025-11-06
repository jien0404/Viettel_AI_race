import os
import sys
import time

sys.path.append(os.getcwd())

from src.step2_chunking_embedding.parser import parse_document
from src.step2_chunking_embedding.chunker import create_chunks
from src.step2_chunking_embedding.embedder import Embedder
from src.step2_chunking_embedding.vector_store_handler import VectorStoreHandler

INPUT_DIRECTORY = "data/raw/output" 
DB_OUTPUT_DIRECTORY = "chroma_database" 
MASTER_COLLECTION_NAME = "all_documents_training"

TEXT_COLLECTION_NAME = "text_chunks_collection"
IMAGE_COLLECTION_NAME = "image_chunks_collection"

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

    # (SỬA ĐỔI) Tạo ra hai collection riêng biệt
    text_collection = vector_store.create_or_get_collection(collection_name=TEXT_COLLECTION_NAME)
    image_collection = vector_store.create_or_get_collection(collection_name=IMAGE_COLLECTION_NAME)
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
            
            # (SỬA ĐỔI) Truyền thêm `doc_folder_path`
            chunks = create_chunks(parsed_blocks, doc_name=doc_name, doc_folder_path=folder_path)
            
            chunks_with_embeddings = embedder.embed_chunks(chunks)
            
            # --- (SỬA ĐỔI LỚN) Tách chunks thành hai danh sách riêng biệt ---
            text_based_chunks = []
            image_based_chunks = []
            for chunk in chunks_with_embeddings:
                if 'embedding_vector' not in chunk: # Bỏ qua nếu chunk không có embedding
                    continue
                
                chunk_type = chunk.get('chunk_type')
                if chunk_type in ['text', 'table', 'formula']:
                    text_based_chunks.append(chunk)
                elif chunk_type == 'image':
                    image_based_chunks.append(chunk)
            
            # Thêm vào các collection tương ứng
            if text_based_chunks:
                print(f"Thêm {len(text_based_chunks)} text chunks vào collection '{TEXT_COLLECTION_NAME}'...")
                vector_store.add_chunks_to_collection(text_collection, text_based_chunks)
            
            if image_based_chunks:
                print(f"Thêm {len(image_based_chunks)} image chunks vào collection '{IMAGE_COLLECTION_NAME}'...")
                vector_store.add_chunks_to_collection(image_collection, image_based_chunks)

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
    print(f"Dữ liệu đã được lưu vào các collection: '{TEXT_COLLECTION_NAME}', '{IMAGE_COLLECTION_NAME}'")
    print(f"Trong cơ sở dữ liệu tại: '{DB_OUTPUT_DIRECTORY}'")
    print("=====================================================")

if __name__ == '__main__':
    run_full_pipeline()