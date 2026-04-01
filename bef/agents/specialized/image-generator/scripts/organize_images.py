#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Organize Images — Organiza imagens na hierarquia correta
"""

import os
import shutil
import re
from pathlib import Path


def get_week_from_lesson(lesson_num):
    """
    Extrai semana do número da aula
    
    Args:
        lesson_num (str): Número da aula (ex: "1.1")
        
    Returns:
        int: Número da semana
    """
    return int(lesson_num.split('.')[0])


def organize_structure(images_dir):
    """
    Organiza imagens na hierarquia correta
    
    Args:
        images_dir (str): Diretório com imagens
    """
    
    images_path = Path(images_dir)
    
    # Listar todas as imagens
    image_files = list(images_path.glob('*_narrar.png'))
    
    print(f"📁 {len(image_files)} imagens encontradas")
    
    # Organizar por semana
    for image_file in image_files:
        # Extrair número da aula
        filename = image_file.name
        lesson_num = filename.split('_')[0]  # Ex: "1.1"
        
        # Extrair semana
        week = get_week_from_lesson(lesson_num)
        
        # Criar pasta da semana
        week_dir = images_path / f"semana-{week}"
        week_dir.mkdir(exist_ok=True)
        
        # Mover arquivo
        dest = week_dir / filename
        shutil.move(str(image_file), str(dest))
        
        # Mover prompt também se existir
        prompt_file = images_path / f"{lesson_num}_narrar_prompt.txt"
        if prompt_file.exists():
            shutil.move(str(prompt_file), str(week_dir / f"{lesson_num}_narrar_prompt.txt"))
        
        print(f"   ✅ {filename} → semana-{week}/")
    
    print("\n✅ Organização concluída!")


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Uso: python organize_images.py <images_dir>")
        sys.exit(1)
    
    organize_structure(sys.argv[1])
