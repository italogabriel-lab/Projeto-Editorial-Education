#!/usr/bin/env python3
import re
import os

base = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto Bibline Academy/Belas Artes - Fase da Gramática/1 Fase - Gramática/3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE/Estrutura Curricular - 3º ANO"
base_lessons = os.path.dirname(base)

macro_path = os.path.join(base, "1 - Curriculo Macro - Arte Cristã Oriental até o Renascimento do Norte - 3º ANO.md")
matriz_path = os.path.join(base, "2 - Matriz-Curricular-objetivos - 3º ANO.md")
visao_path = os.path.join(base, "3 - Visão e Plano pedagogico - 3º ANO.md")
desc_path = os.path.join(base, "6 - Descrições para tickets - 3º ANO.md")

# 1. Extract canonical titles
with open(macro_path, "r", encoding="utf-8") as f:
    macro_content = f.read()

canonical = {}
current_week = None
for line in macro_content.split('\n'):
    week_match = re.match(r'## Semana (\d+)', line)
    if week_match:
        current_week = int(week_match.group(1))
    
    day_match = re.match(r'- Dia (\d): (.+?)(?:\s*✅)?$', line)
    if day_match and current_week:
        lid = f"{current_week}.{day_match.group(1)}"
        canonical[lid] = day_match.group(2).strip()

print(f"Loaded {len(canonical)} canonical titles from Macro.")

# Helper to read/write
def update_file(filepath, processor):
    if not os.path.exists(filepath):
        print(f"Not found: {filepath}")
        return
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    new_content, changes = processor(content)
    if changes > 0:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {filepath.split('/')[-1]} with {changes} changes.")
    else:
        print(f"No changes needed for {filepath.split('/')[-1]}.")

# 2. Update Matriz
def process_matriz(content):
    lines = content.split('\n')
    changes = 0
    for i, line in enumerate(lines):
        match = re.match(r'^(\|\s*)(\d+\.\d+)(\s*\|\s*\*\*)(.+?)(\*\*\s*\|.*)$', line)
        if match:
            pre, lid, mid, old_title, post = match.groups()
            if lid in canonical and old_title != canonical[lid]:
                lines[i] = f"{pre}{lid}{mid}{canonical[lid]}{post}"
                changes += 1
    return '\n'.join(lines), changes

update_file(matriz_path, process_matriz)

# 3. Update Visão
def process_visao(content):
    lines = content.split('\n')
    changes = 0
    for i, line in enumerate(lines):
        # Table format: | **1.1** | **Title** |
        match_table = re.match(r'^(\|\s*\*\*)(\d+\.\d+)(\*\*\s*\|\s*\*\*)(.+?)(\*\*\s*\|.*)$', line)
        if match_table:
            pre, lid, mid, old_title, post = match_table.groups()
            if lid in canonical and old_title != canonical[lid]:
                lines[i] = f"{pre}{lid}{mid}{canonical[lid]}{post}"
                changes += 1
            continue
            
        # List format: 1. **1.1 – Title**
        match_list = re.match(r'^(\d+\.\s*\*\*)(\d+\.\d+)( – )(.+?)(\*\*.*)$', line)
        if match_list:
            pre, lid, mid, old_title, post = match_list.groups()
            if lid in canonical and old_title != canonical[lid]:
                lines[i] = f"{pre}{lid}{mid}{canonical[lid]}{post}"
                changes += 1
                
    return '\n'.join(lines), changes

update_file(visao_path, process_visao)

# 4. Update Descrições
def process_desc(content):
    lines = content.split('\n')
    changes = 0
    for i, line in enumerate(lines):
        # Format 1: [Belas artes] - Ano 3 - X.Y Title
        match_h = re.match(r'^(\[Belas artes\] - Ano 3 - )(\d+\.\d+) (.+)$', line)
        if match_h:
            prefix, lid, old_title = match_h.groups()
            # Skip reviews/exams (e.g., "1.4 Revisão") unless it's a real lesson lid
            parts = lid.split('.')
            if len(parts) == 2 and parts[1] in ('1', '2', '3') and lid in canonical:
                if old_title != canonical[lid]:
                    lines[i] = f"{prefix}{lid} {canonical[lid]}"
                    changes += 1
            continue
            
        # Format 2: - X.Y Title (inside review/exam blocks)
        match_list = re.match(r'^(- )(\d+\.\d+) (.+)$', line)
        if match_list:
            prefix, lid, old_title = match_list.groups()
            if lid in canonical and old_title != canonical[lid]:
                lines[i] = f"{prefix}{lid} {canonical[lid]}"
                changes += 1
                
    return '\n'.join(lines), changes

update_file(desc_path, process_desc)

# 5. Update Lesson Files (H1)
lesson_changes = 0
for filename in os.listdir(base_lessons):
    if not filename.endswith('.md'): continue
    match = re.match(r'^(\d+\.\d+)\.md$', filename)
    if not match: continue
    lid = match.group(1)
    
    parts = lid.split('.')
    if parts[1] in ('4', '5'): continue # skip reviews and exams
    if lid not in canonical: continue
    
    filepath = os.path.join(base_lessons, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('# ') and not line.startswith('## '):
            old_title = line[2:].strip()
            if old_title != canonical[lid]:
                lines[i] = f"# {canonical[lid]}"
                with open(filepath, "w", encoding="utf-8") as f_out:
                    f_out.write('\n'.join(lines))
                lesson_changes += 1
            break

print(f"Updated {lesson_changes} lesson files.")
