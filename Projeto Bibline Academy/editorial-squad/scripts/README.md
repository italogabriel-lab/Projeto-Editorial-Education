# 🛠️ Editorial Squad Scripts

Este diretório contém todos os scripts de automação e sincronização usados pelos agentes da Squad Editorial para manter o currículo perfeitamente alinhado com a **Fonte de Verdade** (`1 - Curriculo Macro`).

> **Regra de Ouro**: O Orquestrador e o DevOps devem consultar este repositório para automatizar consertos e evitar o desalinhamento de títulos e matrizes.

## Catálogo de Scripts

### SCRIPT MESTRE (Principal)
- **`sync_titles.py`**
  - **Uso:** SEMPRE que houver qualquer mudança no título de uma aula ou estrutura no Curriculo Macro.
  - **Função:** Script mestre e unificado. Ele lê as dezenas de títulos do Currículo Macro e atualiza automaticamente todos os outros arquivos (`2 - Matriz`, `3 - Visão`, `6 - Descrições` e os `H1` dos `.md` de aula).

### Scripts de Auditoria & Limpeza
- **`check_matriz.py`**
  - **Uso:** Quando quiser apenas **auditar** (verificar sem alterar) se a Matriz-Curricular está sincronizada com o Macro.
  - **Função:** Lê o Macro e a Matriz e lista as divergências encontradas.
- **`fix_titles.py`**
  - **Uso:** Para formatação cosmética, caso sufixos indesejados ("- Theme") apareçam nos blocos de Revisão/Prova no arquivo de Tickets.
  - **Função:** Roda regex e limpa o documento de descrições.

### Scripts Modulares (Substituídos pelo mestre, mantidos para uso isolado)
- **`align_titles.py`**
  - **Uso:** Apenas se quiser sincronizar isoladamente o arquivo de Tickets (descrições gerais).
- **`align_review_titles.py`**
  - **Uso:** Apenas se quiser sincronizar isoladamente a menção das aulas base dentro dos blocos de revisão do arquivo de Tickets.
- **`fix_lesson_h1.py`**
  - **Uso:** Apenas se quiser arrumar o H1 de dentro de cada arquivo individual de aula (`X.Y.md`).

### Geradores Massivos
- **`generate_descriptions.py`**
  - **Uso:** Em caso de perda total ou necessidade de refazer do zero a estrutura do arquivo `6 - Descrições para tickets`. 
  - **Função:** Tem toda as semanas hardcoded e injeta marcadores de 1º Bimestre, Módulo Final, Revisões, etc. (Cuidado: reescreve o documento inteiro).
