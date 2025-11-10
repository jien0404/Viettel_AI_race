import sqlite3
import json
from typing import List, Dict, Any

class SQLiteHandler:
    def __init__(self, db_file: str):
        """
        Khởi tạo handler và kết nối đến file SQLite.
        :param db_file: Đường dẫn đến file cơ sở dữ liệu SQLite.
        """
        self.db_file = db_file
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
            print(f"Kết nối thành công tới cơ sở dữ liệu SQLite tại: '{db_file}'")
        except sqlite3.Error as e:
            print(f"Lỗi khi kết nối tới SQLite: {e}")

    def create_table(self):
        """
        Tạo bảng 'chunks' nếu nó chưa tồn tại.
        Bảng này sẽ lưu trữ các chunk đã được làm giàu.
        """
        if not self.conn:
            return
            
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS chunks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doc_name TEXT NOT NULL,
            chunk_type TEXT NOT NULL,
            enriched_content TEXT NOT NULL,
            metadata TEXT
        );
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(create_table_sql)
            self.conn.commit()
            print("Bảng 'chunks' đã được kiểm tra/tạo thành công.")
        except sqlite3.Error as e:
            print(f"Lỗi khi tạo bảng: {e}")

    def add_chunks(self, chunks: List[Dict[str, Any]]):
        """
        Thêm một danh sách các chunk vào cơ sở dữ liệu.
        :param chunks: Danh sách các dictionary, mỗi dictionary là một chunk.
        """
        if not self.conn or not chunks:
            return

        insert_sql = """
        INSERT INTO chunks (doc_name, chunk_type, enriched_content, metadata)
        VALUES (?, ?, ?, ?);
        """
        
        chunks_to_insert = []
        for chunk in chunks:
            # Chuyển metadata (dictionary) thành một chuỗi JSON để lưu trữ
            metadata_str = json.dumps(chunk.get('metadata', {}), ensure_ascii=False)
            
            chunks_to_insert.append((
                chunk.get('doc_name'),
                chunk.get('chunk_type'),
                chunk.get('enriched_content'),
                metadata_str
            ))
        
        try:
            cursor = self.conn.cursor()
            cursor.executemany(insert_sql, chunks_to_insert)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Lỗi khi thêm chunk vào SQLite: {e}")

    def __del__(self):
        """Đóng kết nối khi đối tượng bị hủy."""
        if self.conn:
            self.conn.close()
            
    def get_existing_chunk_identifiers(self, doc_name: str) -> set:
        """Lấy một set các định danh của chunk đã có trong DB cho một tài liệu."""
        if not self.conn:
            return set()
        
        query = "SELECT metadata FROM chunks WHERE doc_name = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (doc_name,))
        
        existing_ids = set()
        for row in cursor.fetchall():
            # Tạo một định danh duy nhất cho chunk dựa trên nội dung gốc
            # Đây là một cách đơn giản, bạn có thể làm phức tạp hơn
            metadata = json.loads(row[0])
            content_identifier = str(metadata.get('original_blocks'))
            existing_ids.add(content_identifier)
            
        return existing_ids
    
    def _load_corpus_from_sqlite(self, db_path: str) -> List[Dict[str, Any]]:
        """
        Đọc toàn bộ các chunk từ file SQLite, lấy tất cả các cột cần thiết
        và tái cấu trúc lại dữ liệu.
        """
        corpus_data = []
        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                # === SỬA ĐỔI Ở ĐÂY: Lấy thêm cột doc_name và chunk_type ===
                cursor.execute("SELECT doc_name, chunk_type, enriched_content, metadata FROM chunks")
                
                for row in cursor.fetchall():
                    # Lấy dữ liệu từ các cột tương ứng
                    doc_name, chunk_type, enriched_content, metadata_str = row
                    
                    # Parse metadata từ chuỗi JSON
                    metadata = json.loads(metadata_str)
                    
                    # "Bơm" lại các thông tin còn thiếu vào dictionary metadata
                    # để phần còn lại của chương trình có thể sử dụng
                    metadata['doc_name'] = doc_name
                    metadata['chunk_type'] = chunk_type
                    original_blocks = metadata.get('original_blocks', [])
                    
                    # Tạo cấu trúc dữ liệu cuối cùng mà chương trình mong đợi
                    corpus_data.append({
                        'enriched_content': enriched_content,
                        'original_blocks': original_blocks,
                        'metadata': metadata
                    })
        except Exception as e:
            print(f"LỖI: không thể đọc file database '{db_path}': {e}")
        return corpus_data