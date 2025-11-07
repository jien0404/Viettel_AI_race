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
    subprocess.run(cmd, check=True)
    print(f"✅ Mineru hoàn tất: {pdf_name}")
    return os.path.join(output_dir, "auto"), pdf_name


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
        for old_name, new_name in rename_map.items():
            md_content = re.sub(
                rf'(?<=images/){re.escape(old_name)}(?=[\)"\'\s])',
                new_name,
                md_content
            )
            # Đảm bảo caption ảnh trống ![] để không có text thừa
            md_content = re.sub(
                rf'!\[.*?\]\((images/{re.escape(new_name)})\)',
                r'![](\1)',
                md_content
            )

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


# === 6️⃣ PIPELINE CHÍNH (ĐÃ CẬP NHẬT) ===
def process_all_pdfs(input_root, output_root):
    pdf_files = [f for f in os.listdir(input_root) if f.lower().endswith(".pdf")]
    md_info_list = []

    # --- ĐÃ LOẠI BỎ VIỆC LOAD MÔ HÌNH BLIP2 ---

    for pdf in pdf_files:
        pdf_path = os.path.join(input_root, pdf)
        pdf_name = os.path.splitext(pdf)[0]

        print(f"\n==============================")
        print(f"📄 BẮT ĐẦU XỬ LÝ FILE: {pdf_name}")
        print("==============================")

        # BƯỚC 1: Chạy Mineru để lấy cấu trúc file .md, text và ảnh
        auto_folder, pdf_name_from_mineru = run_mineru(pdf_path, output_root)

        # BƯỚC 2: Chạy Camelot để lấy các bảng chất lượng cao từ file PDF gốc
        camelot_html_tables = extract_and_process_tables_with_camelot(pdf_path)

        # BƯỚC 3: Xử lý hậu kỳ, giữ nguyên luồng logic của script gốc
        # nhưng thay thế bảng của Mineru bằng bảng của Camelot.
        output_folder, main_md, pdf_title = process_auto_folder(auto_folder, pdf_name_from_mineru, camelot_html_tables)
        if main_md:
            # --- ĐÃ LOẠI BỎ LỆNH GỌI add_image_captions ---
            # all_outputs không cần dùng nữa nếu không gom submission
            md_info_list.append((main_md, pdf_title))

        print(f"🎯 Hoàn tất pipeline cho {pdf_title}\n")
        time.sleep(1)

    # Tạo file answer.md (Không thay đổi)
    if md_info_list:
        generate_answer_md(output_root, md_info_list)

    print("\n🏁 HOÀN TẤT TOÀN BỘ QUY TRÌNH")


# === 7️⃣ CHẠY (Không thay đổi) ===
if __name__ == "__main__":
    input_root = "data/raw/public_test_data"
    output_root = "./submission"
    os.makedirs(output_root, exist_ok=True)
    process_all_pdfs(input_root, output_root)
    main_py_path = os.path.join(output_root, "main.py")
    with open(main_py_path, "w", encoding="utf-8") as f:
        f.write('print("AIRONMEN")\n')
    print(f"🧩 Đã tạo file main.py tại: {main_py_path}")