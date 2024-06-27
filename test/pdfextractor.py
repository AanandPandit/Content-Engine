import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    document = fitz.open(pdf_path)
    text = ""

    # Iterate over each page
    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text += page.get_text()

    return text

# Example usage
if __name__ == "__main__":
    pdf_path = "data\\uber-10-k-2023.pdf"
    text = extract_text_from_pdf(pdf_path)
    print(text)  # Or save to a file

#-------------------------------------------------------------------------
