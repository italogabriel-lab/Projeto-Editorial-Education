#!/usr/bin/env python3
"""
Generate images using Pollinations.ai (FREE, no API key required).
Temporary solution while Gemini API quota is being resolved.
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import quote


def generate_image_pollinations(prompt: str, output_path: str, width: int = 1792, height: int = 896) -> bool:
    """
    Generate an image using Pollinations.ai API (FREE, no key needed).
    
    Args:
        prompt: The image generation prompt
        output_path: Path to save the generated image
        width: Image width (default: 1792 for 2:1 ratio)
        height: Image height (default: 896 for 2:1 ratio)
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        print(f"🎨 Generating image with Pollinations.ai (FREE)...")
        print(f"📐 Size: {width}x{height} (2:1 ratio)")
        print(f"📝 Prompt preview: {prompt[:100]}...")
        
        # Encode prompt for URL
        encoded_prompt = quote(prompt)
        
        # Build URL with 2:1 ratio parameters
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width={width}&height={height}&model=flux&nologo=true"
        
        print(f"🔗 Requesting: {url[:150]}...")
        
        # Download image
        response = requests.get(url, timeout=120)
        response.raise_for_status()
        
        # Ensure output directory exists
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        
        # Save image
        with open(output_path, 'wb') as f:
            f.write(response.content)
        
        print(f"✅ Image saved to: {output_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error generating image: {e}")
        return False


def generate_aula_14_2():
    """Generate image for Aula 14.2 — A beleza sem estátuas"""
    
    # Optimized prompt for Pollinations (shorter, more direct)
    prompt = """Watercolor illustration, classical book illustration style, white background with soft faded borders. Islamic architecture with abstract geometric patterns, no statues, ornamental lines and calligraphy. Warm golden light entering from side, delicate shadows, contemplative atmosphere. Balanced palette - luminous gold, ivory, deep blue, soft red, light ochre. Serene devotional figures in historical setting. Texture of watercolor paper, soft brushstrokes. Art as service, discipline and silent prayer. Focus on gesture not result, divine presence in artistic work."""
    
    # Output path following naming convention: 1-r-image-a
    # Structure: 2 - Imagens -> Semana 14 -> Aula 14.2 -> 1-r-image-a
    output_path = "Projeto Bibline Academy/Belas Artes - Fase da Gramática/1 Fase - Gramática/3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE/2 - Imagens/Semana 14/Aula 14.2 - A beleza sem estátuas/1-r-image-a.png"
    
    print("\n" + "="*80)
    print("📚 AULA 14.2 — A beleza sem estátuas")
    print("="*80)
    print("🔧 Using: Pollinations.ai (FREE - No API Key Required)")
    print("="*80)
    
    success = generate_image_pollinations(prompt, output_path, width=1792, height=896)
    
    if success:
        print("\n" + "="*80)
        print("✅ SUCCESS! Image generated successfully")
        print("="*80)
        print(f"📁 Location: {output_path}")
        print(f"📐 Ratio: 2:1 (1792x896)")
        print(f"🏷️  Naming: 1-r-image-a.png")
        print(f"🎨 API: Pollinations.ai (Flux model)")
        print("="*80 + "\n")
    else:
        print("\n❌ Failed to generate image. Please check:")
        print("   1. Internet connection is active")
        print("   2. Pollinations.ai service is available")
        print("   3. Try again in a few minutes\n")
    
    return success


if __name__ == "__main__":
    print("\n🚀 Pollinations Image Generator - Projeto Editorial Education")
    print("="*80)
    print("💡 FREE API - No Key Required")
    print("="*80)
    
    generate_aula_14_2()
