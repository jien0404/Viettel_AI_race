import os
import re
import shutil
import subprocess
import time
from typing import List, Any
import pandas as pd

# Thư viện để trích xuất bảng chất lượng cao
try:
    import camelot
except ImportError:
    print("Lỗi: Thư viện camelot-py chưa được cài đặt. Vui lòng chạy: pip install 'camelot-py[cv]'")
    exit()
    
def select_freest_gpu():
    """
    Sử dụng nvidia-smi để tìm và trả về ID của GPU có nhiều bộ nhớ trống nhất.
    Trả về ID của GPU (int) hoặc None nếu không thể tìm thấy/chọn GPU.
    """
    try:
        # Lệnh nvidia-smi để lấy index và bộ nhớ trống, không header, không đơn vị
        cmd = [
            "nvidia-smi",
            "--query-gpu=index,memory.free",
            "--format=csv,noheader,nounits"
        ]
        # Chạy lệnh và lấy output
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        output = result.stdout.strip()
        
        # Xử lý output
        gpu_info = []
        for line in output.split('\n'):
            if not line:
                continue
            index, memory_free = line.split(',')
            gpu_info.append((int(index.strip()), int(memory_free.strip())))

        # Nếu không có thông tin GPU, trả về None
        if not gpu_info:
            print("⚠️ Không tìm thấy thông tin GPU nào từ nvidia-smi.")
            return None

        # Tìm GPU có bộ nhớ trống nhiều nhất
        best_gpu = max(gpu_info, key=lambda item: item[1])
        return best_gpu[0]

    except FileNotFoundError:
        print("💡 Không tìm thấy lệnh 'nvidia-smi'. Giả định không có GPU hoặc driver NVIDIA.")
        return None
    except Exception as e:
        print(f"❌ Đã xảy ra lỗi khi chọn GPU: {e}")
        return None

# === LOGIC TRÍCH XUẤT BẢNG TỪ SCRIPT THỨ 2 ===
def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Làm sạch DataFrame được trích xuất từ bảng."""
    df = df.copy()
    def _normalize_text(x: Any) -> str:
        s = str(x) if x is not None else ''
        s = s.replace('\n', ' ').strip()
        return ' '.join(s.split())
    df = df.fillna('')
    df = df.applymap(_normalize_text)
    df = df.dropna(how='all').reset_index(drop=True)
    return df

def extract_and_process_tables_with_camelot(pdf_path: str) -> List[str]:
    """
    Sử dụng Camelot để trích xuất tất cả các bảng từ file PDF,
    làm sạch chúng và chuyển thành chuỗi HTML.
    """
    print(f"🐫 Đang trích xuất bảng từ {os.path.basename(pdf_path)} bằng Camelot...")
    processed_html_tables = []
    
    try:
        tables = camelot.read_pdf(pdf_path, pages='all', flavor='lattice', line_scale=40)
        if len(tables) == 0:
            print("   -> Không tìm thấy bảng với 'lattice', thử lại với 'stream'...")
            tables = camelot.read_pdf(pdf_path, pages='all', flavor='stream', split_text=True, edge_tol=500)

        print(f"   -> Tìm thấy {len(tables)} bảng.")
        
        for table in tables:
            cleaned_df = clean_dataframe(table.df)
            if not cleaned_df.empty:
                # Chuyển DataFrame thành HTML, vẫn tạo header để xử lý sau
                html_table = cleaned_df.to_html(index=False, header=True, escape=False, na_rep="")
                
                # Thay thế thẻ mặc định của pandas bằng thẻ table đơn giản
                html_table = html_table.replace('<table border="1" class="dataframe">', '<table>')

                # BỔ SUNG: Xóa bỏ hoàn toàn thẻ thead và nội dung bên trong nó
                html_table = re.sub(r'<thead\b.*?>.*?</thead>', '', html_table, flags=re.DOTALL)
                
                processed_html_tables.append(html_table)
            
    except Exception as e:
        print(f"⚠️ Lỗi khi trích xuất bảng bằng Camelot: {e}")

    return processed_html_tables
# =======================================================


# === 1️⃣ GỌI MINERU (Không thay đổi) ===
def run_mineru(pdf_path, output_root):
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_dir = os.path.join(output_root, pdf_name)
    os.makedirs(output_dir, exist_ok=True)

    cmd = ["mineru", "-p", pdf_path, "-o", output_root]
    print(f"🚀 Đang chạy mineru cho {pdf_name} ...")
    
    # --- THAY ĐỔI TẠI ĐÂY ---
    try:
        # Chạy và bắt output
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        
        # In output để debug
        print("   -> Mineru STDOUT:")
        print(result.stdout)
        print("   -> Mineru STDERR:")
        print(result.stderr)

    except subprocess.CalledProcessError as e:
        # Nếu mineru trả về mã lỗi, in chi tiết lỗi
        print(f"❌ LỖI: Mineru thất bại với mã lỗi {e.returncode}")
        print("   -> Mineru STDOUT:")
        print(e.stdout)
        print("   -> Mineru STDERR:")
        print(e.stderr)
        # Ném lại lỗi hoặc xử lý một cách phù hợp
        raise e
    except FileNotFoundError:
        print("❌ LỖI: Không tìm thấy lệnh 'mineru'. Hãy đảm bảo nó đã được cài đặt và nằm trong PATH của hệ thống.")
        raise
    # --- KẾT THÚC THAY ĐỔI ---

    auto_folder_path = os.path.join(output_dir, "auto")

    # Thêm một bước kiểm tra trước khi trả về
    if not os.path.isdir(auto_folder_path):
        print(f"⚠️ CẢNH BÁO: Mineru đã chạy xong nhưng không tạo ra thư mục mong đợi: {auto_folder_path}")
        # Bạn có thể quyết định ném lỗi ở đây để dừng chương trình sớm hơn
        # raise FileNotFoundError(f"Thư mục auto không được mineru tạo ra cho {pdf_name}")

    print(f"✅ Mineru hoàn tất: {pdf_name}")
    return auto_folder_path, pdf_name


# === 2️⃣ XỬ LÝ auto/ (ĐÃ CẬP NHẬT) ===
def process_auto_folder(auto_folder, pdf_name, camelot_tables: List[str]):
    # Chuẩn hóa tên file thành Public_XXX
    match = re.search(r"(\d+)", pdf_name)
    num = int(match.group(1)) if match else 0
    pdf_title = f"Public_{num:03d}"

    images_folder = os.path.join(auto_folder, "images")
    has_images = os.path.isdir(images_folder)

    # Tìm file .md trong auto/
    md_file = None
    for fname in os.listdir(auto_folder):
        if fname.lower().endswith(".md"):
            md_file = os.path.join(auto_folder, fname)
            break
    if not md_file:
        print(f"❌ Không tìm thấy file .md trong {auto_folder}")
        return None, pdf_title

    with open(md_file, "r", encoding="utf-8") as f:
        md_content = f.read()

    # --- BƯỚC MỚI: Thay thế bảng của Mineru bằng bảng của Camelot ---
    table_pattern = re.compile(r'<table\b.*?>.*?</table>', re.IGNORECASE | re.DOTALL)
    
    camelot_iter = iter(camelot_tables)
    def replace_table_with_camelot(match):
        try:
            return next(camelot_iter)
        except StopIteration:
            # Nếu hết bảng Camelot, xóa bảng còn lại của Mineru
            return ""
    md_content = table_pattern.sub(replace_table_with_camelot, md_content)
    print("✅ Đã thay thế các bảng bằng kết quả từ Camelot.")


    # --- Tìm ảnh theo thứ tự xuất hiện (Không thay đổi) ---
    ordered_images = []
    rename_map = {}
    if has_images:
        image_pattern = re.compile(
            r'!\[[^\]]*\]\((?:\.?/)?images/([^)]+)\)|<img[^>]+src=["\'](?:\.?/)?images/([^"\']+)["\']',
            re.IGNORECASE
        )
        seen = set()
        for match in image_pattern.finditer(md_content):
            fname = match.group(1) or match.group(2)
            if fname and fname not in seen:
                seen.add(fname)
                ordered_images.append(fname)

    output_folder = os.path.dirname(auto_folder)

    # --- Copy ảnh và đổi tên (Không thay đổi) ---
    if ordered_images:
        output_images = os.path.join(output_folder, "images")
        os.makedirs(output_images, exist_ok=True)
        for i, old_name in enumerate(ordered_images, start=1):
            old_path = os.path.join(images_folder, old_name)
            if not os.path.exists(old_path):
                print(f"⚠️ Thiếu ảnh: {old_name}")
                continue
            ext = os.path.splitext(old_name)[1]
            new_name = f"image_{i}{ext}"
            new_path = os.path.join(output_images, new_name)
            shutil.copy2(old_path, new_path)
            rename_map[old_name] = new_name

        # Cập nhật đường dẫn ảnh trong markdown (Không thay đổi)
        for i, old_name in enumerate(ordered_images, start=1):
            # Tạo placeholder mới theo đúng định dạng yêu cầu
            new_placeholder = f"|<image_{i}>|"
            
            # Tìm tất cả các biến thể của thẻ ảnh cũ (cả markdown và html) và thay thế
            # bằng placeholder mới. Dùng re.escape để xử lý các ký tự đặc biệt trong tên file.
            old_pattern = re.compile(
                r'(!\[[^\]]*\]\((?:\.?/)?images/' + re.escape(old_name) + r'\))|' +
                r'(<img[^>]+src=["\'](?:\.?/)?images/' + re.escape(old_name) + r'["\'][^>]*>)',
                re.IGNORECASE
            )
            md_content = old_pattern.sub(new_placeholder, md_content)

    # --- Xóa bảng chứa “Viettel AI Race” (Không thay đổi) ---
    # Chạy lại bước này để đảm bảo các bảng header do Camelot nhận diện cũng bị xóa
    def remove_viettel_tables(match):
        t = match.group(0)
        return "" if "VIETTEL" in t.upper() else t
    md_content = table_pattern.sub(remove_viettel_tables, md_content)

    # --- Ghi file main.md (Không thay đổi) ---
    output_md_path = os.path.join(output_folder, "main.md")
    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write(f"# {pdf_title}\n\n{md_content.strip()}\n")

    # Xóa thư mục auto sau khi xong
    shutil.rmtree(auto_folder, ignore_errors=True)
    print(f"✅ Hoàn tất xử lý {pdf_title} (đã xoá auto/)")
    return output_folder, output_md_path, pdf_title


# === 3️⃣ SINH CAPTION CHO ẢNH (ĐÃ BỊ LOẠI BỎ) ===


# === 4️⃣ TẠO answer.md (Không thay đổi) ===
def generate_answer_md(output_root, md_info_list):
    answer_path = os.path.join(output_root, "answer.md")
    with open(answer_path, "w", encoding="utf-8") as out:
        out.write("### TASK EXTRACT\n\n")
        for md_path, pdf_title in md_info_list:
            with open(md_path, "r", encoding="utf-8") as f:
                content = f.read().strip()

            first_line = content.split("\n", 1)[0].strip()
            if not first_line.startswith("#"):
                out.write(f"# {pdf_title}\n\n")

            out.write(content)
            out.write("\n\n")
    print(f"📦 Đã tạo file answer.md tại: {answer_path}")


# === 5️⃣ GOM submission/ (Không thay đổi) ===
def collect_submission(all_folders, final_root):
    os.makedirs(final_root, exist_ok=True)
    for folder in all_folders:
        dest = os.path.join(final_root, os.path.basename(folder))
        if os.path.exists(dest):
            shutil.rmtree(dest)
        shutil.copytree(folder, dest)
    print(f"\n📁 Đã tạo thư mục submission tại: {final_root}")


# === 6️⃣ PIPELINE CHÍNH (ĐÃ CẬP NHẬT VỚI LOGIC KIỂM TRA) ===
def process_all_pdfs(input_root, output_root):
    pdf_files = [f for f in os.listdir(input_root) if f.lower().endswith(".pdf")]
    md_info_list = []

    for pdf in pdf_files:
        pdf_name = os.path.splitext(pdf)[0]
        # Xây dựng đường dẫn thư mục output dự kiến cho file PDF này
        expected_output_folder = os.path.join(output_root, pdf_name)

        # --- LOGIC MỚI: KIỂM TRA SỰ TỒN TẠI CỦA THƯ MỤC KẾT QUẢ ---
        if os.path.isdir(expected_output_folder):
            print(f"⏭️  Bỏ qua {pdf_name} vì thư mục kết quả '{expected_output_folder}' đã tồn tại.")
            
            # Dù bỏ qua, ta vẫn cần thu thập thông tin file main.md để tạo answer.md
            main_md_path = os.path.join(expected_output_folder, "main.md")
            if os.path.exists(main_md_path):
                # Tái tạo lại pdf_title để thêm vào danh sách
                match = re.search(r"(\d+)", pdf_name)
                num = int(match.group(1)) if match else 0
                pdf_title = f"Public_{num:03d}"
                md_info_list.append((main_md_path, pdf_title))
            else:
                print(f"   ⚠️ Cảnh báo: Thư mục tồn tại nhưng không tìm thấy file main.md tại {main_md_path}")
            
            continue # Chuyển sang file PDF tiếp theo
        # --- KẾT THÚC LOGIC MỚI ---

        # Nếu thư mục chưa tồn tại, bắt đầu quy trình xử lý bình thường
        pdf_path = os.path.join(input_root, pdf)

        print(f"\n==============================")
        print(f"📄 BẮT ĐẦU XỬ LÝ FILE: {pdf_name}")
        print("==============================")

        try:
            # BƯỚC 1: Chạy Mineru để lấy cấu trúc file .md, text và ảnh
            auto_folder, pdf_name_from_mineru = run_mineru(pdf_path, output_root)

            # BƯỚC 2: Chạy Camelot để lấy các bảng chất lượng cao từ file PDF gốc
            camelot_html_tables = extract_and_process_tables_with_camelot(pdf_path)

            # BƯỚC 3: Xử lý hậu kỳ
            output_folder, main_md, pdf_title = process_auto_folder(auto_folder, pdf_name_from_mineru, camelot_html_tables)
            if main_md:
                md_info_list.append((main_md, pdf_title))

            print(f"🎯 Hoàn tất pipeline cho {pdf_title}\n")
            time.sleep(1)

        except Exception as e:
            print(f"❌ Đã xảy ra lỗi nghiêm trọng khi xử lý {pdf_name}: {e}")
            # Tùy chọn: Dọn dẹp thư mục output nếu xử lý thất bại
            if os.path.isdir(expected_output_folder):
                shutil.rmtree(expected_output_folder)
                print(f"   -> Đã dọn dẹp thư mục không hoàn chỉnh: {expected_output_folder}")
            continue # Tiếp tục với file tiếp theo

    # Tạo file answer.md từ tất cả các file đã xử lý (cả lần chạy này và các lần trước)
    if md_info_list:
        generate_answer_md(output_root, md_info_list)

    print("\n🏁 HOÀN TẤT TOÀN BỘ QUY TRÌNH")


# === 7️⃣ CHẠY (Không thay đổi) ===
if __name__ == "__main__":
    # --- BƯỚC MỚI: CHỌN GPU TRƯỚC KHI CHẠY BẤT CỨ THỨ GÌ ---
    gpu_id_to_use = select_freest_gpu()
    if gpu_id_to_use is not None:
        # Đặt biến môi trường để các thư viện (pytorch, tensorflow, cv2) chỉ thấy GPU này
        os.environ["CUDA_VISIBLE_DEVICES"] = str(gpu_id_to_use)
        print(f"✅ Đã chọn GPU {gpu_id_to_use} để chạy.")
    else:
        print("✅ Không chọn được GPU cụ thể, sẽ chạy trên CPU hoặc GPU mặc định.")
    # --- KẾT THÚC BƯỚC MỚI ---

    input_root = "data/raw/private_test_data/input"
    output_root = "./private_submission"
    os.makedirs(output_root, exist_ok=True)
    
    process_all_pdfs(input_root, output_root)
    
    main_py_path = os.path.join(output_root, "main.py")
    with open(main_py_path, "w", encoding="utf-8") as f:
        f.write('print("AIRONMEN")\n')
    print(f"🧩 Đã tạo file main.py tại: {main_py_path}")