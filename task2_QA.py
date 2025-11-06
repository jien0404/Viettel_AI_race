import os
import csv
import argparse
from typing import List
from pathlib import Path

from src.step3_retrieval_qa.retriever import Retriever
from src.step3_retrieval_qa.qwen_client import QwenClient
from src.step3_retrieval_qa.utils import extract_choice_letters

def build_prompt(question: str, choices: List[str], contexts: List[dict]) -> str:
    """
    Tạo prompt cho model Qwen:
    - cung cấp ngữ cảnh (top-k retrieved)
    - hỏi rõ ràng cần chọn đáp án (có thể nhiều đáp án)
    - yêu cầu trả về dạng danh sách chữ cái phân tách bởi dấu phẩy, ví dụ: A,B
    """
    ctx_texts = []
    for i, c in enumerate(contexts):
        md = c.get("metadata", {})
        orig = md.get("original_content") or md.get("context_headings") or str(md)
        snippet = orig
        ctx_texts.append(f"[Context {i+1}] {snippet}")

    ctx_block = "\n".join(ctx_texts) if ctx_texts else "Không có ngữ cảnh liên quan."
    choices_block = "\n".join([f"{chr(65+i)}. {choices[i]}" for i in range(len(choices))])

    prompt = f"""
Bạn là một trợ lý chuyên môn. Dưới đây là ngữ cảnh tìm được (nếu có) và một câu hỏi trắc nghiệm với các lựa chọn. Câu hỏi có thể có một hoặc nhiều đáp án đúng.
Ngữ cảnh:
{ctx_block}

Câu hỏi:
{question}

Lựa chọn:
{choices_block}

Yêu cầu:
1) Trả về chỉ các chữ cái đáp án đúng (A,B,C,D,...) phân tách bởi dấu phẩy nếu có nhiều đáp án, không kèm giải thích.
2) Nếu không thể xác định, trả về 'Không xác định'.
Ví dụ trả về hợp lệ: A hoặc A,B
"""
    return prompt.strip()

def read_questions(csv_path: str):
    rows = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)
    return rows

def run(csv_questions_path: str,
        chroma_dir: str = "chroma_database",
        collection_name: str = "default",
        output_answer_md: str = "submission/answer.md",
        top_k: int = 5):
    retriever = Retriever(persist_directory=chroma_dir, collection_name=collection_name)
    qwen = QwenClient()

    questions = read_questions(csv_questions_path)
    results = []

    for idx, row in enumerate(questions, start=1):
        q_text = row['Question'].strip()
        # build choices list from columns A-D
        choices = []
        for c in ['A','B','C','D']:
            choices.append(row.get(c,"").strip())

        # retrieve context
        contexts = retriever.retrieve(q_text, top_k=top_k)

        prompt = build_prompt(q_text, choices, contexts)
        gen = qwen.generate(prompt, max_tokens=256, temperature=0.0)

        preds = extract_choice_letters(gen)
        if not preds:
            answer = "Không xác định"
        else:
            answer = ",".join(preds)

        results.append((idx, answer))
        print(f"[{idx}] Q: {q_text[:60]}... => Ans: {answer}")

    # Append to submission/answer.md
    out_path = Path(output_answer_md)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open('a', encoding='utf-8') as f:
        f.write("\n### TASK QA\n")
        f.write("num_correct,answers\n")
        for idx, ans in results:
            # ensure CSV-friendly quoting if contains comma
            if "," in ans:
                f.write(f'{idx},"{ans}"\n')
            else:
                f.write(f"{idx},{ans}\n")

    print(f"Hoàn tất. Kết quả được ghi tiếp vào: {output_answer_md}")