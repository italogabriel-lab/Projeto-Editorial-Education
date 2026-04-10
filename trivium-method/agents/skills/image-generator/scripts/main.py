#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Image Generator — Main Script
Gera imagens a partir de prompts do hábito Narrar
"""

import os
import sys
import requests
import argparse
from urllib.parse import quote
from pathlib import Path
from tqdm import tqdm

# Adicionar path do projeto
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from extract_prompts import extract_prompts
from generate_images import generate_image, optimize_prompt
from organize_images import organize_structure
from generate_log import generate_log


def main():
    parser = argparse.ArgumentParser(
        description='🎨 Image Generator — Gera imagens para o hábito Narrar'
    )
    
    parser.add_argument(
        'command',
        choices=['generate', 'generate-week', 'regenerate', 'status', 'organize'],
        help='Comando a executar'
    )
    
    parser.add_argument(
        'year',
        type=int,
        help='Ano escolar (1-5)'
    )
    
    parser.add_argument(
        '--week',
        type=int,
        help='Semana específica (para generate-week)'
    )
    
    parser.add_argument(
        '--lesson',
        type=str,
        help='Aula específica (para regenerate)'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default=None,
        help='Diretório de saída'
    )
    
    parser.add_argument(
        '--platform',
        type=str,
        default='pollinations',
        choices=['pollinations', 'huggingface', 'deepai'],
        help='Plataforma de geração'
    )
    
    parser.add_argument(
        '--width',
        type=int,
        default=1024,
        help='Largura da imagem'
    )
    
    parser.add_argument(
        '--height',
        type=int,
        default=1024,
        help='Altura da imagem'
    )
    
    parser.add_argument(
        '--seed',
        type=int,
        default=None,
        help='Seed para geração'
    )
    
    args = parser.parse_args()
    
    # Diretório padrão de saída
    if not args.output:
        args.output = f"generated/imagens-narrar/{args.year}-ano/"
    
    # Executar comando
    if args.command == 'generate':
        generate_all(args)
    elif args.command == 'generate-week':
        generate_week(args)
    elif args.command == 'regenerate':
        regenerate_lesson(args)
    elif args.command == 'status':
        show_status(args)
    elif args.command == 'organize':
        organize_images(args)


def generate_all(args):
    """Gera todas as imagens de um ano"""
    print(f"\n🎨 Image Generator — Ano {args.year}")
    print("=" * 50)
    
    # Encontrar arquivo de prompts
    prompts_file = find_prompts_file(args.year)
    if not prompts_file:
        print(f"❌ Arquivo de prompts não encontrado para ano {args.year}")
        return
    
    print(f"📄 Prompts: {prompts_file}")
    
    # Extrair prompts
    print("\n📋 Extraindo prompts...")
    prompts = extract_prompts(prompts_file)
    total = len(prompts)
    print(f"✅ {total} prompts encontrados")
    
    # Criar diretório de saída
    os.makedirs(args.output, exist_ok=True)
    
    # Gerar imagens
    print(f"\n🔄 Gerando {total} imagens...")
    print(f" Saída: {args.output}")
    print(f"🎨 Plataforma: {args.platform}")
    print(f"📐 Tamanho: {args.width}x{args.height}")
    print()
    
    success = 0
    failed = 0
    current_week = None
    
    for prompt_data in tqdm(prompts, desc="Gerando"):
        lesson_num = prompt_data['lesson']
        title = prompt_data['title']
        prompt = prompt_data['prompt']
        
        # Extrair semana do número da aula
        week = int(lesson_num.split('.')[0])
        
        # Criar pasta da semana se mudou
        if week != current_week:
            current_week = week
            week_dir = f"{args.output}/semana-{week}/"
            os.makedirs(week_dir, exist_ok=True)
            print(f"\n✅ Semana {week}")
        
        # Gerar imagem
        output_file = f"{args.output}/semana-{week}/{lesson_num}_narrar.png"
        prompt_file = f"{args.output}/semana-{week}/{lesson_num}_narrar_prompt.txt"
        
        # Verificar se já existe
        if os.path.exists(output_file):
            print(f"   ⏭️  {lesson_num} — {title[:40]}... (já existe)")
            success += 1
            continue
        
        # Gerar
        seed = args.seed if args.seed else int(lesson_num.replace('.', ''))
        
        try:
            result = generate_image(
                prompt=prompt,
                output_path=output_file,
                platform=args.platform,
                width=args.width,
                height=args.height,
                seed=seed
            )
            
            if result['success']:
                # Salvar prompt
                with open(prompt_file, 'w', encoding='utf-8') as f:
                    f.write(prompt)
                
                print(f"   ✅ {lesson_num} — {title[:40]}...")
                success += 1
            else:
                print(f"   ❌ {lesson_num} — {title[:40]}... (falha: {result['error']})")
                failed += 1
                
        except Exception as e:
            print(f"   ❌ {lesson_num} — {title[:40]}... (erro: {str(e)})")
            failed += 1
    
    # Gerar log
    print("\n📝 Gerando log...")
    generate_log(args.year, args.output)
    
    # Estatísticas finais
    print("\n" + "=" * 50)
    print("📊 ESTATÍSTICAS")
    print("=" * 50)
    print(f"Total: {total}")
    print(f"✅ Sucesso: {success} ({success/total*100:.1f}%)")
    print(f"❌ Falhas: {failed} ({failed/total*100:.1f}%)")
    print(f"📁 Saída: {args.output}")
    print("=" * 50)
    print("\n✅ Geração concluída!")


def generate_week(args):
    """Gera imagens de uma semana específica"""
    print(f"\n🎨 Image Generator — Ano {args.year}, Semana {args.week}")
    print("=" * 50)
    
    # Implementação similar a generate_all, mas filtrando por semana
    # ...


def regenerate_lesson(args):
    """Regenera imagem específica"""
    print(f"\n🎨 Regenerando aula {args.lesson} — Ano {args.year}")
    print("=" * 50)
    
    # Implementação
    # ...


def show_status(args):
    """Mostra status de geração"""
    print(f"\n📊 Status — Ano {args.year}")
    print("=" * 50)
    
    output_dir = f"generated/imagens-narrar/{args.year}-ano/"
    
    if not os.path.exists(output_dir):
        print("❌ Nenhuma imagem gerada ainda")
        return
    
    # Contar imagens
    total_images = 0
    total_weeks = 0
    
    for week_dir in sorted(os.listdir(output_dir)):
        if week_dir.startswith('semana-'):
            total_weeks += 1
            week_path = f"{output_dir}/{week_dir}/"
            
            images = [f for f in os.listdir(week_path) if f.endswith('_narrar.png')]
            total_images += len(images)
            
            print(f"✅ {week_dir}: {len(images)} imagens")
    
    print("\n" + "=" * 50)
    print(f"Total: {total_images} imagens em {total_weeks} semanas")
    print("=" * 50)


def organize_images(args):
    """Organiza imagens existentes"""
    print(f"\n📁 Organizando imagens de {args.output}")
    print("=" * 50)
    
    organize_structure(args.output)
    
    print("\n✅ Organização concluída!")


def find_prompts_file(year):
    """Encontra arquivo de prompts para o ano"""
    # Procurar em vários locais possíveis
    search_paths = [
        f"Projeto Bibline Academy/Belas Artes - Fase da Gramática/1 Fase - Gramática/{year}º Ano - */Estrutura Curricular - {year}º ANO/5 - Prompts-para-imagens-narrar-{year}-ano*.md",
        f"Projeto Bibline Academy/Belas Artes - Fase da Gramática/1 Fase - Gramática/{year}º Ano - */5 - Prompts*.md",
    ]
    
    from glob import glob
    
    for pattern in search_paths:
        matches = glob(pattern, recursive=True)
        if matches:
            return matches[0]
    
    return None


if __name__ == '__main__':
    main()
