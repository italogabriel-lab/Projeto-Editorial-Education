# 🔌 GitHub MCP Server

## 🎯 Objetivo
Configurar o GitHub MCP (Model Context Protocol) Server para integração com agentes AI, permitindo leitura/escrita no GitHub via comandos naturais.

---

## 📋 Pré-requisitos
- [ ] GitHub CLI (`gh`) instalado
- [ ] Node.js v18+ instalado
- [ ] Conta GitHub com permissões no repositório
- [ ] Token de acesso pessoal (PAT) ou OAuth

---

## 🔧 Instalação

### Passo 1: Instalar GitHub CLI
```bash
# macOS
brew install gh

# Linux (Debian/Ubuntu)
sudo apt install gh

# Windows
winget install GitHub.cli
```

### Passo 2: Autenticar GitHub CLI
```bash
gh auth login
```
- Escolha: **GitHub.com**
- Escolha: **HTTPS**
- Escolha: **Login with a web browser**
- Autorize o OAuth

### Passo 3: Verificar Autenticação
```bash
gh auth status
```

---

## 🔑 Criar Personal Access Token (PAT)

### Via GitHub Web
1. Acesse: https://github.com/settings/tokens
2. Clique em **"Generate new token (classic)"**
3. **Note:** `MCP Server - Projeto Editorial`
4. **Expiration:** 90 dias (ou personalizado)
5. **Scopes necessários:**
   - ✅ `repo` (Full control of private repositories)
   - ✅ `workflow` (Update GitHub Action workflows)
   - ✅ `read:org` (Read org membership)
   - ✅ `read:project` (Read projects data)
6. Clique em **"Generate token"**
7. **Copie o token** (não será mostrado novamente)

### Via CLI (Alternativo)
```bash
gh token create --scopes repo,workflow,read:org,read:project --note "MCP Server"
```

---

## 🔧 Configurar MCP Server

### Opção 1: Claude Desktop (Recomendado)

#### Passo 1: Localizar Config File
```bash
# macOS/Linux
~/.config/claude/claude_desktop_config.json

# Windows
%APPDATA%\Claude\claude_desktop_config.json
```

#### Passo 2: Adicionar GitHub MCP
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

#### Passo 3: Reiniciar Claude
- Feche e reabra o Claude Desktop
- Verifique em **Settings → MCP Servers**

---

### Opção 2: Cursor IDE

#### Passo 1: Abrir Settings
- `Cmd+,` (macOS) ou `Ctrl+,` (Windows/Linux)
- Navegue para **Features → MCP**

#### Passo 2: Adicionar Server
```json
{
  "mcp": {
    "servers": {
      "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": {
          "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_your_token_here"
        }
      }
    }
  }
}
```

---

### Opção 3: Standalone (Terminal)

#### Passo 1: Instalar MCP Server
```bash
npm install -g @modelcontextprotocol/server-github
```

#### Passo 2: Executar
```bash
GITHUB_PERSONAL_ACCESS_TOKEN=ghp_your_token npx @modelcontextprotocol/server-github
```

---

## ✅ Validação

### Testar Conexão
No Claude/Cursor, use:
```
@github List my repositories
```

### Comandos Disponíveis
```
@github create_issue <title> <body>
@github create_pull_request <title> <body>
@github search_repositories <query>
@github get_file_contents <owner> <repo> <path>
@github create_branch <name> <from>
@github push_files <branch> <files>
@github create_or_update_file <path> <content>
```

---

## 🔗 Integração com Agentes

### Exemplo: Publicar Aula no GitHub

#### Prompt para Agente
```
@orchestrator @publisher @github 

Publique a aula 36.3.md no repositório bibline/curriculum:
- Path: br/_/3-belas-artes/36.3.md
- Commit message: "Aula 36.3 — Renascimento e Reforma"
- Branch: master
```

#### Fluxo Automático
1. Agente lê arquivo local
2. Usa MCP para criar/atualizar arquivo
3. Confirma publicação

---

## 🐛 Troubleshooting

| Problema | Solução |
|----------|---------|
| MCP não conecta | Verifique token no config file |
| Permissão negada | Token precisa de escopo `repo` |
| Rate limit | Token expirou ou limite atingido |
| npx não encontrado | Instale Node.js 18+ |

---

## 💡 Melhores Práticas

### Segurança
- ✅ Nunca commitar token no código
- ✅ Usar variáveis de ambiente para tokens
- ✅ Rotacionar tokens a cada 90 dias
- ✅ Usar tokens com escopo mínimo necessário

### Organização
- ✅ Nomear tokens de forma descritiva
- ✅ Usar tokens diferentes por ambiente
- ✅ Documentar tokens em `.env.example`

---

## 📝 Configuração Completa (Exemplo)

### `claude_desktop_config.json`
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_MCP_TOKEN}"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem"
      ],
      "env": {
        "ALLOWED_PATHS": "/home/user/projects"
      }
    }
  }
}
```

### `.env` (Local)
```bash
# GitHub MCP
GITHUB_MCP_TOKEN=ghp_your_token_here
GITHUB_OWNER=italogabriel-lab
GITHUB_REPO=Projeto-Editorial-Education
```

---

## 🔗 Links Úteis
- [MCP Protocol Documentation](https://modelcontextprotocol.io/)
- [GitHub MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/github)
- [GitHub CLI](https://cli.github.com/)
- [Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)

---

## 📚 Comandos MCP GitHub

### Repositórios
```
list_repositories
get_repository <owner> <repo>
create_repository <name>
```

### Issues
```
create_issue <owner> <repo> <title> <body>
list_issues <owner> <repo>
get_issue <owner> <repo> <number>
update_issue <owner> <repo> <number> <updates>
```

### Pull Requests
```
create_pull_request <owner> <repo> <title> <body> <head> <base>
list_pull_requests <owner> <repo>
get_pull_request <owner> <repo> <number>
merge_pull_request <owner> <repo> <number>
```

### Files
```
get_file_contents <owner> <repo> <path> <branch?>
create_or_update_file <owner> <repo> <path> <content> <message> <branch?>
delete_file <owner> <repo> <path> <message> <branch?>
```

### Branches
```
create_branch <owner> <repo> <name> <from>
list_branches <owner> <repo>
```

### Projects (GitHub Projects V2)
```
list_projects <org?>
get_project <owner> <project_number>
add_item_to_project <owner> <project_number> <content_id>
```

---

**Última atualização:** 2026-04-02  
**Status:** ✅ Documentado
