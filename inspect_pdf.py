import pdfplumber

def inspect_pdf(pdf_path):
    with open("pdf_dump.txt", "w", encoding="utf-8") as f:
        try:
            with pdfplumber.open(pdf_path) as pdf:
                f.write(f"Total pages: {len(pdf.pages)}\n")
                for i, page in enumerate(pdf.pages):
                    text = page.extract_text()
                    lines = text.split('\n') if text else []
                    header = lines[:5] if lines else []
                    f.write(f"--- Page {i+1} ---\n")
                    f.write(f"Header: {header}\n")
                    
                    tables = page.extract_tables()
                    if tables:
                        f.write("Table sample (first 5 rows):\n")
                        for row in tables[0][:5]:
                            f.write(str(row) + "\n")
                    else:
                        f.write("No tables found.\n")
                    f.write("\n" + "="*20 + "\n")
        except Exception as e:
            f.write(f"Error: {e}\n")

if __name__ == "__main__":
    inspect_pdf("ITT-Pascal-orario-definitivo-docenti-dal-30-ottobre.pdf")
