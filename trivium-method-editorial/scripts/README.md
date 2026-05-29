# Scripts — Trivium Method Editorial

Scripts de automação, geração e manutenção do framework editorial.
Organizados por responsabilidade para facilitar localização e reutilização.

---

## Mapa de pastas

```
scripts/
├── generation/        Geração de aulas e materiais curriculares em massa
├── sync/              Sincronização de títulos entre currículo macro e arquivos
├── github/            Criação e atualização de issues e tickets no GitHub Projects
├── validation/        Auditoria e verificação de consistência curricular
├── converters/        Conversão de formatos e blocos de conteúdo
├── formatters/        Correção de formatação Markdown em lote
├── image-generation/  Geração de imagens via API (Gemini, Pollinations)
└── examples/          Arquivos de exemplo e dados de entrada para scripts
```

---

## generation/

Scripts que geram conteúdo novo a partir de dados estruturados.

| Script | Quando usar |
|---|---|
| `generate_lessons.py` | Gerar arquivos x.1, x.2, x.3 e x.4 de uma semana a partir de YAML. Principal script de produção em massa. |
| `generate_descriptions.py` | Recriar do zero o arquivo `6 - Descrições para tickets`. Usar apenas em caso de perda total do arquivo. |
| `year1_objectives.json` | Dados de objetivos do 1º ano. Entrada para scripts de geração. |

Uso do gerador de aulas:

```bash
# Gerar todas as aulas de uma semana
python generation/generate_lessons.py examples/semana_exemplo.yaml

# Gerar só uma aula específica
python generation/generate_lessons.py dados_semana3.yaml --apenas x1

# Gerar arquivo YAML de exemplo
python generation/generate_lessons.py --exemplo > minha_semana.yaml
```

---

## sync/

Scripts de sincronização entre o currículo macro e os demais arquivos.
O currículo macro é a fonte de verdade — nunca o contrário.

| Script | Responsabilidade |
|---|---|
| `sync_titles.py` | Script mestre. Atualiza Matriz, Visão, Descrições e H1 dos `.md` de aula a partir do macro. Usar sempre que um título mudar. |
| `align_titles.py` | Sincroniza isoladamente o arquivo de Tickets (descrições gerais). |
| `align_review_titles.py` | Sincroniza as menções de aulas dentro dos blocos de revisão no arquivo de Tickets. |
| `fix_lesson_h1.py` | Corrige o H1 de cada arquivo individual de aula. |
| `fix_titles.py` | Remove sufixos indesejados nos blocos de Revisão e Prova do arquivo de Tickets. |

Uso do script mestre:

```bash
# Sincronizar todos os títulos a partir do currículo macro
python sync/sync_titles.py
```

---

## github/

Scripts de integração com GitHub Issues e GitHub Projects.
Requerem token configurado via variável de ambiente `GITHUB_TOKEN`.

| Script | Disciplina / escopo |
|---|---|
| `create_issues.py` | Criador genérico de issues por disciplina e ano |
| `create_issues_biblia3.py` | Issues para Bíblia 3º ano |
| `create_issues_english1.py` | Issues para Inglês 1º ano |
| `create_issues_matematica5.py` | Issues para Matemática 5º ano |
| `build_year1_tickets.py` | Constrói tickets do 1º ano |
| `sync_issues_week13.py` | Sincroniza issues da semana 13 |
| `update_backlog_tickets.py` | Atualiza tickets no backlog do projeto |
| `update_github_issues_to_year1.py` | Migra issues para o formato do 1º ano |
| `update_tickets_fixed.py` | Corrige e reatualiza tickets existentes |
| `update_year1_tickets.py` | Atualiza tickets do 1º ano |

---

## validation/

Scripts de auditoria. Apenas leem e reportam — não alteram arquivos.

| Script | O que verifica |
|---|---|
| `check_matriz.py` | Divergências entre Matriz-Curricular e Currículo Macro |
| `check_project_items.py` | Itens e campos do projeto no GitHub Projects |

Uso:

```bash
# Auditar matriz sem alterar nada
python validation/check_matriz.py
```

---

## converters/

Scripts de conversão em lote de formatos de blocos de conteúdo.

| Script | O que converte |
|---|---|
| `convert_recordar.py` | Blocos "Recordar" do 3º ano de Música para Rimas Contextuais, injetando as estrofes |
| `convert_recordar_to_rhyme.py` | Utilitário auxiliar: extrai definições e verifica presença de blocos de música |

---

## formatters/

Scripts de correção de formatação Markdown aplicada em lote.

| Script | O que corrige |
|---|---|
| `fix_accordion.py` | Definições no bloco Accordion das aulas do 4º ano — remove repetições redundantes do termo em negrito |

---

## image-generation/

Scripts de geração de imagens via API.
Requerem chave de API configurada no `.env` (`GEMINI_API_KEY` ou `POLLINATIONS_KEY`).

| Script | Função |
|---|---|
| `generate_image.py` | Gerador principal de imagens a partir de prompt |
| `generate_image_temp.py` | Versão experimental para testes de prompt |
| `diagnose_gemini_api.py` | Diagnóstico de erros e conectividade da API Gemini |
| `list_models.py` | Lista modelos disponíveis na API configurada |
| `test_gemini_quick.py` | Teste rápido de autenticação e resposta da API |
| `verify_setup.py` | Verifica se o setup de geração está correto antes de rodar |

---

## examples/

Arquivos de dados de referência e exemplos de entrada para scripts.

| Arquivo | Uso |
|---|---|
| `semana_exemplo.yaml` | YAML de exemplo preenchido para `generate_lessons.py`. Copiar e editar para cada semana nova. |

---

## Referências

- Currículo macro: fonte de verdade para todos os títulos
- Workflow de produção: `trivium-method-editorial/workflows/produce_class.md`
- Template de aula: `trivium-method-editorial/templates/padrao_final_aula.md`
- Scripts do projeto (raiz): `scripts/` — geração de pipeline, publicação no GitHub e ferramentas de apoio ao produto
