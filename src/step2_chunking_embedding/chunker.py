from typing import List, Dict, Any
from bs4 import BeautifulSoup

# Giả sử hàm parse_document từ file parser.py đã được import
# from .parser import parse_document 
# (Chúng ta sẽ kết nối chúng sau, giờ cứ tập trung vào logic)

def linearize_html_table(html_content: str) -> str:
    soup = BeautifulSoup(html_content, 'html.parser')
    text_parts = []
    
    caption = soup.find('caption')
    if caption:
        text_parts.append(f"Nội dung bảng: {caption.get_text(strip=True)}.")

    rows = soup.find_all('tr')
    for row in rows:
        cols = row.find_all(['td', 'th']) 
        row_text = ", ".join([col.get_text(strip=True) for col in cols])
        text_parts.append(f"Một hàng trong bảng chứa: {row_text}.")
        
    return " ".join(text_parts)

def create_chunks(blocks: List[Dict[str, Any]], doc_name: str) -> List[Dict[str, Any]]:
    """
    Chuyển đổi danh sách các khối nội dung thành danh sách các chunk có thể được embedding.

    Mỗi chunk sẽ chứa:
    - doc_name: Tên tài liệu gốc
    - chunk_type: 'text', 'table', 'image', 'formula'
    - content_for_embedding: Nội dung sẽ được đưa vào mô hình embedding.
    - metadata: Thông tin bổ sung để truy xuất và tái tạo ngữ cảnh.
    """
    chunks = []
    current_headings = []
    last_paragraph = ""

    for block in blocks:
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
                'original_content': block.get('content', block.get('raw_html', block.get('raw_latex', f"image_{block.get('id')}")))
            }
        }

        if block_type == 'paragraph':
            content = block.get('content', '')
            last_paragraph = content 
            
            chunk['chunk_type'] = 'text'
            chunk['content_for_embedding'] = f"Ngữ cảnh: {heading_context_str}. Nội dung: {content}"
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
            image_path = f"images/image_{image_id}.jpg" 
            
            chunk['chunk_type'] = 'image'
            chunk['content_for_embedding'] = image_path
            chunk['metadata']['image_path'] = image_path
            chunk['metadata']['text_context'] = last_paragraph 
            chunks.append(chunk)

    return chunks

# --- MAIN ĐỂ KIỂM THỬ ---
if __name__ == '__main__':
    # Đây là output mẫu từ file parser.py của chúng ta
    sample_parsed_blocks = [
        {"type": "heading", "level": 1, "content": "Đây là Tiêu đề chính"},
        {"type": "paragraph", "content": "Đây là đoạn văn bản giới thiệu đầu tiên. Nó mô tả nội dung của tài liệu."},
        {"type": "heading", "level": 2, "content": "Một Tiêu đề phụ"},
        {"type": "paragraph", "content": "Đây là đoạn văn bản thứ hai, nằm dưới tiêu đề phụ."},
        {"type": "image_placeholder", "id": 1},
        {"type": "html_table", "raw_html": "<table><caption>Bảng kết quả</caption><tr><td>Hàng 1, Cột 1</td><td>Hàng 1, Cột 2</td></tr></table>"},
        {"type": "paragraph", "content": "Một đoạn văn bản khác nằm giữa bảng và công thức."},
        {"type": "latex_formula", "raw_latex": "$$\\nE = mc^2\\n$$"},
        {"type": "paragraph", "content": "Đây là đoạn văn bản cuối cùng."}
    ]

    # Chạy hàm chunker
    print("--- Bắt đầu tạo chunks ---")
    final_chunks = create_chunks(sample_parsed_blocks, doc_name="Public_Test_001")

    # In kết quả ra để kiểm tra
    import json
    print(json.dumps(final_chunks, indent=2, ensure_ascii=False))
    print(f"\n--- Tạo chunks hoàn tất. Tổng số chunks: {len(final_chunks)} ---")