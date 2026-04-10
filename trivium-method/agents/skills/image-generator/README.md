# 🎨 Image Generator Agent

> **Agente Especializado em Geração de Imagens com IA**
>
> Geração automática de ilustrações em aquarela clássica para aulas do Projeto Editorial Education.

---

## 📋 Visão Geral

Este agente é responsável por gerar imagens ilustrativas em estilo aquarela clássica para as aulas do projeto, utilizando IA generativa (Gemini Nano Banana ou Pollinations).

### **Responsabilidades**

- ✅ Gerar imagens em estilo aquarela clássica
- ✅ Seguir padrão de nomenclatura oficial
- ✅ Organizar imagens na estrutura correta
- ✅ Manter ratio 2:1 (horizontal)
- ✅ Validar qualidade das imagens geradas

---

## 📁 Estrutura do Agente

```
trivium-method/agents/skills/image-generator/
├── SKILL.md                           # Definição da habilidade e persona
├── README.md                          # Este arquivo - documentação principal
├── QUICKSTART.md                      # Guia de início rápido (5 minutos)
├── IMAGE-GENERATION-WORKFLOW.md       # Fluxo de trabalho completo
└── requirements.txt                   # Dependências Python
```

### **Scripts Relacionados**

Todos os scripts estão centralizados em:

```
trivium-method/scripts/image-generation/
├── generate_image.py                  # Script principal (Gemini)
├── generate_image_temp.py             # Script temporário (Pollinations)
├── test_gemini_quick.py               # Teste rápido da API
├── diagnose_gemini_api.py             # Diagnóstico da API
└── list_models.py                     # Listar modelos disponíveis
```

---

## 🚀 Início Rápido

### **1. Instalar Dependências**

```bash
pip install -r trivium-method/agents/skills/image-generator/requirements.txt
```

### **2. Gerar Imagem (Pollinations - Sem API Key)**

```bash
python trivium-method/scripts/image-generation/generate_image_temp.py
```

### **3. Gerar Imagem (Gemini - Com API Key)**

```bash
# Configurar API Key em Projeto Bibline Academy/.env
python trivium-method/scripts/image-generation/generate_image.py 14.2
```

---

## 📊 APIs Suportadas

### **Hierarquia de Fallback**

```
1. Gemini (Nano Banana) - Recomendado
   ├── Modelo: gemini-2.5-flash-image
   ├── Qualidade: Excelente
   ├── Custo: Free tier (500/dia) ou Pay-as-you-go
   └── API Key: Necessária (GEMINI_API_KEY)
   
2. Pollinations.ai - Temporário/Backup
   ├── Modelo: Flux
   ├── Qualidade: Boa
   ├── Custo: 100% FREE
   └── API Key: Não necessária
```

---

## 🗂️ Estrutura de Destino das Imagens

Todas as imagens são salvas na pasta `2 - Imagens` de cada ano:

```
[Nome do Ano]/
└── 2 - Imagens/
    ├── PADRAO_IMAGENS.md              # Padrão oficial
    └── Semana [N]/
        └── Aula [N.N] - [Título]/
            └── [numero]-r-image-[letra].png
```

**Exemplo:**
```
3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE/
└── 2 - Imagens/
    └── Semana 14/
        └── Aula 14.2 - A beleza sem estátuas/
            └── 1-r-image-a.png
```

---

## 📝 Convenção de Nomenclatura

### **Formato**

```
[numero]-[secao]-image-[letra].png
```

### **Exemplos**

| Arquivo | Significado |
|---------|-------------|
| `1-r-image-a.png` | Aula 1, Narrar, primeira imagem |
| `1-r-image-b.png` | Aula 1, Narrar, segunda imagem |
| `14-r-image-a.png` | Aula 14, Narrar, primeira imagem |

### **Seções do Rise**

| Seção | Código |
|-------|--------|
| Narrar | `r` |
| Conceituar | `c` |
| Aplicar | `a` |
| Analisar | `n` |

---

## 🔧 Configuração

### **Gemini (Nano Banana)**

**1. Obter API Key**
- Acesse: https://aistudio.google.com/app/apikey
- Crie uma nova API key
- Copie a chave

**2. Configurar .env**
```env
# Projeto Bibline Academy/.env
GEMINI_API_KEY=sua_chave_aqui
GEMINI_MODEL=gemini-2.5-flash-image
IMAGE_FORMAT=png
IMAGE_RATIO=2:1
```

**3. Ativar Billing (Se Necessário)**
- https://console.cloud.google.com/billing
- Sem custo mínimo, paga apenas pelo uso excedente

**4. Testar**
```bash
python trivium-method/scripts/image-generation/test_gemini_quick.py
```

### **Pollinations (Sem Configuração)**

- Não requer API key
- Não requer configuração
- Use diretamente: `python trivium-method/scripts/image-generation/generate_image_temp.py`

---

## 📖 Documentação Completa

### **Neste Diretório**

| Arquivo | Quando Usar |
|---------|-------------|
| `SKILL.md` | Entender a persona e habilidades do agente |
| `README.md` | Este arquivo - visão geral e referência rápida |
| `QUICKSTART.md` | Primeiros passos (5 minutos) |
| `IMAGE-GENERATION-WORKFLOW.md` | Fluxo de trabalho completo e detalhado |

### **Scripts**

| Script | Quando Usar |
|--------|-------------|
| `generate_image.py` | Geração principal com Gemini |
| `generate_image_temp.py` | Geração com Pollinations (sem API key) |
| `test_gemini_quick.py` | Testar se API Gemini está funcionando |
| `diagnose_gemini_api.py` | Diagnosticar problemas com API |
| `list_models.py` | Ver modelos disponíveis |

### **Padrões**

| Arquivo | Localização |
|---------|-------------|
| `PADRAO_IMAGENS.md` | `[Ano]/2 - Imagens/PADRAO_IMAGENS.md` |

---

## ⚠️ Regras Importantes

### **OBRIGATÓRIO**

✅ **SEMPRE** usar pasta `2 - Imagens`  
✅ **SEMPRE** organizar por semana  
✅ **SEMPRE** usar nomenclatura padrão  
✅ **SEMPRE** usar ratio 2:1  
✅ **SEMPRE** salvar em PNG  

### **PROIBIDO**

❌ Salvar fora de `2 - Imagens`  
❌ Nomenclatura diferente  
❌ Outros formatos que não PNG  
❌ Ratio diferente de 2:1  

---

## 🔍 Troubleshooting

### **Problemas Comuns**

| Problema | Solução |
|----------|---------|
| `RESOURCE_EXHAUSTED` | Ativar billing ou usar Pollinations |
| `API key not found` | Configurar em `Projeto Bibline Academy/.env` |
| `NOT_FOUND (model)` | Usar modelo: `gemini-2.5-flash-image` |
| Imagem não aparece | Verificar internet e quota |

### **Diagnóstico Completo**

```bash
python trivium-method/scripts/image-generation/diagnose_gemini_api.py
```

---

## 📚 Referências Externas

| Recurso | URL |
|---------|-----|
| Google AI Studio | https://aistudio.google.com |
| Gemini API Docs | https://ai.google.dev/gemini-api/docs |
| Google Cloud Billing | https://console.cloud.google.com/billing |
| Pollinations.ai | https://pollinations.ai |

---

## 📝 Histórico

| Data | Versão | Mudança |
|------|--------|---------|
| 2026-04-06 | 1.0 | Criação do agente centralizado |

---

**Versão:** 1.0  
**Última atualização:** 2026-04-06  
**Status:** ✅ Agente Oficial
