#!/usr/bin/env python3
"""AUDITORIA: Compara a Matriz-Curricular com o Currículo Macro e relata divergências. Uso: Checagem rápida (read-only) antes de commits e publicações."""
"""Check file 2 (Matriz Curricular) for title discrepancies with file 1."""
import re

base = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto Bibline Academy/Belas Artes - Fase da Gramática/1 Fase - Gramática/3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE/Estrutura Curricular - 3º ANO"

macro_path = f"{base}/1 - Curriculo Macro - Arte Cristã Oriental até o Renascimento do Norte - 3º ANO.md"
matriz_path = f"{base}/2 - Matriz-Curricular-objetivos - 3º ANO.md"

# Extract canonical titles
with open(macro_path, "r") as f:
    macro_content = f.read()

canonical = {}
current_week = None
for line in macro_content.split('\n'):
    week_match = re.match(r'## Semana (\d+)', line)
    if week_match:
        current_week = int(week_match.group(1))
    day_match = re.match(r'- Dia (\d): (.+?)(?:\s*✅)?$', line)
    if day_match and current_week:
        lesson_id = f"{current_week}.{int(day_match.group(1))}"
        canonical[lesson_id] = day_match.group(2).strip()

# Check Matriz file
with open(matriz_path, "r") as f:
    matriz = f.read()

# Find table rows: | X.Y | **Title** |
diffs = []
for line in matriz.split('\n'):
    match = re.match(r'\|\s*(\d+\.\d+)\s*\|\s*\*\*(.+?)\*\*\s*\|', line)
    if match:
        lid = match.group(1)
        title = match.group(2).strip()
        if lid in canonical and title != canonical[lid]:
            diffs.append((lid, title, canonical[lid]))

if diffs:
    print(f"Found {len(diffs)} discrepancies in Matriz Curricular:\n")
    for lid, old, new in diffs:
        print(f"  [{lid}] Matriz: '{old}' → Macro: '{new}'")
else:
    print("✅ All titles in Matriz Curricular match the Curriculo Macro.")
