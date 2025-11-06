# Bước 2: Chunking, Embedding và Indexing

## Mục tiêu

Module này chịu trách nhiệm biến đổi dữ liệu đã được trích xuất từ Bước 1 (dạng file `.md` và thư mục `images/`) thành một **cơ sở dữ liệu vector (Vector Store)** có cấu trúc, giàu ngữ cảnh và sẵn sàng cho việc truy vấn ở Bước 3.

Đây là bước xử lý trung tâm, tạo ra "bộ não" cho hệ thống Question-Answering.

---

## Luồng xử lý (Pipeline)

Quy trình được tự động hóa thông qua file `main_step2.py` và bao gồm 4 giai đoạn chính:

1.  **Phân tích Cấu trúc (Parsing):**
    *   **File:** `parser.py`
    *   **Mô tả:** Đọc file `main.md` và "bóc tách" nó thành các khối nội dung riêng biệt như: Tiêu đề (`heading`), Đoạn văn (`paragraph`), Bảng (`html_table`), Công thức (`latex_formula`) và Hình ảnh (`image_placeholder`).

2.  **Chia nhỏ Thông minh (Chunking):**
    *   **File:** `chunker.py`
    *   **Mô tả:** Tạo ra các "chunk" (mẩu dữ liệu) từ các khối đã phân tích. Điểm quan trọng là mỗi chunk văn bản được tự động bổ sung ngữ cảnh từ các tiêu đề cha của nó, giúp tăng độ chính xác khi tìm kiếm.

3.  **Vector hóa (Embedding):**
    *   **File:** `embedder.py`
    *   **Mô tả:** Sử dụng các mô hình AI để chuyển đổi mỗi chunk thành một vector số học đại diện cho ý nghĩa ngữ nghĩa của nó. Hệ thống tự động sử dụng model phù hợp cho văn bản và hình ảnh.

4.  **Lưu trữ & Lập chỉ mục (Indexing):**
    *   **File:** `vector_store_handler.py`
    *   **Mô tả:** Lưu tất cả các vector và thông tin metadata (ngữ cảnh, nội dung gốc, đường dẫn ảnh,...) vào ChromaDB, tạo ra một file index bền vững trên đĩa cứng.

---

## Cấu trúc thư mục

```
step2_chunking_embedding/
├── README.md               <-- File này
├── parser.py               <-- Logic phân tích file .md
├── chunker.py              <-- Logic chia chunks thông minh
├── embedder.py             <-- Logic tạo vector embedding
├── vector_store_handler.py <-- Logic lưu trữ vào ChromaDB
└── main_step2.py           <-- File chính để chạy toàn bộ pipeline
```

---

## Cài đặt

Tất cả các thư viện cần thiết cho bước này nên được thêm vào file `requirements.txt` ở thư mục gốc. Để cài đặt riêng lẻ, chạy lệnh sau (đảm bảo môi trường ảo đã được kích hoạt):

```bash
pip install beautifulsoup4 sentence-transformers torch Pillow chromadb
```

---

## Cách sử dụng

Toàn bộ pipeline có thể được kích hoạt bằng cách chạy file `main_step2.py` từ **thư mục gốc của dự án**.

1.  **Chuẩn bị Input:** Đảm bảo bạn có một thư mục tài liệu đã được xử lý từ Bước 1, chứa file `main.md` và thư mục con `images/`.

2.  **Chỉnh sửa (nếu cần):** Mở file `main_step2.py` và thay đổi các biến trong khối `if __name__ == '__main__':` để trỏ đến đúng thư mục input và thư mục output mong muốn.
    ```python
    # Ví dụ trong main_step2.py
    DOCUMENT_INPUT_PATH = "path/to/your/document_folder"
    DB_OUTPUT_PATH = "path/to/your/chroma_db"
    ```

3.  **Chạy Pipeline:**
    ```bash
    python src/step2_chunking_embedding/main_step2.py
    ```

4.  **Kết quả:** Một thư mục cơ sở dữ liệu ChromaDB (ví dụ: `final_chroma_db`) sẽ được tạo ra tại đường dẫn bạn đã chỉ định. Đây chính là sản phẩm cuối cùng của Bước 2.

---

## Công nghệ sử dụng

*   **Ngôn ngữ:** Python 3
*   **Xử lý HTML:** `BeautifulSoup4`
*   **AI & Embedding:** `Sentence-Transformers`, `PyTorch`
*   **Cơ sở dữ liệu Vector:** `ChromaDB`
*   **Mô hình AI:**
    *   **Text:** `bkai-foundation-models/vietnamese-bi-encoder`
    *   **Image:** `clip-ViT-B-32`