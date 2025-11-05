import os
import subprocess
import re

def run_mineru(pdf_path, output_root):
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_dir = os.path.join(output_root, pdf_name)
    os.makedirs(output_dir, exist_ok=True)

    cmd = ["mineru", "-p", pdf_path, "-o", output_root]
    print(f"🚀 Đang chạy mineru cho {pdf_name} ...")
    subprocess.run(cmd, check=True)
    print(f"✅ Mineru hoàn tất: {pdf_name}")
    return os.path.join(output_dir, "auto"), pdf_name

def process_mineru_output(mineru_output_folder, pdf_name, output_folder="outputs"):
    # 🔹 Chuẩn hóa tên PDF về dạng Public_XXX
    match = re.search(r"(\d+)", pdf_name)
    num = int(match.group(1)) if match else 0
    pdf_title = f"Public_{num:03d}"
    
    images_folder = os.path.join(output_folder, pdf_title, "images")
    has_images = os.path.isdir(images_folder)
