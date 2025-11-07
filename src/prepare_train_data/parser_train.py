# ...existing code...
import re
from typing import List, Dict, Any

def parse_document(file_path: str) -> List[Dict[str, Any]]:
    """
    Đọc và phân tích một file .md có cấu trúc đặc biệt thành một danh sách các khối nội dung.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'", flush=True)
        return []

    content_blocks: List[Dict[str, Any]] = []
    i = 0
    num_lines = len(lines)

    # safety cap to avoid infinite loops in corrupted files
    MAX_LOOP_ITER = 10_000_000

    loop_counter = 0
    while i < num_lines:
        loop_counter += 1
        if loop_counter > MAX_LOOP_ITER:
            print(f"!! CẢNH BÁO: Vượt quá giới hạn vòng lặp khi parse '{file_path}'. Dừng để tránh treo.", flush=True)
            break

        line = lines[i].rstrip('\n')
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # 1. Heading
        if stripped.startswith('#'):
            level = len(stripped) - len(stripped.lstrip('#'))
            content_blocks.append({
                'type': 'heading',
                'level': level,
                'content': stripped.lstrip('# ').strip()
            })
            i += 1
            continue

        # 2. Exact image placeholder line (alone): |<image_1>|
        m_exact = re.match(r'^\|<image_?(\d+)>\|$', stripped)
        if m_exact:
            image_id = int(m_exact.group(1))
            content_blocks.append({
                'type': 'image_placeholder',
                'id': image_id
            })
            i += 1
            continue

        # 2b. Inline image placeholder with trailing text: |<image_1>|Some caption...
        m_inline = re.match(r'^\|<image_?(\d+)>\|(.*)$', line.strip())
        if m_inline:
            image_id = int(m_inline.group(1))
            rest = m_inline.group(2).strip()
            content_blocks.append({
                'type': 'image_placeholder',
                'id': image_id
            })
            if rest:
                content_blocks.append({
                    'type': 'paragraph',
                    'content': rest
                })
            i += 1
            continue

        # 3. HTML table start
        if stripped.lower().startswith('<table'):
            table_html = ""
            start_index = i
            while i < num_lines and '</table>' not in lines[i].lower():
                table_html += lines[i]
                i += 1
            if i < num_lines:
                table_html += lines[i]
                i += 1
            else:
                print(f"!! CẢNH BÁO: Không tìm thấy '</table>' trong file {file_path} từ dòng {start_index}", flush=True)
            content_blocks.append({
                'type': 'html_table',
                'raw_html': table_html.strip()
            })
            continue

        # 4. LaTeX formula $$ ... $$
        if stripped.startswith('$$'):
            formula_latex = ""
            start_index = i
            # single-line $$...$$
            if stripped.endswith('$$') and len(stripped) > 2:
                formula_latex = stripped
                i += 1
            else:
                # collect until a line that ends with $$
                while i < num_lines:
                    formula_latex += lines[i]
                    if lines[i].strip().endswith('$$') and len(lines[i].strip()) > 2:
                        i += 1
                        break
                    i += 1
                if i >= num_lines and not formula_latex.strip().endswith('$$'):
                    print(f"!! CẢNH BÁO: Không tìm thấy đóng '$$' trong file {file_path} từ dòng {start_index}", flush=True)
            content_blocks.append({
                'type': 'latex_formula',
                'raw_latex': formula_latex.strip()
            })
            continue

        # 5. Paragraph (gộp nhiều dòng). Stop when encounter blank or a special-start token.
        paragraph_lines = []
        start_index = i
        while i < num_lines:
            cur = lines[i].rstrip('\n')
            scur = cur.strip()
            # break conditions: blank line or special starters
            if not scur:
                break
            if scur.startswith('#') or scur.startswith('|<') or scur.lower().startswith('<table') or scur.startswith('$$'):
                break
            paragraph_lines.append(cur)
            i += 1

        paragraph_text = "\n".join(paragraph_lines).strip()
        if paragraph_text:
            content_blocks.append({
                'type': 'paragraph',
                'content': paragraph_text
            })
        else:
            # avoid infinite loop if nothing consumed
            if i == start_index:
                i += 1

    return content_blocks
# ...existing code...