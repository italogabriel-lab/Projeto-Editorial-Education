#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Generate Images — Gera imagens via APIs
"""

import requests
from urllib.parse import quote
from pathlib import Path


def optimize_prompt(prompt):
    """
    Otimiza prompt adicionando keywords em inglês
    
    Args:
        prompt (str): Prompt original em português
        
    Returns:
        str: Prompt otimizado
    """
    
    suffix = """
    , watercolor painting, classical book illustration style,
    white background with soft diffused edges, aged paper texture,
    warm golden light, balanced color palette, detailed brushwork,
    serene and contemplative atmosphere, Christian classical art
    """
    
    return prompt.strip() + suffix


def generate_image(prompt, output_path, platform='pollinations', width=1024, height=1024, seed=42):
    """
    Gera imagem usando API
    
    Args:
        prompt (str): Prompt da imagem
        output_path (str): Caminho de saída
        platform (str): Plataforma (pollinations, huggingface, deepai)
        width (int): Largura
        height (int): Altura
        seed (int): Seed para geração
        
    Returns:
        dict: {'success': bool, 'error': str or None}
    """
    
    # Otimizar prompt
    optimized_prompt = optimize_prompt(prompt)
    
    # Escolher plataforma
    if platform == 'pollinations':
        return generate_pollinations(optimized_prompt, output_path, width, height, seed)
    elif platform == 'huggingface':
        return generate_huggingface(optimized_prompt, output_path, width, height, seed)
    elif platform == 'deepai':
        return generate_deepai(optimized_prompt, output_path)
    else:
        return {'success': False, 'error': f'Plataforma desconhecida: {platform}'}


def generate_pollinations(prompt, output_path, width=1024, height=1024, seed=42):
    """
    Gera imagem via Pollinations.ai
    
    Args:
        prompt (str): Prompt otimizado
        output_path (str): Caminho de saída
        width (int): Largura
        height (int): Altura
        seed (int): Seed
        
    Returns:
        dict: Resultado
    """
    
    try:
        # URL encode
        encoded_prompt = quote(prompt)
        
        # Construir URL
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width={width}&height={height}&seed={seed}&model=flux"
        
        # Download
        response = requests.get(url, timeout=120)
        response.raise_for_status()
        
        # Salvar
        with open(output_path, 'wb') as f:
            f.write(response.content)
        
        return {'success': True, 'error': None}
        
    except Exception as e:
        return {'success': False, 'error': str(e)}


def generate_huggingface(prompt, output_path, width=1024, height=1024, seed=42):
    """
    Gera imagem via HuggingFace Inference API
    
    Args:
        prompt (str): Prompt otimizado
        output_path (str): Caminho de saída
        width (int): Largura
        height (int): Altura
        seed (int): Seed
        
    Returns:
        dict: Resultado
    """
    
    import os
    
    # API key
    api_token = os.environ.get('HUGGINGFACE_TOKEN')
    if not api_token:
        return {'success': False, 'error': 'HUGGINGFACE_TOKEN not set'}
    
    try:
        # URL
        url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
        
        # Headers
        headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }
        
        # Body
        payload = {
            "inputs": prompt,
            "parameters": {
                "width": width,
                "height": height,
                "num_inference_steps": 50
            }
        }
        
        # Request
        response = requests.post(url, headers=headers, json=payload, timeout=120)
        response.raise_for_status()
        
        # Salvar
        with open(output_path, 'wb') as f:
            f.write(response.content)
        
        return {'success': True, 'error': None}
        
    except Exception as e:
        return {'success': False, 'error': str(e)}


def generate_deepai(prompt, output_path):
    """
    Gera imagem via DeepAI
    
    Args:
        prompt (str): Prompt otimizado
        output_path (str): Caminho de saída
        
    Returns:
        dict: Resultado
    """
    
    import os
    
    # API key
    api_key = os.environ.get('DEEPAI_API_KEY')
    if not api_key:
        return {'success': False, 'error': 'DEEPAI_API_KEY not set'}
    
    try:
        # URL
        url = "https://api.deepai.org/api/text2img"
        
        # Data
        data = {
            'text': prompt
        }
        
        # Headers
        headers = {
            'api-key': api_key
        }
        
        # Request
        response = requests.post(url, data=data, headers=headers, timeout=120)
        response.raise_for_status()
        
        # Parse response
        result = response.json()
        image_url = result['output_url']
        
        # Download image
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        
        # Salvar
        with open(output_path, 'wb') as f:
            f.write(image_response.content)
        
        return {'success': True, 'error': None}
        
    except Exception as e:
        return {'success': False, 'error': str(e)}


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 3:
        print("Uso: python generate_images.py <prompt> <output.png> [platform]")
        sys.exit(1)
    
    prompt = sys.argv[1]
    output = sys.argv[2]
    platform = sys.argv[3] if len(sys.argv) > 3 else 'pollinations'
    
    result = generate_image(prompt, output, platform)
    
    if result['success']:
        print(f"✅ Imagem gerada: {output}")
    else:
        print(f"❌ Erro: {result['error']}")
