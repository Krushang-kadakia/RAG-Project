import pdfplumber

def read_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    cleaned_row = [cell.strip() if cell else "" for cell in row]
                    text += "\n" + "\t".join(cleaned_row)
            text += "\n"
    return text.strip()
