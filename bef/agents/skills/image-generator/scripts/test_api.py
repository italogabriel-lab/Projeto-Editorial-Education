#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test API — Testa geração de imagens com Pollinations.ai

Uso:
    python test_api.py
    
Resultado:
    - Gera imagem de teste
    - Mostra URL da API
    - Valida qualidade
"""

import os
import sys
from pathlib import Path

# Adicionar path atual
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from generate_images import generate_image, optimize_prompt


def test_pollinations():
    """Testa Pollinations.ai com prompt simples"""
    
    print("\n" + "="*60)
    print("🎨 TESTE POLLINATIONS.AI")
    print("="*60)
    
    # Prompt de teste
    test_prompt = """
    Ilustração em aquarela detalhada, estilo livro ilustrado clássico,
    com fundo totalmente branco e bordas laterais difusas.
    Textura real de papel aquarelado, pinceladas suaves e luz quente e dourada.
    Cena de império bizantino com mosaicos dourados, luz divina entrando
    por janelas, atmosfera contemplativa e serena.
    """
    
    # Otimizar
    optimized = optimize_prompt(test_prompt)
    print(f"\n📝 Prompt otimizado:")
    print(f"   {optimized[:200]}...")
    
    # Output
    output_file = "test_pollinations_output.png"
    print(f"\n🔄 Gerando imagem...")
    print(f"   Saída: {output_file}")
    print(f"   Tamanho: 1024x1024")
    print(f"   Seed: 42")
    
    # Gerar
    result = generate_image(
        prompt=test_prompt,
        output_path=output_file,
        platform='pollinations',
        width=1024,
        height=1024,
        seed=42
    )
    
    # Resultado
    print("\n" + "="*60)
    if result['success']:
        print("✅ SUCESSO!")
        print(f"   Arquivo: {output_file}")
        print(f"   Tamanho: {Path(output_file).stat().st_size / 1024:.1f} KB")
        print(f"   URL: {result.get('url', 'N/A')[:100]}...")
        print("\n🖼️  Para ver a imagem:")
        print(f"   Windows: start {output_file}")
        print(f"   Linux:   xdg-open {output_file}")
        print(f"   Mac:     open {output_file}")
    else:
        print("❌ FALHA!")
        print(f"   Erro: {result['error']}")
        if 'url' in result:
            print(f"   URL: {result['url'][:100]}...")
    
    print("="*60 + "\n")
    
    return result['success']


def test_huggingface():
    """Testa HuggingFace Inference API"""
    
    print("\n" + "="*60)
    print("🤗 TESTE HUGGINGFACE API")
    print("="*60)
    
    # Verificar API key
    api_key = os.environ.get('HUGGINGFACE_TOKEN')
    if not api_key:
        print("⚠️  HUGGINGFACE_TOKEN não configurado")
        print("\n📝 Para obter:")
        print("   1. Acesse: https://huggingface.co/settings/tokens")
        print("   2. Crie token com permissão 'read'")
        print("   3. Adicione ao .env:")
        print("      HUGGINGFACE_TOKEN=hf_xxx...")
        print("\n   Ou execute:")
        print("      export HUGGINGFACE_TOKEN=hf_xxx...")
        return False
    
    test_prompt = "Watercolor illustration, byzantine empire, golden light"
    output_file = "test_huggingface_output.png"
    
    print(f"\n🔄 Gerando imagem...")
    print(f"   Modelo: stabilityai/stable-diffusion-xl-base-1.0")
    print(f"   Saída: {output_file}")
    
    # Gerar
    result = generate_image(
        prompt=test_prompt,
        output_path=output_file,
        platform='huggingface',
        width=1024,
        height=1024,
        seed=42
    )
    
    # Resultado
    print("\n" + "="*60)
    if result['success']:
        print("✅ SUCESSO!")
        print(f"   Arquivo: {output_file}")
        print(f"   Tamanho: {Path(output_file).stat().st_size / 1024:.1f} KB")
    else:
        print("❌ FALHA!")
        print(f"   Erro: {result['error']}")
    
    print("="*60 + "\n")
    
    return result['success']


def main():
    """Executa todos os testes"""
    
    print("\n" + "="*60)
    print("🧪 TESTE DE GERAÇÃO DE IMAGENS")
    print("="*60)
    print("\nEste script testa as APIs de geração de imagens.")
    print("Começando com Pollinations.ai (recomendado)...\n")
    
    # Testar Pollinations
    pollinations_success = test_pollinations()
    
    # Se falhar, tentar HuggingFace
    if not pollinations_success:
        print("\n⚠️  Pollinations falhou, testando HuggingFace...")
        test_huggingface()
    else:
        print("\n✅ Pollinations funcionou! Não é necessário testar HuggingFace.")
    
    # Resumo
    print("\n" + "="*60)
    print("📊 RESUMO")
    print("="*60)
    print("Pollinations.ai: " + ("✅ Funcionando" if pollinations_success else "❌ Falhou"))
    print("\nPróximos passos:")
    print("1. Se Pollinations funcionou: use para gerar todas as imagens")
    print("2. Se falhou: configure HuggingFace token e teste novamente")
    print("3. Para gerar ano completo:")
    print("   python scripts/main.py generate 3")
    print("="*60 + "\n")


if __name__ == '__main__':
    main()
