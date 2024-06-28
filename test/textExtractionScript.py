import fitz  # PyMuPDF
import os
import json

def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""

    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text += page.get_text()

    return text

def save_text_to_file(text, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)

def save_texts_to_json(texts, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(texts, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    pdf_files = [
        r"data\goog-10-k-2023.pdf",
        r"data\tsla-20231231-gen.pdf",
        r"data\uber-10-k-2023.pdf"
    ]

    output_dir = "extracted_texts"
    os.makedirs(output_dir, exist_ok=True)

    texts = {}
    for pdf_file in pdf_files:
        text = extract_text_from_pdf(pdf_file)
        filename = os.path.splitext(os.path.basename(pdf_file))[0]
        output_path_txt = os.path.join(output_dir, filename + ".txt")
        save_text_to_file(text, output_path_txt)
        texts[filename] = text
        print(f"Saved extracted text to {output_path_txt}")

    output_path_json = os.path.join(output_dir, "extracted_texts.json")
    save_texts_to_json(texts, output_path_json)
    print(f"Saved extracted texts to {output_path_json}")
