# Playbook de segurança para tokens e segredos

Documento de referência consolidando o incidente de exposição de tokens GitHub
em maio de 2026 e as práticas adotadas. Use como guia para responder a
incidentes futuros e como checklist para configurar segurança em novos
projetos.

## Sumário

1. [Contexto do incidente original](#1-contexto-do-incidente-original)
2. [Resposta a incidente, passo a passo](#2-resposta-a-incidente-passo-a-passo)
3. [Camadas de defesa para novos projetos](#3-camadas-de-defesa-para-novos-projetos)
4. [Ferramentas adotadas](#4-ferramentas-adotadas)
5. [Configuração do gitleaks](#5-configuração-do-gitleaks)
6. [Hook pre-commit versionável](#6-hook-pre-commit-versionável)
7. [Padrão recomendado para .env](#7-padrão-recomendado-para-env)
8. [Reescrita de histórico com git-filter-repo](#8-reescrita-de-histórico-com-git-filter-repo)
9. [Auditoria final, checklist](#9-auditoria-final-checklist)
10. [Boas práticas contínuas](#10-boas-práticas-contínuas)
11. [Lições aprendidas](#11-lições-aprendidas)

---

## 1. Contexto do incidente original

### O alerta

O SentinelOne reportou que um PAT do GitHub apareceu em texto aberto numa
sessão do Claude Code, gravado no histórico do shell e em `~/.git-credentials`.

### O que foi encontrado

- `~/.git-credentials` continha um token OAuth `gho_*` e um PAT clássico `ghp_*`.
- `.env` do projeto continha 6 segredos em texto puro, sendo 3 tokens GitHub,
  uma chave Gemini, uma chave GLM e uma chave Pollinations.
- Histórico do Git em repositório público continha `POLLINATIONS_KEY` em dois
  commits, expondo o segredo a qualquer pessoa que clonasse o repo.
- Histórico do bash estava limpo. Os tokens entraram via arquivos, não via
  comandos digitados.

### Severidade

Crítica. Repositório público com segredo válido no histórico permanece
acessível mesmo após remoção do arquivo, porque o Git preserva todos os
commits.

---

## 2. Resposta a incidente, passo a passo

Ordem que funciona para qualquer vazamento futuro.

### 2.1 Contenção imediata

1. **Revogar o token na plataforma de origem.** GitHub, Google AI Studio,
   OpenAI, etc. Esta é a única ação que neutraliza o risco. Apagar do disco
   não basta.
2. **Confirmar a autenticidade do alerta** se vier de fonte externa. Mensagens
   urgentes que pedem `rm` e troca de credenciais podem ser phishing.
3. **Não rodar comandos destrutivos** sem confirmar contexto.

### 2.2 Diagnóstico

```bash
ls -la ~/.git-credentials
git config --global --get credential.helper
git config --global --list | grep -i credential
gh auth status
```

Procure também por stores alternativos.

```bash
ls -la ~/.netrc ~/.config/git/credentials 2>/dev/null
```

### 2.3 Limpeza do disco

```bash
# Backup opcional antes de apagar
cp ~/.git-credentials ~/.git-credentials.bak.$(date +%s)

# Remoção
rm -f ~/.git-credentials

# Validação
ls -la ~/.git-credentials   # deve falhar com "No such file"
```

### 2.4 Limpeza do shell

```bash
# Auditoria
grep -E "ghp_|gho_|github_pat_|sk_|AIzaSy" ~/.bash_history
grep -E "ghp_|gho_|github_pat_|sk_|AIzaSy" ~/.zsh_history 2>/dev/null

# Se encontrar, limpa o buffer da sessão atual
history -c

# Para limpar o arquivo persistente
> ~/.bash_history    # zera o arquivo
```

### 2.5 Reautenticação do gh CLI

```bash
gh auth logout --hostname github.com
gh auth login
```

O `gh` armazena o token no **keyring do sistema**, não em arquivo texto. É a
forma correta de manter tokens GitHub sem expor em disco.

### 2.6 Triagem do histórico do repo

```bash
gitleaks detect --no-banner --report-format json --report-path /tmp/leaks.json
jq -r '.[] | "\(.RuleID)|\(.File)|line\(.StartLine)|\(.Match[0:80])"' /tmp/leaks.json | sort -u
```

Classifique cada achado em **falso positivo** ou **vazamento real**. Falsos
positivos comuns:

- AWS keys em URLs `private-user-images.githubusercontent.com`. São do
  próprio GitHub, com URLs assinadas que expiram em minutos.
- Placeholders como `YOUR_GITHUB_TOKEN` em tutoriais.
- Exemplos fictícios em documentação de segurança.

### 2.7 Purgar segredo real do histórico

Use `git-filter-repo`. Procedimento detalhado na seção 8.

### 2.8 Notificar

- Se houver colaboradores, avise que o histórico foi reescrito, todos
  precisam reclonar ou rodar `git fetch && git reset --hard origin/main`.
- Se o repo é público, considere que forks e caches podem ter cópias. A
  revogação do token é o que de fato protege.

---

## 3. Camadas de defesa para novos projetos

Aplicar antes do primeiro commit.

### Camada 1, permissões locais

```bash
chmod 600 .env
```

Só seu usuário lê e escreve. Bloqueia leitura por outros processos.

### Camada 2, gitignore robusto

```gitignore
# Variaveis de ambiente
.env
.env.*
!.env.example

# Credenciais
*.pem
*.key
.netrc
.git-credentials

# Diretorios sensíveis
.aws/
.ssh/
secrets/
```

### Camada 3, template versionável

Mantenha `.env.example` com a estrutura e comentários, mas sem valores.

### Camada 4, pre-commit hook com gitleaks

Bloqueia commit que contenha padrão de segredo. Detalhes nas seções 5 e 6.

### Camada 5, escaneamento periódico

```bash
# Scan rápido do working tree
gitleaks detect --no-git --no-banner --config .gitleaks.toml

# Scan completo do histórico
gitleaks detect --no-banner --config .gitleaks.toml
```

### Camada 6, cofre de segredos para uso real

Para projetos que rodam de verdade, evite `.env` e use:

- **`pass`**, cofre local com GPG.
- **`gh secret`**, para segredos de CI no GitHub Actions.
- **`op`**, 1Password CLI, injeta segredo no ambiente sem escrever em disco.
- **`gh auth token`**, dispensa armazenar PAT GitHub.

---

## 4. Ferramentas adotadas

### gitleaks

Scanner open-source de segredos. Detecta mais de 100 padrões conhecidos.

```bash
# Instalação sem sudo
cd /tmp
curl -sL -o gitleaks.tar.gz \
  "https://github.com/gitleaks/gitleaks/releases/latest/download/gitleaks_linux_x64.tar.gz"
tar -xzf gitleaks.tar.gz gitleaks
mv gitleaks ~/.local/bin/
chmod +x ~/.local/bin/gitleaks
gitleaks version
```

### git-filter-repo

Ferramenta oficial para reescrever histórico do Git. Substitui o antigo
`git filter-branch`.

```bash
pip install --user git-filter-repo
~/.local/bin/git-filter-repo --version
```

### gh CLI

Cliente oficial do GitHub. Armazena token no keyring do sistema.

```bash
# Fedora
sudo dnf install gh

# Login
gh auth login
```

### jq

Processador JSON para triagem de relatórios do gitleaks.

```bash
sudo dnf install jq
```

---

## 5. Configuração do gitleaks

Crie `.gitleaks.toml` na raiz do projeto.

```toml
# Estende as regras default e adiciona allowlist
# para falsos positivos conhecidos.
[extend]
useDefault = true

[allowlist]
description = "Falsos positivos conhecidos"

# Caminhos sem segredos reais
paths = [
  '''(?i)^\.env\.example$''',
  '''(?i)QUICK_REFERENCE\.md$''',
]

# Substrings literais que nao sao segredos
stopwords = [
  "YOUR_GITHUB_TOKEN",
  "sk-live-abc123xyz789",
]

# Regex de contexto, ignora URLs do GitHub user-images
regexes = [
  '''private-user-images\.githubusercontent\.com''',
]
```

**Regra de ouro para allowlist**, mantenha enxuta. Cada entrada deve ter
comentário explicando por que é falso positivo.

---

## 6. Hook pre-commit versionável

Hooks em `.git/hooks/` não são versionados pelo Git. Para compartilhar com
clones futuros e outros desenvolvedores, use `core.hooksPath`.

### Estrutura

```text
scripts/
└── hooks/
    └── pre-commit
```

### Conteúdo de `scripts/hooks/pre-commit`

```bash
#!/usr/bin/env bash
# Bloqueia commit se gitleaks detectar segredos nos arquivos staged.
# Bypass pontual, use com criterio: git commit --no-verify

set -e

if ! command -v gitleaks >/dev/null 2>&1; then
  echo "gitleaks nao encontrado no PATH. Instale antes de commitar." >&2
  exit 1
fi

gitleaks protect --staged --redact --no-banner --verbose --config .gitleaks.toml
```

### Ativação

```bash
chmod +x scripts/hooks/pre-commit
git config core.hooksPath scripts/hooks
```

### Validação

```bash
# Cria um arquivo com segredo fake e testa.
# Substitua FAKE_TOKEN_AQUI por um padrao ghp_ com 36 chars aleatorios
# em sessao isolada, fora deste documento.
echo "API_KEY=FAKE_TOKEN_AQUI" | gitleaks detect --pipe --no-banner --redact

# Resultado esperado, "leaks found: 1".
```

---

## 7. Padrão recomendado para .env

### Estrutura de comentários

```dotenv
# --------------------------------------------
# Categoria de servicos
# --------------------------------------------

# Nome do servico
# URL para gerar a chave: https://...
# Escopo necessario: descricao
NOME_DA_VARIAVEL=
```

### Regras

1. **Nunca commitar `.env`.** Manter no `.gitignore`.
2. **`.env.example` versionado** com valores vazios.
3. **`chmod 600 .env`** sempre que criar ou recriar.
4. **Comentários explicativos** indicando origem e escopo de cada chave.
5. **Não ecoar variáveis no terminal**, evita histórico e logs.

### Carregamento sem expor

```bash
# Ruim, ecoa no shell
export TOKEN=$(cat .env | grep TOKEN | cut -d= -f2)
echo $TOKEN

# Bom, source direto
set -a
source .env
set +a
comando_que_consome
```

---

## 8. Reescrita de histórico com git-filter-repo

Use apenas quando segredo **real** apareceu em commit já enviado para remoto
público. Para repos privados sem colaboradores externos, a revogação do token
basta.

### Pré-requisitos

- Working tree **completamente limpo**. Commitar ou stashear tudo antes.
- Backup do repo, sempre.
- Aviso aos colaboradores, todos os SHAs vão mudar.

### Procedimento

```bash
# 1. Backup
cp -r meu-repo /tmp/repo-backup-$(date +%s)

# 2. Arquivo de substituição
echo 'SEGREDO_LITERAL==>REMOVED_PLACEHOLDER' > /tmp/replace.txt

# 3. Reescrita
cd meu-repo
git-filter-repo --replace-text /tmp/replace.txt --force

# 4. Filter-repo remove o remote por seguranca, readicione
git remote add origin https://github.com/SEU_USER/SEU_REPO.git

# 5. Atualize refs locais
git fetch origin

# 6. Validacao
gitleaks detect --no-banner --config .gitleaks.toml

# 7. Push forcado com protecao
git push --force-with-lease origin main

# 8. Limpeza local
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

### Armadilhas

- **`user.name` com `\n` literal no `~/.gitconfig`** quebra o parser do
  filter-repo. Fix, `git config --global user.name "Nome"`.
- **`--force-with-lease` rejeita com "stale info"** se o filter-repo removeu
  as refs `remotes/origin/*`. Fix, `git fetch origin` antes do push.
- **Não afeta forks nem caches do GitHub**. A revogação do token é o que
  protege de verdade.
- **Issues e PRs com SHAs antigos quebram**.

---

## 9. Auditoria final, checklist

Após responder a um incidente, valide:

### Credenciais locais

```bash
[ ! -f ~/.git-credentials ] && echo "git-credentials OK"
[ ! -f ~/.netrc ] && echo "netrc OK"
gh auth status 2>&1 | grep "Logged in"
```

### Histórico do shell

```bash
grep -cE "ghp_|gho_|github_pat_|sk_|AIzaSy" ~/.bash_history
# Deve retornar 0
```

### Permissões

```bash
stat -c '%a %n' .env       # deve mostrar 600 .env
stat -c '%a %n' .env.example  # 644 ou similar
```

### Repositório

```bash
gitleaks detect --no-banner --config .gitleaks.toml
# Deve mostrar "no leaks found"

git status --short
# Working tree limpo

git config --get core.hooksPath
# Deve apontar para scripts/hooks
```

### Plataformas externas

- [ ] Token antigo revogado no GitHub
- [ ] Token antigo revogado no provedor LLM
- [ ] Token novo gerado e em uso
- [ ] `.env` atualizado com valores novos

---

## 10. Boas práticas contínuas

### Tokens

- Prefira **fine-grained PATs** sobre PATs clássicos.
- Defina **expiração curta**, 30 a 90 dias.
- Escopo **mínimo necessário**.
- Um token **por finalidade**, facilita revogação isolada.

### Repositórios

- Repositórios com segredos potenciais devem ser **privados**.
- Habilite **secret scanning** do GitHub, alerta automático.
- Habilite **push protection** do GitHub, bloqueia push com segredo
  detectado.

### Rotinas

- Scan mensal, `gitleaks detect`.
- Auditoria trimestral de tokens ativos em cada plataforma.
- Documente em algum lugar (cofre ou nota cifrada) qual token serve para
  qual finalidade.

### Cultura

- Nunca cole token em chat, email, issue, comentário ou prompt de LLM.
- Sempre que um LLM precisar acessar serviço autenticado, use o cliente
  oficial (`gh`, `aws`, `gcloud`) em vez de passar token como string.
- Trate alertas de SentinelOne, GitHub secret scanning, etc., como
  obrigações imediatas, nunca como ruído.

---

## 11. Lições aprendidas

### O que funcionou

- Revogação imediata como primeira ação.
- Backup antes de operações destrutivas (filter-repo).
- Pre-commit hook com gitleaks evitou recorrência.
- Hook versionado via `core.hooksPath` propaga proteção para clones futuros.

### O que poderia ter sido evitado

- `.env` com 6 segredos em texto puro acumulados. Cofre teria reduzido
  superfície.
- 3 tokens GitHub diferentes onde 1 fine-grained PAT bastaria.
- `~/.git-credentials` órfão de uso antigo, deveria ter sido removido na
  migração para `gh`.
- Repositório público com `.env` exemplo contendo valores reais nos
  documentos `IMPLEMENTATION_PLAN.md` e `FINAL_REPORT.md`, deveriam ter
  usado placeholders desde o início.

### Princípios

1. **Revogar primeiro, limpar depois.** Sempre.
2. **Hooks bloqueiam erro humano.** Confiar em disciplina pessoal não basta.
3. **Repo público trata todo commit como permanente.** Histórico vira
   patrimônio acessível, planeje commits assim.
4. **Falsos positivos são esperados.** Investir em allowlist tira o ruído e
   mantém o sinal.
5. **Backup antes de reescrita.** `filter-repo` é poderoso e irreversível.

---

## Apêndice A, padrões de tokens detectados

| Prefixo | Tipo | Plataforma |
|---------|------|------------|
| `ghp_` | PAT clássico | GitHub |
| `gho_` | Token OAuth | GitHub |
| `github_pat_` | Fine-grained PAT | GitHub |
| `ghs_` | App installation token | GitHub |
| `ghr_` | Refresh token | GitHub |
| `AIza` | API key | Google |
| `sk-` | API key | OpenAI, Anthropic |
| `sk_live_`, `sk_test_` | Secret key | Stripe |
| `AKIA` | Access key ID | AWS |
| `xoxb-`, `xoxp-` | Bot/User token | Slack |

## Apêndice B, comandos de emergência

Cheat sheet para resposta rápida.

```bash
# Diagnostico rapido
ls -la ~/.git-credentials ~/.netrc 2>/dev/null
git config --global --list | grep credential
gh auth status

# Conter
rm -f ~/.git-credentials
gh auth logout && gh auth login
chmod 600 .env

# Scan
gitleaks detect --no-banner

# Reescrever historico (CUIDADO)
echo 'SEGREDO==>REMOVED' > /tmp/r.txt
git-filter-repo --replace-text /tmp/r.txt --force
git remote add origin URL
git fetch origin
git push --force-with-lease origin main

# Limpar
git reflog expire --expire=now --all
git gc --prune=now --aggressive
history -c
```

## Apêndice C, links úteis

- gitleaks, https://github.com/gitleaks/gitleaks
- git-filter-repo, https://github.com/newren/git-filter-repo
- gh CLI, https://cli.github.com
- GitHub secret scanning, https://docs.github.com/en/code-security/secret-scanning
- GitHub push protection, https://docs.github.com/en/code-security/secret-scanning/push-protection-for-repositories-and-organizations
- OWASP top 10, https://owasp.org/Top10/
