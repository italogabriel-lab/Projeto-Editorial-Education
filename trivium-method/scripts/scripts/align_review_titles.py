#!/usr/bin/env python3
"""SCRIPT MODULAR: Alinha apenas os títulos das aulas base dentro dos blocos de Revisão do arquivo 6 (Descrições). Uso: Correção isolada de tickets de revisão e prova."""
import re

base = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto Bibline Academy/Belas Artes - Fase da Gramática/1 Fase - Gramática/3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE/Estrutura Curricular - 3º ANO"

macro_path = f"{base}/1 - Curriculo Macro - Arte Cristã Oriental até o Renascimento do Norte - 3º ANO.md"
desc_path = f"{base}/6 - Descrições para tickets - 3º ANO.md"

# 1. Extract canonical titles from file 1
with open(macro_path, "r") as f:
    macro_content = f.read()

canonical_titles = {}
current_week = None
for line in macro_content.split('\n'):
    week_match = re.match(r'## Semana (\d+)', line)
    if week_match:
        current_week = int(week_match.group(1))
    day_match = re.match(r'- Dia (\d): (.+?)(?:\s*✅)?$', line)
    if day_match and current_week:
        day_num = int(day_match.group(1))
        title = day_match.group(2).strip()
        lesson_id = f"{current_week}.{day_num}"
        canonical_titles[lesson_id] = title

# 2. Read file 6
with open(desc_path, "r") as f:
    desc_content = f.read()

# 3. Replace lesson listing lines inside review/exam blocks
# Pattern: "- X.Y Old Title" (inside description blocks)
lines = desc_content.split('\n')
new_lines = []
changes = 0

for line in lines:
    match = re.match(r'^(- )(\d+\.\d+) (.+)$', line)
    if match:
        prefix = match.group(1)
        lesson_id = match.group(2)
        old_title = match.group(3)
        
        if lesson_id in canonical_titles:
            canonical = canonical_titles[lesson_id]
            if old_title != canonical:
                new_lines.append(f"{prefix}{lesson_id} {canonical}")
                changes += 1
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

# 4. Write updated file
new_content = '\n'.join(new_lines)
with open(desc_path, 'w') as f:
    f.write(new_content)

print(f"Updated {changes} lesson listing lines inside review/exam blocks.")
