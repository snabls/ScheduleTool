import pdfplumber
import json
import os
import re

def get_teacher_files(directory):
    """Get all teacher JSON files"""
    teacher_files = {}
    for filename in os.listdir(directory):
        if filename.endswith(".json") and filename != "package.json":
            name = filename.replace(".json", "")
            teacher_files[name] = os.path.join(directory, filename)
    return teacher_files

def normalize_name(name):
    """Normalize teacher name for comparison"""
    # Remove extra spaces, convert to uppercase
    return " ".join(name.upper().split())

def parse_room(cell_text):
    """Extract room/activity from cell text"""
    if not cell_text:
        return None
    
    # Normalize text
    text = cell_text.strip()
    
    if "Potenziamento" in text:
        return "Potenziamento"
    if "Vicepresidenza" in text:
        return "Vicepresidenza"
    if "Sportello" in text:
        return "Sportello"
    
    # Split by newline to find the room
    lines = text.split('\n')
    # The room is usually the last line
    if lines:
        return lines[-1].strip()
    return None

def update_json_schedule(json_path, schedule_data):
    """Update JSON file with extracted schedule"""
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    day_map = {
        'Lunedì': 'Lun',
        'Martedì': 'Mar',
        'Mercoledì': 'Mer',
        'Giovedì': 'Gio',
        'Venerdì': 'Ven',
        'Sabato': 'Sab'
    }
    
    hour_map = {
        'H1': 'I',
        'H2': 'II',
        'H3': 'III',
        'H4': 'IV',
        'H5': 'V',
        'H6': 'VI'
    }
    
    for day_obj in data['orario']:
        day_name_key = list(day_obj.keys())[0]
        
        for extract_day, hours in schedule_data.items():
            if day_map.get(extract_day) == day_name_key:
                for h_idx, room in hours.items():
                    if h_idx in hour_map:
                        roman_hour = hour_map[h_idx]
                        if roman_hour in day_obj[day_name_key]:
                            day_obj[day_name_key][roman_hour] = room
                            
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def extract_teacher_name_from_page(page):
    """Extract teacher name from page"""
    text = page.extract_text()
    if not text:
        return None
    
    lines = text.split('\n')
    # Teacher name is typically on line 2 (after "IS Pascal Comandini")
    for i, line in enumerate(lines[:6]):
        clean_line = line.strip()
        # Skip known non-teacher lines
        if clean_line in ['IS Pascal Comandini', 'Commenti: Commenti', 'Indice dei contenuti', '']:
            continue
        if any(x in clean_line for x in ['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato']):
            continue
        # This should be the teacher name
        if len(clean_line) > 3:
            return clean_line
    return None

def extract_schedule(pdf_path, json_dir):
    """Extract schedule from PDF and update JSON files"""
    teacher_files = get_teacher_files(json_dir)
    print(f"Found {len(teacher_files)} teacher JSON files.")
    
    # Create normalized name mapping
    name_to_file = {}
    for teacher_name, file_path in teacher_files.items():
        normalized = normalize_name(teacher_name)
        name_to_file[normalized] = (teacher_name, file_path)
    
    found_teachers = set()
    not_found_in_json = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            # Extract teacher name from page
            teacher_name_pdf = extract_teacher_name_from_page(page)
            
            if not teacher_name_pdf:
                continue
            
            # Try to match with JSON files
            normalized_pdf_name = normalize_name(teacher_name_pdf)
            
            if normalized_pdf_name not in name_to_file:
                not_found_in_json.append((i+1, teacher_name_pdf))
                continue
            
            teacher_name_json, json_path = name_to_file[normalized_pdf_name]
            found_teachers.add(teacher_name_json)
            
            print(f"Processing Page {i+1} for {teacher_name_json}")
            
            tables = page.extract_tables()
            if not tables:
                print(f"  No tables found")
                continue
            
            table = tables[0]
            
            # Don't propagate None values - pdfplumber handles merged cells
            # The previous logic was incorrectly filling empty cells
            
            if not table or len(table) == 0:
                continue

            # Extract days from header
            days = table[0][1:] if len(table[0]) > 1 else []
            days = [d.replace('\n', '').replace('Mercoledì', 'Mercoledì') if d else d for d in days]
            
            extracted_schedule = {}
            
            for row in table[1:]:
                if not row or len(row) < 2:
                    continue
                
                hour_label = row[0]
                if not hour_label or not isinstance(hour_label, str) or not hour_label.startswith('H'):
                    continue
                
                cells = row[1:]
                for day_idx, cell_text in enumerate(cells):
                    if day_idx < len(days):
                        day_name = days[day_idx]
                        if not day_name:
                            continue
                            
                        room = parse_room(cell_text)
                        if room:
                            if day_name not in extracted_schedule:
                                extracted_schedule[day_name] = {}
                            extracted_schedule[day_name][hour_label] = room
            
            # Update JSON
            if extracted_schedule:
                update_json_schedule(json_path, extracted_schedule)
                print(f"  Updated {teacher_name_json}")

    print(f"\n{'='*60}")
    print(f"Processed {len(found_teachers)} teachers successfully")
    
    missing_teachers = set(teacher_files.keys()) - found_teachers
    if missing_teachers:
        print(f"\nMissing teachers (JSON exists but not found in PDF): {len(missing_teachers)}")
        for t in sorted(missing_teachers):
            print(f"  - {t}")
    
    if not_found_in_json:
        print(f"\nTeachers in PDF but no JSON file: {len(not_found_in_json)}")
        for page_num, name in not_found_in_json:
            print(f"  Page {page_num}: {name}")

if __name__ == "__main__":
    pdf_path = "ITT-Pascal-orario-definitivo-docenti-dal-30-ottobre.pdf"
    json_dir = "."
    extract_schedule(pdf_path, json_dir)
