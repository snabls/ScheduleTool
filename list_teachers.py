import pdfplumber

# Create a script to check which teachers are in the PDF
with pdfplumber.open("ITT-Pascal-orario-definitivo-docenti-dal-30-ottobre.pdf") as pdf:
    teachers_in_pdf = []
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        if not text:
            continue
        
        lines = text.split('\n')
        # Teacher name is usually in line 2 or 3
        if len(lines) >= 4:
            # Check lines 1-4 for teacher name
            for line in lines[1:5]:
                # Clean the line
                clean_line = line.strip()
                if clean_line and len(clean_line) > 5 and clean_line != "IS Pascal Comandini":
                    # This might be a teacher name
                    if not any(x in clean_line for x in ['Lunedì', 'Martedì', 'Commenti', 'Indice']):
                        teachers_in_pdf.append((i+1, clean_line))
                        break

print(f"Found {len(teachers_in_pdf)} teacher pages in PDF:")
for page_num, name in teachers_in_pdf:
    print(f"Page {page_num}: {name}")
