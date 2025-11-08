from typing import List, Dict, Any
from bs4 import BeautifulSoup
import os

# Hàm này không thay đổi, dùng để chuyển đổi bảng HTML thành văn bản
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


def _get_block_content_for_length(block: Dict[str, Any]) -> str:
    """Hàm trợ giúp lấy nội dung văn bản của một block để tính độ dài."""
    block_type = block.get('type')
    if block_type == 'paragraph':
        return block.get('content', '')
    elif block_type == 'html_table':
        return linearize_html_table(block.get('raw_html', ''))
    elif block_type == 'latex_formula':
        return block.get('raw_latex', '')
    # Bỏ qua heading và image vì chúng không có nội dung văn bản trực tiếp để gộp
    return ""


def _split_large_text(text: str, chunk_size: int, overlap_size: int) -> List[str]:
    """Chia một đoạn văn bản lớn thành các phần nhỏ hơn có gối đầu."""
    if len(text) <= chunk_size:
        return [text]
    
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        # Bước nhảy = kích thước chunk - kích thước gối đầu
        start += (chunk_size - overlap_size)
    return chunks


def create_chunks(blocks: List[Dict[str, Any]], 
                  doc_name: str, 
                  chunk_size: int = 1024, 
                  overlap_ratio: float = 0.4) -> List[Dict[str, Any]]:
    """
    Tạo các chunk từ danh sách block đã được phân tích.
    Logic mới:
    1. Ưu tiên gộp [block trước, block ảnh, block sau] thành một chunk duy nhất.
    2. Với các block còn lại, gộp các block nhỏ lại với nhau cho đến khi đạt `chunk_size`.
    3. Nếu một block lớn hơn `chunk_size`, chia nhỏ nó ra với overlap.
    """
    final_chunks = []
    current_headings = []
    
    overlap_size = int(chunk_size * overlap_ratio)

    # --- Bước 1: Xử lý ưu tiên các chunk hình ảnh ---
    # Tạo một danh sách các block mới và đánh dấu các block đã được xử lý
    processed_indices = set()
    image_combined_blocks = []
    
    for i, block in enumerate(blocks):
        if block.get('type') == 'image_placeholder':
            # Gom block trước, ảnh và sau vào một "siêu block"
            context_before_block = blocks[i-1] if i > 0 else None
            context_after_block = blocks[i+1] if i < len(blocks) - 1 else None
            
            # Gộp nội dung và metadata
            combined_content = ""
            combined_original_content = []
            if context_before_block and (i-1) not in processed_indices:
                combined_content += _get_block_content_for_length(context_before_block) + "\n\n"
                combined_original_content.append(context_before_block)
                processed_indices.add(i-1)

            # Thêm thông tin ảnh
            image_id = block.get('id')
            image_path = os.path.join('images', f'image_{image_id}.jpg')
            image_placeholder_text = f"[[MÔ TẢ CHO HÌNH ẢNH TẠI ĐƯỜNG DẪN: {image_path}]]"
            combined_content += image_placeholder_text

            combined_original_content.append({
                'type': 'image_placeholder',
                'id': image_id,
                'image_path': image_path
            })
            processed_indices.add(i)

            if context_after_block and (i+1) not in processed_indices:
                combined_content += "\n\n" + _get_block_content_for_length(context_after_block)
                combined_original_content.append(context_after_block)
                processed_indices.add(i+1)
            
            # Tạo một chunk duy nhất cho cụm ảnh này
            chunk = {
                'doc_name': doc_name,
                'chunk_type': 'image_context',
                'content_for_enrichment': combined_content,
                'metadata': {
                    'context_headings': " > ".join(current_headings),
                    'original_blocks': combined_original_content,
                    'image_path': image_path
                }
            }
            final_chunks.append(chunk)

    # --- Bước 2: Xử lý các block văn bản còn lại ---
    buffer_blocks = []
    buffer_len = 0

    for i, block in enumerate(blocks):
        if i in processed_indices:
            continue

        block_type = block.get('type')
        if block_type == 'heading':
            level = block.get('level', 1)
            current_headings = current_headings[:level-1]
            current_headings.append(block.get('content', ''))
            continue
        
        block_content = _get_block_content_for_length(block)
        block_len = len(block_content)

        if block_len == 0:
            continue

        # Trường hợp 1: Một block đã quá lớn, cần chia nhỏ ngay lập tức
        if block_len > chunk_size:
            # Xử lý buffer hiện có trước khi xử lý block lớn này
            if buffer_blocks:
                combined_buffer_content = "\n\n".join([_get_block_content_for_length(b) for b in buffer_blocks])
                final_chunks.append({
                    'doc_name': doc_name, 'chunk_type': 'text',
                    'content_for_enrichment': combined_buffer_content,
                    'metadata': {'context_headings': " > ".join(current_headings), 'original_blocks': buffer_blocks}
                })
                buffer_blocks, buffer_len = [], 0

            # Chia nhỏ block lớn
            sub_chunks_text = _split_large_text(block_content, chunk_size, overlap_size)
            for text_part in sub_chunks_text:
                final_chunks.append({
                    'doc_name': doc_name, 'chunk_type': 'text',
                    'content_for_enrichment': text_part,
                    'metadata': {'context_headings': " > ".join(current_headings), 'original_blocks': [block]}
                })
            continue

        # Trường hợp 2: Thêm block vào buffer sẽ làm buffer quá lớn
        if buffer_len + block_len > chunk_size:
            # Xử lý buffer cũ
            combined_buffer_content = "\n\n".join([_get_block_content_for_length(b) for b in buffer_blocks])
            final_chunks.append({
                'doc_name': doc_name, 'chunk_type': 'text',
                'content_for_enrichment': combined_buffer_content,
                'metadata': {'context_headings': " > ".join(current_headings), 'original_blocks': buffer_blocks}
            })
            # Bắt đầu buffer mới với block hiện tại
            buffer_blocks = [block]
            buffer_len = block_len
        
        # Trường hợp 3: Thêm block vào buffer bình thường
        else:
            buffer_blocks.append(block)
            buffer_len += block_len

    # Xử lý nốt phần buffer còn lại sau khi kết thúc vòng lặp
    if buffer_blocks:
        combined_buffer_content = "\n\n".join([_get_block_content_for_length(b) for b in buffer_blocks])
        final_chunks.append({
            'doc_name': doc_name, 'chunk_type': 'text',
            'content_for_enrichment': combined_buffer_content,
            'metadata': {'context_headings': " > ".join(current_headings), 'original_blocks': buffer_blocks}
        })
        
    return final_chunks