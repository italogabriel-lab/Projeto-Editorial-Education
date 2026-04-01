#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Generate Log — Gera log de produção em Markdown
"""

import os
from pathlib import Path
from datetime import datetime


def generate_log(year, images_dir):
    """
    Gera log de produção
    
    Args:
        year (int): Ano escolar
        images_dir (str): Diretório das imagens
    """
    
    images_path = Path(images_dir)
    
    log_content = f"# Log de Geração — {year}º Ano\n\n"
    log_content += f"**Data:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    
    # Estatísticas
    total_images = 0
    total_weeks = 0
    weeks_data = {}
    
    # Listar semanas
    for week_dir in sorted(images_path.glob('semana-*')):
        if week_dir.is_dir():
            week_num = int(week_dir.name.replace('semana-', ''))
            total_weeks += 1
            
            # Listar imagens da semana
            images = list(week_dir.glob('*_narrar.png'))
            total_images += len(images)
            
            weeks_data[week_num] = {
                'count': len(images),
                'images': [img.name for img in images]
            }
    
    # Adicionar estatísticas
    log_content += "## Estatísticas\n\n"
    log_content += f"- **Total de semanas:** {total_weeks}\n"
    log_content += f"- **Total de imagens:** {total_images}\n"
    log_content += f"- **Média por semana:** {total_images/total_weeks:.1f}\n\n"
    
    # Status por semana
    log_content += "## Status por Semana\n\n"
    log_content += "| Semana | Imagens | Status |\n"
    log_content += "|--------|---------|--------|\n"
    
    for week_num in sorted(weeks_data.keys()):
        count = weeks_data[week_num]['count']
        status = "✅" if count >= 3 else "⏳"
        log_content += f"| {week_num} | {count} | {status} |\n"
    
    log_content += "\n"
    
    # Lista detalhada
    log_content += "## Lista Detalhada\n\n"
    
    for week_num in sorted(weeks_data.keys()):
        log_content += f"### Semana {week_num}\n\n"
        
        for image_name in sorted(weeks_data[week_num]['images']):
            lesson_num = image_name.split('_')[0]
            log_content += f"- [ ] {lesson_num} — `{image_name}`\n"
        
        log_content += "\n"
    
    # Salvar log
    log_file = images_path / "LOG.md"
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write(log_content)
    
    print(f"📝 Log gerado: {log_file}")


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 3:
        print("Uso: python generate_log.py <year> <images_dir>")
        sys.exit(1)
    
    year = int(sys.argv[1])
    images_dir = sys.argv[2]
    
    generate_log(year, images_dir)
