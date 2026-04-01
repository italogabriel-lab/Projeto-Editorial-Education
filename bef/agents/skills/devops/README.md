# ⚙️ DevOps Agent - Documentação Completa

**Engenheiro de Operações e Gatekeeper de Repositório**

---

## Visão Geral

| Propriedade | Valor |
|-------------|-------|
| **Nome** | DevOps |
| **Tipo** | Engenheiro DevOps |
| **Escopo** | Editorial Squad |
| **Status** | ✅ Ativo |
| **Versão** | 1.0 |

---

## Objetivo

Blindar o ecossistema do repositório, garantindo que o versionamento contenha apenas inteligência do projeto (Markdown, Canvas, Estrutura) e nada de ativos pesados.

**Lema:** *"O Git NÃO é para armazenar mídia pesada. É para texto, histórico e conhecimento."*

---

## Comandos

### **1. `/devops publish`**

**Descrição:** Publica alterações no GitHub.

**Sintaxe:**
```bash
/devops publish
```

**Exemplo:**
```bash
/devops publish
```

**Saída:**
```bash
# 🚀 Publicação — Vision Board

## Status do Repositório
✅ Local: 3 files changed
✅ Remote: origin/main

## Ações Executadas
1. git add public/data.json
2. git commit -m "data: sync Kanban - 3180 items"
3. git pull --rebase
4. git push origin main

## Resultado
✅ Push successful
✅ GitHub Actions triggered
✅ Vision Board updated

## Tempo Total: 45s
```

---

### **2. `/devops cleanup`**

**Descrição:** Limpa arquivos pesados do cache Git.

**Sintaxe:**
```bash
/devops cleanup
```

**Exemplo:**
```bash
/devops cleanup
```

**Saída:**
```bash
# 🧹 Limpeza Estrutural

## Arquivos Removidos do Cache
- *.mp4 (12 files)
- *.pdf (5 files)
- .obsidian/cache/*
- .qwen/settings.json.orig

## Comandos Executados
1. git rm -r --cached *.mp4
2. git rm -r --cached *.pdf
3. git rm -r --cached .obsidian/cache/
4. git add .
5. git commit -m "chore: limpeza estrutural"

## Resultado
✅ Cache limpo
✅ Repositório otimizado
✅ Pronto para push
```

---

### **3. `/devops status`**

**Descrição:** Verifica status do repositório.

**Sintaxe:**
```bash
/devops status
```

**Exemplo:**
```bash
/devops status
```

**Saída:**
```bash
# 📊 Status do Repositório

## Branch
- Current: main
- Remote: origin/main
- Status: Up to date ✅

## Files Changed
- Modified: public/data.json
- Untracked: none

## Last Commit
- Hash: a4e4c6b
- Message: "data: sync Kanban - 3180 items"
- Date: 2026-04-01 14:31:35

## GitHub Actions
- Last run: success
- Duration: 57s
```

---

### **4. `/devops fix-conflict`**

**Descrição:** Resolve conflitos de merge.

**Sintaxe:**
```bash
/devops fix-conflict <arquivo>
```

**Exemplo:**
```bash
/devops fix-conflict public/data.json
```

---

## Atribuições Principais

### **1. Guardião da Regra de Ouro do Git**

**O que NÃO vai no Git:**
- ❌ `*.mp4` (vídeos)
- ❌ `*.pdf` (PDFs pesados)
- ❌ `*.zip`, `*.rar` (arquivos compactados)
- ❌ `*.mp3` (áudios)
- ❌ `.obsidian/cache/` (cache Obsidian)
- ❌ `.qwen/settings.json.orig` (backups)

**O que VAI no Git:**
- ✅ `*.md` (Markdown)
- ✅ `*.canvas` (Canvas Obsidian)
- ✅ `*.json` (dados estruturados)
- ✅ `*.html`, `*.css`, `*.js` (código)
- ✅ `.github/workflows/` (Actions)

---

### **2. Executor do Workflow de Publicação**

#### Passos Padrão
```bash
# 1. Staging
git add <files>

# 2. Commit
git commit -m "type: message"

# 3. Pull (rebase)
git pull --rebase

# 4. Push
git push origin main
```

#### Tipos de Commit
```
chore: limpeza estrutural
content: adição da Aula X.X do Ano Y
fix: atualização na matriz de links
data: sync Kanban - X items
feat: nova funcionalidade
docs: documentação
```

---

### **3. Gerador Estruturado de Commits**

**Padrões de Commit:**

| Tipo | Descrição | Exemplo |
|------|-----------|---------|
| `chore` | Limpeza, manutenção | `chore: cleanup cache` |
| `content` | Conteúdo de aula | `content: add Aula 36.3` |
| `fix` | Correções | `fix: update links` |
| `data` | Sync de dados | `data: sync Kanban` |
| `feat` | Features novas | `feat: add analytics` |
| `docs` | Documentação | `docs: add README` |

---

### **4. Responsável por Comunicação Terminal**

**Autorizações:**
- ✅ GitHub CLI (`gh`)
- ✅ HTTPS com credencial
- ✅ Git push/pull automático
- ✅ GitHub Actions trigger

**Sempre:**
- Emite ordens automáticas
- Não perturba usuário com TTY
- Mantém progresso escrito a salvo
- Gerencia desastres no Git

---

## Casos de Uso

### **1. Publicação Rotineira**

```bash
@devops "Publicar alterações do Vision Board"
```

**Processo:**
1. Verifica status
2. Adiciona arquivos
3. Commit com mensagem padrão
4. Pull --rebase
5. Push para origin/main
6. Trigger GitHub Actions

---

### **2. Limpeza de Emergência**

```bash
@devops "Repositório está muito pesado!"
```

**Processo:**
```bash
# Limpeza pesada
git rm -r --cached .
git add .
git commit -m "chore: limpeza estrutural"
git push origin --force
```

---

### **3. Resolução de Conflito**

```bash
@devops "Conflito no data.json após pull"
```

**Processo:**
1. Identifica conflito
2. Usa versão mais recente
3. Marca como resolvido
4. Completa rebase
5. Push normal

---

## FAQ

### **P: Por que não posso subir PDFs?**
**R:** Git não é feito para arquivos binários grandes. Use Google Drive ou outro storage para mídia.

---

### **P: O que fazer se `git push` falhar?**
**R:** Execute `git pull --rebase` primeiro para integrar mudanças remotas.

---

### **P: Como limpar cache do Obsidian?**
**R:** Use `/devops cleanup` que remove automaticamente `.obsidian/cache/` e arquivos temporários.

---

### **P: Qual tipo de commit usar?**
**R:**
- Conteúdo de aula → `content`
- Dados do Kanban → `data`
- Documentação → `docs`
- Limpeza → `chore`
- Correções → `fix`

---

## Links

- [Skill](SKILL.md)
- [Workflow Publish](../../workflows/publish.md)
- [GitHub Actions](../../.github/workflows/)
