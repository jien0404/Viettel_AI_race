import sqlite3
import json
import argparse
import os

def display_chunk(row: tuple):
    """
    In thông tin của một chunk (một hàng từ database) ra màn hình.
    """
    # Dữ liệu trong `row` tương ứng với thứ tự các cột trong câu lệnh SELECT
    chunk_id, doc_name, chunk_type, enriched_content, metadata_json = row

    print("=" * 80)
    print(f"  CHUNK ID: {chunk_id}")
    print(f"  DOCUMENT: {doc_name}")
    print(f"      TYPE: {chunk_type}")
    print("-" * 80)
    print("  ENRICHED CONTENT (Nội dung đã làm giàu):")
    # Thêm thụt lề để dễ đọc
    print("\n".join(f"    {line}" for line in enriched_content.split('\n')))
    print("-" * 80)

    # Parse chuỗi JSON trong metadata để in ra đẹp hơn
    try:
        metadata_dict = json.loads(metadata_json)
        # Dùng json.dumps với indent để pretty-print
        pretty_metadata = json.dumps(metadata_dict, indent=4, ensure_ascii=False)
        print("  METADATA:")
        print(pretty_metadata)
    except json.JSONDecodeError:
        print("  METADATA (Không thể parse JSON):")
        print(metadata_json)
    
    print("=" * 80 + "\n")


def read_data_from_db(db_file: str, limit: int):
    """
    Kết nối tới database, đọc dữ liệu và gọi hàm để hiển thị.
    """
    if not os.path.exists(db_file):
        print(f"Lỗi: Không tìm thấy file database tại '{db_file}'")
        print("Vui lòng đảm bảo bạn đã chạy pipeline chính để tạo file này.")
        return

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        print(f"Đang đọc {limit} dòng đầu tiên từ bảng 'chunks'...")
        
        # Lấy tất cả các cột từ bảng, giới hạn số lượng dòng
        query = "SELECT id, doc_name, chunk_type, enriched_content, metadata FROM chunks LIMIT ?"
        
        cursor.execute(query, (limit,))
        
        rows = cursor.fetchall()

        if not rows:
            print("Không tìm thấy dữ liệu nào trong bảng 'chunks'.")
            return

        print(f"\nTìm thấy {len(rows)} chunk. Bắt đầu hiển thị:\n")
        for row in rows:
            display_chunk(row)

    except sqlite3.Error as e:
        print(f"Lỗi khi tương tác với SQLite: {e}")
    finally:
        if conn:
            conn.close()
            print("Đã đóng kết nối database.")


def main():
    parser = argparse.ArgumentParser(
        description="Đọc và hiển thị các chunk đã được làm giàu từ cơ sở dữ liệu SQLite."
    )
    
    parser.add_argument(
        "db_file", 
        type=str,
        default="bm25_database.sqlite",
        nargs='?', # Dấu '?' làm cho argument này là tùy chọn, và sẽ lấy giá trị từ 'default' nếu không được cung cấp
        help="Đường dẫn tới file database SQLite (mặc định: bm25_database.sqlite)."
    )
    
    parser.add_argument(
        "-n", "--limit", 
        type=int, 
        default=5,
        help="Số lượng chunk cần hiển thị (mặc định: 5)."
    )

    args = parser.parse_args()
    
    read_data_from_db(args.db_file, args.limit)


if __name__ == "__main__":
    main()