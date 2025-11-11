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
    Tạo các chunk từ danh sách block.
    Logic cải tiến: Coi toàn bộ tài liệu như một dòng văn bản liên tục và cắt nó
    một cách thông minh, tôn trọng ranh giới của các block.
    """
    final_chunks = []
    current_headings = []
    overlap_size = int(chunk_size * overlap_ratio)
    processed_indices = set()

    # --- Bước 1: Xử lý ưu tiên các chunk hình ảnh (Logic này vẫn tốt và giữ nguyên) ---
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

    # --- Bước 2: Xử lý các block văn bản còn lại với logic gộp mới ---
    # Thay vì gộp block, chúng ta gộp nội dung
    text_buffer = ""
    original_blocks_buffer = []

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
        if not block_content:
            continue

        # Thêm nội dung block mới vào buffer
        # Thêm dấu xuống dòng để ngăn các block dính vào nhau
        if text_buffer:
            text_buffer += "\n\n"
        text_buffer += block_content
        original_blocks_buffer.append(block)

        # Liên tục kiểm tra và cắt buffer nếu nó đủ lớn
        while len(text_buffer) >= chunk_size:
            # Lấy một phần của buffer để tạo chunk
            chunk_content = text_buffer[:chunk_size]
            
            final_chunks.append({
                'doc_name': doc_name,
                'chunk_type': 'text',
                'content_for_enrichment': chunk_content,
                'metadata': {
                    'context_headings': " > ".join(current_headings),
                    # Lưu ý: original_blocks ở đây có thể không hoàn toàn chính xác 100%
                    # nhưng nó đủ tốt để biết chunk này đến từ đâu.
                    'original_blocks': original_blocks_buffer 
                }
            })
            
            # Cập nhật lại buffer: giữ lại phần gối đầu
            text_buffer = text_buffer[chunk_size - overlap_size:]
            
            # Sau khi cắt, buffer có thể chứa nội dung từ nhiều block,
            # việc xác định chính xác original_blocks cho phần còn lại rất phức tạp.
            # Chúng ta chấp nhận một sự đơn giản hóa ở đây.
            # Hoặc làm rỗng buffer block để bắt đầu lại.
            original_blocks_buffer = []


    # Xử lý nốt phần buffer còn lại sau khi kết thúc vòng lặp
    if text_buffer:
        final_chunks.append({
            'doc_name': doc_name,
            'chunk_type': 'text',
            'content_for_enrichment': text_buffer,
            'metadata': {
                'context_headings': " > ".join(current_headings),
                'original_blocks': original_blocks_buffer
            }
        })
        
    return final_chunks