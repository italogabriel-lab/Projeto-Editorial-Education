#!/usr/bin/env python3
"""SCRIPT MODULAR: Arruma o título principal (H1) dentro de cada arquivo individual de aula (.md) puxando do Macro. Uso: Quando títulos internos de arquivos estão desatualizados."""
import re
import os

base_lessons = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto Bibline Academy/Belas Artes - Fase da Gramática/1 Fase - Gramática/3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE"
macro_path = f"{base_lessons}/Estrutura Curricular - 3º ANO/1 - Curriculo Macro - Arte Cristã Oriental até o Renascimento do Norte - 3º ANO.md"

# 1. Extract canonical titles from Curriculo Macro
with open(macro_path, 'r') as f:
    macro_content = f.read()

canonical = {}
current_week = None
for line in macro_content.split('\n'):
    week_match = re.match(r'## Semana (\d+)', line)
    if week_match:
        current_week = int(week_match.group(1))
    day_match = re.match(r'- Dia (\d): (.+?)(?:\s*✅)?$', line)
    if day_match and current_week:
        lid = f"{current_week}.{int(day_match.group(1))}"
        canonical[lid] = day_match.group(2).strip()

print(f"Loaded {len(canonical)} canonical titles from Curriculo Macro\n")

# 2. Scan all lesson files and compare H1 titles
changes = []
already_correct = []
no_h1 = []
skipped = []

for filename in sorted(os.listdir(base_lessons)):
    if not filename.endswith('.md'):
        continue
    
    # Parse lesson ID from filename (e.g., "8.1.md" -> "8.1")
    match = re.match(r'^(\d+\.\d+)\.md$', filename)
    if not match:
        continue
    
    lid = match.group(1)
    filepath = os.path.join(base_lessons, filename)
    
    # Skip review (x.4) and exam (x.5) files - they have their own titles
    parts = lid.split('.')
    if parts[1] in ('4', '5'):
        skipped.append(lid)
        continue
    
    if lid not in canonical:
        skipped.append(lid)
        continue
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Find the H1 title (first line starting with "# ")
    lines = content.split('\n')
    h1_line_idx = None
    h1_title = None
    
    for i, line in enumerate(lines):
        if line.startswith('# ') and not line.startswith('## '):
            h1_line_idx = i
            h1_title = line[2:].strip()
            break
    
    if h1_title is None:
        no_h1.append(lid)
        continue
    
    expected = canonical[lid]
    
    if h1_title == expected:
        already_correct.append(lid)
    else:
        # Fix the title
        lines[h1_line_idx] = f"# {expected}"
        new_content = '\n'.join(lines)
        with open(filepath, 'w') as f:
            f.write(new_content)
        changes.append((lid, h1_title, expected))

# 3. Report
print("=" * 70)
print("AUDIT RESULTS")
print("=" * 70)

print(f"\n✅ Already correct: {len(already_correct)} files")
if already_correct:
    print(f"   {', '.join(already_correct)}")

print(f"\n🔄 Fixed: {len(changes)} files")
for lid, old, new in changes:
    print(f"   [{lid}] '{old}' → '{new}'")

print(f"\n⏭️ Skipped (reviews/exams): {len(skipped)} files")

if no_h1:
    print(f"\n⚠️ No H1 found: {len(no_h1)} files")
    for lid in no_h1:
        print(f"   {lid}")

print(f"\n📊 Total: {len(changes)} titles corrected")
