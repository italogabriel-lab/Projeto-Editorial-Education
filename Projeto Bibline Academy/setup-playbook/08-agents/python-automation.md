# 🐍 Python Automation Scripts

## 🎯 Objetivo
Automatizar tarefas repetitivas de gestão editorial, sincronização de currículo, e integração com GitHub usando scripts Python.

---

## 📋 Pré-requisitos
- [ ] Python 3.8+ instalado
- [ ] Dependências instaladas (`pip install -r requirements.txt`)
- [ ] GitHub CLI (`gh`) autenticado
- [ ] Acesso de leitura/escrita ao repositório

---

## 📁 Estrutura de Scripts

```
bef/scripts/scripts/
├── github_integration/       # Integração com GitHub
│   ├── create_issues.py      # Cria Issues e adiciona ao Project
│   └── check_project_items.py # Audita itens do Project
│
├── sync/                     # Sincronização de Currículo
│   ├── sync_titles.py        # Master sync de títulos
│   ├── align_titles.py       # Alinha títulos em tickets
│   ├── align_review_titles.py # Alinha títulos de revisão
│   ├── fix_lesson_h1.py      # Corrige headers H1
│   └── fix_titles.py         # Limpeza cosmética
│
├── curriculum/               # Gestão de Currículo
│   ├── check_matriz.py       # Audita matriz curricular
│   ├── build_year1_tickets.py # Estrutura tickets Ano 1
│   └── update_year1_tickets.py # Atualiza tickets Ano 1
│
├── descriptions/             # Descrições de Tickets
│   └── generate_descriptions.py # Gera descrições (destrutivo)
│
├── converters/               # Conversão de Blocos
│   ├── convert_recordar.py   # Converte Music → Rhyme
│   └── convert_recordar_to_rhyme.py # Extrai definições
│
├── formatters/               # Formatação de Conteúdo
│   └── fix_accordion.py     # Corrige blocos accordion
│
└── utils/                    # Utilitários
    └── [utilitários diversos]
```

---

## 🔧 Instalação

### Passo 1: Instalar Python

```bash
# macOS
brew install python@3.11

# Linux (Ubuntu/Debian)
sudo apt install python3 python3-pip

# Windows
winget install Python.Python.3.11
```

### Passo 2: Instalar Dependências

```bash
cd bef/scripts
pip install -r requirements.txt
```

### `requirements.txt` Típico:
```txt
requests>=2.31.0
python-dotenv>=1.0.0
click>=8.1.0
rich>=13.0.0
pygithub>=2.1.0
```

### Passo 3: Configurar Environment

Crie `.env` na raiz dos scripts:
```bash
# GitHub
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxx
GITHUB_OWNER=bibline
GITHUB_REPO=curriculum
GITHUB_PROJECT_ID=PVT_kwDODLv1ac4BH1XW

# Application
APP_ENV=development
DEBUG=true
```

---

## 📚 Scripts de Integração GitHub

### 1. `create_issues.py`

**Propósito:** Cria GitHub Issues em lote a partir do currículo e adiciona ao Projects.

**Uso:**
```bash
python scripts/create_issues.py --year 3 --week 1
```

**O que faz:**
1. Lê `1 - Curriculo Macro - 3º ANO.md`
2. Extrai títulos das aulas da semana
3. Cria Issue para cada aula no GitHub
4. Adiciona Issues ao Projects V2
5. Define labels (ano, disciplina, status)
6. Atribui responsáveis (se configurado)

**Exemplo de Output:**
```
✅ Created issue #123: [Belas Artes] - Ano 3 - 1.1 Império Bizantino
✅ Added to project: Bibline Aulas
✅ Set labels: ano:3, belas-artes, status:backlog
✅ Assigned to: joao-silva
```

---

### 2. `check_project_items.py`

**Propósito:** Audita itens do Projects, lista itens em Backlog.

**Uso:**
```bash
python scripts/check_project_items.py --status backlog
python scripts/check_project_items.py --year 3
```

**O que faz:**
1. Conecta ao Projects V2 via GraphQL
2. Filtra por status ou ano
3. Lista itens com assignee, status, data
4. Gera relatório de auditoria

**Exemplo de Output:**
```
📊 Backlog Items - Ano 3

| Issue | Título | Assignee | Created |
|-------|--------|----------|---------|
| #123  | 1.1 Império Bizantino | joao-silva | 2026-03-01 |
| #124  | 1.2 Constantinopla | maria-santos | 2026-03-01 |

Total: 2 items
```

---

## 🔄 Scripts de Sincronização

### 3. `sync_titles.py` (MASTER SYNC)

**Propósito:** Sincroniza títulos do Currículo Macro para TODOS os arquivos dependentes.

**Uso:**
```bash
python scripts/sync_titles.py --year 3
```

**O que faz:**
1. Lê `1 - Curriculo Macro - 3º ANO.md` (fonte da verdade)
2. Extrai todos os títulos de aulas
3. Atualiza os seguintes arquivos:
   - `2 - Matriz-Curricular-objetivos.md`
   - `3 - Visao e Plano pedagogico.md`
   - `6 - Descricoes para tickets.md`
   - Todos os arquivos de aula `.md` (H1)
4. Valida consistência após sync

**Exemplo de Output:**
```
📖 Reading Macro Curriculum: 3º Ano
📊 Found 40 weeks, 120 lessons

🔄 Syncing to Matriz Curricular...
✅ Updated 120 titles

🔄 Syncing to Visão e Plano...
✅ Updated 120 titles

🔄 Syncing to Descrições para tickets...
✅ Updated 120 titles

🔄 Syncing lesson H1 headers...
✅ Updated 118 files (2 unchanged)

✅ Sync complete! All titles aligned.
```

**Regra de Ouro:**
> O `1 - Curriculo Macro` é a **única fonte oficial** de títulos. Todos os outros arquivos devem refletir exatamente os mesmos títulos.

---

### 4. `align_titles.py`

**Propósito:** Alinha títulos de aulas nas descrições de tickets (Issues).

**Uso:**
```bash
python scripts/align_titles.py --year 3 --week 1
```

**O que faz:**
1. Lê títulos do Currículo Macro
2. Busca Issues correspondentes no GitHub
3. Atualiza descrição da Issue com título correto
4. Mantém formatação padrão da descrição

---

### 5. `align_review_titles.py`

**Propósito:** Alinha títulos de aulas de revisão (X.4).

**Uso:**
```bash
python scripts/align_review_titles.py --year 3
```

**Diferença para `align_titles.py`:**
- Foca apenas em aulas de revisão (.4)
- Considera estrutura específica de revisões

---

### 6. `fix_lesson_h1.py`

**Propósito:** Corrige headers H1 em arquivos de aula.

**Uso:**
```bash
python scripts/fix_lesson_h1.py --year 3 --week 1
```

**O que faz:**
1. Lê arquivos de aula
2. Verifica se H1 bate com Currículo Macro
3. Corrige divergências
4. Mantém formatação consistente

---

### 7. `fix_titles.py`

**Propósito:** Limpeza cosmética de títulos (remove caracteres especiais, padroniza).

**Uso:**
```bash
python scripts/fix_titles.py --year 3
```

**O que faz:**
- Remove espaços extras
- Padroniza capitalização
- Remove caracteres problemáticos

---

## 📖 Scripts de Currículo

### 8. `check_matriz.py`

**Propósito:** Audita alinhamento entre Matriz Curricular e Currículo Macro.

**Uso:**
```bash
python scripts/check_matriz.py --year 3
```

**O que faz:**
1. Lê `1 - Curriculo Macro`
2. Lê `2 - Matriz-Curricular-objetivos`
3. Compara título por título
4. Reporta divergências

**Exemplo de Output:**
```
🔍 Auditing Matriz Curricular - 3º Ano

✅ 118/120 titles aligned
⚠️ 2 divergences found:

❌ Week 5.2:
   Macro: "Arte Românica"
   Matriz: "Arte Romanica" (missing accent)

❌ Week 10.1:
   Macro: "Prova Bimestral"
   Matriz: "Avaliação Bimestral" (different term)

Run sync_titles.py to fix
```

---

### 9. `build_year1_tickets.py`

**Propósito:** Estrutura tickets para o Ano 1 inteiro.

**Uso:**
```bash
python scripts/build_year1_tickets.py
```

**O que faz:**
1. Lê currículo do Ano 1
2. Cria estrutura de tickets para 40 semanas
3. Define labels, milestones
4. Adiciona ao Projects

---

### 10. `update_year1_tickets.py`

**Propósito:** Atualiza tickets existentes do Ano 1.

**Uso:**
```bash
python scripts/update_year1_tickets.py --week 1-10
```

---

## 📝 Scripts de Descrição

### 11. `generate_descriptions.py`

**Propósito:** Gera descrições para tickets (DESTRUTIVO - substitui conteúdo existente).

**Uso:**
```bash
python scripts/generate_descriptions.py --year 3 --week 1 --dry-run
```

**⚠️ Atenção:**
- Este script **substitui** descrições existentes
- Sempre use `--dry-run` primeiro para preview
- Faça backup antes de rodar sem `--dry-run`

**O que faz:**
1. Lê conteúdo da aula
2. Extrai objetivos, termos, atividades
3. Gera descrição estruturada para Issue
4. Atualiza no GitHub

---

## 🔄 Scripts de Conversão

### 12. `convert_recordar.py`

**Propósito:** Converte blocos "Recordar" de formato Music para Rhyme.

**Uso:**
```bash
python scripts/convert_recordar.py --year 3 --week 1
```

**O que faz:**
- Identifica blocos `[+STATEMENT_D]` com música
- Converte para formato de rima/verso
- Mantém definição original

---

### 13. `convert_recordar_to_rhyme.py`

**Propósito:** Extrai definições e verifica blocos de música.

**Uso:**
```bash
python scripts/convert_recordar_to_rhyme.py --file 1.1.md
```

---

## 🎨 Scripts de Formatação

### 14. `fix_accordion.py`

**Propósito:** Corrige blocos accordion (remove repetição redundante do termo).

**Problema que resolve:**
```markdown
# Errado (termo repetido)
[+ACCORDION]
O que é Arte Bizantina?
Arte Bizantina é...
[-ACCORDION]

# Correto (definição direta)
[+ACCORDION]
O que é Arte Bizantina?
É uma expressão artística...
[-ACCORDION]
```

**Uso:**
```bash
python scripts/fix_accordion.py --year 3 --week 1
```

---

## ✅ Validação

### Testar Script em Dry-Run

```bash
# Sempre teste com --dry-run primeiro
python scripts/sync_titles.py --year 3 --dry-run
```

### Verificar Logs

Scripts bem comportados geram logs:
```
✅ Success operations
⚠️  Warnings
❌ Errors
📊 Summary statistics
```

### Validar Resultado

```bash
# Git diff para ver mudanças
git diff

# Se satisfeito, commit
git add .
git commit -m "sync: titles update year 3 week 1"
git push
```

---

## 🔑 Variáveis de Ambiente

| Variável | Obrigatória | Descrição | Exemplo |
|----------|-------------|-----------|---------|
| `GITHUB_TOKEN` | Sim | PAT Token GitHub | `ghp_xxxxx` |
| `GITHUB_OWNER` | Sim | Owner do repo | `bibline` |
| `GITHUB_REPO` | Sim | Nome do repo | `curriculum` |
| `GITHUB_PROJECT_ID` | Sim | Projects V2 ID | `PVT_...` |
| `APP_ENV` | Não | Ambiente | `development` |
| `DEBUG` | Não | Debug mode | `true` |

---

## 🐛 Troubleshooting

| Problema | Solução |
|----------|---------|
| ModuleNotFoundError | `pip install -r requirements.txt` |
| GitHub API rate limit | Aguarde 1 hora ou use token com mais limites |
| Permission denied | Verifique escopos do token (repo, project) |
| Arquivo não encontrado | Verifique caminho relativo vs absoluto |
| Sync não atualiza | Verifique se arquivo está no .gitignore |
| Script falha no meio | Use `--verbose` para debug, verifique logs |

---

## 💡 Melhores Práticas

### Antes de Rodar
- ✅ Sempre use `--dry-run` se disponível
- ✅ Faça `git status` para ver estado atual
- ✅ Tenha backup ou branch de fallback

### Durante Execução
- ✅ Monitore logs em tempo real
- ✅ Interrompa se ver erro crítico
- ✅ Anote operações realizadas

### Após Execução
- ✅ Verifique `git diff`
- ✅ Teste em staging primeiro
- ✅ Valide com usuário antes de push

---

## 📊 Scripts por Categoria

### GitHub Integration (2 scripts)
| Script | Função | Status |
|--------|--------|--------|
| `create_issues.py` | Cria Issues + Projects | ✅ Ativo |
| `check_project_items.py` | Audita Projects | ✅ Ativo |

### Sync (5 scripts)
| Script | Função | Status |
|--------|--------|--------|
| `sync_titles.py` | Master sync | ✅ Ativo |
| `align_titles.py` | Alinha tickets | ✅ Ativo |
| `align_review_titles.py` | Revisões | ✅ Ativo |
| `fix_lesson_h1.py` | Headers H1 | ✅ Ativo |
| `fix_titles.py` | Limpeza | ✅ Ativo |

### Curriculum (3 scripts)
| Script | Função | Status |
|--------|--------|--------|
| `check_matriz.py` | Auditoria | ✅ Ativo |
| `build_year1_tickets.py` | Estrutura Ano 1 | ✅ Ativo |
| `update_year1_tickets.py` | Atualiza Ano 1 | ✅ Ativo |

### Descriptions (1 script)
| Script | Função | Status |
|--------|--------|--------|
| `generate_descriptions.py` | Gera descrições | ⚠️ Destrutivo |

### Converters (2 scripts)
| Script | Função | Status |
|--------|--------|--------|
| `convert_recordar.py` | Music → Rhyme | ✅ Ativo |
| `convert_recordar_to_rhyme.py` | Extrai definições | ✅ Ativo |

### Formatters (1 script)
| Script | Função | Status |
|--------|--------|--------|
| `fix_accordion.py` | Corrige accordion | ✅ Ativo |

---

## 🔗 Links Úteis
- [GitHub GraphQL API](https://docs.github.com/en/graphql)
- [PyGitHub Documentation](https://pygithub.readthedocs.io/)
- [Click CLI Framework](https://click.palletsprojects.com/)
- [Python Requests](https://requests.readthedocs.io/)

---

## 📝 Exemplo de Workflow Completo

### Cenário: Mudança de Título no Macro

1. **Usuário altera título no `1 - Curriculo Macro`**
   ```markdown
   ## Semana 5 – **Arte Românica e Gótica**
   ```

2. **Rodar sync_titles.py**
   ```bash
   python scripts/sync_titles.py --year 3
   ```

3. **Verificar mudanças**
   ```bash
   git diff
   ```

4. **Rodar check_matriz.py para validar**
   ```bash
   python scripts/check_matriz.py --year 3
   ```

5. **Se tudo OK, commit**
   ```bash
   git add .
   git commit -m "sync: update week 5 title year 3"
   git push
   ```

6. **Rodar align_titles.py para tickets**
   ```bash
   python scripts/align_titles.py --year 3 --week 5
   ```

7. **Verificar Issues no GitHub**
   - Títulos atualizados
   - Descrições alinhadas

---

**Última atualização:** 2026-04-02  
**Status:** ✅ Documentado e em Produção
