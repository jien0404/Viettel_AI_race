import os
import sys
import time

sys.path.append(os.getcwd())

from src.step2_chunking_embedding.parser import parse_document
from src.step2_chunking_embedding.chunker import create_chunks
from src.step2_chunking_embedding.embedder import Embedder
from src.step2_chunking_embedding.vector_store_handler import VectorStoreHandler

INPUT_DIRECTORY = "private_submission" 
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
    # Ghi chú: ta không dùng single master_collection cố định nữa.
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
            
            # Tạo embedding (chú ý: embedder sẽ gán 'embedding_vector' vào mỗi chunk)
            chunks_with_embeddings = embedder.embed_chunks(chunks)

            # --- BƯỚC KIỂM TRA + NHÓM THEO DIMENSION ---
            # Lọc những chunk có embedding
            chunks_valid = []
            chunks_invalid = []
            for c in chunks_with_embeddings:
                if 'embedding_vector' in c and getattr(c['embedding_vector'], 'shape', None) is not None:
                    # đảm bảo là numpy array hoặc list -> chuẩn hóa về 1D numpy
                    chunks_valid.append(c)
                else:
                    chunks_invalid.append(c)

            if chunks_invalid:
                print(f"Cảnh báo: {len(chunks_invalid)} chunk không có embedding, sẽ bị bỏ qua khi thêm vào DB.")

            # Nhóm theo chiều embedding (số chiều = len vector)
            from collections import defaultdict
            groups_by_dim = defaultdict(list)
            for c in chunks_valid:
                vec = c['embedding_vector']
                try:
                    dim = int(getattr(vec, 'shape', (len(vec),))[0])
                except Exception:
                    # fallback nếu vec là list
                    try:
                        dim = len(vec)
                    except Exception:
                        print("Cảnh báo: Không thể xác định dimension cho 1 chunk, bỏ qua.")
                        continue
                groups_by_dim[dim].append(c)

            # Nếu không có nhóm nào (không có embedding hợp lệ) thì bỏ qua
            if not groups_by_dim:
                print("Không có embedding hợp lệ để thêm vào collection. Tiếp tục tài liệu tiếp theo.")
                continue

            # Với mỗi nhóm dimension, tạo collection riêng (hoặc lấy lại nếu đã có)
            for dim, group_chunks in groups_by_dim.items():
                coll_name = f"{MASTER_COLLECTION_NAME}_dim_{dim}"
                collection = vector_store.create_or_get_collection(collection_name=coll_name)
                print(f"Thêm {len(group_chunks)} chunk vào collection '{coll_name}' (dimension={dim})...")
                try:
                    vector_store.add_chunks_to_collection(collection, group_chunks)
                except Exception as e:
                    # Bắt lỗi cụ thể khi thêm batch vẫn gặp lỗi (ví dụ do vectorstore nội bộ)
                    print(f"LỖI khi thêm batch vào collection '{coll_name}': {e}")
                    # Thử thêm từng chunk một — chậm hơn nhưng an toàn
                    for c in group_chunks:
                        try:
                            vector_store.add_chunks_to_collection(collection, [c])
                        except Exception as e2:
                            print(f"-> LỖI khi thêm 1 chunk (bỏ qua): {e2}")
                    print("Tiếp tục...")

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