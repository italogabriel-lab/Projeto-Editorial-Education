#!/usr/bin/env python3
"""LIMPEZA: Remove sufixos indesejados e formatações estranhas geradas em aulas de Revisão e Prova. Uso: Limpeza cosmética de documentos (Regex)."""
"""Fix title formats in the descriptions file."""
import re

filepath = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto Bibline Academy/Belas Artes - Fase da Gramática/1 Fase - Gramática/3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE/Estrutura Curricular - 3º ANO/6 - Descrições para tickets - 3º ANO.md"

with open(filepath, "r") as f:
    content = f.read()

# 1. Fix weekly review titles: remove " – Theme" suffix from x.4 Revisão lines
# Pattern: [Belas artes] - Ano 3 - X.4 Revisão – Whatever
content = re.sub(
    r'\[Belas artes\] - Ano 3 - (\d+\.\d+) Revisão – [^\n]+',
    r'[Belas artes] - Ano 3 - \1 Revisão',
    content
)

# 2. Fix weekly exam titles: remove " – Theme" suffix from x.5 Provas lines
# Pattern: [Belas artes] - Ano 3 - X.5 Provas – Whatever
content = re.sub(
    r'\[Belas artes\] - Ano 3 - (\d+\.\d+) Provas – [^\n]+',
    r'[Belas artes] - Ano 3 - \1 Provas',
    content
)

# 3. Fix bimestral review titles: [Belas artes] - Ano 3 - Semana X - Revisão do Módulo Y
# Should become: [Belas artes] - Ano 3 - X Revisão
content = re.sub(
    r'\[Belas artes\] - Ano 3 - Semana (\d+) - Revisão do Módulo \d+',
    r'[Belas artes] - Ano 3 - \1 Revisão',
    content
)

# 4. Fix bimestral exam titles: [Belas artes] - Ano 3 - Semana X - Prova do Módulo Y
# Should become: [Belas artes] - Ano 3 - X Prova
content = re.sub(
    r'\[Belas artes\] - Ano 3 - Semana (\d+) - Prova do Módulo \d+',
    r'[Belas artes] - Ano 3 - \1 Prova',
    content
)

# 5. Fix final review/exam titles
content = re.sub(
    r'\[Belas artes\] - Ano 3 - Semana (\d+) - Revisão Final',
    r'[Belas artes] - Ano 3 - \1 Revisão',
    content
)
content = re.sub(
    r'\[Belas artes\] - Ano 3 - Semana (\d+) - Prova Final',
    r'[Belas artes] - Ano 3 - \1 Prova',
    content
)

with open(filepath, "w") as f:
    f.write(content)

# Verify by printing all title lines
lines = content.split('\n')
print("=== All ticket title lines (reviews, exams, and bimestral) ===\n")
for i, line in enumerate(lines, 1):
    if line.startswith('[Belas artes]') and ('Revisão' in line or 'Provas' in line or 'Prova' in line):
        print(f"L{i}: {line}")
