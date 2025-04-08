import pymupdf  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = pymupdf.open(pdf_path)
    full_text = ""

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        clean_text = text.replace('\n', ' ').strip()
        full_text += clean_text
        print(f"Page {page_num + 1}:\n{clean_text}\n")
    
    doc.close()
    return full_text

# Example usage
pdf_path = r""  # Fill with your file path
text = extract_text_from_pdf(pdf_path)

# Print or save the result
print(text)

# Optional: save to a .txt file
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(text)
