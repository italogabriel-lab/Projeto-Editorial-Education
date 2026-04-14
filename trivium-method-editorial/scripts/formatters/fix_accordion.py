#!/usr/bin/env python3
"""
Script to fix Accordion definitions in 4th year lesson files.
Removes term name repetition from lines 39 and 43 of each file.
"""
import os
import re
import glob

BASE_DIR = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto Bibline Academy/Belas Artes - Fase da Gramática/1 Fase - Gramática/4º Ano - IMPRESSIONISMO ATÉ A ARTE CONTEMPORÂNEA"

# Get all lesson files (excluding .4 review and .5 exam files)
files = glob.glob(os.path.join(BASE_DIR, "*.md"))
lesson_files = [f for f in files if re.search(r'\d+\.[123]\.md$', f)]
lesson_files.sort(key=lambda x: (int(re.search(r'(\d+)\.\d+\.md$', x).group(1)), 
                                  int(re.search(r'\d+\.(\d+)\.md$', x).group(1))))

fixed = 0
already_ok = 0
errors = []

for filepath in lesson_files:
    filename = os.path.basename(filepath)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        if len(lines) < 44:
            errors.append(f"{filename}: file too short ({len(lines)} lines)")
            continue
        
        # Line 39 (index 38) - plain definition
        line39 = lines[38].rstrip('\n')
        # Line 43 (index 42) - bold definition
        line43 = lines[42].rstrip('\n')
        
        # Check if line 39 already starts with "É " or other non-term patterns
        if line39.startswith("É ") or line39.startswith("Ocorre ") or line39.startswith("Permitiu ") or line39.startswith("Foi "):
            already_ok += 1
            continue
        
        # Extract the term from line 31 (index 30) - "O que é [Termo]?"
        line31 = lines[30].rstrip('\n')
        term_match = re.match(r'O que é (.+?)\?', line31)
        if not term_match:
            errors.append(f"{filename}: could not extract term from line 31: '{line31}'")
            continue
        
        term = term_match.group(1)
        
        # Fix line 39: remove term from beginning
        # Pattern: "Term é ..." -> "É ..."
        # Pattern: "Term permitiu..." -> "Permitiu..."  
        # Pattern: "Term ocorre..." -> "Ocorre..."
        new_line39 = line39
        
        # Try "Term é" pattern (most common)
        if line39.startswith(f"{term} é "):
            new_line39 = "É " + line39[len(f"{term} é "):]
        elif line39.lower().startswith(f"{term.lower()} é "):
            new_line39 = "É " + line39[len(f"{term} é "):]
        elif line39.startswith(f"{term} "):
            # Other verb patterns: "Term permitiu...", "Term ocorre..."
            rest = line39[len(f"{term} "):]
            new_line39 = rest[0].upper() + rest[1:]
        else:
            errors.append(f"{filename}: line 39 doesn't start with term '{term}': '{line39}'")
            continue
        
        # Fix line 43: remove bold term from beginning
        new_line43 = line43
        
        # Pattern: "**Term** é ..." -> "É ..."
        bold_term_patterns = [
            f"**{term}** é ",  # **Term** é
            f"**{term}** ",    # **Term** + verb
        ]
        
        # Also handle multi-word terms where each word might be bolded separately
        # e.g., "**Cor arbitrária** é" or "O **tubo de metal** permitiu"
        
        found = False
        for pattern in bold_term_patterns:
            if line43.startswith(pattern):
                if "é " in pattern:
                    new_line43 = "É " + line43[len(pattern):]
                else:
                    rest = line43[len(pattern):]
                    new_line43 = rest[0].upper() + rest[1:]
                found = True
                break
        
        if not found:
            # Try pattern with "O " prefix: "O **term** verb..."
            o_match = re.match(r'^O \*\*.+?\*\* (.+)$', line43)
            if o_match:
                rest = o_match.group(1)
                new_line43 = rest[0].upper() + rest[1:]
                found = True
        
        if not found:
            # Try generic bold term at start
            bold_match = re.match(r'^\*\*[^*]+\*\* é (.+)$', line43)
            if bold_match:
                new_line43 = "É " + bold_match.group(1)
                found = True
        
        if not found:
            bold_match2 = re.match(r'^\*\*[^*]+\*\* (.+)$', line43)
            if bold_match2:
                rest = bold_match2.group(1)
                new_line43 = rest[0].upper() + rest[1:]
                found = True
        
        if not found:
            errors.append(f"{filename}: could not parse line 43: '{line43}'")
            continue
        
        # Apply changes
        lines[38] = new_line39 + '\n'
        lines[42] = new_line43 + '\n'
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        
        fixed += 1
        print(f"✅ {filename}: '{term}' -> fixed")
        
    except Exception as e:
        errors.append(f"{filename}: {str(e)}")

print(f"\n{'='*50}")
print(f"Total lesson files: {len(lesson_files)}")
print(f"Fixed: {fixed}")
print(f"Already OK: {already_ok}")
print(f"Errors: {len(errors)}")

if errors:
    print(f"\nErrors:")
    for err in errors:
        print(f"  ❌ {err}")
