#!/usr/bin/env python3
import json
import os
import re

BASE_DIR = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto Bibline Academy/Belas Artes - Fase da Gramática/1 Fase - Gramática/1º Ano/Estrutura Curricular - 1º ANO"
MACRO_FILE = os.path.join(BASE_DIR, "1 - Curriculo Macro - 1º ANO.md")
TARGET_FILE = os.path.join(BASE_DIR, "6 - Descrições para tickets - 1º ANO.md")
OBJ_FILE = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto Bibline Academy/editorial-squad/scripts/year1_objectives.json"

with open(OBJ_FILE, "r", encoding="utf-8") as f:
    objectives_map = json.load(f)

# Parse Macro File
with open(MACRO_FILE, "r", encoding="utf-8") as f:
    content = f.read()

weeks = {}

# Example: ## 1ª Semana: **A Essência da Arte**
week_match_pattern = re.compile(r"## (\d+)ª Semana:\s*\*\*(.*?)\*\*")
# Also match Revision/Provas like: ## 9ª Semana: Revisão
special_week_pattern = re.compile(r"## (\d+)ª Semana:\s*(Revisão|Provas?)")

lines = content.split('\n')
current_week = None

for line in lines:
    line = line.strip()
    w_match = week_match_pattern.match(line)
    if w_match:
        current_week = int(w_match.group(1))
        weeks[current_week] = (w_match.group(2).strip(), [])
        continue
    
    s_match = special_week_pattern.match(line)
    if s_match:
        current_week = None # don't parse lessons for review/exam weeks
        continue
        
    if current_week and line.startswith('- '):
        # - 1.1 A essência da arte
        lesson = line[2:].strip()
        weeks[current_week][1].append(lesson)

default_objectives = [
    "Aprecie a arte com um olhar curioso e observador das belezas criadas por Deus.",
    "Experimente ativamente os elementos visuais propostos com dedicação.",
    "Reconheça habilidades motoras e o progresso em suas obras."
]

output = []
output.append("# Descrições para tickets – Belas Artes – 1º Ano\n")
output.append("> Arquivo de referência para copiar e colar a descrição de cada aula nos issues do GitHub.\n")
output.append("---\n")

def get_bimestral_info(week_num):
    if week_num <= 10: return 1, "1º Bimestre", list(range(1, 9))
    if week_num <= 20: return 2, "2º Bimestre", list(range(11, 19))
    if week_num <= 30: return 3, "3º Bimestre", list(range(21, 29))
    return 4, "4º Bimestre", list(range(31, 39))

for week_idx in range(1, 41):
    if week_idx in [9, 10, 19, 20, 29, 30, 39, 40]:
        bim_idx, bim_name, bim_weeks = get_bimestral_info(week_idx)
        is_exam = (week_idx % 10 == 0)
        
        type_prefix = "Prova" if is_exam else "Revisão"
        title_suffix = f"{type_prefix} do {bim_name}"
        
        output.append(f"## Semana {week_idx} – {title_suffix}\n")
        output.append("---\n")
        output.append(f"[Belas artes] - Ano 1 - Semana {week_idx} - {title_suffix}\n")
        output.append("# Description\n")
        output.append(f"# {title_suffix}\n")
        
        for p_week in bim_weeks:
            if p_week in weeks:
                ptheme, plessons = weeks[p_week]
                output.append(f"## {p_week}ª Semana: **{ptheme}**\n")
                for pl in plessons:
                    output.append(f"- {pl}")
                output.append("")
        
        output.append("---\n")
        continue

    if week_idx not in weeks:
        print(f"Warning: Week {week_idx} missing from parsed curriculum.")
        continue

    theme, lessons = weeks[week_idx]
    output.append(f"## Semana {week_idx} – {theme}\n")
    output.append("---\n")
    
    for lesson in lessons:
        lesson_id = lesson.split(" ")[0] # '1.1'
        objs = objectives_map.get(lesson_id, default_objectives)
        
        output.append(f"[Belas artes] - Ano 1 - {lesson}\n")
        output.append("# Description\n")
        output.append("## Objetivos")
        for obj in objs:
            output.append(f"   → {obj}")
        output.append("\n---\n")
        
    output.append(f"[Belas artes] - Ano 1 - {week_idx}.4 Revisão\n")
    output.append("# Description\n")
    output.append(f"Revisar os conhecimentos das aulas da semana {week_idx}\n")
    output.append(f"## {week_idx}ª Semana: **{theme}**\n")
    for lesson in lessons:
        output.append(f"- {lesson}")
    output.append("\n---\n")
    
    output.append(f"[Belas artes] - Ano 1 - {week_idx}.5 Provas\n")
    output.append("# Description\n")
    output.append(f"Avaliar os conhecimentos das aulas da semana {week_idx}\n")
    output.append(f"## {week_idx}ª Semana: **{theme}**\n")
    for lesson in lessons:
        output.append(f"- {lesson}")
    output.append("\n---\n")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(output))

print(f"File generated successfully: {TARGET_FILE}")
print(f"Total lines: {len(output)}")
