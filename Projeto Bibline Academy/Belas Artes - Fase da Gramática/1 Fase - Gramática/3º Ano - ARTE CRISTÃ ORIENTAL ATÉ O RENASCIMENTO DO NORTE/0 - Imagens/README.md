# 📁 2 - Imagens

> **Repositório Central de Imagens Geradas por IA**
>
> Esta pasta contém todas as imagens ilustrativas geradas automaticamente para as aulas deste ano.

---

## 📋 Padrão de Organização

### **Estrutura**

```
2 - Imagens/
├── README.md                        # Este arquivo
├── PADRAO_IMAGENS.md                # Padrão oficial de organização
└── Semana [N]/
    └── Aula [N.N] - [Título]/
        └── [numero]-r-image-[letra].png
```

### **Nomenclatura**

Formato: `[numero]-[secao]-image-[letra].png`

**Exemplos:**
- `1-r-image-a.png` → Aula 1, Narrar, primeira imagem
- `14-r-image-a.png` → Aula 14, Narrar, primeira imagem
- `1-r-image-b.png` → Aula 1, Narrar, segunda imagem

---

## 🎨 Geração de Imagens

### **Documentação Completa**

Toda a documentação sobre geração de imagens está centralizada no agente especializado:

📁 **`bef/agents/skills/image-generator/`**

| Arquivo | Propósito |
|---------|-----------|
| `README.md` | Visão geral e referência rápida |
| `QUICKSTART.md` | Guia de início rápido (5 minutos) |
| `IMAGE-GENERATION-WORKFLOW.md` | Fluxo de trabalho completo |
| `SKILL.md` | Definição da habilidade do agente |

### **Scripts de Geração**

Todos os scripts estão em:

📁 **`bef/scripts/image-generation/`**

| Script | Quando Usar |
|--------|-------------|
| `generate_image.py` | Geração com Gemini (Nano Banana) |
| `generate_image_temp.py` | Geração com Pollinations (FREE, sem API key) |
| `test_gemini_quick.py` | Testar API Gemini |
| `diagnose_gemini_api.py` | Diagnosticar problemas |

---

## 🚀 Como Gerar Imagens

### **Opção 1: Pollinations (FREE - Sem API Key)**

```bash
python bef/scripts/image-generation/generate_image_temp.py
```

### **Opção 2: Gemini (Nano Banana - Com API Key)**

```bash
# Configurar API Key em: Projeto Bibline Academy/.env
python bef/scripts/image-generation/generate_image.py 14.2
```

---

## ✅ Checklist de Validação

Antes de considerar uma imagem pronta:

- [ ] Salva na pasta correta: `2 - Imagens/Semana [N]/Aula [N.N] - [Título]/`
- [ ] Nomenclatura segue padrão: `[numero]-r-image-[letra].png`
- [ ] Formato PNG
- [ ] Ratio 2:1 (1792x896)
- [ ] Qualidade visual verificada
- [ ] Estilo aquarela clássica confirmado

---

## 📊 Status de Geração

### **Imagens Geradas**

| Semana | Aula | Status | Arquivo |
|--------|------|--------|---------|
| 14 | 14.2 - A beleza sem estátuas | ✅ Gerada | `1-r-image-a.png` |
| 14 | 14.3 - O oceano azul de Istambul | ✅ Gerada | `1-r-image-a.png` |

### **Imagens Pendentes**

| Semana | Aula | Prioridade |
|--------|------|------------|
| 1-13 | Todas | Alta |
| 15-40 | Todas | Média |

---

## 🔗 Referências Rápidas

| Recurso | Localização |
|---------|-------------|
| **Workflow Completo** | `bef/agents/skills/image-generator/IMAGE-GENERATION-WORKFLOW.md` |
| **Padrão de Organização** | `PADRAO_IMAGENS.md` (nesta pasta) |
| **Guia Rápido** | `bef/agents/skills/image-generator/QUICKSTART.md` |
| **Troubleshooting** | `bef/agents/skills/image-generator/README.md` |

---

## ⚠️ Regras Importantes

### **SEMPRE**

✅ Usar pasta `2 - Imagens`  
✅ Organizar por semana  
✅ Usar nomenclatura padrão  
✅ Ratio 2:1  
✅ Formato PNG  

### **NUNCA**

❌ Salvar fora desta pasta  
❌ Nomenclatura diferente  
❌ Outros formatos  
❌ Ratio diferente  

---

**Última atualização:** 2026-04-06  
**Status:** ✅ Padrão Oficial
