import os
import sys
import time
import json

sys.path.append(os.getcwd())

from src.step2_context_enrichment.parser import parse_document
from src.step2_context_enrichment.chunker import create_chunks
from src.step2_context_enrichment.context_enricher import ContextEnricher
from src.step2_context_enrichment.sqlite_handler import SQLiteHandler

INPUT_DIRECTORY = "private_submission" 
DB_OUTPUT_FILE = "bm25_database_private.sqlite" 

def run_full_pipeline():
    """
    Pipeline hoàn chỉnh để phân tích, làm giàu ngữ cảnh và lưu trữ các chunk.
    """
    doc_folders = [f.path for f in os.scandir(INPUT_DIRECTORY) if f.is_dir()]
    
    if not doc_folders:
        print(f"LỖI: Không tìm thấy thư mục tài liệu nào bên trong '{INPUT_DIRECTORY}'.")
        return

    total_docs = len(doc_folders)
    print(f"Tìm thấy tổng cộng {total_docs} tài liệu để xử lý.")
    
    print("\nKhởi tạo các công cụ xử lý (Context Enricher, SQLite Handler)...")
    # Khởi tạo mô hình VLM để làm giàu ngữ cảnh
    enricher = ContextEnricher()
    # Khởi tạo handler để lưu vào SQLite
    db_handler = SQLiteHandler(db_file=DB_OUTPUT_FILE)
    db_handler.create_table()
    print("Khởi tạo hoàn tất.\n")
    
    start_time_full = time.time()

    for i, folder_path in enumerate(doc_folders):
        doc_name = os.path.basename(os.path.normpath(folder_path))
        print(f"--- Đang xử lý tài liệu {i+1}/{total_docs}: {doc_name} ---")
        try:
            md_file_path = os.path.join(folder_path, 'main.md')
            
            # Bước 1: Parse file markdown thành các block
            parsed_blocks = parse_document(md_file_path)
            if not parsed_blocks:
                print(f"Cảnh báo: File rỗng hoặc không phân tích được. Bỏ qua.")
                continue
            
            # Bước 2: Tạo các chunk ban đầu từ block
            chunks = create_chunks(parsed_blocks, doc_name=doc_name)
            print(f"Đã tạo {len(chunks)} chunk ban đầu.")
            
            # --- LOGIC CACHING MỚI ---
            existing_chunk_ids = db_handler.get_existing_chunk_identifiers(doc_name)
            chunks_to_process = []
            for chunk in chunks:
                identifier = str(chunk['metadata'].get('original_blocks'))
                if identifier not in existing_chunk_ids:
                    chunks_to_process.append(chunk)
            
            print(f"Phát hiện {len(existing_chunk_ids)} chunk đã được xử lý. Còn lại {len(chunks_to_process)} chunk cần làm giàu.")
            # --- KẾT THÚC LOGIC CACHING ---
            
            if not chunks_to_process:
                print("Tất cả các chunk trong tài liệu này đã được xử lý. Bỏ qua.")
                continue
            
            # Bước 3: Làm giàu ngữ cảnh cho từng chunk bằng VLM
            print("Bắt đầu làm giàu ngữ cảnh cho các chunk...")
            enriched_chunks = enricher.enrich_chunks_with_llm(chunks, folder_path)
            print("Làm giàu ngữ cảnh hoàn tất.")

            # Bước 4: Lưu các chunk đã làm giàu vào SQLite
            db_handler.add_chunks(enriched_chunks)
            print(f"Đã lưu {len(enriched_chunks)} chunk vào cơ sở dữ liệu SQLite.")

        except Exception as e:
            print(f"\n!!!! GẶP LỖI khi xử lý tài liệu '{doc_name}' !!!!")
            print(f"Lỗi chi tiết: {e}")
            print("Tiếp tục với tài liệu tiếp theo...\n")
            continue
        print(f"--- Hoàn tất xử lý {doc_name} ---\n")

    end_time_full = time.time()
    print("\n==========================================================")
    print(f"===   HOÀN TẤT TOÀN BỘ PIPELINE LÀM GIÀU NGỮ CẢNH   ===")
    print(f"Đã xử lý {total_docs} tài liệu trong {end_time_full - start_time_full:.2f} giây.")
    print(f"Tất cả dữ liệu đã được lưu vào file: '{DB_OUTPUT_FILE}'")
    print("Cơ sở dữ liệu đã sẵn sàng cho việc retrieval bằng BM25.")
    print("==========================================================")

if __name__ == '__main__':
    run_full_pipeline()