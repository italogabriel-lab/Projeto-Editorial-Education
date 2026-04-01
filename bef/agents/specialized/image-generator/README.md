# 🎨 Image Generator Agent - Documentação Completa

**Especialista em Geração de Imagens a partir de Prompts do Hábito Narrar**

---

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [Objetivo](#objetivo)
3. [Comandos Disponíveis](#comandos-disponíveis)
4. [Exemplos de Uso](#exemplos-de-uso)
5. [Plataformas de Geração](#plataformas-de-geração)
6. [Hierarquia de Armazenamento](#hierarquia-de-armazenamento)
7. [Estrutura de Pastas](#estrutura-de-pastas)
8. [Workflow de Geração](#workflow-de-geração)
9. [Casos de Uso](#casos-de-uso)
10. [FAQ](#faq)

---

## Visão Geral

| Propriedade | Valor |
|-------------|-------|
| **Nome** | Image Generator |
| **Tipo** | Artista Digital |
| **Escopo** | Editorial Squad |
| **Status** | ✅ Ativo |
| **Versão** | 1.0 |
| **Especialidade** | Geração de imagens com IA |

---

## Objetivo

O **Image Generator** transforma prompts literários do hábito Narrar em ilustrações em aquarela clássica usando APIs gratuitas de IA generativa, organizando-as em hierarquia de pastas por ano/semana/aula.

**Quando usar:**
- Gerar imagens para todas as aulas de um ano
- Criar ilustrações específicas para uma semana
- Regenerar imagens com qualidade insatisfatória
- Organizar imagens existentes na hierarquia correta

---

## Comandos Disponíveis

### **1. `/image-generator generate <ano>`**

**Descrição:** Gera todas as imagens de um ano específico.

**Sintaxe:**
```bash
/image-generator generate <ano> --output <diretório>
```

**Parâmetros:**
| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| `ano` | number | ✅ | Ano escolar (1-5) |
| `--output` | string | ❌ | Diretório de saída (padrão: `assets/imagens-narrar/[ano]-ano/`) |
| `--platform` | string | ❌ | Plataforma (pollinations, huggingface, deepai) |
| `--width` | number | ❌ | Largura da imagem (padrão: 1024) |
| `--height` | number | ❌ | Altura da imagem (padrão: 1024) |

**Exemplo:**
```bash
/image-generator generate 3 --output assets/imagens-narrar/3-ano/
```

**Saída:**
```bash
🎨 Image Generator — Ano 3

📊 Status:
- Total de prompts: 120
- Imagens geradas: 0
- Pendentes: 120

🔄 Gerando imagens...

✅ Semana 1
   ✅ 1.1_narrar.png (Pollinations)
   ✅ 1.2_narrar.png (Pollinations)
   ✅ 1.3_narrar.png (Pollinations)

✅ Semana 2
   ✅ 2.1_narrar.png (Pollinations)
   ...

📊 Estatísticas:
- Total: 120
- Sucesso: 118
- Falhas: 2
- Tempo: 45m 32s

📁 Estrutura criada:
assets/imagens-narrar/3-ano/
├── semana-1/
│   ├── 1.1_narrar.png
│   ├── 1.1_narrar_prompt.txt
│   └── ...
└── semana-2/
    └── ...

✅ Geração concluída!
```

---

### **2. `/image-generator generate-week <ano> <semana>`**

**Descrição:** Gera imagens de uma semana específica.

**Sintaxe:**
```bash
/image-generator generate-week <ano> <semana>
```

**Exemplo:**
```bash
/image-generator generate-week 3 5
```

**Saída:**
```bash
🎨 Image Generator — Ano 3, Semana 5

📊 Prompts encontrados: 3
🔄 Gerando...

✅ 1.1 — Império Bizantino
✅ 1.2 — Constantinopla
✅ 1.3 — Cristianismo

✅ Semana 5 concluída!
```

---

### **3. `/image-generator regenerate <aula> <ano>`**

**Descrição:** Regenera imagem específica.

**Sintaxe:**
```bash
/image-generator regenerate <aula> <ano> [--seed <numero>]
```

**Exemplo:**
```bash
/image-generator regenerate 1.1 3 --seed 42
```

---

### **4. `/image-generator status <ano>`**

**Descrição:** Verifica status de geração.

**Sintaxe:**
```bash
/image-generator status <ano>
```

**Exemplo:**
```bash
/image-generator status 3
```

**Saída:**
```bash
📊 Status — Ano 3

Total de aulas: 40
Imagens geradas: 38 (95%)
Pendentes: 2
Falhas: 0

Por semana:
✅ Semana 1-10: 100%
✅ Semana 11-20: 100%
⏳ Semana 21-30: 85%
⏳ Semana 31-40: 90%
```

---

### **5. `/image-generator organize <diretório>`**

**Descrição:** Organiza imagens existentes na hierarquia correta.

**Sintaxe:**
```bash
/image-generator organize <diretório>
```

**Exemplo:**
```bash
/image-generator organize downloads/
```

---

## Plataformas de Geração

### **1. Pollinations.ai (Recomendada)**

| Característica | Valor |
|----------------|-------|
| **Custo** | Gratuito |
| **Limite** | Ilimitado |
| **Qualidade** | Alta (Flux model) |
| **Velocidade** | ~10-20s/imagem |
| **API** | REST (GET) |

**Configuração:**
```bash
URL: https://image.pollinations.ai/prompt/{PROMPT}
Parâmetros:
  - width: 1024
  - height: 1024
  - seed: {lesson_number}
  - model: flux
```

**Vantagens:**
- ✅ Sem necessidade de API key
- ✅ Ilimitado
- ✅ Alta qualidade
- ✅ Rápido

---

### **2. HuggingFace Inference API**

| Característica | Valor |
|----------------|-------|
| **Custo** | Gratuito |
| **Limite** | 1000 requests/day |
| **Qualidade** | Alta (SDXL) |
| **Velocidade** | ~5-15s/imagem |
| **API** | REST (POST) |

**Configuração:**
```bash
URL: https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0
Headers:
  - Authorization: Bearer {HF_TOKEN}
Body:
  - inputs: "{PROMPT}"
  - parameters:
    - width: 1024
    - height: 1024
    - num_inference_steps: 50
```

**Vantagens:**
- ✅ Modelos de ponta
- ✅ Controle fino de parâmetros
- ✅ Rápido

**Desvantagens:**
- ❌ Requer API key
- ❌ Limite diário

---

### **3. DeepAI**

| Característica | Valor |
|----------------|-------|
| **Custo** | Gratuito |
| **Limite** | 500 requests/day |
| **Qualidade** | Média |
| **Velocidade** | ~15-30s/imagem |
| **API** | REST (POST) |

---

### **4. Craiyon**

| Característica | Valor |
|----------------|-------|
| **Custo** | Gratuito |
| **Limite** | Ilimitado |
| **Qualidade** | Média |
| **Velocidade** | ~30-60s/imagem |
| **API** | Web scraping |

---

## Hierarquia de Armazenamento

### **Estrutura Completa**

```
assets/
└── imagens-narrar/
    ├── 1-ano/
    │   ├── semana-1/
    │   │   ├── 1.1_narrar.png
    │   │   ├── 1.1_narrar_prompt.txt
    │   │   ├── 1.2_narrar.png
    │   │   ├── 1.2_narrar_prompt.txt
    │   │   └── 1.3_narrar.png
    │   ├── semana-2/
    │   │   └── ...
    │   └── LOG.md
    ├── 2-ano/
    │   └── ...
    ├── 3-ano/
    │   └── ...
    ├── 4-ano/
    │   └── ...
    └── 5-ano/
        └── ...
```

### **Arquivos por Aula**

Cada aula gera **2 arquivos**:

1. **Imagem:** `[AULA].[NUMERO]_narrar.png`
   - Formato: PNG
   - Tamanho: 1024x1024
   - Qualidade: Alta

2. **Prompt:** `[AULA].[NUMERO]_narrar_prompt.txt`
   - Formato: TXT
   - Conteúdo: Prompt completo usado
   - Referência: Para regeneração futura

---

### **Arquivo de Log (LOG.md)**

Cada ano tem um `LOG.md`:

```markdown
# Log de Geração — 3º Ano

## Status por Aula

| Aula | Título | Status | Plataforma | Arquivo |
|------|--------|--------|------------|---------|
| 1.1 | Império Bizantino | ✅ | Pollinations | 1.1_narrar.png |
| 1.2 | Constantinopla | ✅ | Pollinations | 1.2_narrar.png |
| 1.3 | Cristianismo | ✅ | Pollinations | 1.3_narrar.png |

## Estatísticas
- Total: 120
- Geradas: 118
- Pendentes: 2
- Falhas: 0

## Histórico
- 2026-04-01: Geração inicial (118/120)
- 2026-04-02: Regeneração (2/2)
```

---

## Workflow de Geração

### **Passo 1: Extrair Prompts**

```python
# Script: extract_prompts.py
import re

def extract_prompts(markdown_file):
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern para encontrar prompts
    pattern = r'### Aula (\d+\.\d+) — (.+?)\n\n\*\*Prompt:\*\*\n```\n(.+?)```'
    matches = re.findall(pattern, content, re.DOTALL)
    
    prompts = []
    for lesson_num, title, prompt in matches:
        prompts.append({
            'lesson': lesson_num,
            'title': title,
            'prompt': prompt.strip()
        })
    
    return prompts
```

---

### **Passo 2: Otimizar Prompt**

```python
# Adicionar keywords em inglês
def optimize_prompt(prompt):
    suffix = """
    , watercolor painting, classical book illustration style,
    white background with soft diffused edges, aged paper texture,
    warm golden light, balanced color palette, detailed brushwork,
    serene and contemplative atmosphere, Christian classical art
    """
    return prompt + suffix
```

---

### **Passo 3: Gerar Imagem**

```python
# Script: generate_images.py
import requests
from urllib.parse import quote

def generate_image(prompt, output_path, seed=42):
    # Otimizar prompt
    optimized = optimize_prompt(prompt)
    
    # URL encode
    encoded_prompt = quote(optimized)
    
    # Pollinations API
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&seed={seed}&model=flux"
    
    # Download
    response = requests.get(url)
    
    # Salvar
    with open(output_path, 'wb') as f:
        f.write(response.content)
    
    return True
```

---

### **Passo 4: Organizar**

```python
# Script: organize_images.py
import os
import shutil

def organize_images(source_dir, output_dir, year):
    # Criar estrutura
    os.makedirs(f"{output_dir}/{year}-ano/", exist_ok=True)
    
    # Mover imagens para pastas corretas
    for filename in os.listdir(source_dir):
        if filename.endswith('_narrar.png'):
            # Extrair número da aula
            lesson_num = filename.split('_')[0]  # Ex: "1.1"
            week = get_week_from_lesson(lesson_num)
            
            # Criar pasta da semana
            week_dir = f"{output_dir}/{year}-ano/semana-{week}/"
            os.makedirs(week_dir, exist_ok=True)
            
            # Mover arquivo
            shutil.move(
                f"{source_dir}/{filename}",
                f"{week_dir}/{filename}"
            )
```

---

### **Passo 5: Gerar Log**

```python
# Script: generate_log.py
def generate_log(year, images_dir):
    log_content = f"# Log de Geração — {year}º Ano\n\n"
    
    # Listar todas as imagens
    for week in sorted(os.listdir(f"{images_dir}/{year}-ano/")):
        week_dir = f"{images_dir}/{year}-ano/{week}/"
        
        for image_file in sorted(os.listdir(week_dir)):
            if image_file.endswith('_narrar.png'):
                lesson_num = image_file.split('_')[0]
                log_content += f"- [ ] {lesson_num} — {week}\n"
    
    # Salvar log
    with open(f"{images_dir}/{year}-ano/LOG.md", 'w') as f:
        f.write(log_content)
```

---

## Exemplos de Uso

### **Cenário 1: Gerar Todas as Imagens do Ano**

```bash
# Comando completo
/image-generator generate 3 \
  --output assets/imagens-narrar/3-ano/ \
  --platform pollinations \
  --width 1024 \
  --height 1024
```

**Processo:**
1. Extrai 120 prompts do arquivo
2. Otimiza cada prompt
3. Gera imagem via Pollinations
4. Salva na hierarquia correta
5. Gera LOG.md

**Tempo estimado:** 45-60 minutos

---

### **Cenário 2: Gerar Apenas Uma Semana**

```bash
# Gerar semana 5 do 3º ano
/image-generator generate-week 3 5
```

**Processo:**
1. Extrai apenas prompts da semana 5
2. Gera 3 imagens
3. Salva em `semana-5/`

**Tempo estimado:** 1-2 minutos

---

### **Cenário 3: Regenerar Imagem com Falha**

```bash
# Regenerar com seed diferente
/image-generator regenerate 1.1 3 --seed 123
```

**Processo:**
1. Lê prompt original
2. Gera nova imagem com seed 123
3. Substitui arquivo existente

---

### **Cenário 4: Verificar Status**

```bash
/image-generator status 3
```

**Saída:**
```
📊 Status — Ano 3

Total: 120
Geradas: 118 (98.3%)
Pendentes: 2
Falhas: 0

Por semana:
✅ 1-10: 100%
✅ 11-20: 100%
⏳ 21-30: 95%
⏳ 31-40: 97%
```

---

## Casos de Uso

### **1. Produção em Lote**

**Objetivo:** Gerar todas as imagens de um ano

**Comando:**
```bash
/image-generator generate 3
```

**Benefícios:**
- Automatizado
- Hierarquia automática
- Log completo

---

### **2. Correção de Qualidade**

**Objetivo:** Regenerar imagens com qualidade insatisfatória

**Comando:**
```bash
/image-generator regenerate 5.3 3 --seed 99
```

**Benefícios:**
- Seed customizada
- Mantém prompt original
- Rápido

---

### **3. Organização de Imagens Existentes**

**Objetivo:** Organizar imagens baixadas manualmente

**Comando:**
```bash
/image-generator organize downloads/
```

**Benefícios:**
- Estrutura consistente
- Renomeação automática
- Sem perda de dados

---

## FAQ

### **P: Qual plataforma é melhor?**
**R:** **Pollinations.ai** é a recomendada por ser gratuita, ilimitada e de alta qualidade. Use HuggingFace como backup.

---

### **P: Quanto tempo leva para gerar todas as imagens?**
**R:** Para 120 imagens (40 semanas × 3 aulas):
- Pollinations: ~45-60 minutos
- HuggingFace: ~30-40 minutos
- DeepAI: ~90-120 minutos

---

### **P: Posso usar minha própria API key?**
**R:** Sim! Configure:
```bash
export HUGGINGFACE_TOKEN=hf_xxx
export DEEPAI_API_KEY=xxx
```

---

### **P: E se a geração falhar?**
**R:** O agente:
1. Tenta 3x com seeds diferentes
2. Se falhar, tenta plataforma alternativa
3. Loga o erro e continua
4. Relatório final mostra falhas

---

### **P: Como faço para usar imagens no Rise 360?**
**R:** As imagens já estão no formato correto (PNG 1024x1024). Use no bloco `[+IMAGE_LABELED]`:
```markdown
[+IMAGE_LABELED]
@link_png@ assets/imagens-narrar/3-ano/semana-1/1.1_narrar.png
-- Hotspot 1
-- Hotspot 2
[-IMAGE_LABELED]
```

---

### **P: Posso gerar em outras resoluções?**
**R:** Sim! Use os parâmetros:
```bash
/image-generator generate 3 --width 2048 --height 2048
```

---

## Scripts Auxiliares

### **Localização:**
```
bef/agents/specialized/image-generator/scripts/
├── extract_prompts.py
├── generate_images.py
├── organize_images.py
├── generate_log.py
└── utils.py
```

### **Instalação:**
```bash
cd bef/agents/specialized/image-generator/
pip install -r requirements.txt
```

### **Requisitos:**
```txt
requests==2.31.0
Pillow==10.2.0
tqdm==4.66.1
```

---

## Links Úteis

- [Skill Definition](SKILL.md)
- [Narrating Template](../../templates/narrating.md)
- [Rise Blocks Reference](../../knowledge-base/rise-blocks-reference.md)
- [Pollinations.ai](https://pollinations.ai/)
- [HuggingFace](https://huggingface.co/)

---

**Gerado por:** Editorial Squad  
**Data:** 2026-04-01  
**Versão:** 1.0

---

> "A arte é a linguagem da fé — cada imagem conta uma história eterna."
