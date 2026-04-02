# 🚀 Vercel Deployment

## 🎯 Objetivo
Deploy de aplicações estáticas e dinâmicas na Vercel com deploy automático via GitHub.

## 📋 Pré-requisitos
- [ ] Conta na Vercel (https://vercel.com)
- [ ] Repositório no GitHub
- [ ] Node.js instalado (para CLI opcional)

---

## 🔧 Passo a Passo

### Método 1: Via Interface Web (Recomendado)

#### Passo 1: Acessar Vercel
1. Acesse https://vercel.com/new
2. Faça login com sua conta GitHub

#### Passo 2: Importar Repositório
1. Clique em **"Import Git Repository"**
2. Selecione o repositório: `italogabriel-lab/Projeto-Editorial-Education`
3. Clique em **"Import"**

#### Passo 3: Configurar Projeto
1. **Project Name:** `agent-command-center` (ou nome preferido)
2. **Framework Preset:** Detecta automaticamente
3. **Root Directory:** Deixe como `./` (raiz)
4. **Build Command:** Deixe padrão
5. **Output Directory:** Deixe padrão

#### Passo 4: Deploy
1. Clique em **"Deploy"**
2. Aguarde o build (aproximadamente 1-2 minutos)
3. Clique em **"Continue to Dashboard"**

#### Passo 5: Configurar Domínio
- URL padrão: `https://projeto-editorial-education-[username].vercel.app`
- Para domínio customizado: **Settings → Domains → Add**

---

### Método 2: Via CLI (Terminal)

#### Passo 1: Instalar Vercel CLI
```bash
npm install -g vercel
```

#### Passo 2: Login
```bash
vercel login
```
- Escolha método de login (GitHub recomendado)

#### Passo 3: Deploy de Preview
```bash
vercel
```
- Responda as perguntas (Y/n)
- Aceite as configurações padrão

#### Passo 4: Deploy de Produção
```bash
vercel --prod
```

---

## 📁 Estrutura de Arquivos

### `vercel.json` (Configuração)
```json
{
  "version": 2,
  "builds": [
    {
      "src": "agent-command-center.html",
      "use": "@vercel/static"
    }
  ],
  "routes": [
    {
      "src": "/",
      "dest": "/agent-command-center.html"
    }
  ]
}
```

### Arquivos Estáticos
- HTML, CSS, JS na raiz do projeto
- Vercel detecta automaticamente

---

## 🔑 Variáveis de Ambiente

Configure em: **Project Settings → Environment Variables**

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `VERCEL_ENV` | Ambiente (auto) | `production` |

Para adicionar via CLI:
```bash
vercel env add VARIABLE_NAME
```

---

## ✅ Validação

### Checklist de Deploy Bem-Sucedido
- [ ] Build completou sem erros
- [ ] URL de preview está acessível
- [ ] URL de produção está acessível
- [ ] Assets (CSS, JS, imagens) carregando
- [ ] Interatividade funcionando

### Testes
1. Acesse a URL fornecida
2. Verifique no console do navegador por erros
3. Teste interatividade (search, filter, copy)

---

## 🔄 Deploy Automático

### Como Funciona
- **Push para `main`:** Deploy automático em produção
- **Pull Request:** Deploy de preview automático
- **Rollback:** Via dashboard da Vercel

### Fluxo Git
```bash
# Desenvolvimento
git checkout -b feature/nova-feature
git commit -m "feat: nova feature"
git push origin feature/nova-feature

# Cria PR → Vercel gera preview URL

# Merge na main → Deploy automático em produção
```

---

## 📊 Dashboard e Analytics

### Acessar Dashboard
1. https://vercel.com/dashboard
2. Selecione o projeto

### Métricas Disponíveis
- **Visitas:** Page views por dia
- **Bandwidth:** Uso de banda
- **Builds:** Histórico de deploys
- **Errors:** Erros de build/runtime

---

## 🔗 Links Úteis
- [Documentação Oficial Vercel](https://vercel.com/docs)
- [Vercel CLI](https://vercel.com/docs/cli)
- [vercel.json Reference](https://vercel.com/docs/project-configuration)
- [Environment Variables](https://vercel.com/docs/environment-variables)

---

## 🐛 Troubleshooting

| Problema | Solução |
|----------|---------|
| Build falha | Verifique logs em **Deployments → [Deploy] → View Logs** |
| 404 na página | Confirme o caminho no `vercel.json` routes |
| Assets não carregam | Use caminhos relativos ou absolute URLs |
| Variáveis não aplicam | Redeploy necessário após adicionar env vars |
| Deploy lento | Otimize assets, use lazy loading |

---

## 💡 Dicas e Melhores Práticas

### Performance
- ✅ Minifique CSS/JS em produção
- ✅ Use CDN para assets grandes
- ✅ Implemente lazy loading
- ✅ Ative compressão Gzip/Brotli

### Segurança
- ✅ Nunca commitar `.env` no git
- ✅ Use Environment Variables da Vercel
- ✅ Ative HTTPS automático (já vem por padrão)

### Organização
- ✅ Use `vercel.json` para configurações complexas
- ✅ Nomeie projetos de forma descritiva
- ✅ Use branches para previews de features

---

## 📝 Histórico de Configurações

| Data | Mudança | Responsável |
|------|---------|-------------|
| 2026-04-02 | Configuração inicial do Agent Command Center | Editorial Squad |

---

**Última atualização:** 2026-04-02  
**Status:** ✅ Documentado e Testado
