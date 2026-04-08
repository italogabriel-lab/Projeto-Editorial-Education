# 🎨 Image Generation Workflow

> **Fluxo Oficial de Geração de Imagens com IA**
>
> Este documento define o fluxo completo para geração automática de imagens usando IA no Projeto Editorial Education.

---

## 📋 Visão Geral

Este workflow cobre todo o processo de geração de imagens para aulas, desde a extração do prompt até a validação final da imagem gerada.

### **Agent Responsável**
- **Agente:** `image-generator` (bef/agents/skills/image-generator/)
- **Tipo:** Specialized Agent
- **Função:** Geração de imagens em aquarela clássica a partir de prompts literários

---

## 🗂️ Estrutura de Pastas

### **Documentação Centralizada**

Toda a documentação sobre geração de imagens está concentrada neste agente:

```
bef/agents/skills/image-generator/
├── SKILL.md                           # Definição da habilidade do agente
├── README.md                          # Documentação completa do agente
├── QUICKSTART.md                      # Guia de início rápido
├── IMAGE-GENERATION-WORKFLOW.md       # Este arquivo - fluxo de trabalho
└── requirements.txt                   # Dependências Python
```

### **Scripts Centralizados**

Todos os scripts de geração estão em:

```
bef/scripts/image-generation/
├── generate_image.py                  # Script principal (Gemini Nano Banana)
├── generate_image_temp.py             # Script temporário (Pollinations - FREE)
├── test_gemini_quick.py               # Teste rápido da API Gemini
├── diagnose_gemini_api.py             # Diagnóstico da API
└── list_models.py                     # Listar modelos disponíveis
```

### **Padrão de Organização de Imagens**

O padrão oficial está em:

```
[Nome do Ano]/
└── 2 - Imagens/
    ├── PADRAO_IMAGENS.md              # Padrão oficial de organização
    └── Semana [N]/
        └── Aula [N.N] - [Título]/
            └── [nomenclatura].png
```

**Exemplo (3º Ano):**
```
3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE/
└── 2 - Imagens/
    ├── PADRAO_IMAGENS.md
    └── Semana 14/
        └── Aula 14.2 - A beleza sem estátuas/
            └── 1-r-image-a.png
```

---

## 🔧 Configuração Inicial

### **1. Instalar Dependências**

```bash
cd /home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education
pip install -r bef/agents/skills/image-generator/requirements.txt
```

### **2. Configurar API Key**

**Opção A: Gemini (Nano Banana) - Recomendado**

1. Obter API Key em: https://aistudio.google.com/app/apikey
2. Adicionar em: `Projeto Bibline Academy/.env`
   ```env
   GEMINI_API_KEY=sua_chave_aqui
   ```
3. Ativar billing (se necessário): https://console.cloud.google.com/billing

**Opção B: Pollinations - Gratuito (Sem API Key)**

- Não requer configuração
- Use o script temporário diretamente

### **3. Verificar Configuração**

```bash
python bef/scripts/image-generation/diagnose_gemini_api.py
```

---

## 📝 Fluxo de Geração de Imagem

### **Fase 1: Preparação**

#### **Passo 1.1: Identificar Aula**

Determine:
- **Ano:** 1º, 2º, 3º, etc.
- **Semana:** 1-40
- **Aula:** N.N (ex: 14.2)
- **Título:** Nome completo da aula

#### **Passo 1.2: Extrair Prompt**

Localize o arquivo de prompts:
```
[Nome do Ano]/
└── 1-Estrutura Curricular - [N]º ANO/
    └── 5 - Prompts-para-imagens-narrar-[N]-ano.md
```

Extraia o prompt da aula específica.

#### **Passo 1.3: Verificar Estrutura de Destino**

```bash
# Navegue até a pasta do ano
cd "[Caminho]/3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE/"

# Verifique se pasta 2 - Imagens existe
ls "2 - Imagens/"

# Crie estrutura se necessário
mkdir -p "2 - Imagens/Semana 14/Aula 14.2 - A beleza sem estátuas/"
```

---

### **Fase 2: Geração**

#### **Opção A: Gemini (Nano Banana) - Recomendado**

```bash
python bef/scripts/image-generation/generate_image.py 14.2
```

**Configurações:**
- **Modelo:** `gemini-2.5-flash-image`
- **Ratio:** 2:1 (1792x896)
- **Formato:** PNG
- **Estilo:** Aquarela clássica

#### **Opção B: Pollinations - Temporário/Gratuito**

```bash
python bef/scripts/image-generation/generate_image_temp.py
```

**Configurações:**
- **Modelo:** Flux (Pollinations)
- **Ratio:** 2:1 (1792x896)
- **Formato:** PNG
- **API Key:** Não necessária

---

### **Fase 3: Validação**

#### **Passo 3.1: Verificar Arquivo Gerado**

```bash
ls -lh "2 - Imagens/Semana 14/Aula 14.2 - A beleza sem estátuas/1-r-image-a.png"
```

**Verificar:**
- ✅ Arquivo existe
- ✅ Tamanho razoável (>50KB)
- ✅ Formato PNG

#### **Passo 3.2: Verificar Nomenclatura**

Padrão obrigatório: `[numero]-[secao]-image-[letra].png`

Exemplos válidos:
- ✅ `1-r-image-a.png` (Aula 1, Narrar, primeira imagem)
- ✅ `14-r-image-a.png` (Aula 14, Narrar, primeira imagem)
- ✅ `1-r-image-b.png` (Aula 1, Narrar, segunda imagem)

#### **Passo 3.3: Verificar Qualidade**

Abra a imagem e verifique:
- ✅ Estilo aquarela clássica
- ✅ Fundo branco com bordas difusas
- ✅ Ratio 2:1 (horizontal)
- ✅ Qualidade visual adequada
- ✅ Conteúdo alinhado com prompt

---

## 🎯 Convenção de Nomenclatura

### **Formato Padrão**

```
[numero]-[secao]-image-[letra].png
```

### **Componentes**

| Parte | Significado | Exemplo |
|-------|-------------|---------|
| **`[numero]`** | Número da aula | `1`, `2`, `14` |
| **`[secao]`** | Seção do Rise | `r` = Narrar, `c` = Conceituar |
| **`image`** | Tipo de arquivo | `image` (fixo) |
| **`[letra]`** | Ordem da imagem | `a`, `b`, `c` |

### **Seções do Rise**

| Seção | Código | Uso |
|-------|--------|-----|
| **Narrar** | `r` | Imagens para blocos de narração |
| **Conceituar** | `c` | Imagens para blocos de conceitos |
| **Aplicar** | `a` | Imagens para blocos de aplicação |
| **Analisar** | `n` | Imagens para blocos de análise |

---

## 📊 APIs Disponíveis

### **Comparação**

| Recurso | Gemini (Nano Banana) | Pollinations |
|---------|---------------------|--------------|
| **Custo** | Free tier (500/dia) ou Pay-as-you-go | 100% FREE |
| **API Key** | Necessária | Não necessária |
| **Qualidade** | Excelente | Boa |
| **Controle de Estilo** | Avançado | Limitado |
| **Velocidade** | ~10-20s | ~30-60s |
| **Recomendado Para** | Produção | Testes/Temporário |

### **Configuração de APIs**

**Gemini:**
```env
# Projeto Bibline Academy/.env
GEMINI_API_KEY=AIzaSy...
GEMINI_MODEL=gemini-2.5-flash-image
IMAGE_FORMAT=png
IMAGE_RATIO=2:1
```

**Pollinations:**
- Sem configuração necessária
- URL: `https://image.pollinations.ai/prompt/{PROMPT}`

---

## ⚠️ Regras Obrigatórias

### **SEMPRE**

✅ Usar pasta `2 - Imagens` dentro do ano  
✅ Organizar por semana (`Semana [N]`)  
✅ Criar pasta da aula com título completo  
✅ Usar nomenclatura padrão (`1-r-image-a.png`)  
✅ Usar ratio 2:1  
✅ Salvar em formato PNG  
✅ Validar qualidade após geração  

### **NUNCA**

❌ Salvar imagens fora da pasta `2 - Imagens`  
❌ Usar nomenclatura diferente do padrão  
❌ Misturar imagens de anos diferentes  
❌ Usar outros formatos que não PNG  
❌ Usar ratio diferente de 2:1 (salvo exceção documentada)  

---

## 🔍 Troubleshooting

### **Erro: RESOURCE_EXHAUSTED (limit: 0)**

**Causa:** Free tier do Gemini está desativado (quota = 0)

**Solução:**
1. Ativar billing: https://console.cloud.google.com/billing
2. OU solicitar aumento de quota: https://console.cloud.google.com/apis/api/generativelanguage.googleapis.com/quotas
3. **Temporariamente:** Use Pollinations (`generate_image_temp.py`)

### **Erro: NOT_FOUND (model)**

**Causa:** Nome do modelo incorreto

**Solução:**
- Modelo correto: `gemini-2.5-flash-image`
- Verificar com: `python bef/scripts/image-generation/list_models.py`

### **Erro: API key not found**

**Causa:** GEMINI_API_KEY não configurada

**Solução:**
1. Adicionar em `Projeto Bibline Academy/.env`:
   ```env
   GEMINI_API_KEY=sua_chave_aqui
   ```
2. Ou exportar temporariamente:
   ```bash
   export GEMINI_API_KEY=sua_chave_aqui
   ```

### **Imagem não aparece**

**Verificar:**
1. Internet está ativa?
2. API key é válida?
3. Quota disponível?
4. Pasta de destino existe?

---

## 📚 Documentação Relacionada

### **Neste Agente**

| Arquivo | Propósito |
|---------|-----------|
| `SKILL.md` | Definição da habilidade do agente |
| `README.md` | Documentação completa do agente |
| `QUICKSTART.md` | Guia de início rápido |
| `IMAGE-GENERATION-WORKFLOW.md` | Este arquivo - fluxo de trabalho |

### **Scripts**

| Arquivo | Propósito |
|---------|-----------|
| `bef/scripts/image-generation/generate_image.py` | Script principal (Gemini) |
| `bef/scripts/image-generation/generate_image_temp.py` | Script temporário (Pollinations) |
| `bef/scripts/image-generation/test_gemini_quick.py` | Teste rápido |
| `bef/scripts/image-generation/diagnose_gemini_api.py` | Diagnóstico |
| `bef/scripts/image-generation/list_models.py` | Listar modelos |

### **Padrões**

| Arquivo | Localização |
|---------|-------------|
| `PADRAO_IMAGENS.md` | `[Ano]/2 - Imagens/PADRAO_IMAGENS.md` |

### **Integrações**

| Arquivo | Localização |
|---------|-------------|
| `ai-image-generation.md` | `Projeto Bibline Academy/setup-playbook/02-integrations/` |

---

## ✅ Checklist de Geração

### **Antes de Gerar**

- [ ] Verificar se pasta `2 - Imagens` existe no ano
- [ ] Confirmar semana e número da aula
- [ ] Verificar título correto da aula
- [ ] Extrair prompt do arquivo de prompts
- [ ] Definir qual API usar (Gemini ou Pollinations)
- [ ] Verificar configuração da API (se Gemini)

### **Durante Geração**

- [ ] Prompt revisado e otimizado
- [ ] Ratio configurado (2:1 padrão)
- [ ] Nomenclatura correta definida
- [ ] Script executado com sucesso

### **Após Geração**

- [ ] Imagem salva na pasta correta
- [ ] Nome do arquivo segue convenção
- [ ] Qualidade da imagem verificada
- [ ] Ratio 2:1 confirmado
- [ ] Formato PNG confirmado

---

## 🔄 Fluxo Completo (Resumo Visual)

```
1. IDENTIFICAR
   ├── Ano: 3º Ano
   ├── Semana: 14
   ├── Aula: 14.2
   └── Título: A beleza sem estátuas

2. EXTRAIR
   └── Prompt do arquivo de prompts

3. PREPARAR
   ├── Criar pasta: 2 - Imagens/Semana 14/Aula 14.2 - [Título]/
   └── Configurar script

4. GERAR
   ├── Gemini: python bef/scripts/image-generation/generate_image.py
   └── Pollinations: python bef/scripts/image-generation/generate_image_temp.py

5. VALIDAR
   ├── Arquivo existe?
   ├── Nomenclatura correta?
   ├── Qualidade adequada?
   └── Ratio 2:1?

6. FINALIZAR
   └── ✅ Imagem pronta para uso nas aulas
```

---

## 📝 Histórico de Atualizações

| Data | Versão | Mudança | Responsável |
|------|--------|---------|-------------|
| 2026-04-06 | 1.0 | Criação do workflow centralizado | Editorial Squad |

---

**Versão:** 1.0  
**Última atualização:** 2026-04-06  
**Status:** ✅ Workflow Oficial
