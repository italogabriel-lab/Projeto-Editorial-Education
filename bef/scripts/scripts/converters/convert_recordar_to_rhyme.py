#!/usr/bin/env python3
"""
Bulk convert Recordar sections from music to rhyme format in 3rd year lesson files.
"""
import os
import re
import glob

BASE_DIR = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto Bibline Academy/Belas Artes - Fase da Gramática/1 Fase - Gramática/3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE"

def get_lesson_files():
    """Get all .1, .2, .3 lesson files (skip .4 review and .5 exam files)."""
    files = []
    for f in glob.glob(os.path.join(BASE_DIR, "*.md")):
        basename = os.path.basename(f)
        if re.match(r'^\d+\.[123]\.md$', basename):
            files.append(f)
    files.sort(key=lambda x: (int(os.path.basename(x).split('.')[0]), int(os.path.basename(x).split('.')[1])))
    return files

def extract_info(filepath):
    """Extract definition and music content from a lesson file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "sem título"
    
    # Extract STATEMENT_D definition
    stmt_match = re.search(
        r'\[MP3\\\]\s*\n\s*\n(.+?)\s*\n\s*\n\[-STATEMENT_D\]',
        content, re.DOTALL
    )
    definition = stmt_match.group(1).strip() if stmt_match else None
    
    # Extract music text
    music_match = re.search(
        r'\[\+IMAGE_TEXT_ON\]\s*\n\s*\n@link_png@\s*\n\s*\n@link_mp3@\s*\n\s*\n(.+?)\s*\n\s*\n\[-IMAGE_TEXT_ON\]',
        content, re.DOTALL
    )
    music_content = music_match.group(1).strip() if music_match else None
    
    has_music = "Hora de memorizar com música" in content
    
    return {
        'title': title,
        'definition': definition,
        'music_content': music_content,
        'has_music': has_music,
        'filepath': filepath,
        'basename': os.path.basename(filepath),
    }

def main():
    files = get_lesson_files()
    print(f"Found {len(files)} lesson files")
    
    results = []
    for f in files:
        info = extract_info(f)
        results.append(info)
        status = "HAS_MUSIC" if info['has_music'] else "NO_MUSIC"
        defn = info['definition'][:60] if info['definition'] else 'NONE'
        print(f"  {info['basename']}: {status} | Def: {defn}...")
    
    with_music = [r for r in results if r['has_music']]
    without_music = [r for r in results if not r['has_music']]
    
    print(f"\nFiles with music: {len(with_music)}")
    print(f"Files without music: {len(without_music)}")
    if without_music:
        for r in without_music:
            print(f"  SKIP: {r['basename']}")

if __name__ == "__main__":
    main()
