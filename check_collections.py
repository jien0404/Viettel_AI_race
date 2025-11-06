import chromadb

DB_PATH = "chroma_database"

try:
    # Kết nối tới cơ sở dữ liệu ChromaDB đã tồn tại
    client = chromadb.PersistentClient(path=DB_PATH)

    # Lấy danh sách tất cả các collection
    collections = client.list_collections()

    if not collections:
        print(f"Không tìm thấy BẤT KỲ collection nào trong cơ sở dữ liệu tại '{DB_PATH}'.")
        print("Điều này có nghĩa là Bước 2 có thể đã chạy nhưng gặp lỗi trước khi tạo collection.")
        print("Vui lòng chạy lại 'run_step2_pipeline.py' và kiểm tra log thật kỹ.")
    else:
        print(f"Đã tìm thấy các collection sau trong '{DB_PATH}':")
        for collection in collections:
            # In ra tên và số lượng mục trong mỗi collection
            print(f"- Tên: '{collection.name}', Số lượng mục: {collection.count()}")

except Exception as e:
    print(f"Đã xảy ra lỗi khi kết nối hoặc đọc cơ sở dữ liệu: {e}")
    print(f"Hãy chắc chắn rằng bạn đang chạy script này từ thư mục gốc của dự án (VIETTEL_AI_RACE).")