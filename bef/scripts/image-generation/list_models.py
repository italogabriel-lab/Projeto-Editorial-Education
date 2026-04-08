#!/usr/bin/env python3
"""
List available Gemini models to find the correct image generation model.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env
load_dotenv("Projeto Bibline Academy/.env")

try:
    from google import genai
except ImportError:
    print("❌ Install: pip install google-genai")
    exit(1)

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("❌ GEMINI_API_KEY not found")
    exit(1)

client = genai.Client(api_key=api_key)

print("\n🔍 Listing available Gemini models...\n")

models = client.models.list()

image_models = []
for model in models:
    if 'image' in model.name.lower() or 'flash' in model.name.lower():
        image_models.append(model)
        print(f"📸 {model.name}")
        print(f"   Description: {getattr(model, 'description', 'N/A')}")
        print(f"   Version: {getattr(model, 'version', 'N/A')}")
        print()

if not image_models:
    print("⚠️  No image models found!")
    print("\nAll available models:")
    for model in list(models)[:30]:
        print(f"  • {model.name}")

print(f"\n✅ Found {len(image_models)} image-capable models")
