# 🎨 Image Generator — Guia de Uso com Ratio 2:1

**Como gerar imagens no formato panorâmico (2048x1024) usando os prompts reais do arquivo**

---

## 📐 Ratio 2:1 (PADRÃO)

### **Por que 2:1?**

O formato **2:1 (2048x1024)** é ideal para:
- ✅ **Rise 360** — Blocos de imagem panorâmicos
- ✅ **Apresentações** — Formato widescreen
- ✅ **Web** — Layouts modernos
- ✅ **Impressão** — Alta qualidade

### **Dimensões**

| Ratio | Largura | Altura | Uso |
|-------|---------|--------|-----|
| **2:1** | **2048px** | **1024px** | **PADRÃO** ✅ |
| 1:1 | 1024px | 1024px | Quadrado |
| 3:2 | 1536px | 1024px | Clássico |
| 4:3 | 1365px | 1024px | Standard |
| 16:9 | 1820px | 1024px | Widescreen |

---

## 🚀 COMANDOS DE USO

### **1. Gerar Semana Específica (Ratio 2:1)**

```bash
cd bef/agents/skills/image-generator/

python scripts/generate_from_file.py \
  --prompts-file "/caminho/5 - Prompts-para-imagens-narrar-3-ano .md" \
  --year 3 \
  --week 1 \
  --ratio 2:1 \
  --output imagens_semana1/
```

**Resultado:**
```
📐 Ratio: 2:1 (2048x1024)
✅ 3 prompts encontrados
✅ Semana 1
   ✅ 1.1_narrar.png (108 KB)
   ✅ 1.2_narrar.png (115 KB)
   ✅ 1.3_narrar.png (88 KB)
```

---

### **2. Gerar Todas as Semanas de Uma Vez**

```bash
python scripts/generate_from_file.py \
  --prompts-file "/caminho/5 - Prompts-para-imagens-narrar-3-ano .md" \
  --year 3 \
  --ratio 2:1 \
  --output imagens_ano3_completo/
```

**Tempo estimado:** 60-90 minutos (120 imagens)

---

### **3. Gerar com Ratio Diferente**

```bash
# Quadrado (1:1)
python scripts/generate_from_file.py \
  --ratio 1:1 \
  --output imagens_quadradas/

# Widescreen (16:9)
python scripts/generate_from_file.py \
  --ratio 16:9 \
  --output imagens_widescreen/
```

---

## 📁 ESTRUTURA DE SAÍDA

```
imagens_ano3/
└── semana-1/
    ├── 1.1_narrar.png           # 2048x1024 (108 KB)
    ├── 1.1_narrar_prompt.txt    # Prompt completo
    ├── 1.2_narrar.png           # 2048x1024 (115 KB)
    ├── 1.2_narrar_prompt.txt    # Prompt completo
    ├── 1.3_narrar.png           # 2048x1024 (88 KB)
    └── 1.3_narrar_prompt.txt    # Prompt completo
```

---

## 🎨 EXEMPLO DE PROMPT (Reais do Arquivo)

### **Aula 1.1 — Império Romano do oriente e arte bizantina**

**Prompt Extraído:**
```
Ilustração em aquarela detalhada, estilo livro ilustrado clássico, com fundo 
totalmente branco e bordas laterais difusas e suavemente desbotadas, criando 
aparência de página ilustrada antiga.
Textura real de papel aquarelado, pinceladas suaves e luz quente e dourada.
Paleta em tons equilibrados — dourado luminoso, marfim, azul profundo, vermelho 
suave, ocre claro e sombras delicadas.

Cena inspirada no trecho:
"Dois filhos nasceram da mesma mãe Roma. Um adormeceu na noite dos bárbaros, 
o outro despertou ao sol de Cristo..."

Composição da cena:
• Cenário coerente com o período histórico e o contexto artístico descrito
• Figuras humanas em atividade relacionada ao tema, com expressões serenas e devotas
• Detalhes arquitetônicos ou artísticos mencionados no texto
• Objetos e materiais relevantes ao contexto da cena

Iluminação:
• Luz quente entrando lateralmente, suave e dourada
• Sombras delicadas e ambiente contemplativo
• Sensação de tempo lento e silêncio profundo
```

**URL de Geração:**
```
https://image.pollinations.ai/prompt/{PROMPT_URL_ENCODED}?width=2048&height=1024&seed=11&model=flux
```

---

## ⚙️ VARIÁVEL DE RATIO NO CÓDIGO

### **Função `parse_ratio()`**

```python
RATIO_PRESETS = {
    '1:1': (1024, 1024),      # Quadrado
    '2:1': (2048, 1024),      # Panorâmico (PADRÃO)
    '3:2': (1536, 1024),      # Clássico
    '4:3': (1365, 1024),      # Standard
    '16:9': (1820, 1024),     # Widescreen
}

def parse_ratio(ratio_str):
    """
    Parse ratio string (e.g., '2:1') and return (width, height)
    """
    if ratio_str in RATIO_PRESETS:
        return RATIO_PRESETS[ratio_str]
    
    # Parse custom ratio
    parts = ratio_str.split(':')
    w_ratio = int(parts[0])
    h_ratio = int(parts[1])
    
    height = 1024
    width = int((w_ratio / h_ratio) * height)
    width = (width // 64) * 64  # Round to multiple of 64
    
    return (width, height)
```

### **Uso na API**

```python
width, height = parse_ratio('2:1')  # (2048, 1024)

url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width={width}&height={height}&seed={seed}&model=flux&nologo=true"
```

---

## 📊 RESULTADOS DE TESTE (Semana 1)

| Aula | Título | Arquivo | Tamanho | Ratio | Status |
|------|--------|---------|---------|-------|--------|
| 1.1 | Império Bizantino | `1.1_narrar.png` | 108 KB | 2:1 | ✅ |
| 1.2 | Constantinopla | `1.2_narrar.png` | 115 KB | 2:1 | ✅ |
| 1.3 | Cristianismo | `1.3_narrar.png` | 88 KB | 2:1 | ✅ |

**Total:** 311 KB (Semana 1 completa)  
**Resolução:** 2048x1024 pixels  
**Formato:** PNG

---

## 🔗 LINKS DO ARQUIVO DE PROMPTS

### **Caminho do Arquivo**

```
/Projeto Bibline Academy/Belas Artes - Fase da Gramática/
  1 Fase - Gramática/
    3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE/
      Estrutura Curricular - 3º ANO/
        5 - Prompts-para-imagens-narrar-3-ano .md
```

### **Estrutura do Arquivo**

```markdown
# Prompts para Imagens — Narrar (3º Ano)

## Semana 1

### Aula 1.1 — Império Romano do oriente e arte bizantina

**Prompt:**
```
[conteúdo do prompt]
```

### Aula 1.2 — Constantinopla como centro

**Prompt:**
```
[conteúdo do prompt]
```
```

---

## 📝 COMANDOS RÁPIDOS

### **Teste Rápido (1 imagem)**

```bash
python scripts/generate_from_file.py \
  --prompts-file "/caminho/5 - Prompts-para-imagens-narrar-3-ano .md" \
  --week 1 \
  --ratio 2:1 \
  --output teste/
```

### **Produção Completa (Ano 3)**

```bash
mkdir -p assets/imagens-narrar/3-ano/

python scripts/generate_from_file.py \
  --prompts-file "/caminho/5 - Prompts-para-imagens-narrar-3-ano .md" \
  --year 3 \
  --ratio 2:1 \
  --output assets/imagens-narrar/3-ano/
```

---

## ✅ CHECKLIST DE GERAÇÃO

### **Antes de Gerar**

- [ ] Arquivo de prompts localizado
- [ ] Dependências instaladas (`pip install -r requirements.txt`)
- [ ] Ratio definido (padrão: 2:1)
- [ ] Diretório de saída criado

### **Após Gerar**

- [ ] Todas as imagens geradas
- [ ] Prompts salvos em .txt
- [ ] Estrutura de pastas correta
- [ ] Qualidade validada (abrir algumas imagens)
- [ ] LOG.md gerado

---

## 🎯 DICAS DE USO

### **1. Use Ratio 2:1 para Rise 360**

O formato 2048x1024 é ideal para blocos de imagem do Rise.

### **2. Mantenha Prompts Originais**

Sempre use os prompts reais do arquivo — eles já estão otimizados.

### **3. Valide Qualidade**

Abra algumas imagens aleatórias para validar:
- Resolução (2048x1024)
- Estilo (aquarela clássica)
- Qualidade (sem artefatos)

### **4. Faça Backup**

```bash
# Após gerar tudo
cp -r assets/imagens-narrar/3-ano/ backup/imagens-narrar-3-ano-2048x1024/
```

---

## 📞 SUPORTE

### **Problemas Comuns**

**❌ "Nenhum prompt encontrado"**
- Verificar se arquivo está no formato correto
- Verificar encoding (UTF-8)
- Usar caminho completo do arquivo

**❌ "Imagem muito pequena"**
- Verificar conexão com API
- Tentar seed diferente
- Aguardar e tentar novamente

**❌ "Ratio inválido"**
- Usar formatos: 1:1, 2:1, 3:2, 4:3, 16:9
- Ou especificar manualmente: `--ratio 2:1`

---

## 🔗 DOCUMENTAÇÃO COMPLETA

- [SKILL.md](SKILL.md) — Definição do agente
- [README.md](README.md) — Documentação completa
- [QUICKSTART.md](QUICKSTART.md) — Guia rápido
- [FINAL_REPORT.md](FINAL_REPORT.md) — Relatório de testes

---

**Versão:** 2.0.0  
**Data:** 2026-04-01  
**Status:** ✅ **PRODUCTION READY**  
**Ratio Padrão:** 2:1 (2048x1024)

---

> "A arte é a linguagem da fé — agora em formato panorâmico!"
