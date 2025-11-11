### Cấu trúc thư mục
```code
Viettel_AI_Race_NLP/
├── .gitignore
├── README.md
├── data/
│   └── raw/ (dữ liệu thô)
│   └── processed/ (dữ liệu đã xử lý)
├── data_test_w2_w3/ (test set của của giai đoạn 2 và 3)
├── submission_template/
├── src/
│   ├── step1_pdf_processing/ (cho Bước 1 - Dũng)
│   │   └── process_pdf.py
│   │   └── images/ (thư mục lưu ảnh)
│   ├── step2_chunking_embedding/ (cho Bước 2 - Minh)
│   │   └── chunking_data.py
│   │   └── embedding_index.py
│   ├── step3_retrieval_qa/ (cho Bước 3 - Chiến)
│       └── retrieval.py
│       └── qa_generation.py
├── task1_extract.py
├── task1_extract.sh
├── task2_QA.py
├── task2_QA.sh
├── requirements.txt
```


### Lưu ý: 
- public_test của gd 3 chính là private_test của qd 2
- public_test của gd 4 chính là private_test của qd 3

### Chạy chương trình 
1. Tạo môi trường ảo
2. Cài thư viện
```bash 
pip install -r requirements.txt
```
3. Tải data tại: https://drive.google.com/drive/folders/1WDXPWaMIJL6FM7k4cAiGPV04eFGoNaQA?usp=sharing rồi giải nén vào thư mục gốc
4. Chạy step 3
```bash
python run_step3_pipeline.py
