from typing import List, Dict, Any
from bs4 import BeautifulSoup
import textwrap
import os

def linearize_html_table(html_content: str) -> str:
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
        if not cols:
            continue
        
        if headers and [col.get_text(strip=True) for col in cols] == headers:
            continue

        if headers and len(headers) == len(cols):
            row_description = ", ".join([
                f"cột '{headers[i]}' là '{cols[i].get_text(strip=True)}'" 
                for i in range(len(cols))
            ])
            text_parts.append(f"Một hàng trong bảng có: {row_description}.")
        else:
            row_text = ", ".join([col.get_text(strip=True) for col in cols])
            text_parts.append(f"Một hàng trong bảng chứa: {row_text}.")
            
    return " ".join(text_parts)


def split_text_by_max_length(text: str, max_length: int) -> List[str]:
    """
    Chia text thành nhiều phần nhỏ sao cho mỗi phần <= max_length ký tự.
    Giữ nguyên từ (tránh cắt giữa từ).
    """
    if len(text) <= max_length:
        return [text]
    return textwrap.wrap(text, width=max_length, break_long_words=False, replace_whitespace=False)


def create_chunks(blocks: List[Dict[str, Any]], doc_name: str, max_length: int = 1024) -> List[Dict[str, Any]]:
    """
    Hàm tạo danh sách các chunk từ danh sách block.
    Thêm tham số max_length để giới hạn độ dài mỗi chunk (tính theo ký tự).
    """
    chunks = []
    current_headings = []

    for i, block in enumerate(blocks):
        block_type = block.get('type')

        # === Cập nhật heading context ===
        if block_type == 'heading':
            level = block.get('level', 1)
            current_headings = current_headings[:level-1]
            current_headings.append(block.get('content', ''))
            continue

        heading_context_str = " > ".join(current_headings)
        
        base_metadata = {
            'context_headings': heading_context_str,
        }

        # === Paragraph ===
        if block_type == 'paragraph':
            content = block.get('content', '')
            base_text = f"Ngữ cảnh: {heading_context_str}. Nội dung: {content}"

            # Chia nhỏ nếu dài quá
            parts = split_text_by_max_length(base_text, max_length)
            for part in parts:
                chunk = {
                    'doc_name': doc_name,
                    'chunk_type': 'text',
                    'content_for_embedding': part,
                    'metadata': {
                        **base_metadata,
                        'original_content': content
                    }
                }
                chunks.append(chunk)

        # === HTML Table ===
        elif block_type == 'html_table':
            raw_html = block.get('raw_html', '')
            linearized_text = linearize_html_table(raw_html)
            base_text = f"Ngữ cảnh: {heading_context_str}. Bảng: {linearized_text}"

            parts = split_text_by_max_length(base_text, max_length)
            for part in parts:
                chunk = {
                    'doc_name': doc_name,
                    'chunk_type': 'table',
                    'content_for_embedding': part,
                    'metadata': {
                        **base_metadata,
                        'original_content': raw_html
                    }
                }
                chunks.append(chunk)

        # === LaTeX Formula ===
        elif block_type == 'latex_formula':
            raw_latex = block.get('raw_latex', '')
            chunk = {
                'doc_name': doc_name,
                'chunk_type': 'formula',
                'content_for_embedding': f"Ngữ cảnh: {heading_context_str}. Nội dung là một công thức toán học.",
                'metadata': {
                    **base_metadata,
                    'original_content': raw_latex
                }
            }
            chunks.append(chunk)

        # === Image Placeholder ===
        elif block_type == 'image_placeholder':
            image_id = block.get('id')
            # 🔧 Ảnh nằm trong thư mục tài liệu tương ứng
            image_path = os.path.join("private_submission", doc_name, "images", f"image_{image_id}.jpg")
            
            text_context_before = ""
            if i > 0 and blocks[i-1].get('type') == 'paragraph':
                text_context_before = blocks[i-1].get('content', '')
            
            text_context_after = ""
            if i < len(blocks) - 1 and blocks[i+1].get('type') == 'paragraph':
                text_context_after = blocks[i+1].get('content', '')

            full_text_context = f"Đoạn văn trước ảnh: '{text_context_before}'. Đoạn văn sau ảnh: '{text_context_after}'"

            chunk = {
                'doc_name': doc_name,
                'chunk_type': 'image',
                'content_for_embedding': image_path,
                'metadata': {
                    **base_metadata,
                    'original_content': f"image_{image_id}",
                    'image_path': image_path,
                    'text_context': full_text_context.strip()
                }
            }
            chunks.append(chunk)

    return chunks
