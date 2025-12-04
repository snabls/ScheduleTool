import pdfplumber

# Extract PULGA LUCA with proper handling of merged cells (double hours)
with pdfplumber.open("ITT-Pascal-orario-definitivo-docenti-dal-30-ottobre.pdf") as pdf:
    page = pdf.pages[69]  # Page 70, 0-indexed
    
    tables = page.extract_tables()
    if tables:
        table = tables[0]
        
        print("PULGA LUCA - With double hours handling")
        print("="*80)
        
        # Process each day column
        for day_idx in range(1, 7):  # Columns 1-6 are the days
            day_names = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato"]
            day_name = day_names[day_idx - 1]
            
            print(f"\n{day_name}:")
            
            # Track previous value for double hours
            prev_value = None
            
            for hour_idx in range(1, 7):  # Rows 1-6 are H1-H6
                if hour_idx < len(table) and day_idx < len(table[hour_idx]):
                    cell = table[hour_idx][day_idx]
                    
                    # If cell is None, use previous value (double hour)
                    if cell is None:
                        room = prev_value
                    else:
                        # Extract room from cell
                        if cell:
                            lines = cell.split('\n')
                            room = lines[-1] if lines else None
                        else:
                            room = None
                        prev_value = room
                    
                    hour_names = ['I', 'II', 'III', 'IV', 'V', 'VI']
                    print(f"  {hour_names[hour_idx-1]}: {room if room else 'null'}")
