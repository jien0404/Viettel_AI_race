# Còn 2 vấn đề là: thêm các ví dụ các đáp án là các chữ cái, chỉ dẫn trả lời cho đúng (check lại xem đã truyền đáp án vào đúng kiểu A: abc chưa)
#                 xử lý các trường hợp đầu vào của model bị quá max length, thêm cơ chế nếu vượt quá thì giảm dần số lượng context đến khi vừa

import os
import re
import pandas as pd
import torch
import chromadb
from sentence_transformers import SentenceTransformer
from sentence_transformers.cross_encoder import CrossEncoder
from transformers import AutoTokenizer
from unsloth import FastLanguageModel
from typing import List, Dict, Any
from typing import Optional
import subprocess
import torch

def get_freest_gpu():
    """
    Tìm và trả về định danh của GPU có nhiều VRAM trống nhất.
    Sử dụng pynvml nếu có, nếu không thì fallback về việc phân tích `nvidia-smi`.
    """
    if not torch.cuda.is_available():
        return 'cpu'
    
    try:
        # Ưu tiên sử dụng pynvml vì ổn định hơn
        from pynvml import nvmlInit, nvmlDeviceGetCount, nvmlDeviceGetHandleByIndex, nvmlDeviceGetMemoryInfo, nvmlShutdown
        nvmlInit()
        device_count = nvmlDeviceGetCount()
        if device_count == 0:
            return 'cpu'
        
        max_free_mem = 0
        best_gpu_id = 0
        for i in range(device_count):
            handle = nvmlDeviceGetHandleByIndex(i)
            mem_info = nvmlDeviceGetMemoryInfo(handle)
            if mem_info.free > max_free_mem:
                max_free_mem = mem_info.free
                best_gpu_id = i
        nvmlShutdown()
        return f'cuda:{best_gpu_id}'
    except ImportError:
        # Phương án dự phòng: phân tích output của nvidia-smi
        print("Cảnh báo: Thư viện 'pynvml' không được tìm thấy. Sử dụng phương án dự phòng `nvidia-smi`. (pip install pynvml)")
        try:
            result = subprocess.check_output(['nvidia-smi', '--query-gpu=memory.free', '--format=csv,nounits,noheader'])
            free_memory = [int(x) for x in result.decode().strip().split('\n')]
            if not free_memory:
                 return 'cpu'
            best_gpu_id = free_memory.index(max(free_memory))
            return str(best_gpu_id) # Trả về ID dưới dạng chuỗi
        except (subprocess.CalledProcessError, FileNotFoundError):
            return "0" if torch.cuda.device_count() > 0 else "cpu"

# --- CẤU HÌNH ---
DB_PATH = "chroma_database"
COLLECTION_NAME = "all_documents"
QUESTIONS_FILE_PATH = "data/raw/private_test_data/input/question.csv"
OUTPUT_FILE_PATH = "private_submission/answer.md"

# Model dùng cho embedding câu hỏi (PHẢI GIỐNG model ở bước 2)
EMBEDDING_MODEL_NAME = 'bkai-foundation-models/vietnamese-bi-encoder'

# Model ngôn ngữ lớn để sinh câu trả lời (Qwen tối ưu bởi Unsloth)
LLM_MODEL_NAME = "unsloth/Qwen2.5-3B-Instruct-bnb-4bit"
# LLM_MODEL_NAME = "unsloth/Qwen3-4B-Instruct-2507"
RERANKER_MODEL_NAME = "thanhtantran/Vietnamese_Reranker"

# Số lượng context chunk sẽ truy xuất cho mỗi câu hỏi
NUM_RETRIEVED_CHUNKS = 50
TOP_N_AFTER_RERANK = 3 


def load_llm_model_and_tokenizer():
    """
    Tải mô hình ngôn ngữ lớn (LLM) và tokenizer đã được tối ưu hóa bằng Unsloth.
    """
    print(f"Đang tải mô hình LLM: {LLM_MODEL_NAME}...")
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=LLM_MODEL_NAME,
        max_seq_length= 16384,
        dtype=None, 
        load_in_4bit=True,
    )
    print("Tải mô hình LLM hoàn tất.")
    return model, tokenizer


class RetrieverQA:
    def __init__(self, db_path, collection_name, embedding_model_name, llm_model, tokenizer, device: str):
        self.device = device
        print(f"Sử dụng thiết bị được chỉ định: {self.device}")

        # 1. Khởi tạo ChromaDB client
        print("Đang kết nối tới ChromaDB...")
        self.db_client = chromadb.PersistentClient(path=db_path)
        self.base_collection_name = collection_name  # e.g. "all_documents"
        print("Kết nối tới ChromaDB hoàn tất.")

        # 2. Tải mô hình embedding (PHẢI GIỐNG BƯỚC 2)
        print(f"Đang tải mô hình embedding: {embedding_model_name}...")
        self.embedding_model = SentenceTransformer(embedding_model_name, device=self.device)
        print("Tải mô hình embedding hoàn tất.")

        # 2.a Tính dimension embedding (bằng cách encode chuỗi mẫu)
        try:
            sample_vec = self.embedding_model.encode("test sample", convert_to_tensor=False)
            # sample_vec có thể là list hoặc numpy array
            self.text_embedding_dim = len(sample_vec)
            print(f"Xác định embedding dimension cho text: {self.text_embedding_dim}")
        except Exception as e:
            print(f"Cảnh báo: Không xác định được embedding dim tự động: {e}")
            self.text_embedding_dim = None

        # 2.b Lấy collection tương ứng với dimension
        self.collection: Optional[Any] = None
        if self.text_embedding_dim is not None:
            coll_name = f"{self.base_collection_name}_dim_{self.text_embedding_dim}"
            try:
                self.collection = self.db_client.get_collection(name=coll_name)
                print(f"Kết nối thành công tới collection '{coll_name}'.")
            except Exception as e:
                print(f"Cảnh báo: Không tìm thấy collection '{coll_name}' trong DB: {e}")
                # Không raise, vẫn cho phép chạy (sẽ fallback trong retrieve_context)
        else:
            print("Cảnh báo: text_embedding_dim = None, sẽ không tự động lấy collection theo dim.")

        # 3. Tải Reranker
        print(f"Đang tải mô hình Reranker: {RERANKER_MODEL_NAME}...")
        self.reranker_model = CrossEncoder(RERANKER_MODEL_NAME, max_length=512, device=self.device)
        print("Tải mô hình Reranker hoàn tất.")
        
        # 4. Lưu LLM & tokenizer
        self.llm_model = llm_model
        self.tokenizer = tokenizer

    def retrieve_context(self, question: str, n_results: int, top_n_rerank: int) -> str:
        """
        Truy xuất ban đầu, sau đó rerank để lấy ngữ cảnh chính xác nhất.
        SỬA: chỉ query collection phù hợp dimension embedding text.
        """
        print(f"  - Đang truy xuất {n_results} ngữ cảnh ứng viên...")

        # 1) Tính embedding câu hỏi bằng chính model embedding (same as step 2)
        try:
            question_embedding = self.embedding_model.encode(question, convert_to_tensor=False).tolist()
        except Exception as e:
            print(f"Lỗi khi encode câu hỏi: {e}")
            return ""

        candidate_metadatas = []

        # 2) Nếu self.collection đã được set (collection đúng dim), query trực tiếp
        if self.collection is not None:
            try:
                results = self.collection.query(
                    query_embeddings=[question_embedding],
                    n_results=n_results,
                    include=["metadatas"]  # cần metadata chứa original_content & context_headings
                )
                candidate_metadatas = results.get('metadatas', [[]])[0]
            except Exception as e:
                print(f"Cảnh báo: Lỗi khi query collection '{self.collection.name if hasattr(self.collection,'name') else 'unknown'}': {e}")
                candidate_metadatas = []
        else:
            # 3) Fallback: dò các collection có pattern base_collection_name_dim_*
            print("  - Fallback: đang dò các collection theo pattern dimension...")
            try:
                all_collections = self.db_client.list_collections()  # trả về list dict (tùy chroma wrapper)
            except Exception:
                all_collections = []

            # Lọc các collection phù hợp (tên chứa base_collection_name)
            matched = []
            for coll in all_collections:
                # coll có thể là dict hoặc object tùy chromadb wrapper
                name = coll['name'] if isinstance(coll, dict) and 'name' in coll else getattr(coll, 'name', None)
                if name and name.startswith(self.base_collection_name + "_dim_"):
                    matched.append(name)

            # Query mỗi collection đã matched, gộp kết quả
            for name in matched:
                try:
                    coll = self.db_client.get_collection(name=name)
                    r = coll.query(query_embeddings=[question_embedding], n_results=n_results, include=["metadatas"])
                    m = r.get('metadatas', [[]])[0]
                    candidate_metadatas.extend(m)
                except Exception as e:
                    print(f"  - Cảnh báo: Không query được collection {name}: {e}")

        if not candidate_metadatas:
            print("  - Không tìm thấy ngữ cảnh ứng viên nào.")
            return ""

        # 4) Chuẩn bị pairs (question, chunk_content) cho reranker
        pairs = []
        for doc_meta in candidate_metadatas:
            # 'original_content' là metadata bạn đã lưu khi chunking
            content = doc_meta.get('original_content', '')
            # bạn có thể muốn thêm context_headings vào content để reranker hiểu thêm
            headings = doc_meta.get('context_headings', '')
            combined = f"{headings}\n{content}" if headings else content
            pairs.append([question, combined])

        # 5) Rerank
        print(f"  - Đang Rerank {len(pairs)} ứng viên để chọn ra top {top_n_rerank}...")
        scores = self.reranker_model.predict(pairs, show_progress_bar=False)

        # 6) Lấy top N sau rerank
        doc_scores = list(zip(candidate_metadatas, scores))
        doc_scores.sort(key=lambda x: x[1], reverse=True)
        final_docs = [doc for doc, score in doc_scores[:top_n_rerank]]

        # 7) Tạo chuỗi ngữ cảnh trả về
        context_str = ""
        for i, metadata in enumerate(final_docs):
            content = metadata.get('original_content', '')
            headings = metadata.get('context_headings', 'N/A')
            context_str += f"--- Ngữ cảnh tham khảo {i+1} ---\n"
            context_str += f"Tiêu đề liên quan: {headings}\n"
            context_str += f"Nội dung: {content}\n\n"

        return context_str.strip()

    def generate_answer(self, context: str, question: str, options: Dict[str, str]) -> str:
        """
        Tạo prompt chi tiết (có hướng dẫn và few-shot), đưa vào mô hình LLM và sinh câu trả lời.
        (Phiên bản cải tiến với thẻ [ANSWER])
        """
        print("  - Đang sinh câu trả lời bằng LLM (với prompt nâng cao)...")
        
        # Xây dựng phần lựa chọn trong prompt
        options_str = "\n".join([f"{key}: {value}" for key, value in options.items()])
        
        # --- PROMPT MỚI VỚI HƯỚNG DẪN CHI TIẾT VÀ THẺ ĐÁP ÁN ---
        prompt = f"""
Bạn là một **trợ lý QA tiếng Việt chuyên nghiệp**, được huấn luyện đặc biệt để xử lý **câu hỏi trắc nghiệm nhiều đáp án đúng**.

QUY TẮC BẮT BUỘC:
0. Câu trả lời cuối cùng **BẮT BUỘC** phải được đặt trong cặp thẻ `[ANSWER]` và `[/ANSWER]`. **Đây là quy tắc quan trọng nhất.**
1. Bạn **chỉ** được sử dụng thông tin trong phần NGỮ CẢNH bên dưới.
2. **Tuyệt đối** không được liệt kê lại danh sách các đáp án được cung cấp, câu trả lời chỉ được phép nhắc đến đáp án mà bạn chọn.
3. Đáp án **chỉ** là chuỗi ký tự gồm các lựa chọn đúng, viết hoa, phân tách bằng dấu phẩy **(không có khoảng trắng)**.
   - Ví dụ: `A` hoặc `A,C,D`
4. **Tuyệt đối không** viết thêm lời giải thích, nhận xét, hay ký tự ngoài đáp án.
5. Nếu không có bất kì thông tin nào từ ngữ cảnh thì vẫn phải chọn (các) đáp án nào mà bạn cho là đúng, không cần giải thích thêm.

--- VÍ DỤ ---

**VÍ DỤ 1: Trường hợp chỉ có 1 đáp án đúng**
NGỮ CẢNH: Công thức hóa học của nước là H2O
CÂU HỎI: Các nguyên tố hóa học nào tạo nên phân tử nước?
CÁC LỰA CHỌN:
A: A, H
B: H, O
C: A, O
D: H, 2
ĐÁP ÁN: [ANSWER]B[/ANSWER]

**VÍ DỤ 2: Trường hợp nhiều đáp án đúng**
NGỮ CẢNH: Sản phẩm mới hỗ trợ kết nối qua cả Wi-Fi và Bluetooth. Cổng USB-C dùng để sạc.
CÂU HỎI: Sản phẩm hỗ trợ những kết nối không dây nào?
CÁC LỰA CHỌN:
A: Wi-Fi
B: Cổng USB-C
C: Bluetooth
D: NFC
ĐÁP ÁN: [ANSWER]A,C[/ANSWER]

**VÍ DỤ 3: Trường hợp nội dung lựa chọn chứa ký tự có thể gây nhiễu**
NGỮ CẢNH: Yêu cầu kỹ thuật cho bộ phận C là phải có chứng chỉ "A D M".
CÂU HỎI: Bộ phận nào cần chứng chỉ "A D M"?
CÁC LỰA CHỌN:
A: Bộ phận C
B: Bộ phận D
C: Bộ phận A
D: Bộ phận B
ĐÁP ÁN: [ANSWER]A[/ANSWER]

--- KẾT THÚC VÍ DỤ ---

--- BẮT ĐẦU NHIỆM VỤ ---
NGỮ CẢNH:
{context}

CÂU HỎI: {question}

CÁC LỰA CHỌN:
{options_str}

ĐÁP ÁN:"""
        
        # Sử dụng template chat của Qwen
        messages = [
            {"role": "user", "content": prompt}
        ]
        
        input_ids = self.tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            return_tensors="pt"
        ).to(self.device)
        
        outputs = self.llm_model.generate(
            input_ids=input_ids, 
            max_new_tokens=2048, # Chỉ cần token cho đáp án (A,B,C,D) nên không cần nhiều
            pad_token_id=self.tokenizer.eos_token_id
        )
        
        response = self.tokenizer.batch_decode(outputs[:, input_ids.shape[1]:], skip_special_tokens=True)[0]
        return response.strip()

    def process_question(self, question_row: pd.Series) -> str:
        """
        Thực hiện toàn bộ pipeline cho một câu hỏi: retrieve -> generate -> format.
        (Phiên bản cải tiến với logic trích xuất thông minh)
        """
        question = question_row['Question']
        options = {
            'A': question_row['A'],
            'B': question_row['B'],
            'C': question_row['C'],
            'D': question_row['D']
        }
        
        # Bước 1: Truy xuất và Rerank ngữ cảnh
        context = self.retrieve_context(
            question, 
            n_results=NUM_RETRIEVED_CHUNKS,
            top_n_rerank=TOP_N_AFTER_RERANK
        )
        
        # Bước 2: Sinh câu trả lời thô từ LLM
        raw_answer = self.generate_answer(context, question, options)
        print(f"  - Phản hồi thô từ LLM: '{raw_answer}'")
        
        # --- LOGIC XỬ LÝ CÂU TRẢ LỜI MỚI ---
        answer_content = ""
        # Bước 3.1: Ưu tiên tìm kiếm câu trả lời trong thẻ [ANSWER]
        # re.DOTALL cho phép '.' khớp với cả ký tự xuống dòng
        match = re.search(r'\[ANSWER\](.*?)\[/ANSWER\]', raw_answer, re.DOTALL)
        
        if match:
            # Nếu tìm thấy, chỉ lấy nội dung bên trong thẻ
            answer_content = match.group(1).strip()
            print(f"  - Đã tìm thấy thẻ [ANSWER]. Nội dung: '{answer_content}'")
        else:
            # Bước 3.2: Nếu không có thẻ, sử dụng toàn bộ phản hồi (phương án dự phòng)
            # Đồng thời cảnh báo để chúng ta biết LLM không tuân thủ
            print("  - Cảnh báo: Không tìm thấy thẻ [ANSWER]. Sử dụng toàn bộ phản hồi để phân tích.")
            answer_content = raw_answer

        # Bước 3.3: Trích xuất các ký tự A, B, C, D hợp lệ từ nội dung đã được xác định
        # Regex này đơn giản hơn vì ta đã thu hẹp phạm vi tìm kiếm.
        # Nó tìm tất cả các ký tự A, B, C, D (không phân biệt hoa thường)
        found_answers = re.findall(r'[A-D]', answer_content.upper())

        # Bước 4: Chuẩn hóa kết quả đã trích xuất
        # Đưa tất cả về chữ hoa, loại bỏ các đáp án trùng lặp và sắp xếp lại.
        valid_answers = sorted(list(set(found_answers)))
        
        # Bước 5: Định dạng output cuối cùng theo yêu cầu
        num_correct = len(valid_answers)
        answers_str = ",".join(valid_answers)
        
        if num_correct > 1:
            formatted_answer = f'{num_correct},"{answers_str}"'
        elif num_correct == 1:
            formatted_answer = f'1,{answers_str}'
        else:
            # Trường hợp không trích xuất được đáp án nào
            formatted_answer = '0,""' 
            
        print(f"  - Kết quả cuối cùng: {formatted_answer}")
        return formatted_answer

def main():
    """
    Hàm chính điều khiển toàn bộ pipeline của bước 3.
    """
    print("================================================")
    print("===   BẮT ĐẦU PIPELINE BƯỚC 3: RETRIEVAL & QA   ===")
    print("================================================")
    
    # === THAY ĐỔI QUAN TRỌNG ===
    # Bước 1: Chọn GPU rảnh nhất
    gpu_id_to_use = get_freest_gpu()
    
    if gpu_id_to_use != "cpu":
        # Bước 2: Thiết lập biến môi trường ĐỂ chương trình chỉ "nhìn thấy" GPU này
        # Việc này PHẢI được thực hiện TRƯỚC KHI tải mô hình
        os.environ["CUDA_VISIBLE_DEVICES"] = gpu_id_to_use
        print(f"Đã thiết lập CUDA_VISIBLE_DEVICES='{gpu_id_to_use}'. Chương trình sẽ chạy trên GPU vật lý {gpu_id_to_use}.")
        # Sau khi thiết lập, PyTorch sẽ coi GPU này là 'cuda:0'
        selected_device = "cuda:0"
    else:
        print("Không có GPU. Chương trình sẽ chạy trên CPU.")
        selected_device = "cpu"

    # Tải các mô hình. Unsloth/Transformers sẽ tự động tải lên 'cuda:0' (chính là GPU vật lý ta đã chọn)
    llm_model, tokenizer = load_llm_model_and_tokenizer() # Không cần truyền device vào đây nữa

    # Khởi tạo pipeline và truyền device đã chọn vào
    # Tất cả các model khác (embedding, reranker) cũng sẽ được đưa lên device này
    qa_pipeline = RetrieverQA(
        db_path=DB_PATH,
        collection_name=COLLECTION_NAME,
        embedding_model_name=EMBEDDING_MODEL_NAME,
        llm_model=llm_model,
        tokenizer=tokenizer,
        device=selected_device
    )
    
    # Đọc file câu hỏi
    try:
        questions_df = pd.read_csv(QUESTIONS_FILE_PATH)
        print(f"Đã đọc thành công {len(questions_df)} câu hỏi từ '{QUESTIONS_FILE_PATH}'.")
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file câu hỏi tại '{QUESTIONS_FILE_PATH}'. Vui lòng kiểm tra lại.")
        return

    # Chuẩn bị file output
    # Tạo thư mục nếu chưa tồn tại
    os.makedirs(os.path.dirname(OUTPUT_FILE_PATH), exist_ok=True)
    # Ghi header nếu file chưa có hoặc trống
    if not os.path.exists(OUTPUT_FILE_PATH) or os.path.getsize(OUTPUT_FILE_PATH) == 0:
        with open(OUTPUT_FILE_PATH, 'w', encoding='utf-8') as f:
            f.write("### TASK QA\n")
            f.write("num_correct,answers\n")
        print(f"Đã tạo và ghi header cho file output tại '{OUTPUT_FILE_PATH}'.")

    # Mở file ở chế độ ghi tiếp (append)
    with open(OUTPUT_FILE_PATH, 'a', encoding='utf-8') as f:
        total_questions = len(questions_df)
        for index, row in questions_df.iterrows():
            print(f"\n--- Xử lý câu hỏi {index + 1}/{total_questions} ---")
            print(f"Câu hỏi: {row['Question']}")
            
            final_answer_line = qa_pipeline.process_question(row)
            
            # Ghi kết quả vào file
            f.write(final_answer_line + "\n")
            f.flush() # Đảm bảo dữ liệu được ghi ngay lập tức
            
    print("\n================================================")
    print("===   HOÀN TẤT TOÀN BỘ PIPELINE BƯỚC 3   ===")
    print(f"Kết quả đã được ghi vào file: '{OUTPUT_FILE_PATH}'")
    print("================================================")


if __name__ == '__main__':
    main()