# 🔐 Environment Variables Setup

## 🎯 Objetivo
Configurar e gerenciar variáveis de ambiente de forma segura em diferentes ambientes (development, staging, production).

---

## 📋 Pré-requisitos
- [ ] `.env` na lista de exclusão do `.gitignore`
- [ ] `.env.example` como template
- [ ] Entendimento de escopos (local vs remote)

---

## 🔧 Estrutura de Arquivos

### `.gitignore` (Obrigatório)
```gitignore
# Environment variables
.env
.env.local
.env.*.local

# Vercel
.vercel

# Node modules
node_modules/
```

### `.env.example` (Template Público)
```bash
# Copy this file to .env and fill in your values

# Application
APP_NAME=
APP_URL=
APP_ENV=development

# API Keys
API_KEY=

# Database
DATABASE_URL=

# Services
VERCEL_PROJECT_ID=
```

### `.env` (Local - Não Commitar)
```bash
# Application
APP_NAME=Agent Command Center
APP_URL=http://localhost:3000
APP_ENV=development

# API Keys
API_KEY=sk_your_key_here

# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/dbname

# Services
VERCEL_PROJECT_ID=prj_xxxxxxxxxxxxx
```

---

## 📊 Hierarquia de Variáveis

### 1. Development (`.env`)
```bash
APP_ENV=development
DEBUG=true
API_URL=http://localhost:3000/api
```

### 2. Staging (`.env.staging`)
```bash
APP_ENV=staging
DEBUG=false
API_URL=https://staging.yourapp.com/api
```

### 3. Production (`.env.production` ou Vercel)
```bash
APP_ENV=production
DEBUG=false
API_URL=https://api.yourapp.com/api
```

---

## 🔑 Tipos de Variáveis

### System Variables
Variáveis do sistema/ambiente:
```bash
NODE_ENV=production
VERCEL_ENV=production
VERCEL_URL=yourapp.vercel.app
```

### Application Variables
Variáveis da aplicação:
```bash
APP_NAME=My App
APP_SECRET=your_secret_key
```

### Service Variables
Variáveis de serviços externos:
```bash
DATABASE_URL=postgresql://...
REDIS_URL=redis://...
```

### API Keys
Chaves de APIs externas:
```bash
GITHUB_TOKEN=ghp_...
STRIPE_KEY=sk_live_...
SENDGRID_KEY=SG....
```

---

## 🔧 Configuração na Vercel

### Via Dashboard
1. Acesse **Project Settings → Environment Variables**
2. Clique em **"Add New"**
3. Preencha:
   - **Name:** `DATABASE_URL`
   - **Value:** `postgresql://...`
   - **Environment:** Production/Preview/Development
4. Clique em **"Save"**

### Via CLI
```bash
# Adicionar variável
vercel env add DATABASE_URL

# Listar variáveis
vercel env ls

# Remover variável
vercel env rm DATABASE_URL

# Importar do .env local
vercel env pull
```

### No `vercel.json`
```json
{
  "env": {
    "APP_NAME": "My App",
    "APP_URL": "https://myapp.com"
  },
  "build": {
    "env": {
      "BUILD_VAR": "value"
    }
  }
}
```

---

## ✅ Validação

### Checklist de Segurança
- [ ] `.env` está no `.gitignore`
- [ ] `.env.example` não contém valores reais
- [ ] Variáveis sensíveis estão na Vercel, não no código
- [ ] Diferentes ambientes têm variáveis separadas

### Testes Locais
```bash
# Verificar se variáveis estão carregando
node -e "console.log(process.env.APP_NAME)"

# Testar com dotenv
require('dotenv').config()
console.log(process.env.DATABASE_URL)
```

---

## 🔗 Integração com GitHub Actions

### Workflow Example
```yaml
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Environment
        run: |
          echo "APP_ENV=production" >> .env
          echo "API_KEY=${{ secrets.API_KEY }}" >> .env
      
      - name: Deploy to Vercel
        uses: amondnet/vercel-action@v20
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
```

---

## 🐛 Troubleshooting

| Problema | Solução |
|----------|---------|
| Variável não carrega | Verifique se `.env` está na raiz do projeto |
| Variável undefined no build | Configure na Vercel Dashboard, não apenas no .env |
| `.env` foi commitado | 1. Remova do git: `git rm --cached .env` 2. Adicione ao .gitignore 3. Rotação de secrets |
| Variáveis diferentes por ambiente | Use prefixos: `VERCEL_ENV_` para escopo |

---

## 💡 Melhores Práticas

### Segurança
- ✅ Nunca commitar valores reais de `.env`
- ✅ Usar `.env.example` como template
- ✅ Rotacionar chaves periodicamente
- ✅ Usar secrets manager para produção crítica

### Organização
- ✅ Agrupar variáveis por serviço (DB, API, etc.)
- ✅ Usar nomes descritivos e consistentes
- ✅ Documentar cada variável no `.env.example`
- ✅ Manter `.env.example` atualizado

### Desenvolvimento
- ✅ Ter `.env` local idêntico ao de produção (em estrutura)
- ✅ Usar valores mock para desenvolvimento
- ✅ Testar com variáveis de produção em staging

---

## 📝 Template `.env.example`

```bash
# ============================================
# APPLICATION
# ============================================
APP_NAME=
APP_DESCRIPTION=
APP_URL=
APP_PORT=3000

# ============================================
# ENVIRONMENT
# ============================================
NODE_ENV=development
VERCEL_ENV=

# ============================================
# DATABASE
# ============================================
DATABASE_URL=postgresql://user:pass@localhost:5432/dbname
DATABASE_POOL_SIZE=10

# ============================================
# AUTHENTICATION
# ============================================
JWT_SECRET=
JWT_EXPIRES_IN=7d
SESSION_SECRET=

# ============================================
# API KEYS - EXTERNAL SERVICES
# ============================================
# GitHub
GITHUB_TOKEN=
GITHUB_WEBHOOK_SECRET=

# Email
RESEND_API_KEY=
SENDGRID_API_KEY=

# Storage
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_BUCKET_NAME=

# Analytics
GOOGLE_ANALYTICS_ID=
SENTRY_DSN=

# ============================================
# FEATURE FLAGS
# ============================================
ENABLE_FEATURE_X=true
ENABLE_BETA=false
```

---

## 🔗 Links Úteis
- [Vercel Environment Variables](https://vercel.com/docs/environment-variables)
- [dotenv (npm)](https://www.npmjs.com/package/dotenv)
- [GitGuardian - .gitignore templates](https://github.com/github/gitignore)
- [12 Factor App - Config](https://12factor.net/config)

---

**Última atualização:** 2026-04-02  
**Status:** ✅ Documentado
