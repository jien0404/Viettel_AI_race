from typing import List, Dict, Any
from bs4 import BeautifulSoup
import os

# Hàm linearize_html_table không thay đổi, giữ nguyên như cũ
def linearize_html_table(html_content: str) -> str:
    # ... (giữ nguyên code cũ)
    soup = BeautifulSoup(html_content, 'html.parser')
    text_parts = []
    
    caption = soup.find('caption')
    if caption:
        text_parts.append(f"Nội dung bảng: {caption.get_text(strip=True)}.")

    headers = []
    header_row = soup.find('thead')
    if not header_row:
        header_row = soup.find('tr')

    if header_row:
        header_cols = header_row.find_all('th')
        if header_cols:
            headers = [col.get_text(strip=True) for col in header_cols]

    rows = soup.find_all('tr')
    for row in rows:
        cols = row.find_all(['td', 'th'])
        if not cols: continue
        
        if headers and [col.get_text(strip=True) for col in cols] == headers:
            continue

        if headers and len(headers) == len(cols):
            row_description = ", ".join([f"cột '{headers[i]}' là '{cols[i].get_text(strip=True)}'" for i in range(len(cols))])
            text_parts.append(f"Một hàng trong bảng có: {row_description}.")
        else:
            row_text = ", ".join([col.get_text(strip=True) for col in cols])
            text_parts.append(f"Một hàng trong bảng chứa: {row_text}.")
            
    return " ".join(text_parts)


def create_chunks(blocks: List[Dict[str, Any]], doc_name: str) -> List[Dict[str, Any]]:
    chunks = []
    current_headings = []

    for i, block in enumerate(blocks):
        block_type = block.get('type')

        if block_type == 'heading':
            level = block.get('level', 1)
            current_headings = current_headings[:level-1]
            current_headings.append(block.get('content', ''))
            continue

        heading_context_str = " > ".join(current_headings)
        
        chunk = {
            'doc_name': doc_name,
            'metadata': {
                'context_headings': heading_context_str,
            }
        }

        if block_type == 'paragraph':
            content = block.get('content', '')
            chunk['chunk_type'] = 'text'
            chunk['metadata']['original_content'] = content
            chunks.append(chunk)

        elif block_type == 'html_table':
            raw_html = block.get('raw_html', '')
            linearized_text = linearize_html_table(raw_html)
            chunk['chunk_type'] = 'table'
            # Giữ cả 2 để tiện tham khảo nếu cần
            chunk['metadata']['original_content'] = raw_html
            chunk['metadata']['linearized_text'] = linearized_text
            chunks.append(chunk)

        elif block_type == 'latex_formula':
            raw_latex = block.get('raw_latex', '')
            chunk['chunk_type'] = 'formula'
            chunk['metadata']['original_content'] = raw_latex
            chunks.append(chunk)

        elif block_type == 'image_placeholder':
            image_id = block.get('id')
            # Đường dẫn tương đối đến ảnh, dựa trên cấu trúc `doc_folder/images/`
            image_path = os.path.join('images', f'image_{image_id}.jpg')
            
            chunk['chunk_type'] = 'image'
            chunk['metadata']['original_content'] = f"Placeholder for image_{image_id}"
            chunk['metadata']['image_path'] = image_path # Lưu đường dẫn tương đối để truy xuất
            chunks.append(chunk)

    return chunks