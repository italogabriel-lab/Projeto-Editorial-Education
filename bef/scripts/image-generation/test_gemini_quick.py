#!/usr/bin/env python3
"""
Quick test for Gemini image generation with correct model name.
"""

import os
import sys
import io
from pathlib import Path
from dotenv import load_dotenv

load_dotenv("Projeto Bibline Academy/.env")

try:
    from google import genai
    from google.genai import types
    from PIL import Image
except ImportError as e:
    print(f"❌ Missing packages: pip install google-genai pillow")
    sys.exit(1)

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("❌ GEMINI_API_KEY not found")
    sys.exit(1)

print("\n" + "="*80)
print("🧪 TESTING GEMINI IMAGE GENERATION")
print("="*80)
print(f"🔑 API Key: {api_key[:10]}...{api_key[-4:]}")
print(f"📡 Model: gemini-2.5-flash-image")
print("="*80 + "\n")

client = genai.Client(api_key=api_key)

# Simple test prompt
prompt = "A beautiful watercolor illustration of Islamic architecture with abstract geometric patterns, white background, warm golden light, classical book illustration style"

output_path = "Projeto Bibline Academy/Belas Artes - Fase da Gramática/1 Fase - Gramática/3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE/Semana 14/Aula 14.2 - A beleza sem estátuas/1-r-image-a-gemini.png"

try:
    print("🎨 Generating image...")
    
    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
        ),
    )
    
    # Extract and save image
    for part in response.candidates[0].content.parts:
        if part.inline_data is not None:
            print("✅ Image data received!")
            
            image = Image.open(io.BytesIO(part.inline_data.data))
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            image.save(output_path, "PNG")
            
            print(f"✅ Image saved: {output_path}")
            print(f"📐 Size: {image.size}")
            print(f"📊 File size: {os.path.getsize(output_path) / 1024:.1f} KB")
            print("\n" + "="*80)
            print("✅ SUCCESS! Gemini API is working correctly!")
            print("="*80 + "\n")
            sys.exit(0)
    
    print("❌ No image data in response")
    sys.exit(1)

except Exception as e:
    error_str = str(e)
    print(f"\n❌ Error: {e}")
    
    if "limit: 0" in error_str or "RESOURCE_EXHAUSTED" in error_str:
        print("\n📊 QUOTA EXHAUSTED - Free tier is disabled (limit: 0)")
        print("\n🔧 SOLUTION:")
        print("   1. Enable billing at: https://console.cloud.google.com/billing")
        print("   2. OR request quota increase at:")
        print("      https://console.cloud.google.com/apis/api/generativelanguage.googleapis.com/quotas")
        print("\n💡 Until then, use: python generate_image_temp.py (Pollinations - FREE)")
    
    sys.exit(1)
