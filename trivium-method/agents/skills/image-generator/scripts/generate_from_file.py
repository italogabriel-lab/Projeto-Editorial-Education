#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Generate from File — Gera imagens extraindo prompts do arquivo real

Uso:
    python generate_from_file.py --year 3 --week 1 --ratio 2:1
"""

import os
import sys
import re
import argparse
from pathlib import Path
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Adicionar path atual
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from generate_images import generate_image


# RATIO PRESETS
RATIO_PRESETS = {
    '1:1': (1024, 1024),      # Quadrado
    '2:1': (2048, 1024),      # Panorâmico (PADRÃO)
    '3:2': (1536, 1024),      # Clássico
    '4:3': (1365, 1024),      # Standard
    '16:9': (1820, 1024),     # Widescreen
}


def parse_ratio(ratio_str):
    """
    Parse ratio string (e.g., '2:1') and return (width, height)
    
    Args:
        ratio_str (str): Ratio in format 'W:H'
        
    Returns:
        tuple: (width, height)
    """
    if ratio_str in RATIO_PRESETS:
        return RATIO_PRESETS[ratio_str]
    
    # Parse custom ratio
    try:
        parts = ratio_str.split(':')
        if len(parts) != 2:
            raise ValueError
        
        w_ratio = int(parts[0])
        h_ratio = int(parts[1])
        
        # Calculate dimensions (base height: 1024)
        height = 1024
        width = int((w_ratio / h_ratio) * height)
        
        # Round to multiple of 64 (better for AI models)
        width = (width // 64) * 64
        
        return (width, height)
    
    except:
        print(f"⚠️  Ratio '{ratio_str}' inválido, usando 2:1")
        return RATIO_PRESETS['2:1']


def extract_prompts_from_file(markdown_file, year=None, week=None):
    """
    Extract prompts from the actual prompts file
    
    Args:
        markdown_file (str): Path to markdown file
        year (int, optional): Filter by year
        week (int, optional): Filter by week
        
    Returns:
        list: List of dicts with lesson, title, prompt, week
    """
    
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern para encontrar prompts (formato real do arquivo)
    # ### Aula X.Y — Título
    # **Prompt:**
    # ```
    # [conteúdo]
    # ```
    pattern = r'### Aula (\d+\.\d+) — (.+?)\n+\*\*Prompt:\*\*\n+```\n+(.+?)\n+```'
    
    matches = re.findall(pattern, content, re.DOTALL)
    
    # Se não encontrou, tentar pattern alternativo
    if not matches:
        print("⚠️  Pattern principal não encontrou prompts, tentando alternativo...")
        # Pattern alternativo mais flexível
        pattern = r'### Aula (\d+\.\d+) — ([^\n]+)\n+.*?\*\*Prompt:\*\*.*?\n+```\n+(.+?)\n+```'
        matches = re.findall(pattern, content, re.DOTALL)
    
    prompts = []
    for lesson_num, title, prompt in matches:
        # Extrair semana do número da aula
        week_num = int(lesson_num.split('.')[0])
        
        # Filtrar por semana se especificado
        if week and week_num != week:
            continue
        
        # Filtrar por ano se especificado
        if year and week_num > (year * 40):  # Aproximação
            continue
        
        prompts.append({
            'lesson': lesson_num.strip(),
            'title': title.strip(),
            'prompt': prompt.strip(),
            'week': week_num
        })
    
    return prompts


def generate_from_file(prompts_file, output_dir, year=3, week=None, ratio='2:1'):
    """
    Generate images from prompts file
    
    Args:
        prompts_file (str): Path to prompts markdown file
        output_dir (str): Output directory
        year (int): Year to generate
        week (int, optional): Specific week
        ratio (str): Aspect ratio (default: 2:1)
    """
    
    print("\n" + "="*70)
    print("🎨 GERANDO IMAGENS A PARTIR DO ARQUIVO DE PROMPTS")
    print("="*70)
    
    # Parse ratio
    width, height = parse_ratio(ratio)
    
    print(f"\n📐 Ratio: {ratio} ({width}x{height})")
    print(f" Prompts: {prompts_file}")
    
    # Extrair prompts
    print(f"\n📋 Extraindo prompts...")
    prompts = extract_prompts_from_file(prompts_file, year=year, week=week)
    
    if not prompts:
        print("❌ Nenhum prompt encontrado!")
        return False
    
    total = len(prompts)
    print(f"✅ {total} prompts encontrados")
    
    # Criar diretório de saída
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    print(f"\n🔄 Gerando {total} imagens...")
    print(f" Saída: {output_path}")
    print(f"🎨 Plataforma: Pollinations.ai (Flux)")
    print()
    
    success = 0
    failed = 0
    current_week = None
    
    for prompt_data in prompts:
        lesson_num = prompt_data['lesson']
        title = prompt_data['title']
        prompt = prompt_data['prompt']
        week_num = prompt_data['week']
        
        # Criar pasta da semana se mudou
        if week_num != current_week:
            current_week = week_num
            week_dir = output_path / f"semana-{week_num}"
            week_dir.mkdir(exist_ok=True)
            print(f"\n✅ Semana {week_num}")
        
        # Arquivos de saída
        image_file = week_dir / f"{lesson_num}_narrar.png"
        prompt_file = week_dir / f"{lesson_num}_narrar_prompt.txt"
        
        # Seed baseada no número da aula
        seed = int(lesson_num.replace('.', ''))
        
        # Verificar se já existe
        if image_file.exists():
            print(f"   ⏭️  {lesson_num} — {title[:40]}... (já existe)")
            success += 1
            continue
        
        # Gerar imagem
        print(f"   🔄 {lesson_num} — {title[:40]}...")
        
        result = generate_image(
            prompt=prompt,
            output_path=str(image_file),
            platform='pollinations',
            width=width,
            height=height,
            seed=seed
        )
        
        if result['success']:
            # Salvar prompt
            with open(prompt_file, 'w', encoding='utf-8') as f:
                f.write(prompt)
            
            file_size = image_file.stat().st_size / 1024
            print(f"   ✅ {lesson_num}_narrar.png ({file_size:.1f} KB)")
            success += 1
        else:
            print(f"   ❌ {lesson_num} — {title[:40]}... (falha: {result['error']})")
            failed += 1
    
    # Estatísticas finais
    print("\n" + "="*70)
    print("📊 ESTATÍSTICAS")
    print("="*70)
    print(f"Total: {total}")
    print(f"✅ Sucesso: {success} ({success/total*100:.1f}%)")
    print(f"❌ Falhas: {failed} ({failed/total*100:.1f}%)")
    print(f"📁 Saída: {output_path}")
    print(f"📐 Ratio: {ratio} ({width}x{height})")
    print("="*70)
    
    if success == total:
        print("\n✅ GERAÇÃO CONCLUÍDA COM SUCESSO!")
    else:
        print(f"\n⚠️  {failed} imagem(s) falharam")
    
    print("\n🖼️  Para ver as imagens:")
    print(f"   ls -lh {output_path}/semana-*/")
    print("="*70 + "\n")
    
    return success == total


def main():
    parser = argparse.ArgumentParser(
        description='🎨 Generate images from prompts file'
    )
    
    parser.add_argument(
        '--year',
        type=int,
        default=3,
        help='Ano escolar (default: 3)'
    )
    
    parser.add_argument(
        '--week',
        type=int,
        default=None,
        help='Semana específica (default: todas)'
    )
    
    parser.add_argument(
        '--ratio',
        type=str,
        default='2:1',
        help='Aspect ratio (default: 2:1). Options: 1:1, 2:1, 3:2, 4:3, 16:9'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default='generated_images',
        help='Diretório de saída (default: generated_images)'
    )
    
    parser.add_argument(
        '--prompts-file',
        type=str,
        default=None,
        help='Arquivo de prompts (default: auto-detect)'
    )
    
    args = parser.parse_args()
    
    # Encontrar arquivo de prompts automaticamente
    if not args.prompts_file:
        prompts_files = list(Path('../../').rglob('*Prompts-para-imagens-narrar-3-ano*.md'))
        if prompts_files:
            args.prompts_file = str(prompts_files[0])
        else:
            print("❌ Arquivo de prompts não encontrado!")
            print("\nUse --prompts-file para especificar o arquivo:")
            print("   python generate_from_file.py --prompts-file /caminho/arquivo.md")
            sys.exit(1)
    
    # Gerar imagens
    success = generate_from_file(
        prompts_file=args.prompts_file,
        output_dir=args.output,
        year=args.year,
        week=args.week,
        ratio=args.ratio
    )
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
