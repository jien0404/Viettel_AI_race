import os
from typing import List, Dict, Any, Optional
from bs4 import BeautifulSoup

def _find_flexible_image_path(base_dir: str, image_id: int) -> Optional[str]:
    """
    Tìm kiếm đường dẫn file ảnh linh hoạt, hỗ trợ nhiều định dạng đuôi ảnh
    và hai kiểu đặt tên 'image_{id}' và 'image{id}'.
    """
    # Danh sách các đuôi file ảnh phổ biến để kiểm tra
    supported_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp']

    for ext in supported_extensions:
        # Thử kiểu tên 'image_{id}.ext'
        path_with_underscore = os.path.join(base_dir, f"image_{image_id}{ext}")
        if os.path.exists(path_with_underscore):
            return path_with_underscore

        # Thử kiểu tên 'image{id}.ext'
        path_without_underscore = os.path.join(base_dir, f"image{image_id}{ext}")
        if os.path.exists(path_without_underscore):
            return path_without_underscore
    
    # Trả về None nếu không tìm thấy bất kỳ file nào khớp
    return None

def linearize_html_table(html_content: str) -> str:
    """
    Chuyển đổi một bảng HTML thành một chuỗi văn bản tuyến tính, dễ hiểu hơn cho LLM.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    text_parts = []
    
    caption = soup.find('caption')
    if caption:
        text_parts.append(f"Nội dung bảng: {caption.get_text(strip=True)}.")

    headers = []
    header_row = soup.find('thead')
    if not header_row:
        header_row = soup.find('tr') # Lấy hàng đầu tiên nếu không có thead

    if header_row:
        header_cols = header_row.find_all('th')
        if header_cols:
            headers = [col.get_text(strip=True) for col in header_cols]

    rows = soup.find_all('tr')
    for row in rows:
        cols = row.find_all(['td', 'th'])
        if not cols: continue
        
        # Bỏ qua hàng header nếu nó được lặp lại trong tbody
        if headers and [col.get_text(strip=True) for col in cols] == headers:
            continue

        # Tạo mô tả chi tiết nếu có header khớp
        if headers and len(headers) == len(cols):
            row_description = ", ".join([f"cột '{headers[i]}' là '{cols[i].get_text(strip=True)}'" for i in range(len(cols))])
            text_parts.append(f"Một hàng trong bảng có: {row_description}.")
        else: # Fallback cho các bảng không có cấu trúc chuẩn
            row_text = ", ".join([col.get_text(strip=True) for col in cols])
            text_parts.append(f"Một hàng trong bảng chứa: {row_text}.")
            
    return " ".join(text_parts)

def create_chunks(blocks: List[Dict[str, Any]], doc_name: str, doc_folder_path: str) -> List[Dict[str, Any]]:
    """
    Chuyển đổi danh sách các khối nội dung thành danh sách các chunk có thể được embedding.
    """
    chunks = []
    current_headings = []
    last_paragraph = ""

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
            last_paragraph = content
            
            chunk['chunk_type'] = 'text'
            chunk['content_for_embedding'] = f"Ngữ cảnh: {heading_context_str}. Nội dung: {content}"
            chunk['metadata']['original_content'] = content
            chunks.append(chunk)

        elif block_type == 'html_table':
            raw_html = block.get('raw_html', '')
            linearized_text = linearize_html_table(raw_html)
            chunk['chunk_type'] = 'table'
            chunk['content_for_embedding'] = f"Ngữ cảnh: {heading_context_str}. Bảng: {linearized_text}"
            chunk['metadata']['original_content'] = raw_html
            chunks.append(chunk)

        elif block_type == 'latex_formula':
            raw_latex = block.get('raw_latex', '')
            chunk['chunk_type'] = 'formula'
            chunk['content_for_embedding'] = f"Ngữ cảnh: {heading_context_str}. Nội dung là một công thức toán học."
            chunk['metadata']['original_content'] = raw_latex
            chunks.append(chunk)

        elif block_type == 'image_placeholder':
            image_id = block.get('id')
            images_base_dir = os.path.join(doc_folder_path, "images")
            image_path = _find_flexible_image_path(images_base_dir, image_id)
            
            # Nếu không tìm thấy đường dẫn ảnh hợp lệ, bỏ qua chunk này
            if image_path is None:
                print(f"!! CẢNH BÁO: Bỏ qua ảnh ID {image_id} cho tài liệu '{doc_name}' vì không tìm thấy file tương ứng.")
                continue 
            
            # Chỉ thực hiện các bước dưới đây NẾU tìm thấy ảnh
            chunk['chunk_type'] = 'image'
            chunk['content_for_embedding'] = image_path
            chunk['metadata']['image_path'] = image_path
            chunk['metadata']['text_context'] = last_paragraph 
            chunks.append(chunk)

    return chunks