#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Extract Prompts — Extrai prompts do arquivo Markdown
"""

import re
from pathlib import Path


def extract_prompts(markdown_file):
    """
    Extrai prompts do arquivo de prompts Narrar
    
    Args:
        markdown_file (str): Caminho para o arquivo Markdown
        
    Returns:
        list: Lista de dicionários com lesson, title, prompt
    """
    
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern para encontrar prompts
    # ### Aula X.Y — Título
    # **Prompt:**
    # ```
    # [conteúdo]
    # ```
    pattern = r'### Aula (\d+\.\d+) — (.+?)\n\n\*\*Prompt:\*\*\n```\n(.+?)```'
    
    matches = re.findall(pattern, content, re.DOTALL)
    
    prompts = []
    for lesson_num, title, prompt in matches:
        prompts.append({
            'lesson': lesson_num.strip(),
            'title': title.strip(),
            'prompt': prompt.strip()
        })
    
    return prompts


def extract_prompts_by_week(markdown_file, week):
    """
    Extrai prompts de uma semana específica
    
    Args:
        markdown_file (str): Caminho para o arquivo Markdown
        week (int): Número da semana
        
    Returns:
        list: Lista de prompts da semana
    """
    
    all_prompts = extract_prompts(markdown_file)
    
    # Filtrar por semana
    week_prompts = []
    for prompt in all_prompts:
        lesson_week = int(prompt['lesson'].split('.')[0])
        if lesson_week == week:
            week_prompts.append(prompt)
    
    return week_prompts


def save_prompts(prompts, output_dir):
    """
    Salva prompts em arquivos separados
    
    Args:
        prompts (list): Lista de prompts
        output_dir (str): Diretório de saída
    """
    
    from pathlib import Path
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    for prompt_data in prompts:
        lesson = prompt_data['lesson']
        prompt = prompt_data['prompt']
        
        # Salvar prompt
        prompt_file = output_path / f"{lesson}_narrar_prompt.txt"
        with open(prompt_file, 'w', encoding='utf-8') as f:
            f.write(prompt)


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Uso: python extract_prompts.py <arquivo.md> [output_dir]")
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "prompts/"
    
    prompts = extract_prompts(markdown_file)
    
    print(f"✅ {len(prompts)} prompts extraídos")
    
    save_prompts(prompts, output_dir)
    print(f"📁 Prompts salvos em {output_dir}")
