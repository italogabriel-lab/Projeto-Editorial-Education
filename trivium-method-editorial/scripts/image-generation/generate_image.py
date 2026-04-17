#!/usr/bin/env python3
"""
Generate images using Google Gemini API for educational content.
Organized by week and lesson structure with proper naming conventions.
"""

import os
import sys
import io
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

try:
    from google import genai
    from google.genai import types
    from PIL import Image
except ImportError as e:
    print(f"❌ Missing required packages. Install with:")
    print(f"   pip install google-genai pillow python-dotenv")
    sys.exit(1)


def get_gemini_client():
    """Initialize and return Gemini API client."""
    # Try multiple locations for .env file
    env_paths = [
        Path(".env"),
        Path("Projeto Bibline Academy/.env"),
        Path.home() / ".env"
    ]

    api_key = os.environ.get("GEMINI_API_KEY")

    # If not in environment, try to load from .env files
    if not api_key:
        from dotenv import load_dotenv
        for env_path in env_paths:
            if env_path.exists():
                load_dotenv(env_path)
                api_key = os.environ.get("GEMINI_API_KEY")
                if api_key:
                    print(f"✅ Loaded API key from: {env_path}")
                    break

    if not api_key:
        raise ValueError(
            "❌ GEMINI_API_KEY not found in environment variables.\n"
            "   Please set it in your .env file or environment."
        )
    return genai.Client(api_key=api_key)


def generate_image(prompt: str, output_path: str, ratio: str = "2:1") -> bool:
    """
    Generate an image using Gemini 2.5 Flash Image model.
    
    Args:
        prompt: The image generation prompt
        output_path: Path to save the generated image
        ratio: Aspect ratio (default: "2:1")
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        print(f"🎨 Generating image with ratio {ratio}...")
        print(f"📝 Prompt preview: {prompt[:100]}...")
        
        client = get_gemini_client()
        
        # Add aspect ratio to prompt
        enhanced_prompt = f"{prompt}\n\nAspect ratio: {ratio}"
        
        response = client.models.generate_content(
            model="gemini-2.5-flash-image",
            contents=enhanced_prompt,
            config=types.GenerateContentConfig(
                response_modalities=["TEXT", "IMAGE"],
            ),
        )
        
        # Extract and save image
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                image = Image.open(io.BytesIO(part.inline_data.data))
                
                # Ensure output directory exists
                Path(output_path).parent.mkdir(parents=True, exist_ok=True)
                
                # Save image
                image.save(output_path, "PNG")
                print(f"✅ Image saved to: {output_path}")
                return True
        
        print("❌ No image data found in response")
        return False
        
    except Exception as e:
        print(f"❌ Error generating image: {e}")
        return False


def generate_aula_14_2():
    """Generate image for Aula 14.2 — A beleza sem estátuas"""
    
    # Full prompt from the markdown file
    prompt = """Ilustração em aquarela detalhada, estilo ilustração de livro clássico, com fundo totalmente branco e bordas laterais difusas e suavemente desbotadas, criando aparência de página ilustrada antiga.
Textura real de papel aquarelado, pinceladas suaves e luz quente e dourada.
Paleta em tons equilibrados — dourado luminoso, marfim, azul profundo, vermelho suave, ocre claro e sombras delicadas.

Cena inspirada no trecho

"Onde não há estátua, o olhar descansa nas linhas. Onde não há rosto, a mente contempla o conceito. A abstração islâmica nasce do temor reverente diante de um Deus que não cabe em forma humana.

O cristão que entra numa mesquita sente a ausência do rosto e compreende a intenção. Mas carrega consigo a boa notícia de que Deus, embora infinito, se fez visível em Cristo. A encarnação transformou a arte cristã para sempre."

— inspirado em Atos 7.48 e Herman Dooyeweerd

Composição da cena

A ilustração deve representar visualmente o conteúdo descrito no trecho acima, com foco no tema "A beleza sem estátuas" e no conceito de abstração.

Elementos visuais principais:
• Cenário coerente com o período histórico e o contexto artístico descrito
• Figuras humanas em atividade relacionada ao tema, com expressões serenas e devotas
• Detalhes arquitetônicos ou artísticos mencionados no texto
• Objetos e materiais relevantes ao contexto da cena

Iluminação:
• Luz quente entrando lateralmente, suave e dourada
• Sombras delicadas e ambiente contemplativo
• Sensação de tempo lento e silêncio profundo

Linguagem visual e simbolismo:
• A arte como serviço, disciplina e oração silenciosa
• Ausência de ostentação — foco no gesto, não no resultado
• A luz indicando presença divina no trabalho artístico
• Sensação de que o trabalho paciente é caminho de ascensão espiritual"""

    # Output path following naming convention: 1-r-image-a
    # Structure: 2 - Imagens -> Semana 14 -> Aula 14.2 -> 1-r-image-a
    output_path = "Projeto Bibline Academy/Belas Artes - Fase da Gramática/1 Fase - Gramática/3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE/2 - Imagens/Semana 14/Aula 14.2 - A beleza sem estátuas/1-r-image-a.png"
    
    print("\n" + "="*80)
    print("📚 AULA 14.2 — A beleza sem estátuas")
    print("="*80)
    
    success = generate_image(prompt, output_path, ratio="2:1")
    
    if success:
        print("\n" + "="*80)
        print("✅ SUCCESS! Image generated successfully")
        print("="*80)
        print(f"📁 Location: {output_path}")
        print(f"📐 Ratio: 2:1")
        print(f"🏷️  Naming: 1-r-image-a.png")
        print("="*80 + "\n")
    else:
        print("\n❌ Failed to generate image. Please check:")
        print("   1. GEMINI_API_KEY is set correctly in .env")
        print("   2. You have sufficient API quota")
        print("   3. Internet connection is active\n")
    
    return success


def generate_aula_14_3():
    """Generate image for Aula 14.3 — O oceano azul de Istambul"""
    
    # Full prompt from the markdown file
    prompt = """Ilustração em aquarela detalhada, estilo ilustração de livro clássico, com fundo totalmente branco e bordas laterais difusas e suavemente desbotadas, criando aparência de página ilustrada antiga.
Textura real de papel aquarelado, pinceladas suaves e luz quente e dourada.
Paleta em tons equilibrados — dourado luminoso, marfim, azul profundo, vermelho suave, ocre claro e sombras delicadas.

Cena inspirada no trecho

"O oceano de azulejos que cobre cada parede da Mesquita Azul lança o visitante num mar de beleza sem margens. As flores estilizadas dançam em azul sobre fundo branco, e a luz do sol, filtrada por centenas de janelas, faz os padrões brilharem como céu líquido.

O cristão contempla esse esplendor com admiração sincera e sabe que o Deus que os céus dos céus não podem conter não se impressiona com paredes. Ele busca adoradores que O adorem em espírito e verdade, com o coração mais azul que qualquer azulejo."

— inspirado em 1 Reis 8.27 e A. W. Tozer

Composição da cena

A ilustração deve representar visualmente o conteúdo descrito no trecho acima, com foco no tema "O oceano azul de Istambul" e no conceito de esplendor.

Elementos visuais principais:
• Cenário coerente com o período histórico e o contexto artístico descrito
• Figuras humanas em atividade relacionada ao tema, com expressões serenas e devotas
• Detalhes arquitetônicos ou artísticos mencionados no texto
• Objetos e materiais relevantes ao contexto da cena

Iluminação:
• Luz quente entrando lateralmente, suave e dourada
• Sombras delicadas e ambiente contemplativo
• Sensação de tempo lento e silêncio profundo

Linguagem visual e simbolismo:
• A arte como serviço, disciplina e oração silenciosa
• Ausência de ostentação — foco no gesto, não no resultado
• A luz indicando presença divina no trabalho artístico
• Sensação de que o trabalho paciente é caminho de ascensão espiritual"""

    # Output path following naming convention: 1-r-image-a
    # Structure: 2 - Imagens -> Semana 14 -> Aula 14.3 -> 1-r-image-a
    output_path = "Projeto Bibline Academy/Belas Artes - Fase da Gramática/1 Fase - Gramática/3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE/2 - Imagens/Semana 14/Aula 14.3 - O oceano azul de Istambul/1-r-image-a.png"
    
    print("\n" + "="*80)
    print("📚 AULA 14.3 — O oceano azul de Istambul")
    print("="*80)
    
    success = generate_image(prompt, output_path, ratio="2:1")
    
    if success:
        print("\n" + "="*80)
        print("✅ SUCCESS! Image generated successfully")
        print("="*80)
        print(f"📁 Location: {output_path}")
        print(f"📐 Ratio: 2:1")
        print(f"🏷️  Naming: 1-r-image-a.png")
        print("="*80 + "\n")
    else:
        print("\n❌ Failed to generate image. Please check:")
        print("   1. GEMINI_API_KEY is set correctly in .env")
        print("   2. You have sufficient API quota")
        print("   3. Internet connection is active\n")
    
    return success


if __name__ == "__main__":
    print("\n🚀 Gemini Image Generator - Projeto Editorial Education")
    print("="*80)
    
    # Check if specific lesson was requested
    if len(sys.argv) > 1:
        lesson = sys.argv[1]
        if lesson == "14.2":
            generate_aula_14_2()
        elif lesson == "14.3":
            generate_aula_14_3()
        else:
            print(f"⚠️  Lesson {lesson} not implemented yet.")
            print("   Available: 14.2, 14.3")
    else:
        # Default: generate Aula 14.2
        generate_aula_14_2()
