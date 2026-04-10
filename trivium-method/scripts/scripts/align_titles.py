#!/usr/bin/env python3
"""SCRIPT MODULAR: Alinha apenas os títulos principais no arquivo 6 (Descrições para tickets) com o Currículo Macro. Uso: Sincronização isolada de tickets."""
import re

base = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto Bibline Academy/Belas Artes - Fase da Gramática/1 Fase - Gramática/3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE/Estrutura Curricular - 3º ANO"

macro_path = f"{base}/1 - Curriculo Macro - Arte Cristã Oriental até o Renascimento do Norte - 3º ANO.md"
desc_path = f"{base}/6 - Descrições para tickets - 3º ANO.md"

# 1. Extract canonical titles from file 1 (Curriculo Macro)
with open(macro_path, "r") as f:
    macro_content = f.read()

# Pattern: "- Dia X: Title"
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

print(f"Extracted {len(canonical_titles)} canonical titles from Curriculo Macro:\n")
for lid, title in sorted(canonical_titles.items(), key=lambda x: (int(x[0].split('.')[0]), int(x[0].split('.')[1]))):
    print(f"  {lid}: {title}")

# 2. Read file 6
with open(desc_path, "r") as f:
    desc_content = f.read()

# 3. Find and replace lesson title lines in file 6
# Pattern: [Belas artes] - Ano 3 - X.Y OldTitle
changes = []
lines = desc_content.split('\n')
new_lines = []
for i, line in enumerate(lines):
    match = re.match(r'^(\[Belas artes\] - Ano 3 - )(\d+\.\d+) (.+)$', line)
    if match:
        prefix = match.group(1)
        lesson_id = match.group(2)
        old_title = match.group(3)
        
        # Skip review and exam titles
        if 'Revisão' in old_title or 'Provas' in old_title or 'Prova' in old_title:
            new_lines.append(line)
            continue
        
        # Only update lesson titles (x.1, x.2, x.3)
        parts = lesson_id.split('.')
        if len(parts) == 2 and parts[1] in ('1', '2', '3'):
            if lesson_id in canonical_titles:
                canonical = canonical_titles[lesson_id]
                if old_title != canonical:
                    new_line = f"{prefix}{lesson_id} {canonical}"
                    changes.append((i+1, lesson_id, old_title, canonical))
                    new_lines.append(new_line)
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

# 4. Print changes
print(f"\n\n{'='*80}")
print(f"CHANGES TO APPLY ({len(changes)} total):")
print(f"{'='*80}\n")

for line_num, lid, old, new in changes:
    print(f"L{line_num} [{lid}]:")
    print(f"  OLD: {old}")
    print(f"  NEW: {new}")
    print()

# 5. Write updated file
new_content = '\n'.join(new_lines)
with open(desc_path, 'w') as f:
    f.write(new_content)

print(f"\nFile updated successfully. {len(changes)} titles changed.")
