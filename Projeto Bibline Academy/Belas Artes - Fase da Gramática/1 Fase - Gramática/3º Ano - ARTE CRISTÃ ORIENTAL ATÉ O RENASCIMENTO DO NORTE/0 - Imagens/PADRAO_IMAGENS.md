# 📁 Padrão de Organização de Imagens

> **Padrão Oficial para Organização de Imagens Geradas por IA**
>
> Este documento define a estrutura de pastas e nomenclatura para todas as imagens geradas automaticamente no Projeto Editorial Education.

---

## 🎯 Estrutura de Pastas

### **Localização Padrão**

Todas as imagens devem ser armazenadas dentro da pasta **`2 - Imagens`** de cada ano:

```
[Nome do Ano]/
└── 2 - Imagens/
    └── Semana [N]/
        └── Aula [N.N] - [Título da Aula]/
            └── [nomenclatura].png
```

### **Exemplo Prático - 3º Ano**

```
3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE/
├── 1-Estrutura Curricular - 3º ANO/
├── 2 - Imagens/
│   ├── Semana 1/
│   │   ├── Aula 1.1 - Império Romano do oriente e arte bizantina/
│   │   │   └── 1-r-image-a.png
│   │   ├── Aula 1.2 - Constantinopla como centro/
│   │   │   └── 1-r-image-a.png
│   │   └── Aula 1.3 - Cristianismo e transformação da arte pública/
│   │       └── 1-r-image-a.png
│   ├── Semana 2/
│   │   ├── Aula 2.1 - Cristo como centro da arte/
│   │   │   └── 1-r-image-a.png
│   │   └── ...
│   ├── Semana 14/
│   │   └── Aula 14.2 - A beleza sem estátuas/
│   │       └── 1-r-image-a.png
│   └── Semana 15/
│       └── ...
├── 1.1.md
├── 1.2.md
└── ...
```

---

## 📝 Convenção de Nomenclatura

### **Formato Padrão**

```
[numero]-[secao]-image-[letra].png
```

### **Componentes**

| Parte | Significado | Exemplo |
|-------|-------------|---------|
| **`[numero]`** | Número da aula | `1`, `2`, `14` |
| **`[secao]`** | Seção do Rise | `r` = Narrar |
| **`image`** | Tipo de arquivo | `image` (fixo) |
| **`[letra]`** | Ordem da imagem | `a`, `b`, `c` |

### **Exemplos**

| Nomenclatura | Significado |
|--------------|-------------|
| `1-r-image-a.png` | Aula 1, seção Narrar, primeira imagem |
| `1-r-image-b.png` | Aula 1, seção Narrar, segunda imagem |
| `14-r-image-a.png` | Aula 14, seção Narrar, primeira imagem |
| `2-c-image-a.png` | Aula 2, seção Conceituar, primeira imagem |

---

## 🗂️ Seções do Rise (Código de Seção)

| Seção | Código | Uso |
|-------|--------|-----|
| **Narrar** | `r` | Imagens para blocos de narração |
| **Conceituar** | `c` | Imagens para blocos de conceitos |
| **Aplicar** | `a` | Imagens para blocos de aplicação |
| **Analisar** | `n` | Imagens para blocos de análise |

---

## 📂 Estrutura por Ano

### **3º Ano - Arte Cristã Oriental até o Renascimento do Norte**

```
3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE/
└── 2 - Imagens/
    ├── Semana 1/
    ├── Semana 2/
    ├── Semana 3/
    ├── Semana 4/
    ├── Semana 5/
    ├── Semana 6/
    ├── Semana 7/
    ├── Semana 8/
    ├── Semana 11/
    ├── Semana 12/
    ├── Semana 13/
    ├── Semana 14/
    ├── Semana 15/
    ├── Semana 16/
    ├── Semana 17/
    ├── Semana 18/
    ├── Semana 21/
    ├── Semana 22/
    ├── Semana 23/
    ├── Semana 24/
    ├── Semana 25/
    ├── Semana 26/
    ├── Semana 27/
    ├── Semana 28/
    ├── Semana 31/
    ├── Semana 32/
    ├── Semana 33/
    ├── Semana 34/
    ├── Semana 35/
    ├── Semana 36/
    ├── Semana 37/
    └── Semana 38/
```

### **2º Ano - Da Criação até a Arte Bizantina**

```
2º Ano - DA CRIAÇÃO ATÉ A ARTE BIZANTINA/
└── 2 - Imagens/
    ├── Semana 1/
    ├── Semana 2/
    └── ...
```

### **1º Ano**

```
1º Ano - [NOME]/
└── 2 - Imagens/
    ├── Semana 1/
    ├── Semana 2/
    └── ...
```

---

## 🔧 Scripts de Geração

### **Script Principal (Gemini Nano Banana)**

```bash
python generate_image.py
```

**Configuração:**
- API: Google Gemini (Nano Banana)
- Modelo: `gemini-2.5-flash-image`
- Ratio: 2:1 (1792x896)
- Formato: PNG

### **Script Temporário (Pollinations - FREE)**

```bash
python generate_image_temp.py
```

**Configuração:**
- API: Pollinations.ai
- Modelo: Flux
- Ratio: 2:1 (1792x896)
- Formato: PNG
- **Sem necessidade de API Key**

---

## 📋 Checklist de Geração

### **Antes de Gerar**

- [ ] Verificar se a pasta `2 - Imagens` existe no ano
- [ ] Confirmar a semana e número da aula
- [ ] Verificar o título correto da aula
- [ ] Definir qual API usar (Gemini ou Pollinations)

### **Durante a Geração**

- [ ] Prompt revisado e otimizado
- [ ] Ratio configurado (2:1 padrão)
- [ ] Nomenclatura correta (`1-r-image-a.png`)

### **Após a Geração**

- [ ] Imagem salva na pasta correta: `2 - Imagens/Semana [N]/Aula [N.N] - [Título]/`
- [ ] Nome do arquivo segue convenção
- [ ] Qualidade da imagem verificada
- [ ] Ratio 2:1 confirmado

---

## 🎨 Especificações Técnicas das Imagens

### **Padrão Gemini (Nano Banana)**

| Propriedade | Valor |
|-------------|-------|
| **Modelo** | `gemini-2.5-flash-image` |
| **Ratio** | 2:1 |
| **Resolução** | ~1792x896 |
| **Formato** | PNG |
| **Estilo** | Aquarela clássica |
| **Fundo** | Branco com bordas difusas |

### **Padrão Pollinations (Temporário)**

| Propriedade | Valor |
|-------------|-------|
| **Modelo** | Flux |
| **Ratio** | 2:1 |
| **Resolução** | 1792x896 |
| **Formato** | PNG |
| **Estilo** | Aquarela clássica |
| **Fundo** | Branco |

---

## 📖 Exemplo Completo de Uso

### **Gerar imagem da Aula 14.2**

**1. Verificar estrutura:**
```bash
ls "3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE/2 - Imagens/"
```

**2. Executar script:**
```bash
python generate_image.py 14.2
```

**3. Resultado esperado:**
```
3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE/
└── 2 - Imagens/
    └── Semana 14/
        └── Aula 14.2 - A beleza sem estátuas/
            └── 1-r-image-a.png ✅
```

---

## 🔄 Fluxo de Trabalho

### **Passo 1: Preparar**
```
1. Identificar o ano (1º, 2º, 3º)
2. Identificar a semana (1-40)
3. Identificar a aula (N.N)
4. Extrair prompt do arquivo de prompts
```

### **Passo 2: Configurar**
```
1. Criar pasta: 2 - Imagens/Semana [N]/Aula [N.N] - [Título]/
2. Configurar script com prompt
3. Verificar nomenclatura: [N]-r-image-[letra].png
```

### **Passo 3: Gerar**
```
1. Executar script
2. Aguardar geração (~30-60s)
3. Verificar qualidade
```

### **Passo 4: Validar**
```
1. Confirmar local correto
2. Confirmar nomenclatura
3. Confirmar ratio 2:1
4. Confirmar formato PNG
```

---

## ⚠️ Regras Importantes

### **OBRIGATÓRIO**

✅ **SEMPRE** usar pasta `2 - Imagens` dentro do ano  
✅ **SEMPRE** organizar por semana (`Semana [N]`)  
✅ **SEMPRE** criar pasta da aula com título (`Aula [N.N] - [Título]`)  
✅ **SEMPRE** usar nomenclatura padrão (`1-r-image-a.png`)  
✅ **SEMPRE** usar ratio 2:1  
✅ **SEMPRE** salvar em formato PNG  

### **NUNCA**

❌ Salvar imagens fora da pasta `2 - Imagens`  
❌ Usar nomenclatura diferente do padrão  
❌ Misturar imagens de anos diferentes  
❌ Usar outros formatos que não PNG  
❌ Usar ratio diferente de 2:1 (salvo exceção documentada)  

---

## 📊 Organização de Pastas do Ano

### **Estrutura Completa**

```
[Nome do Ano]/
├── 1-Estrutura Curricular - [N]º ANO/
│   └── Prompts e materiais curriculares
├── 2 - Imagens/
│   └── Todas as imagens geradas por IA
│       └── Semana [N]/
│           └── Aula [N.N] - [Título]/
│               └── [nomenclatura].png
├── 3-Assets/
│   └── Outros assets (vídeos, áudios, etc.)
├── [N.N].md
│   └── Arquivos das aulas
└── README.md
    └── Documentação específica do ano
```

---

## 🔗 Referências

| Arquivo | Propósito |
|---------|-----------|
| `PADRAO_IMAGENS.md` | Este arquivo - padrão geral |
| `generate_image.py` | Script Gemini (Nano Banana) |
| `generate_image_temp.py` | Script Pollinations (FREE) |
| `GEMINI_IMAGE_GENERATION.md` | Documentação técnica do Gemini |
| `GEMINI_SETUP_SUMMARY.md` | Resumo de configuração |

---

## 📝 Histórico de Atualizações

| Data | Versão | Mudança | Responsável |
|------|--------|---------|-------------|
| 2026-04-06 | 1.0 | Criação do padrão de organização | Editorial Squad |

---

## ✅ Checklist de Validação

Antes de commitar imagens, verifique:

### **Estrutura**
- [ ] Pasta `2 - Imagens` existe no ano correto
- [ ] Pasta `Semana [N]` criada corretamente
- [ ] Pasta `Aula [N.N] - [Título]` com nome completo
- [ ] Caminho completo segue o padrão

### **Nomenclatura**
- [ ] Arquivo nomeado como `[N]-r-image-[letra].png`
- [ ] Número da aula correto
- [ ] Seção correta (r = Narrar)
- [ ] Letra sequencial (a, b, c...)

### **Qualidade**
- [ ] Imagem em formato PNG
- [ ] Ratio 2:1 (1792x896)
- [ ] Qualidade visual adequada
- [ ] Estilo aquarela clássico

---

**Versão:** 1.0  
**Última atualização:** 2026-04-06  
**Status:** ✅ Padrão Oficial
