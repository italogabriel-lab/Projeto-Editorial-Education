#!/usr/bin/env python3
"""
Verify that all dependencies and configurations are ready for image generation.
"""

import os
import sys
from pathlib import Path

def check_env_file():
    """Check if .env file exists and has API key."""
    env_path = Path(".env")
    if not env_path.exists():
        print("❌ .env file not found")
        return False
    
    with open(env_path) as f:
        content = f.read()
    
    if "GEMINI_API_KEY=" not in content:
        print("❌ GEMINI_API_KEY not found in .env file")
        return False
    
    # Check if it's still the placeholder
    if "your_api_key_here" in content:
        print("⚠️  GEMINI_API_KEY is set to placeholder value")
        print("   Please update .env with your actual API key from aistudio.google.com")
        return False
    
    print("✅ .env file exists with GEMINI_API_KEY")
    return True

def check_dependencies():
    """Check if required Python packages are installed."""
    missing = []
    
    try:
        from google import genai
    except ImportError:
        missing.append("google-genai")
    
    try:
        from PIL import Image
    except ImportError:
        missing.append("pillow")
    
    try:
        import dotenv
    except ImportError:
        missing.append("python-dotenv")
    
    if missing:
        print(f"❌ Missing packages: {', '.join(missing)}")
        print(f"   Install with: pip install -r requirements.txt")
        return False
    
    print("✅ All required packages installed")
    return True

def check_prompt_file():
    """Check if the prompt file exists."""
    prompt_path = Path("Projeto Bibline Academy/Belas Artes - Fase da Gramática/1 Fase - Gramática/3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE/Estrutura Curricular - 3º ANO/5 - Prompts-para-imagens-narrar-3-ano ,separando as pastas por semana e colocando as imagens com o numero da aula para que seja facil de visualizar de onde é cada imagem que foi gerada .md")
    
    if not prompt_path.exists():
        print("⚠️  Prompt file not found (expected path)")
        return False
    
    print("✅ Prompt file exists")
    return True

def check_script():
    """Check if generation script exists."""
    script_path = Path("generate_image.py")
    if not script_path.exists():
        print("❌ generate_image.py not found")
        return False
    
    print("✅ Generation script exists")
    return True

def main():
    print("\n" + "="*80)
    print("🔍 GEMINI IMAGE GENERATION - SETUP VERIFICATION")
    print("="*80 + "\n")
    
    checks = [
        ("Environment", check_env_file),
        ("Dependencies", check_dependencies),
        ("Prompt File", check_prompt_file),
        ("Script", check_script),
    ]
    
    results = []
    for name, check_func in checks:
        print(f"Checking {name}...")
        results.append(check_func())
        print()
    
    print("="*80)
    if all(results):
        print("✅ ALL CHECKS PASSED - Ready to generate images!")
        print("="*80)
        print("\nNext steps:")
        print("1. If you haven't already, update .env with your actual GEMINI_API_KEY")
        print("2. Run: python generate_image.py")
        print("3. Check the generated image in the Semana 14 folder\n")
        return 0
    else:
        print("⚠️  SOME CHECKS FAILED - Please fix the issues above")
        print("="*80 + "\n")
        return 1

if __name__ == "__main__":
    sys.exit(main())
