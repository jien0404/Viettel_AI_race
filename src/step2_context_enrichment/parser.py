import re
from typing import List, Dict, Any

def parse_document(file_path: str) -> List[Dict[str, Any]]:
    """
    Đọc và phân tích một file .md có cấu trúc đặc biệt thành một danh sách các khối nội dung.

    Các loại khối được nhận dạng:
    - heading: Tiêu đề (ví dụ: # Tiêu đề)
    - paragraph: Đoạn văn bản
    - html_table: Bảng được định dạng bằng HTML (bắt đầu bằng <table>)
    - latex_formula: Công thức LaTeX (bắt đầu bằng $$)
    - image_placeholder: Placeholder cho hình ảnh (ví dụ: |<image_n>|)
    """

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'")
        return []

    content_blocks: List[Dict[str, Any]] = []
    i = 0
    num_lines = len(lines)

    while i < num_lines:
        line = lines[i].strip()

        if not line:
            i += 1
            continue

        # 1. Nhận dạng Tiêu đề (Heading)
        if line.startswith('#'):
            level = len(line) - len(line.lstrip('#'))
            content_blocks.append({
                'type': 'heading',
                'level': level,
                'content': line.lstrip('# ').strip()
            })
            i += 1

        # 2. Nhận dạng Placeholder hình ảnh (Image Placeholder)
        elif re.match(r'^\|<image_(\d+)>\|$', line):
            match = re.match(r'^\|<image_(\d+)>\|$', line)
            image_id = int(match.group(1))
            content_blocks.append({
                'type': 'image_placeholder',
                'id': image_id
            })
            i += 1
            
        # 3. Nhận dạng Bảng HTML (HTML Table)
        elif line.lower().startswith('<table>'):
            table_html = ""
            start_index = i
            while i < num_lines and '</table>' not in lines[i].lower():
                table_html += lines[i]
                i += 1
            if i < num_lines:
                table_html += lines[i]
                i += 1
            
            content_blocks.append({
                'type': 'html_table',
                'raw_html': table_html.strip()
            })

        # 4. Nhận dạng Công thức LaTeX (LaTeX Formula)
        elif line.startswith('$$'):
            formula_latex = ""
            start_index = i
            if line.endswith('$$') and len(line) > 2:
                 formula_latex = line
                 i += 1
            else:
                while i < num_lines and not (lines[i].strip().endswith('$$') and i > start_index):
                    formula_latex += lines[i]
                    i += 1
                if i < num_lines:
                    formula_latex += lines[i]
                    i += 1
            
            content_blocks.append({
                'type': 'latex_formula',
                'raw_latex': formula_latex.strip()
            })

        # 5. Mặc định là Đoạn văn bản (Paragraph)
        else:
            paragraph_text = ""
            while i < num_lines and lines[i].strip() and not lines[i].strip().startswith(('#', '|<', '<table', '$$')):
                paragraph_text += lines[i].strip() + " "
                i += 1
            
            content_blocks.append({
                'type': 'paragraph',
                'content': paragraph_text.strip()
            })
            
    return content_blocks
