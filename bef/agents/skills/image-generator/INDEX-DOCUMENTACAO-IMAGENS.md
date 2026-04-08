# 📚 Índice de Documentação - Geração de Imagens

> **Guia Central para Toda Documentação de Geração de Imagens**
>
> Este arquivo serve como índice mestre para localizar rapidamente qualquer documentação relacionada à geração de imagens no projeto.

---

## 🎯 Localização Rápida

### **Para Usuários que Querem:**

| Quero... | Vá Para |
|----------|---------|
| **Gerar uma imagem agora** | `bef/scripts/image-generation/generate_image_temp.py` |
| **Entender o fluxo completo** | `bef/agents/skills/image-generator/IMAGE-GENERATION-WORKFLOW.md` |
| **Configurar API Gemini** | `bef/agents/skills/image-generator/README.md` |
| **Ver padrão de organização** | `[Ano]/2 - Imagens/PADRAO_IMAGENS.md` |
| **Início rápido (5 min)** | `bef/agents/skills/image-generator/QUICKSTART.md` |

---

## 📁 Estrutura de Documentação

### **1. Agente Especializado (Fonte Principal)**

📁 **`bef/agents/skills/image-generator/`**

| Arquivo | Conteúdo | Quando Usar |
|---------|----------|-------------|
| `README.md` | Visão geral, configuração, troubleshooting | Referência rápida |
| `QUICKSTART.md` | Guia de 5 minutos para começar | Primeira vez |
| `IMAGE-GENERATION-WORKFLOW.md` | Fluxo completo passo-a-passo | Uso diário |
| `SKILL.md` | Definição da persona e habilidades | Entender o agente |
| `requirements.txt` | Dependências Python | Instalação |

### **2. Scripts de Geração**

📁 **`bef/scripts/image-generation/`**

| Arquivo | Função | API | Quando Usar |
|---------|--------|-----|-------------|
| `generate_image.py` | Geração principal | Gemini | Produção |
| `generate_image_temp.py` | Geração temporária | Pollinations | Testes/Backup |
| `test_gemini_quick.py` | Teste rápido | Gemini | Verificar API |
| `diagnose_gemini_api.py` | Diagnóstico | Gemini | Troubleshooting |
| `list_models.py` | Listar modelos | Gemini | Descobrir modelos |

### **3. Padrões de Organização**

📁 **`[Ano]/2 - Imagens/`**

| Arquivo | Localização |
|---------|-------------|
| `README.md` | `[Ano]/2 - Imagens/README.md` |
| `PADRAO_IMAGENS.md` | `[Ano]/2 - Imagens/PADRAO_IMAGENS.md` |

### **4. Integrações e Setup**

📁 **`Projeto Bibline Academy/setup-playbook/02-integrations/`**

| Arquivo | Conteúdo |
|---------|----------|
| `ai-image-generation.md` | Configuração de todas as APIs de imagem |

---

## 🗺️ Mapa de Navegação por Tópico

### **Configuração Inicial**

```
1. Instalar dependências
   → pip install -r bef/agents/skills/image-generator/requirements.txt

2. Configurar API Key (opcional)
   → bef/agents/skills/image-generator/README.md

3. Testar configuração
   → python bef/scripts/image-generation/diagnose_gemini_api.py
```

### **Gerar Imagem (Fluxo Rápido)**

```
1. Preparar estrutura
   → mkdir -p "[Ano]/2 - Imagens/Semana [N]/Aula [N.N] - [Título]/"

2. Executar script
   → python bef/scripts/image-generation/generate_image_temp.py

3. Validar resultado
   → ls -lh "[Ano]/2 - Imagens/Semana [N]/Aula [N.N] - [Título]/"
```

### **Gerar Imagem (Fluxo Completo)**

```
1. Ler workflow completo
   → bef/agents/skills/image-generator/IMAGE-GENERATION-WORKFLOW.md

2. Extrair prompt do arquivo de prompts

3. Configurar script com prompt personalizado

4. Executar com Gemini
   → python bef/scripts/image-generation/generate_image.py

5. Validar qualidade e nomenclatura
```

### **Troubleshooting**

```
1. Diagnosticar problema
   → python bef/scripts/image-generation/diagnose_gemini_api.py

2. Ver documentação de erros comuns
   → bef/agents/skills/image-generator/README.md#troubleshooting

3. Verificar lista de modelos
   → python bef/scripts/image-generation/list_models.py
```

---

## 📊 APIs Disponíveis

### **Comparação Rápida**

| API | Custo | Qualidade | Velocidade | API Key |
|-----|-------|-----------|------------|---------|
| **Gemini (Nano Banana)** | Free/Pago | Excelente | ~10-20s | ✅ Necessária |
| **Pollinations** | FREE | Boa | ~30-60s | ❌ Não necessária |

### **Quando Usar Cada Uma**

| Situação | API Recomendada |
|----------|----------------|
| Produção final | Gemini |
| Testes rápidos | Pollinations |
| Sem API Key | Pollinations |
| Máxima qualidade | Gemini |
| Backup | Pollinations |

---

## ✅ Checklists por Contexto

### **Primeiro Uso**

- [ ] Ler `QUICKSTART.md`
- [ ] Instalar dependências
- [ ] Configurar API (se usar Gemini)
- [ ] Testar com Pollinations (sem API key)
- [ ] Gerar primeira imagem de teste

### **Uso Diário**

- [ ] Verificar `IMAGE-GENERATION-WORKFLOW.md`
- [ ] Extrair prompt correto
- [ ] Criar estrutura de pastas
- [ ] Executar script apropriado
- [ ] Validar resultado

### **Antes de Commitar**

- [ ] Imagem na pasta correta
- [ ] Nomenclatura padrão verificada
- [ ] Qualidade validada
- [ ] Ratio 2:1 confirmado
- [ ] Formato PNG

---

## 🔗 Links Externos Importantes

| Recurso | URL |
|---------|-----|
| Google AI Studio | https://aistudio.google.com |
| Criar API Key | https://aistudio.google.com/app/apikey |
| Google Cloud Billing | https://console.cloud.google.com/billing |
| Gemini API Docs | https://ai.google.dev/gemini-api/docs |
| Pollinations.ai | https://pollinations.ai |

---

## 📝 Histórico de Centralização

| Data | Ação | Resultado |
|------|------|-----------|
| 2026-04-06 | Centralização completa | Documentação consolidada no agente |
| 2026-04-06 | Scripts movidos | Todos em `bef/scripts/image-generation/` |
| 2026-04-06 | Docs redundantes removidos | Arquivados em `.archive/redundant-docs/` |

---

## 🎯 Resumo Final

### **Antes (Desorganizado)**

```
❌ GEMINI_IMAGE_GENERATION.md (raiz)
❌ GEMINI_SETUP_SUMMARY.md (raiz)
❌ generate_image.py (raiz)
❌ generate_image_temp.py (raiz)
❌ test_gemini_quick.py (raiz)
❌ diagnose_gemini_api.py (raiz)
❌ list_models.py (raiz)
❌ verify_setup.py (raiz)
→ Documentação espalhada em 8+ arquivos
```

### **Depois (Organizado)**

```
✅ bef/agents/skills/image-generator/
   ├── README.md                    # Documentação principal
   ├── QUICKSTART.md                # Guia rápido
   ├── IMAGE-GENERATION-WORKFLOW.md # Fluxo completo
   └── SKILL.md                     # Definição do agente

✅ bef/scripts/image-generation/
   ├── generate_image.py
   ├── generate_image_temp.py
   ├── test_gemini_quick.py
   ├── diagnose_gemini_api.py
   └── list_models.py

✅ [Ano]/2 - Imagens/
   ├── README.md
   └── PADRAO_IMAGENS.md
→ Documentação centralizada em 1 agente
```

---

**Versão:** 1.0  
**Última atualização:** 2026-04-06  
**Status:** ✅ Índice Centralizado
