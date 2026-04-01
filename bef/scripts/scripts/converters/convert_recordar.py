#!/usr/bin/env python3
"""
Bulk convert Recordar sections from music to rhyme format in 3rd year lesson files.
Generates contextual rhymes based on each lesson's definition.
"""
import os
import re
import sys

BASE = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education"
PROJECT = os.path.join(BASE, "Projeto Bibline Academy")
YEAR_DIR = os.path.join(
    PROJECT,
    "Belas Artes - Fase da Gramática",
    "1 Fase - Gramática",
    "3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE"
)

def get_lesson_files():
    files = []
    for f in os.listdir(YEAR_DIR):
        if re.match(r'^\d+\.[123]\.md$', f):
            files.append(f)
    files.sort(key=lambda x: (int(x.split('.')[0]), int(x.split('.')[1])))
    return files

def extract_info(content):
    title_m = re.search(r'^# (.+)$', content, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else ""

    defn_m = re.search(r'\[MP3\\\]\s*\n\s*\n(.+?)\s*\n\s*\n\[-STATEMENT_D\]', content, re.DOTALL)
    defn = defn_m.group(1).strip() if defn_m else ""

    term_m = re.search(r'O que (?:é|são) (.+?)\?', content)
    term = term_m.group(1).strip() if term_m else ""

    return title, defn, term

def make_rhyme_block(title, defn, term):
    defn_clean = defn.rstrip('.')
    topic = term.lower() if term else 'o tema da aula'

    v1 = f"{defn_clean}, vamos entender e guardar."
    v2 = "Na história da arte esse saber vai brilhar."
    v3 = "Aprenda com atenção, repita sem parar,"
    v4 = "que a arte nos ensina a observar e pensar."

    return f"""[+HEADING]

Hora de memorizar com rima

[-HEADING]

[+PARAGRAPH]

Clique abaixo para ouvir a rima e reforçar o aprendizado sobre {topic}.

[-PARAGRAPH]

[+STATEMENT_A]

[MP3/]

#11L:9pDzHy2OpOgeXM8SeL0t

*{title}*

{v1}

{v2}

{v3}

{v4}

[MP3\\]

*{title}*

{v1}

{v2}

{v3}

{v4}

[-STATEMENT_A]"""

def convert_file(filepath, dry_run=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if "Hora de memorizar com rima" in content:
        return "ALREADY_DONE"

    if "Hora de memorizar com música" not in content:
        return "NO_MUSIC"

    title, defn, term = extract_info(content)
    if not defn:
        return "NO_DEFINITION"

    old_pattern = re.compile(
        r'\[\+HEADING\]\s*\n\s*\n'
        r'Hora de memorizar com música\s*\n\s*\n'
        r'\[-HEADING\]\s*\n\s*\n'
        r'\[\+IMAGE_TEXT_ON\]\s*\n\s*\n'
        r'@link_png@\s*\n\s*\n'
        r'@link_mp3@\s*\n\s*\n'
        r'.+?\s*\n\s*\n'
        r'\[-IMAGE_TEXT_ON\]',
        re.DOTALL
    )

    match = old_pattern.search(content)
    if not match:
        return "PATTERN_MISMATCH"

    new_block = make_rhyme_block(title, defn, term)
    new_content = content[:match.start()] + new_block + content[match.end():]

    if not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return "CONVERTED"

def main():
    dry_run = '--dry-run' in sys.argv

    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}")
    print(f"Directory: {YEAR_DIR}")
    print()

    files = get_lesson_files()
    print(f"Found {len(files)} lesson files\n")

    stats = {"CONVERTED": 0, "ALREADY_DONE": 0, "NO_MUSIC": 0, "NO_DEFINITION": 0, "PATTERN_MISMATCH": 0}

    for fname in files:
        filepath = os.path.join(YEAR_DIR, fname)
        result = convert_file(filepath, dry_run)
        stats[result] += 1
        icon = {"CONVERTED": "✅", "ALREADY_DONE": "⏭️", "NO_MUSIC": "⚠️", "NO_DEFINITION": "❌", "PATTERN_MISMATCH": "❓"}
        print(f"  {icon.get(result, '?')} {fname}: {result}")

    print(f"\n--- RESULTS ---")
    for k, v in stats.items():
        if v > 0:
            print(f"  {k}: {v}")
    print(f"  TOTAL: {len(files)}")

if __name__ == "__main__":
    main()
