import sqlite3
import json
import os
import argparse

def check_database_format(db_file: str, limit: int):
    """
    Kết nối tới database, đọc và kiểm tra định dạng của một vài chunk.
    """
    if not os.path.exists(db_file):
        print(f"LỖI: Không tìm thấy file database tại '{db_file}'")
        return

    print(f"--- Bắt đầu kiểm tra file database: {db_file} ---")
    
    try:
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            query = "SELECT enriched_content, metadata FROM chunks LIMIT ?"
            cursor.execute(query, (limit,))
            rows = cursor.fetchall()

            if not rows:
                print("Database không có dữ liệu nào trong bảng 'chunks'.")
                return

            print(f"Đã lấy được {len(rows)} chunk để kiểm tra.\n")

            for i, row in enumerate(rows):
                print("=" * 50)
                print(f"  KIỂM TRA CHUNK #{i + 1}")
                print("=" * 50)

                enriched_content, metadata_str = row
                
                # --- Kiểm tra enriched_content ---
                print("[1] Kiểm tra 'enriched_content':")
                if isinstance(enriched_content, str) and enriched_content:
                    print("  [PASS] 'enriched_content' là một chuỗi không rỗng.")
                    print(f"  Nội dung (50 ký tự đầu): '{enriched_content[:50]}...'")
                else:
                    print("  [FAIL] 'enriched_content' không hợp lệ (rỗng hoặc không phải chuỗi).")
                
                print("-" * 20)

                # --- Kiểm tra metadata ---
                print("[2] Kiểm tra 'metadata':")
                metadata = None
                try:
                    metadata = json.loads(metadata_str)
                    print("  [PASS] Chuỗi metadata đã được parse thành công sang JSON.")
                except (json.JSONDecodeError, TypeError):
                    print("  [FAIL] Không thể parse chuỗi metadata thành JSON.")
                    print(f"  Dữ liệu metadata gốc: {metadata_str}")
                    continue # Bỏ qua các kiểm tra sâu hơn nếu không parse được

                if isinstance(metadata, dict):
                    print("  [PASS] Metadata là một dictionary.")
                    print("  Các keys có trong metadata:", list(metadata.keys()))

                    # Kiểm tra các key quan trọng bên trong metadata
                    chunk_type = metadata.get('chunk_type')
                    if isinstance(chunk_type, str):
                        print(f"  [PASS] Key 'chunk_type' tồn tại với giá trị: '{chunk_type}'")
                        
                        # Kiểm tra có điều kiện cho 'image_path'
                        if chunk_type == 'image_context':
                            image_path = metadata.get('image_path')
                            if isinstance(image_path, str):
                                print("  [PASS] 'chunk_type' là image_context và key 'image_path' tồn tại.")
                            else:
                                print("  [FAIL] 'chunk_type' là image_context nhưng key 'image_path' bị thiếu hoặc không phải chuỗi.")
                    else:
                        print("  [FAIL] Key 'chunk_type' bị thiếu hoặc không phải là chuỗi.")

                    doc_name = metadata.get('doc_name')
                    if isinstance(doc_name, str):
                        print(f"  [PASS] Key 'doc_name' tồn tại với giá trị: '{doc_name}'")
                    else:
                        print("  [FAIL] Key 'doc_name' bị thiếu hoặc không phải là chuỗi.")

                else:
                    print("  [FAIL] Dữ liệu metadata sau khi parse không phải là dictionary.")
                
                print("\n")

    except sqlite3.Error as e:
        print(f"LỖI khi thao tác với SQLite: {e}")

def main():
    parser = argparse.ArgumentParser(description="Kiểm tra định dạng dữ liệu trong database SQLite.")
    parser.add_argument(
        "db_file", 
        type=str,
        default="bm25_database.sqlite",
        nargs='?',
        help="Đường dẫn tới file database (mặc định: bm25_database.sqlite)."
    )
    parser.add_argument(
        "-n", "--limit", 
        type=int, 
        default=5,
        help="Số lượng chunk cần kiểm tra (mặc định: 5)."
    )
    args = parser.parse_args()
    check_database_format(args.db_file, args.limit)

if __name__ == '__main__':
    main()