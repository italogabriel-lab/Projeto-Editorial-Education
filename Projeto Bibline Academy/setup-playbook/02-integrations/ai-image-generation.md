# 🎨 AI Image Generation APIs

## 🎯 Objetivo
Gerar ilustrações em aquarela clássica automaticamente a partir de prompts literários usando APIs gratuitas de IA generativa.

---

## 📋 Pré-requisitos
- [ ] Python 3.8+ instalado
- [ ] Prompts organizados em arquivo Markdown
- [ ] Estrutura de pastas para assets

---

## 🌐 APIs Suportadas

### Hierarquia de Fallback

```
1. Pollinations.ai (Primário - FREE, ilimitado)
        ↓ (falha ou qualidade ruim)
2. HuggingFace Inference API (Backup - FREE, 1000/day)
        ↓ (falha ou rate limit)
3. DeepAI (Terciário - FREE, 500/day)
```

---

## 🔧 Configuração das APIs

### 1. Pollinations.ai (Recomendado)

**Configuração:**
- **URL:** `https://image.pollinations.ai/prompt/{PROMPT}`
- **Método:** GET
- **Autenticação:** Nenhuma
- **Limites:** Ilimitado (gratuito)
- **Modelo:** Flux (automático)

**Parâmetros na URL:**
```
https://image.pollinations.ai/prompt/{PROMPT_URL_ENCODED}?width={width}&height={height}&seed={seed}&model=flux
```

| Parâmetro | Valor Padrão | Descrição |
|-----------|--------------|-----------|
| `width` | 1024 | Largura em pixels |
| `height` | 1024 | Altura em pixels |
| `seed` | random | Seed para reprodutibilidade |
| `model` | flux | Modelo de IA (flux, stable-diffusion) |

**Exemplo de Uso:**
```bash
curl -o "output.png" \
  "https://image.pollinations.ai/prompt/Ilustracao%20em%20aquarela%20crista?width=1024&height=1024&seed=1.1&model=flux"
```

---

### 2. HuggingFace Inference API

**Configuração:**
- **URL:** `https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0`
- **Método:** POST
- **Autenticação:** Bearer Token
- **Limites:** 1000 requisições/dia (gratuito)
- **Modelo:** Stable Diffusion XL

**Headers:**
```json
{
  "Authorization": "Bearer {HF_TOKEN}",
  "Content-Type": "application/json"
}
```

**Body:**
```json
{
  "inputs": "{PROMPT}",
  "parameters": {
    "width": 1024,
    "height": 1024,
    "num_inference_steps": 50,
    "guidance_scale": 7.5
  }
}
```

**Exemplo de Uso:**
```bash
curl -X POST \
  -H "Authorization: Bearer hf_xxxxxxxxxxxxxx" \
  -H "Content-Type: application/json" \
  -d '{"inputs": "Ilustracao em aquarela cristã", "parameters": {"width": 1024, "height": 1024}}' \
  "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0" \
  -o output.png
```

---

### 3. DeepAI

**Configuração:**
- **URL:** `https://api.deepai.org/api/text2img`
- **Método:** POST
- **Autenticação:** API Key header
- **Limites:** 500 requisições/dia (gratuito)

**Headers:**
```json
{
  "api-key": "{DEEPAI_API_KEY}"
}
```

**Body:**
```
text={PROMPT}
```

**Exemplo de Uso:**
```bash
curl -X POST \
  -H "api-key: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" \
  -d "text=Ilustracao em aquarela cristã" \
  https://api.deepai.org/api/text2img
```

---

## 📁 Estrutura de Arquivos

### Scripts do Image Generator

```
bef/agents/specialized/image-generator/
├── SKILL.md                          # Definição do agente
├── README.md                         # Documentação
├── scripts/
│   ├── main.py                       # CLI entry point
│   ├── generate_images.py            # Core generation
│   ├── extract_prompts.py            # Extrai prompts do Markdown
│   ├── organize_images.py            # Organiza na hierarquia
│   ├── generate_log.py               # Gera LOG.md
│   ├── test_api.py                   # Testa conectividade
│   └── generate_from_file.py         # Gera com aspect ratio
└── assets/
    └── imagens-narrar/
        ├── 1-ano/
        │   ├── semana-1/
        │   │   ├── 1.1_narrar.png
        │   │   └── 1.1_narrar_prompt.txt
        │   └── LOG.md
        └── 3-ano/
            └── ...
```

---

## 🔧 Passo a Passo

### Passo 1: Instalar Dependências

```bash
pip install requests pillow python-dotenv
```

### Passo 2: Configurar Environment (Opcional)

Crie `.env` na raiz do script:
```bash
# HuggingFace Token (opcional, para backup)
HUGGINGFACE_TOKEN=hf_xxxxxxxxxxxxxx

# DeepAI API Key (opcional, para terciário)
DEEPAI_API_KEY=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

### Passo 3: Organizar Prompts

Arquivo: `5 - Prompts-para-imagens-narrar-[ANO].md`

```markdown
# Prompts para Imagens - Narrar - 3º Ano

## Semana 1

### Aula 1.1 - Império Bizantino
Uma cena majestosa de Constantinopla com Santa Sofia ao fundo...

### Aula 1.2 - Constantinopla
Vista panorâmica da cidade murada de Constantinopla...
```

### Passo 4: Executar Geração

```bash
# Gerar todas as imagens do ano
cd bef/agents/specialized/image-generator
python scripts/main.py generate --year 3

# Gerar semana específica
python scripts/main.py generate-week --year 3 --week 1

# Gerar com aspect ratio personalizado
python scripts/generate_from_file.py --year 3 --week 1 --ratio 2:1

# Regenerar imagem específica
python scripts/main.py regenerate --lesson 1.1 --year 3

# Verificar status
python scripts/main.py status --year 3
```

---

## 🎨 Prompt Engineering

### Estrutura do Prompt Otimizado

```python
prompt_base = "[Descrição da cena em português]"

prompt_keywords = """
, watercolor painting, classical book illustration style,
white background with soft diffused edges, aged paper texture,
warm golden light, balanced color palette, detailed brushwork,
serene and contemplative atmosphere, Christian classical art
"""

prompt_final = prompt_base + prompt_keywords
```

### Palavras-Chave Recomendadas

| Categoria | Keywords |
|-----------|----------|
| **Técnica** | `watercolor painting`, `oil painting`, `fresco style` |
| **Estilo** | `classical book illustration`, `medieval manuscript`, `byzantine art` |
| **Fundo** | `white background`, `soft diffused edges`, `aged paper texture` |
| **Iluminação** | `warm golden light`, `divine light`, `chiaroscuro` |
| **Paleta** | `balanced color palette`, `earth tones`, `muted colors` |
| **Atmosfera** | `serene atmosphere`, `contemplative`, `reverent` |

### Exemplo de Prompt Completo

**Entrada (Português):**
```
Uma cena de Jesus ensinando no templo, com discípulos aos seus pés
```

**Saída (Inglês + Keywords):**
```
Jesus teaching in the temple with disciples at his feet, 
watercolor painting, classical book illustration style,
white background with soft diffused edges, aged paper texture,
warm golden light, balanced color palette, detailed brushwork,
serene and contemplative atmosphere, Christian classical art
```

---

## 📊 Aspect Ratios

### Ratios Suportados

| Ratio | Dimensões | Uso |
|-------|-----------|-----|
| `2:1` | 2048x1024 | **PADRÃO** - Panorâmico (Narrar) |
| `1:1` | 1024x1024 | Quadrado (Redes sociais) |
| `3:2` | 1536x1024 | Clássico (Fotografia) |
| `4:3` | 1365x1024 | Standard (Apresentações) |
| `16:9` | 1820x1024 | Widescreen (Vídeos) |

### Código para Parse de Ratio

```python
def parse_ratio(ratio_str):
    """Parse ratio string to dimensions"""
    width_ratio, height_ratio = map(int, ratio_str.split(':'))
    
    # Base dimension
    base = 1024
    
    # Calculate dimensions
    width = (width_ratio * base) // height_ratio
    height = base
    
    # Ensure divisible by 8 (model requirement)
    width = (width // 8) * 8
    height = (height // 8) * 8
    
    return width, height
```

---

## ✅ Validação

### Checklist de Qualidade

**Antes de Gerar:**
- [ ] Prompt extraído corretamente do Markdown
- [ ] Prompt otimizado (keywords em inglês adicionadas)
- [ ] URL encoded corretamente
- [ ] Parâmetros configurados (width, height, seed)

**Após Gerar:**
- [ ] Imagem salva no local correto
- [ ] Nome padronizado (`X.Y_narrar.png`)
- [ ] Prompt salvo em `.txt` separado
- [ ] Qualidade verificada (estilo coerente)
- [ ] LOG.md atualizado

### Testar API

```bash
# Testar Pollinations
python scripts/test_api.py pollinations

# Testar HuggingFace
python scripts/test_api.py huggingface

# Testar DeepAI
python scripts/test_api.py deepai
```

---

## 🔑 Variáveis de Ambiente

| Variável | Obrigatória | Descrição | Exemplo |
|----------|-------------|-----------|---------|
| `HUGGINGFACE_TOKEN` | Não (backup) | Token para HuggingFace API | `hf_xxxxx` |
| `DEEPAI_API_KEY` | Não (terciário) | API Key para DeepAI | `xxxx-xxxx-xxxx` |

---

## 📊 Hierarquia de Armazenamento

```
assets/
└── imagens-narrar/
    ├── 1-ano/
    │   ├── semana-1/
    │   │   ├── 1.1_narrar.png           # Imagem gerada
    │   │   ├── 1.1_narrar_prompt.txt    # Prompt usado
    │   │   ├── 1.2_narrar.png
    │   │   ├── 1.2_narrar_prompt.txt
    │   │   └── 1.3_narrar.png
    │   ├── semana-2/
    │   │   └── ...
    │   └── LOG.md                       # Log de produção
    ├── 2-ano/
    │   └── ...
    ├── 3-ano/
    │   └── ...
    ├── 4-ano/
    │   └── ...
    └── 5-ano/
        └── ...
```

### Nomenclatura de Arquivos

| Tipo | Padrão | Exemplo |
|------|--------|---------|
| **Imagem** | `[AULA].[NUMERO]_narrar.png` | `1.1_narrar.png` |
| **Prompt** | `[AULA].[NUMERO]_narrar_prompt.txt` | `1.1_narrar_prompt.txt` |
| **Pasta Ano** | `[N]-ano/` | `3-ano/` |
| **Pasta Semana** | `semana-[N]/` | `semana-1/` |

---

## 🐛 Troubleshooting

| Problema | Solução |
|----------|---------|
| Imagem não gera | Verifique conexão e URL da API |
| Qualidade ruim | Ajuste prompt, adicione mais keywords |
| Rate limit | Aguarde ou use API alternativa (fallback) |
| Seed não reproduz | Algumas APIs ignoram seed |
| Dimensões erradas | Verifique parse de ratio, deve ser múltiplo de 8 |
| Prompt em português não funciona | Traduza para inglês antes de enviar |

---

## 💡 Melhores Práticas

### Performance
- ✅ Use Pollinations como primário (sem rate limit)
- ✅ Implemente retry com backoff exponencial
- ✅ Cache de prompts e seeds para reprodutibilidade

### Qualidade
- ✅ Sempre adicione keywords de estilo em inglês
- ✅ Use seeds fixas para aulas específicas
- ✅ Valide aspecto ratio antes de gerar

### Organização
- ✅ Salve prompts em arquivos separados
- ✅ Gere LOG.md com status de cada aula
- ✅ Use hierarquia de pastas por ano/semana

---

## 📝 Exemplo de LOG.md

```markdown
# Log de Geração de Imagens — 3º Ano

## Status por Aula

| Aula | Título | Status | Plataforma | Arquivo |
|------|--------|--------|------------|---------|
| 1.1 | Império Bizantino | ✅ Gerada | Pollinations | 1.1_narrar.png |
| 1.2 | Constantinopla | ✅ Gerada | Pollinations | 1.2_narrar.png |
| 1.3 | Cristianismo | ⏳ Pendente | - | - |
| 2.1 | Arte Islâmica | ✅ Gerada | HuggingFace | 2.1_narrar.png |

## Estatísticas
- Total de aulas: 40
- Imagens geradas: 38
- Pendentes: 2
- Falhas: 0
- Pollinations: 35
- HuggingFace: 3
- DeepAI: 0
```

---

## 🔗 Links Úteis
- [Pollinations.ai Docs](https://pollinations.ai/docs)
- [HuggingFace Inference API](https://huggingface.co/docs/api-inference)
- [DeepAI API Docs](https://deepai.org/apis)
- [Flux Model](https://blackforestlabs.ai/announcing-black-forest-labs/)

---

## 📚 Scripts Disponíveis

### `main.py` (CLI Principal)
```bash
python scripts/main.py generate --year 3
python scripts/main.py generate-week --year 3 --week 1
python scripts/main.py regenerate --lesson 1.1 --year 3
python scripts/main.py status --year 3
```

### `generate_from_file.py` (Com Ratio)
```bash
python scripts/generate_from_file.py --year 3 --week 1 --ratio 2:1
```

### `extract_prompts.py` (Extrair Prompts)
```bash
python scripts/extract_prompts.py --input "5 - Prompts-para-imagens-narrar-3.md" --output prompts/
```

### `organize_images.py` (Organizar)
```bash
python scripts/organize_images.py --input generated/ --output assets/imagens-narrar/3-ano/
```

### `generate_log.py` (Gerar Log)
```bash
python scripts/generate_log.py --year 3 --output assets/imagens-narrar/3-ano/LOG.md
```

---

## 🔄 Fluxo Completo

```
1. EXTRAIR PROMPTS
   5 - Prompts-para-imagens-narrar-[ANO].md
           ↓ (extract_prompts.py)
   Lista de prompts em JSON
   
2. OTIMIZAR PROMPTS
   Prompt em português
           ↓ (translate + add keywords)
   Prompt em inglês + style keywords
   
3. GERAR IMAGEM
   Prompt otimizado
           ↓ (Pollinations API)
   Imagem PNG (1024x1024)
   
4. SALVAR
   Imagem PNG
           ↓ (organize_images.py)
   assets/imagens-narrar/[ANO]/semana-[N]/[X.Y]_narrar.png
   
5. LOGAR
   Status da geração
           ↓ (generate_log.py)
   LOG.md com tabela de status
```

---

**Última atualização:** 2026-04-02  
**Status:** ✅ Documentado e em Produção
