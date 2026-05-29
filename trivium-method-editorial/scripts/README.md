# Scripts — Trivium Method Editorial

Scripts de automação, geração e manutenção do framework editorial.

## Estrutura de pastas

```
scripts/
├── generation/        Geração de conteúdo em massa
├── sync/              Sincronização e correção de títulos
├── github/            Integração com GitHub Issues e Projects
├── validation/        Auditoria e verificação de consistência
├── converters/        Conversão de formatos e blocos de conteúdo
├── formatters/        Correção de formatação Markdown
├── image-generation/  Geração de imagens via API
└── examples/          Arquivos de exemplo e dados de referência
```

---

## generation/

Scripts de geração de conteúdo estruturado.

- **`generate_lessons.py`** — Gera arquivos x.1, x.2, x.3 e x.4 a partir de um YAML de dados da semana. Aplicar ao criar aulas novas em massa. Uso: `python generate_lessons.py dados_semana.yaml`
- **`generate_descriptions.py`** — Gera do zero o arquivo `6 - Descrições para tickets` com todas as semanas. Usar apenas em caso de perda total do arquivo.
- **`year1_objectives.json`** — Dados de objetivos do 1º ano usados como entrada em scripts de geração.

Exemplo de dados: `examples/semana_exemplo.yaml`

---

## sync/

Scripts de sincronização e correção de títulos entre currículo macro e arquivos de aula.

- **`sync_titles.py`** — Script mestre. Lê o Currículo Macro e atualiza Matriz, Visão, Descrições e H1 dos `.md` de aula. Usar sempre que um título mudar no macro.
- **`align_titles.py`** — Sincroniza isoladamente o arquivo de Tickets (descrições gerais).
- **`align_review_titles.py`** — Sincroniza as menções de aulas nos blocos de revisão do arquivo de Tickets.
- **`fix_lesson_h1.py`** — Corrige o H1 de cada arquivo individual de aula.
- **`fix_titles.py`** — Remove sufixos indesejados nos blocos de Revisão/Prova do arquivo de Tickets.

---

## github/

Scripts de criação e atualização de issues e tickets no GitHub Projects.

- **`create_issues.py`** — Criador genérico de issues por disciplina e ano.
- **`create_issues_biblia3.py`** — Issues para Bíblia 3º ano.
- **`create_issues_english1.py`** — Issues para Inglês 1º ano.
- **`create_issues_matematica5.py`** — Issues para Matemática 5º ano.
- **`build_year1_tickets.py`** — Constrói tickets do 1º ano.
- **`sync_issues_week13.py`** — Sincroniza issues da semana 13.
- **`update_backlog_tickets.py`** — Atualiza tickets no backlog.
- **`update_github_issues_to_year1.py`** — Migra issues para o formato do 1º ano.
- **`update_tickets_fixed.py`** — Corrige e atualiza tickets existentes.
- **`update_year1_tickets.py`** — Atualiza tickets do 1º ano.

---

## validation/

Scripts de auditoria e verificação de consistência.

- **`check_matriz.py`** — Audita (sem alterar) se a Matriz-Curricular está sincronizada com o Macro.
- **`check_project_items.py`** — Verifica itens do projeto no GitHub Projects.

---

## converters/

Scripts de conversão de formatos de blocos de conteúdo.

- **`convert_recordar.py`** — Converte blocos "Recordar" do 3º ano de Música para Rimas Contextuais.
- **`convert_recordar_to_rhyme.py`** — Utilitário para extrair definições e verificar presença de blocos de música.

---

## formatters/

Scripts de correção de formatação Markdown corrompida ou sistemática.

- **`fix_accordion.py`** — Corrige definições no bloco Accordion das aulas do 4º ano.

---

## image-generation/

Scripts de geração de imagens via API (Gemini, Pollinations).

- **`generate_image.py`** — Gerador principal de imagens.
- **`generate_image_temp.py`** — Versão temporária/experimental.
- **`diagnose_gemini_api.py`** — Diagnóstico da API Gemini.
- **`list_models.py`** — Lista modelos disponíveis.
- **`test_gemini_quick.py`** — Teste rápido da API.
- **`verify_setup.py`** — Verificação do setup de geração.
