---
description: Sincronização e versionamento profissional do Vault do Obsidian no GitHub.
---

# Fluxo de Versionamento e Sincronização (Publish)

Este workflow garante que o repositório sincronize de forma saudável com o GitHub, prevenindo o bloqueio de commits por excesso de tamanho e organizando estritamente nosso fluxo em cima de textos e conhecimentos reais, e não mídia pesada.

## ⚠️ Problemas Resolvidos
- Quebra de *push* com arquivos grandes (.mp4, .pdf).
- Passar o Limite rígido de 100MB do GitHub.
- Repositório (*Pack*) acima de 2GB tornando tudo lento e instável.
- Falha na sincronização misturando notas ativas com mídias inutilizadas.

## 👉 Objetivos da Sincronização
✔ **Versionar apenas o que importa:** O foco é registrar conhecimento e organização estrutural (textos, Canvas).
✔ **Ignorar pesos / lixos temporários:** Ignorar vídeos, aúdios, PDFs, compactados e cache do sistema.
✔ **Manter sinc automátca:** Deixar o Git leve o bastante para pushes rápidos diários.
✔ **Evitar erros:** Previne o cenário onde um grande PDF impede todo o progresso de ser salvo.

---

## 🧠 Regra de Ouro
> **O Git NÃO é para armazenar mídia pesada! O Git é exclusivamente para texto, histórico de revisões e gestão de conhecimento puro.**

---

## ✅ Padrão Ouro do `.gitignore`

Manter um `.gitignore` configurado na raiz do Vault previne a adição de materiais prejudiciais:

1. **Ignorar mídia por extensão crítica:** `*.mp4`, `*.pdf`, `*.zip`, `.mp3`.
2. **Ignorar mídias em fluxo (opcional mas recomendado):** `*.png`, `*.jpg`, `*.webp`.
3. **Ignorar lixo do framework:** `.DS_Store`, subpastas de `.obsidian/` como caches, pacotes e workspaces temporários.
4. **Abrir uma exceção para Conhecimento!** Regras como `!README.md`, `!*.md` e `!*.canvas` garantem que, independente de diretórios filtrados, o que for texto rico seja adicionado.

---

## 🔥 Limpeza Profissional Recomendada (Passo Inicial e de Manutenção Crítica)

Para forçar um repo já "contaminado" com mídias pesadas na árvore atual a obedecer essa triagem ou limpar seu diretório:

```bash
# Sincroniza a exclusão e limpa os arquivos localmente do index (mantendo do disco do PC):
// turbo-all
git rm -r --cached .

# Re-adiciona somente os não ignorados (o novo filtro em ação):
git add .

# Registra a alteração do bypass
git commit -m "chore: Limpeza profissional - removendo arquivos pesados do versionamento"

# Subindo e forçando essa limpeza no histórico central:
git push origin main --force
```

**Instruções para a Tropa Editorial:** 
Qualquer *push* que trave com "Large files detected" (Erro GH001), deve ser corrigido imediatamente atualizando a lista de exceções do `.gitignore` e rodando esta "Limpeza Obrigatória" listada acima.
