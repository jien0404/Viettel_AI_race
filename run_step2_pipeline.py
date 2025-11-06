import os
import sys
import glob
import time


sys.path.append(os.getcwd())

from src.step2_chunking_embedding.main_step2 import process_document_pipeline


INPUT_DIRECTORY = "submission" 

DB_OUTPUT_DIRECTORY = "chroma_database" 

def run_full_pipeline():

    print("=====================================================")
    print("===   BẮT ĐẦU PIPELINE BƯỚC 2: CHUNKING & EMBEDDING   ===")
    print("=====================================================")
    

    doc_folders = [f.path for f in os.scandir(INPUT_DIRECTORY) if f.is_dir()]
    
    if not doc_folders:
        print(f"LỖI: Không tìm thấy thư mục tài liệu nào bên trong '{INPUT_DIRECTORY}'.")
        print("Vui lòng kiểm tra lại cấu trúc thư mục.")
        return

    total_docs = len(doc_folders)
    print(f"Tìm thấy tổng cộng {total_docs} tài liệu để xử lý.\n")
    
    start_time_full = time.time()

    for i, folder_path in enumerate(doc_folders):
        print(f"--- Đang xử lý tài liệu {i+1}/{total_docs} ---")
        try:
            process_document_pipeline(
                doc_folder_path=folder_path, 
                db_path=DB_OUTPUT_DIRECTORY
            )
        except Exception as e:
            doc_name = os.path.basename(folder_path)
            print(f"\n!!!! GẶP LỖI khi xử lý tài liệu '{doc_name}' !!!!")
            print(f"Lỗi chi tiết: {e}")
            print("Tiếp tục với tài liệu tiếp theo...\n")
            continue

    end_time_full = time.time()
    print("\n=====================================================")
    print(f"===   HOÀN TẤT TOÀN BỘ PIPELINE BƯỚC 2   ===")
    print(f"Tổng thời gian xử lý: {end_time_full - start_time_full:.2f} giây")
    print(f"Cơ sở dữ liệu vector đã được lưu tại: '{DB_OUTPUT_DIRECTORY}'")
    print("=====================================================")


if __name__ == '__main__':
    run_full_pipeline()