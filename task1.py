import os
import re
import shutil
import subprocess
import time
from PIL import Image
from transformers import Blip2Processor, Blip2ForConditionalGeneration


# === 1️⃣ GỌI MINERU ===
def run_mineru(pdf_path, output_root):
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_dir = os.path.join(output_root, pdf_name)
    os.makedirs(output_dir, exist_ok=True)

    cmd = ["mineru", "-p", pdf_path, "-o", output_root]
    print(f"🚀 Đang chạy mineru cho {pdf_name} ...")
    subprocess.run(cmd, check=True)
    print(f"✅ Mineru hoàn tất: {pdf_name}")
    return os.path.join(output_dir, "auto"), pdf_name


# === 2️⃣ XỬ LÝ auto/ ===
def process_auto_folder(auto_folder, pdf_name):
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

    # --- Tìm ảnh theo thứ tự xuất hiện ---
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

    # ✅ output_folder là thư mục cha của auto/
    output_folder = os.path.dirname(auto_folder)

    # --- Copy ảnh và đổi tên ---
    if ordered_images:
        output_images = os.path.join(output_folder, "images")
        os.makedirs(output_images, exist_ok=True)
        for i, old_name in enumerate(ordered_images, start=1):
            old_path = os.path.join(images_folder, old_name)
            if not os.path.exists(old_path):
                print(f"⚠️ Thiếu ảnh: {old_name}")
                continue
            ext = os.path.splitext(old_name)[1]
            new_name = f"{i}{ext}"
            new_path = os.path.join(output_images, new_name)
            shutil.copy2(old_path, new_path)
            rename_map[old_name] = new_name

        # Cập nhật đường dẫn ảnh trong markdown
        for old_name, new_name in rename_map.items():
            md_content = re.sub(
                rf'(?<=images/){re.escape(old_name)}(?=[\)"\'\s])',
                new_name,
                md_content
            )

    # --- Xóa bảng chứa “Viettel AI Race” ---
    table_pattern = re.compile(r'<table\b.*?>.*?</table>', re.IGNORECASE | re.DOTALL)

    def remove_viettel_tables(match):
        t = match.group(0)
        return "" if "VIETTEL" in t.upper() else t

    md_content = table_pattern.sub(remove_viettel_tables, md_content)

    # --- Ghi file main.md ---
    output_md_path = os.path.join(output_folder, "main.md")
    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write(f"# {pdf_title}\n\n{md_content.strip()}\n")

    # 🧹 Xóa thư mục auto sau khi xong
    shutil.rmtree(auto_folder, ignore_errors=True)

    print(f"✅ Hoàn tất xử lý {pdf_title} (đã xoá auto/)")
    return output_folder, output_md_path, pdf_title


# === 3️⃣ SINH CAPTION CHO ẢNH ===
def add_image_captions(md_path, images_folder, model, processor):
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    pattern = re.compile(r'!\[.*?\]\((images/[^)]+)\)')
    matches = pattern.findall(md_text)
    if not matches:
        return

    for img_rel_path in matches:
        img_path = os.path.join(os.path.dirname(md_path), img_rel_path)
        if not os.path.exists(img_path):
            print(f"⚠️ Không tìm thấy ảnh: {img_path}")
            continue

        image = Image.open(img_path).convert("RGB")
        inputs = processor(image, return_tensors="pt")
        out = model.generate(**inputs)
        caption = processor.decode(out[0], skip_special_tokens=True)

        print(f"🖼️ {img_rel_path}: {caption}")
        caption_line = f"\n\n> **Hình chú thích:** {caption}\n"
        md_text = md_text.replace(f"![]({img_rel_path})", f"![]({img_rel_path}){caption_line}")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_text)


# === 4️⃣ TẠO answer.md ===
def generate_answer_md(output_root, md_info_list):
    answer_path = os.path.join(output_root, "answer.md")
    with open(answer_path, "w", encoding="utf-8") as out:
        out.write("### TASK EXTRACT\n\n")
        for md_path, pdf_title in md_info_list:
            with open(md_path, "r", encoding="utf-8") as f:
                content = f.read().strip()

            # Nếu file main.md đã có tiêu đề rồi thì không chèn thêm
            first_line = content.split("\n", 1)[0].strip()
            if not first_line.startswith("#"):
                out.write(f"# {pdf_title}\n\n")

            out.write(content)
            out.write("\n\n")

    print(f"📦 Đã tạo file answer.md tại: {answer_path}")


# === 5️⃣ GOM submission/ ===
def collect_submission(all_folders, final_root):
    os.makedirs(final_root, exist_ok=True)
    for folder in all_folders:
        dest = os.path.join(final_root, os.path.basename(folder))
        if os.path.exists(dest):
            shutil.rmtree(dest)
        shutil.copytree(folder, dest)
    print(f"\n📁 Đã tạo thư mục submission tại: {final_root}")


# === 6️⃣ PIPELINE CHÍNH ===
def process_all_pdfs(input_root, output_root):
    pdf_files = [f for f in os.listdir(input_root) if f.lower().endswith(".pdf")]
    all_outputs = []
    md_info_list = []

    # Load mô hình caption một lần
    print("🧠 Đang load mô hình BLIP2...")
    model_name = "Salesforce/blip2-opt-2.7b"
    processor = Blip2Processor.from_pretrained(model_name)
    model = Blip2ForConditionalGeneration.from_pretrained(model_name)
    print("✅ Đã load mô hình BLIP2")

    for pdf in pdf_files:
        pdf_path = os.path.join(input_root, pdf)
        pdf_name = os.path.splitext(pdf)[0]

        print(f"\n==============================")
        print(f"📄 BẮT ĐẦU XỬ LÝ FILE: {pdf_name}")
        print("==============================")

        # Mineru
        auto_folder, pdf_name = run_mineru(pdf_path, output_root)

        # Hậu kỳ
        output_folder, main_md, pdf_title = process_auto_folder(auto_folder, pdf_name)
        if main_md:
            add_image_captions(main_md, os.path.join(output_folder, "images"), model, processor)
            all_outputs.append(output_folder)
            md_info_list.append((main_md, pdf_title))

        print(f"🎯 Hoàn tất pipeline cho {pdf_title}\n")
        time.sleep(1)

    # Gom submission
    # collect_submission(all_outputs, os.path.join(output_root, "submission"))

    # Tạo file answer.md
    if md_info_list:
        generate_answer_md(output_root, md_info_list)

    print("\n🏁 HOÀN TẤT TOÀN BỘ QUY TRÌNH")


# === 7️⃣ CHẠY ===
if __name__ == "__main__":
    input_root = "./data/raw/public_test_data"
    output_root = "./submission"
    os.makedirs(output_root, exist_ok=True)
    process_all_pdfs(input_root, output_root)
    main_py_path = os.path.join(output_root, "main.py")
    with open(main_py_path, "w", encoding="utf-8") as f:
        f.write('print("AIRONMEN")\n')
    print(f"🧩 Đã tạo file main.py tại: {main_py_path}")
    
