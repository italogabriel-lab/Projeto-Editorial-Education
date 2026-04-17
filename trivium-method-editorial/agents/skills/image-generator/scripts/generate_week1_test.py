#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Generate Week 1 Test — Gera Semana 1 completa para teste
"""

import os
import sys
from pathlib import Path

# Adicionar path atual
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from generate_images import generate_image, optimize_prompt


# Prompts da Semana 1 (extraídos do arquivo de prompts)
WEEK_1_PROMPTS = {
    '1.1': {
        'title': 'Império Romano do oriente e arte bizantina',
        'prompt': '''Ilustração em aquarela detalhada, estilo ilustração de livro clássico, com fundo totalmente branco e bordas laterais difusas e suavemente desbotadas, criando aparência de página ilustrada antiga.
Textura real de papel aquarelado, pinceladas suaves e luz quente e dourada.
Paleta em tons equilibrados — dourado luminoso, marfim, azul profundo, vermelho suave, ocre claro e sombras delicadas.

Cena inspirada no trecho: "Dois filhos nasceram da mesma mãe Roma. Um adormeceu na noite dos bárbaros, o outro despertou ao sol de Cristo. O que sobreviveu não guardou apenas muralhas e leis, guardou pincéis, tesselas de ouro e a arte de proclamar a fé em cada parede."

Composição:
• Cenário: Império Bizantino, arquitetura com cúpulas e mosaicos dourados
• Figuras humanas em atividade relacionada ao tema, com expressões serenas e devotas
• Detalhes arquitetônicos: arcos, colunas, mosaicos bizantinos
• Iluminação: Luz quente entrando lateralmente, suave e dourada
• Sensação de tempo lento e silêncio profundo'''
    },
    
    '1.2': {
        'title': 'Constantinopla como centro',
        'prompt': '''Ilustração em aquarela detalhada, estilo ilustração de livro clássico, com fundo totalmente branco e bordas laterais difusas e suavemente desbotadas.
Textura real de papel aquarelado, pinceladas suaves e luz quente e dourada.
Paleta em tons equilibrados — dourado luminoso, marfim, azul profundo, vermelho suave, ocre claro e sombras delicadas.

Cena inspirada no trecho: "Entre dois mares e dois continentes, Deus plantou uma cidade de ouro e de fé. Constantinopla ergueu-se como farol para o oriente e o ocidente."

Composição:
• Cenário: Vista panorâmica de Constantinopla com muralhas e cúpulas
• Hagia Sophia ao centro com sua grande cúpula
• Mar ao fundo, navios comerciais
• Iluminação: Luz dourada do amanhecer
• Sensação de grandeza e centralidade'''
    },
    
    '1.3': {
        'title': 'Cristianismo e transformação da arte pública',
        'prompt': '''Ilustração em aquarela detalhada, estilo ilustração de livro clássico, com fundo totalmente branco e bordas laterais difusas e suavemente desbotadas.
Textura real de papel aquarelado, pinceladas suaves e luz quente e dourada.
Paleta em tons equilibrados — dourado luminoso, marfim, azul profundo, vermelho suave, ocre claro e sombras delicadas.

Cena inspirada no trecho: "Quando a perseguição cessou, as sombras se dissiparam. A fé que sussurrava nas grutas úmidas passou a ressoar sob o teto forrado de ouro das basílicas imperiais."

Composição:
• Cenário: Interior de basílica cristã primitiva
• Mosaicos dourados nas paredes
• Cristãos em adoração, expressões de devoção
• Iluminação: Luz divina entrando por janelas altas
• Sensação de triunfo e glorificação'''
    }
}


def generate_week_1(output_dir='test_semana1'):
    """Gera todas as imagens da Semana 1"""
    
    print("\n" + "="*60)
    print("🎨 GERANDO SEMANA 1 — ANO 3")
    print("="*60)
    
    # Criar diretório
    output_path = Path(output_dir) / 'semana-1'
    output_path.mkdir(parents=True, exist_ok=True)
    
    print(f"\n📁 Saída: {output_path}")
    print(f"🎨 Plataforma: Pollinations.ai (Flux)")
    print(f"📐 Tamanho: 1024x1024")
    print()
    
    success = 0
    failed = 0
    
    for lesson_num, lesson_data in WEEK_1_PROMPTS.items():
        title = lesson_data['title']
        prompt = lesson_data['prompt']
        
        print(f"🔄 Aula {lesson_num} — {title[:50]}...")
        
        # Arquivos de saída
        image_file = output_path / f"{lesson_num}_narrar.png"
        prompt_file = output_path / f"{lesson_num}_narrar_prompt.txt"
        
        # Seed baseada no número da aula
        seed = int(lesson_num.replace('.', ''))
        
        # Gerar imagem
        result = generate_image(
            prompt=prompt,
            output_path=str(image_file),
            platform='pollinations',
            width=1024,
            height=1024,
            seed=seed
        )
        
        if result['success']:
            # Salvar prompt
            with open(prompt_file, 'w', encoding='utf-8') as f:
                f.write(prompt)
            
            print(f"   ✅ {lesson_num}_narrar.png ({Path(image_file).stat().st_size / 1024:.1f} KB)")
            success += 1
        else:
            print(f"   ❌ Falha: {result['error']}")
            failed += 1
    
    # Resumo
    print("\n" + "="*60)
    print("📊 RESUMO SEMANA 1")
    print("="*60)
    print(f"Total: {len(WEEK_1_PROMPTS)}")
    print(f"✅ Sucesso: {success}")
    print(f"❌ Falhas: {failed}")
    print(f"📁 Diretório: {output_path}")
    print("="*60)
    
    if success == len(WEEK_1_PROMPTS):
        print("\n✅ SEMANA 1 GERADA COM SUCESSO!")
        print("\n🖼️  Para ver as imagens:")
        print(f"   ls -lh {output_path}/")
        return True
    else:
        print(f"\n⚠️  {failed} imagem(s) falharam")
        return False


if __name__ == '__main__':
    output_dir = sys.argv[1] if len(sys.argv) > 1 else 'test_semana1'
    success = generate_week_1(output_dir)
    sys.exit(0 if success else 1)
