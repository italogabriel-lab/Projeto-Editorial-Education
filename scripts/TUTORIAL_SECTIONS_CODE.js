// ============================================================================
// TUTORIAL VIEWER - COURSE-STYLE DOCS (10 SECTIONS - COMPREHENSIVE)
// Substitua o array tutorialSections no agent-command-center.html por este
// ============================================================================

const tutorialSections = [

// ============================================================================
// SECAO 1 — VISAO GERAL DO PROJETO
// ============================================================================
{id:'overview',number:1,title:'Visao Geral do Projeto',icon:'<i class="ph ph-target"></i>',color:'#2dd4bf',content:`
<h2><i class="ph ph-target" style="color:var(--accent-primary);margin-right:0.5rem;"></i> 1. Visao Geral do Projeto Editorial</h2>

<div class="tutorial-content-section">
<h3>O que e o Trivium Method?</h3>
<p>O <strong>Trivium Method</strong> e o sistema completo de producao, gestao e publicacao de conteudo educacional da <strong>Bibline Academy</strong>. Ele foi projetado para criar aulas de alta qualidade alinhadas a <strong>Educacao Classica Crista</strong> e ao <strong>Trivium</strong>, utilizando agentes de IA especializados, pipelines automatizados e dashboards em tempo real.</p>
<p>Imagine uma linha de montagem editorial onde cada etapa tem um especialista dedicado, tudo e documentado, e o progresso e visivel em tempo real. Isso e o Trivium Method.</p>
</div>

<div class="tutorial-content-section">
<h3>Objetivo do Projeto</h3>
<p>O Trivium Method existe para prover uma estrutura <strong>escalavel e reproduzivel</strong> que permita:</p>
<ul>
<li>Producao de aulas no formato <strong>Rise 360</strong> (Articulate)</li>
<li>Revisao e padronizacao de conteudo com <strong>QA rigoroso</strong></li>
<li>Gestao de pipeline editorial via <strong>GitHub Projects Kanban</strong></li>
<li>Analytics e acompanhamento de producao em tempo real</li>
<li>Automacao de workflows via <strong>GitHub Actions</strong></li>
</ul>
</div>

<div class="tutorial-content-section">
<h3>Arquitetura de Alto Nivel</h3>
<p>O ecossistema e composto por <strong>5 camadas interdependentes</strong>:</p>
<div class="tutorial-code-block">+------------------------------------------------------------------+
|                      ORQUESTRACAO                                |
|          orchestrator/SKILL.md  +  orchestrate.md                |
|    (Diagnostico de progresso, priorizacao, delegacao)            |
+------------------------------------------------------------------+
         |                    |                    |
         v                    v                    v
+------------------+  +------------------+  +------------------+
|   PRODUCAO       |  |  POS-PRODUCAO    |  |  PUBLICACAO      |
|  (Pipeline 7     |  | (Revisoes        |  | (Versionamento   |
|   etapas)        |  |  Bimestrais +    |  |  e GitHub)       |
|                  |  |  Provas)         |  |                  |
|  produce_class   |  | bimester-review  |  |  publisher +     |
|  .md             |  | bimester-exam    |  |  devops +        |
+------------------+  +------------------+  |  publish.md      |
                                            +------------------+
         |                    |                    |
         v                    v                    v
+------------------------------------------------------------------+
|                   AUTOMACAO (Scripts Python)                      |
|   sync_titles.py  |  check_matriz.py  |  generate_descriptions   |
|   align_titles.py |  fix_accordion.py |  convert_recordar.py     |
+------------------------------------------------------------------+
         |
         v
+------------------------------------------------------------------+
|                   BASE DE CONHECIMENTO                           |
|   doutrina-pedagogica  |  guia-de-estilo  |  rise-blocks-ref     |
|   Golden Template      |  Templates por Habito                   |
+------------------------------------------------------------------+</div>
</div>

<div class="tutorial-content-section">
<h3>Fluxo de Dados (Data Flow)</h3>
<div class="tutorial-code-block">[GitHub Projects Kanban] (bibline/org - Project V2)
         |
         | GraphQL API (cron 5 min)
         v
[GitHub Actions: data-sync.yml] (node src/sync.js)
         |
         | Gera public/data.json
         v
[Commit automatico se mudou] (atomic diff check)
         |
         | Push para main
         v
[GitHub Pages Deploy] (deploy-pages.yml)
         |
         | Live URL:
         v
https://italogabriel-lab.github.io/Projeto-Editorial-Education/
         |
         +-- Overview Geral
         +-- Metas (Curriculo)
         +-- Metas (Disciplinas) + Year Health
         +-- Videos Pipeline
         +-- Agent Command Center</div>
</div>

<div class="tutorial-content-section">
<h3>Principais Metricas do Framework</h3>
<div class="tutorial-metrics-grid">
<div class="metric-card"><div class="metric-value">22</div><div class="metric-label">Agentes Ativos (18 operacionais + 4 legacy)</div></div>
<div class="metric-card"><div class="metric-value">7</div><div class="metric-label">Etapas no Pipeline Editorial</div></div>
<div class="metric-card"><div class="metric-value">21</div><div class="metric-label">Skills Registradas</div></div>
<div class="metric-card"><div class="metric-value">5</div><div class="metric-label">Categorias de Agentes</div></div>
<div class="metric-card"><div class="metric-value">~4,200</div><div class="metric-label">Aulas Planejadas (5 disciplinas x 5 anos x 168)</div></div>
<div class="metric-card"><div class="metric-value">168</div><div class="metric-label">Meta de Aulas por Disciplina/Ano</div></div>
<div class="metric-card"><div class="metric-value">2-3</div><div class="metric-label">Lead Time Medio (dias por aula)</div></div>
<div class="metric-card"><div class="metric-value">~9</div><div class="metric-label">Throughput (aulas/semana por autor)</div></div>
</div>
</div>

<div class="tutorial-content-section">
<h3>Calculo das ~4,200 Aulas</h3>
<div class="tutorial-code-block">5 disciplinas (Belas Artes, Ciencias, Geografia, Historia, Portugues)
x 5 anos (1o ao 5o ano da Fase da Gramatica)
x ~168 aulas/ano (40 semanas x 3 aulas/semana + revisoes + provas)
= ~4,200 aulas totais planejadas</div>
</div>

<div class="tutorial-content-section">
<h3>Principios de Design do Framework</h3>
<ul>
<li><strong>Modularidade:</strong> Agentes independentes e especializados. Cada agente faz uma coisa bem feita.</li>
<li><strong>Automatizacao:</strong> Workflows repetiveis, scripts de automacao, GitHub Actions para deploy.</li>
<li><strong>Documentacao:</strong> 100% dos agentes documentados com SKILL.md, exemplos de uso.</li>
<li><strong>Qualidade:</strong> Revisao em multiplas etapas, QA rigoroso, padroes consistentes.</li>
<li><strong>Escalabilidade:</strong> Estrutura que cresce com a equipe. Novos agentes podem ser adicionados.</li>
</ul>
</div>

<div class="tutorial-content-section">
<h3>Filosofia Pedagogica Subjacente</h3>
<p>O Trivium Method e fundamentado em tres pilares:</p>
<ol>
<li><strong>Trivium Classico:</strong> Gramatica (fatos, definicoes, memorizacao), Logica (relacoes, raciocinio), Retorica (expressao, aplicacao, sabedoria). Todas as aulas atuais estao na <strong>Fase da Gramatica</strong> (7-11 anos).</li>
<li><strong>Cosmovisao Crista Reformada:</strong> Centralidade de Deus, autoridade das Escrituras, educacao como discipulado, excelencia como adoracao.</li>
<li><strong>5 Habitos da Gramatica:</strong> Definir, Perceber, Recordar, Praticar, Narrar — a estrutura de cada aula.</li>
</ol>
</div>
`},

// ============================================================================
// SECAO 2 — ESTRUTURA DE ARQUIVOS
// ============================================================================
{id:'structure',number:2,title:'Estrutura de Arquivos',icon:'<i class="ph ph-folder"></i>',color:'#67e8f9',content:`
<h2><i class="ph ph-folder" style="color:var(--accent-primary);margin-right:0.5rem;"></i> 2. Estrutura Completa de Arquivos</h2>

<div class="tutorial-content-section">
<h3>Visao Geral da Arvore de Diretorio</h3>
<p>O projeto e organizado em camadas: UI publica na raiz, engine de sync no <code>src/</code>, dados no <code>public/</code>, workflows CI/CD no <code>.github/</code>, framework no <code>trivium-method/</code>, e operacoes editoriais no <code>Projeto Bibline Academy/editorial-squad/</code>.</p>
</div>

<div class="tutorial-content-section">
<h3>Root Level (Vision Board UI)</h3>
<div class="tutorial-code-block">Projeto-Editorial-Education/
│
├── index.html                      # Landing page / Overview do projeto
├── metas.html                      # Metas do Curriculo (tracking geral)
├── metas-disciplinas.html          # Metas por Disciplina + Year Health Feature
├── videos.html                     # Pipeline de Videos (tracking de producao)
├── agent-command-center.html       # Centro de Comando dos Agentes (5300+ linhas)
│                                   # Mostra 22 agentes, workflow, performance
│
├── vercel.json                     # Configuracao Vercel (static HTML hosting)
├── .gitignore                      # Exclui node_modules, media, caches
├── README.md                       # Documentacao master do Framework Trivium Method
├── QUICK_REFERENCE.md              # URLs rapidas e comandos uteis
├── requirements.txt                # Python dependencies (requests, etc.)
├── query.graphql                   # GraphQL query para sync do Kanban
└── test-*.js                       # Scripts de teste (GraphQL, producao)</div>
</div>

<div class="tutorial-content-section">
<h3>public/ — Dashboard Data &amp; Scripts</h3>
<div class="tutorial-code-block">public/
├── data.json                       # Dados LIVE do Kanban (auto-generated pelo sync)
│                                   # Contem: last_updated, total_items, items[]
│                                   # Cada item: id, number, title, status, assignee, labels
│
├── app.js                          # Logica do dashboard principal (index.html)
├── sidebar.js                      # Navegacao sidebar do dashboard
├── styles.css                      # Estilos globais do Vision Board
├── metas.js                        # Logica da pagina Metas (metas.html)
├── metas-disciplinas.js            # Metas por disciplina + Year Health
└── videos.js                       # Logica da pagina Videos Pipeline</div>
</div>

<div class="tutorial-content-section">
<h3>src/ — Sync Engine</h3>
<div class="tutorial-code-block">src/
└── sync.js                         # Core sync engine
                                    # Consulta GitHub Projects via GraphQL
                                    # Extrai todos os items com paginacao
                                    # Parse subject/year de titulos
                                    # Calcula lead time (created_at → closed_at)
                                    # Gera public/data.json</div>
</div>

<div class="tutorial-content-section">
<h3>.github/workflows/ — CI/CD</h3>
<div class="tutorial-code-block">.github/workflows/
│
├── deploy-pages.yml                # Deploy para GitHub Pages
│                                   # Trigger: push para main (paths: *.html, public/**)
│                                   # Jobs: Build (valida) → Deploy (upload pages)
│                                   # Output: https://italogabriel-lab.github.io/...
│
└── data-sync.yml                   # Vision Board Live Sync
                                    # Trigger: cron */5 * * * * (a cada 5 min)
                                    # Token: VISIONBOARDBIBLINE (PAT com repo + project)
                                    # Project ID: PVT_kwDODLv1ac4BH1XW
                                    # Jobs: Checkout → Sync → Verify → Commit &amp; Push
                                    # Mensagem: "data: sync Kanban - N items (auto-sync)"
                                    # SLA: ~3-4 minutos total</div>
</div>

<div class="tutorial-content-section">
<h3>trivium-method/ — Trivium Method (Canonical Reference)</h3>
<div class="tutorial-code-block">trivium-method/
├── README.md                       # Documentacao do framework Trivium Method
│
├── core/                           # Nucleo do framework
│   ├── README.md                   # Doc do core
│   └── constants.js                # Constantes e configuracoes
│
├── agents/                         # Definicoes de agentes (referencia)
│   ├── core/                       # 6 agentes do fluxo principal
│   ├── specialized/                # 4 agentes especializados
│   ├── analytics/                  # 4 agentes de analytics
│   ├── bimester/                   # 2 agentes bimestrais
│   └── legacy/                     # 4 agentes legados
│
├── workflows/                      # Definicoes de workflows (referencia)
├── knowledge-base/                 # Base de conhecimento (referencia)
├── templates/                      # Templates de conteudo (referencia)
├── scripts/                        # Scripts de automacao (referencia)
└── reports/                        # Relatorios gerados</div>
</div>

<div class="tutorial-content-section">
<h3>Projeto Bibline Academy/editorial-squad/ — Operational Hub</h3>
<p><strong>Este e o coracao operacional do projeto.</strong> Todos os agentes ativos, workflows, scripts e templates de producao vivem aqui:</p>
<div class="tutorial-code-block">Projeto Bibline Academy/editorial-squad/
│
├── AGENTS-DOCUMENTATION.md         # Documentacao central de todos os agentes
├── DOCUMENTATION-PLAN.md           # Plano de documentacao do projeto
│
├── skills/                         # 20 skills de agentes ATIVOS
│   ├── orchestrator/SKILL.md       # Diretor editorial (diagnostica e delega)
│   ├── researcher/SKILL.md         # Pesquisa de conteudo (Etapa 1)
│   ├── writer/SKILL.md             # Redacao de aulas (Etapa 2)
│   ├── standardizer/SKILL.md       # Padronizacao Rise Blocks (Etapa 3)
│   ├── capitalizer/SKILL.md        # Capitalizacao europeia (Etapa 3 sub-passo)
│   ├── reviewer/SKILL.md           # Revisao e QA (Etapa 4)
│   ├── copywriter/SKILL.md         # Polimento final (Etapa 5)
│   ├── publisher/SKILL.md          # Publicacao local + GitHub (Etapa 7)
│   ├── design-thinking/SKILL.md    # UX research, personas, wireframes
│   ├── ui-designer/SKILL.md        # Design systems, componentes responsivos
│   ├── devops/SKILL.md             # Gatekeeper de repositorio, .gitignore
│   ├── performance-analytics/      # Analise de produtividade individual/equipe
│   ├── vision-bottleneck-detector/ # Detector de gargalos no pipeline
│   ├── vision-github-analyzer/     # Analise de dados GitHub
│   ├── vision-progress-engine/     # Engine de tracking de progresso
│   ├── bimester-exam-builder/      # Provas bimestrais (semanas 10,20,30,40)
│   ├── bimester-review-builder/    # Revisoes bimestrais (semanas 9,19,29,39)
│   ├── exam-builder/               # Legacy: construtor de quizzes
│   ├── review-builder/             # Legacy: construtor de revisoes
│   └── image-link-extractor/       # Legacy: extrator de imagens
│
├── workflows/                      # Workflows operacionais
│   ├── produce_class.md            # Pipeline de 7 etapas (documento mestre)
│   ├── publish.md                  # Workflow de publicacao Git
│   └── orchestrate.md              # Ativacao do Orchestrator
│
├── knowledge-base/                 # Base de conhecimento ativa
│   ├── visao-geral-fluxo-editorial.md   # Mapa editorial master (572 linhas)
│   ├── doutrina-pedagogica.md           # Fundacao teologica/filosofica
│   ├── guia-de-estilo.md                # Guia de estilo editorial
│   ├── rise-blocks-reference.md         # Referencia blocos Rise 360 (12 blocos)
│   └── relatorio-vision-board-projeto.md
│
├── templates/                      # Templates de aula
│   ├── padrao_final_aula.md        # Golden Template (esqueleto oficial)
│   ├── exemplo_aula_final.md       # Exemplo concreto do Golden Template
│   ├── defining.md                 # Template do habito "Definir"
│   ├── perceiving.md               # Template do habito "Perceber"
│   ├── remembering.md              # Template do habito "Recordar"
│   ├── practicing.md               # Template do habito "Praticar"
│   └── narrating.md                # Template do habito "Narrar"
│
├── scripts/                        # 18+ scripts Python de automacao
│   ├── README.md                   # Catalogo de scripts
│   ├── sync_titles.py              # MASTER: Sincroniza titulos do Macro
│   ├── align_titles.py             # Alinha titulos em tickets
│   ├── align_review_titles.py      # Alinha referencias de review
│   ├── fix_lesson_h1.py            # Corrige headers H1
│   ├── fix_titles.py               # Limpa sufixos cosmeticos
│   ├── check_matriz.py             # Audit: Matriz vs Macro
│   ├── generate_descriptions.py    # Regenera descricoes em massa (DESTRUTIVO)
│   ├── create_issues.py            # Cria issues no GitHub
│   ├── update_github_issues_to_year1.py
│   ├── update_backlog_tickets.py
│   ├── update_year1_tickets.py
│   ├── update_tickets_fixed.py
│   ├── build_year1_tickets.py
│   ├── sync_issues_week13.py
│   ├── check_project_items.py
│   ├── year1_objectives.json
│   ├── converters/
│   │   ├── convert_recordar.py     # Converte musica → rima (3o ano)
│   │   └── convert_recordar_to_rhyme.py  # Audit: quais aulas precisam
│   └── formatters/
│       └── fix_accordion.py        # Corrige redundancia accordion (4o ano)
│
└── reports/                        # Relatorios gerados</div>
</div>

<div class="tutorial-content-section">
<h3>Projeto Bibline Academy/ — Curriculum Vault</h3>
<p>Aqui vive o conteudo curricular propriamente dito:</p>
<div class="tutorial-code-block">Projeto Bibline Academy/
├── .env                            # Variaveis de ambiente (tokens, secrets)
│
├── setup-playbook/                 # Configuracao de ambiente
│   ├── README.md
│   ├── 01-deployment/vercel.md
│   ├── 02-integrations/
│   │   ├── ai-image-generation.md
│   │   ├── github-actions-sync.md
│   │   └── github-mcp.md
│   ├── 07-environment/env-setup.md
│   └── 08-agents/python-automation.md
│
├── .agent/                         # Configuracao de agente de IA
│   ├── workflows/
│   │   ├── create-lesson.md
│   │   ├── create-macro.md
│   │   ├── create-matriz.md
│   │   ├── create-vision.md
│   │   ├── full-pipeline.md
│   │   └── publish.md
│   └── knowledge-base/
│
├── Base de Conhecimento/           # Base de conhecimento expandida
│   └── 2-Base de Conhecimento/
│       ├── Referencias Literarias e Livros Vivos.md
│       ├── Obras de Arte e Autores Classicos.md
│       ├── Pontos de Atencao para Revisao.md
│       ├── Principais erros da IA.md
│       ├── 13-Style conventions.md
│       ├── 12-Structuring the content.md
│       └── 14-Structuring the Review.md
│
└── Belas Artes - Fase da Gramatica/  # Conteudo curricular
    └── 1 Fase - Gramatica/
        ├── 1o Ano - ARTE CRISTA PRIMITIVA E ICONES BIZANTINOS/
        ├── 2o Ano - DA CRIACAO ATE A ARTE BIZANTINA/
        ├── 3o Ano - RENASCIMENTO E REFORMA/
        ├── 4o Ano - BARROCO ATE O NEOCLASSICISMO/
        └── 5o Ano - MANEIRISMO ATE O REALISMO AMERICANO/
            └── Estrutura Curricular/
                ├── 0 - Movimentos Artisticos trabalhados.md
                ├── 1 - Curriculo Macro - *.md         # FONTE DA VERDADE
                ├── 2 - Matriz-Curricular-objetivos - *.md
                ├── 3 - Visao e Plano pedagogico - *.md
                ├── 4 - Links-para-imagens-perceber - *.md
                ├── 5 - Prompts-para-imagens-narrar - *.md
                └── 6 - Descricoes para tickets.md</div>
</div>

<div class="tutorial-content-section">
<h3>Arquivos Estruturais por Ano (Explicacao)</h3>
<table class="tutorial-table">
<thead><tr><th>Arquivo</th><th>Funcao</th><th>Aplicavel a</th></tr></thead>
<tbody>
<tr><td><code>0 - Movimentos Artisticos</code></td><td>Lista de movimentos cobertos no ano</td><td>Todos os anos</td></tr>
<tr><td><code>1 - Curriculo Macro</code></td><td><strong>FONTE DA VERDADE</strong> para titulos e sequencia</td><td>Todos os anos</td></tr>
<tr><td><code>2 - Matriz-Curricular-objetivos</code></td><td>Objetivos pedagogicos por aula</td><td>Todos os anos</td></tr>
<tr><td><code>3 - Visao e Plano pedagogico</code></td><td>Narrativa e progressao pedagogica</td><td>Todos os anos</td></tr>
<tr><td><code>4 - Links-para-imagens-perceber</code></td><td>Links de banco de imagens para Perceber</td><td>Apenas 3o ano</td></tr>
<tr><td><code>5 - Prompts-para-imagens-narrar</code></td><td>Prompts de geracao de imagem para Narrar</td><td>Apenas 3o ano</td></tr>
<tr><td><code>6 - Descricoes para tickets</code></td><td>Descricoes de tarefas para gestao de projetos</td><td>Apenas Arte</td></tr>
</tbody>
</table>
</div>

<div class="tutorial-content-section">
<h3>Regra de Ouro: Curriculo Macro como Fonte da Verdade</h3>
<div class="tutorial-info-card">
<strong>REGRA ABSOLUTA:</strong> O arquivo <code>1 - Curriculo Macro</code> e a UNICA FONTE OFICIAL dos titulos de cada aula. Todos os demais arquivos devem usar EXATAMENTE os mesmos titulos do Macro. Se um titulo precisa ser alterado, a mudanca deve ser feita PRIMEIRO no Curriculo Macro e depois propagada para todos os demais arquivos (manualmente ou via <code>sync_titles.py</code>).
</div>
</div>
`},

// ============================================================================
// SECAO 3 — 22 AGENTES DETALHADOS
// ============================================================================
{id:'agents',number:3,title:'22 Agentes Detalhados',icon:'<i class="ph ph-robot"></i>',color:'#8b5cf6',content:`
<h2><i class="ph ph-robot" style="color:var(--accent-primary);margin-right:0.5rem;"></i> 3. Os 22 Agentes Detalhados</h2>

<div class="tutorial-content-section">
<h3>Mapa Geral dos Agentes por Categoria</h3>
<p>O Trivium Method possui <strong>22 agentes</strong> organizados em 5 categorias. Cada agente e definido por um arquivo <code>SKILL.md</code> que contem persona, atribuicoes, inputs, outputs e regras de operacao.</p>
<div class="tutorial-code-block">CATEGORIA              | AGENTES | STATUS
-----------------------|---------|--------
Core Pipeline          |    7    | Ativo
Specialized            |    4    | Ativo
Analytics (Vision)     |    4    | Ativo
Bimester               |    2    | Ativo
Legacy (deprecated)    |    4    | Legacy
-----------------------|---------|--------
TOTAL                  |   22    | 18 ativos + 4 legacy</div>
</div>

<div class="tutorial-content-section">
<h3>AGENTE 1: Orchestrator (Diretor Editorial)</h3>
<p><strong>Categoria:</strong> Core Pipeline | <strong>Etapa:</strong> Transversal | <strong>Arquivo:</strong> <code>editorial-squad/skills/orchestrator/SKILL.md</code></p>
<p><strong>Persona:</strong> Diretor Editorial da Squad Bibline. Ponto central de orientacao do projeto. Conhece profundamente cada skill, workflow, regra de sincronizacao e documento da knowledge-base. <strong>Nao executa o trabalho dos outros agentes</strong> — diagnostica, prioriza e delega.</p>

<h4>Atribuicoes Principais:</h4>
<ul>
<li><strong>Diagnostico de Progresso:</strong> Le o Curriculo Macro, conta semanas completas, identifica semana em andamento e proxima semana. Apresenta relatorio executivo.</li>
<li><strong>Priorizacao Inteligente:</strong> Sugere proximas acoes em ordem: (1) Completar semana em andamento, (2) Sincronizar documentos, (3) Publicar no GitHub, (4) Iniciar nova semana.</li>
<li><strong>Delegacao ao Agente Correto:</strong> Usa tabela de roteamento para direcionar usuario ao skill/workflow adequado.</li>
<li><strong>Auditoria de Consistencia:</strong> Verifica titulos H1 vs Macro, definicoes identicas, secao Perceber vs Revisao, links de imagens.</li>
</ul>

<h4>Quando Usar:</h4>
<p>"O que devo fazer agora?", "Como esta o 3o ano?", "Quem cuida disso?", "As aulas estao sincronizadas?"</p>

<h4>Exemplo de Output:</h4>
<div class="tutorial-code-block">STATUS — 3o Ano
Semanas completas: 1-6 (18 aulas + 6 revisoes)
Em andamento: Semana 7 (7.1 OK | 7.2 pendente | 7.3 pendente)
Proxima: Semana 8

PROXIMAS ACOES:
1. Completar aula 7.2 do 3o ano
2. Completar aula 7.3 do 3o ano
3. Criar revisao da semana 7 (X.4)
4. Sincronizar documentos estruturais</div>

<h4>Regras de Ouro:</h4>
<ul>
<li>NUNCA execute o trabalho de outro agente. Diagnostique e delegue.</li>
<li>SEMPRE leia o Curriculo Macro antes de dar qualquer orientacao.</li>
<li>Seja executivo: respostas curtas, formato de lista, sem rodeios.</li>
<li>Priorize completude: semana parcial tem prioridade sobre comecar nova.</li>
<li>Execute <code>sync_titles.py</code> sempre que detectar divergencia de titulos.</li>
</ul>
</div>

<div class="tutorial-content-section">
<h3>AGENTE 2: Researcher (Pesquisador — Etapa 1)</h3>
<p><strong>Categoria:</strong> Core Pipeline | <strong>Etapa:</strong> 1 — Pesquisa | <strong>Arquivo:</strong> <code>editorial-squad/skills/researcher/SKILL.md</code></p>
<p><strong>Persona:</strong> O Investigador. Coleta informacoes profundas, autoritativas e alinhadas a Educacao Classica Crista Reformada.</p>

<h4>Metodologia:</h4>
<ul>
<li><strong>Ad Fontes:</strong> Prioriza fontes primarias e referencias classicas.</li>
<li><strong>Trivium:</strong> Foco na fase da Gramatica (definicoes, fatos, memorizacao).</li>
<li><strong>Cosmovisao Crista:</strong> Conteudo alinhado a perspectiva biblica reformada.</li>
</ul>

<h4>Pre-Requisitos Obrigatorios:</h4>
<ol>
<li>Resolver caminhos do ano (diretorio correto baseado no ano)</li>
<li>Consultar o Plano Pedagogico e extrair tema, visao teologica, progressao</li>
<li>Receber lista de termos proibidos (marcados com check no Curriculo Macro)</li>
</ol>

<h4>Instrucoes de Pesquisa:</h4>
<ul>
<li><strong>Definir:</strong> Definicao Webster 1828, etimologia, parafrase em portugues</li>
<li><strong>Perceber:</strong> Descricao de imagens/obras de arte para secao visual</li>
<li><strong>Recordar:</strong> Versiculo-chave, poema ou hino para memorizacao</li>
<li><strong>Praticar:</strong> Ideias de atividades praticas</li>
<li><strong>Narrar:</strong> Trecho literario com atribuicao do autor (usa DB de autores)</li>
</ul>

<h4>Base de Autores para Narrar (5 categorias):</h4>
<table class="tutorial-table">
<thead><tr><th>Categoria</th><th>Exemplos</th><th>Uso</th></tr></thead>
<tbody>
<tr><td>Pais da Igreja</td><td>Agostinho, Basilio, Irineu</td><td>Fundamento, criacao, beleza</td></tr>
<tr><td>Puritanos</td><td>John Owen, Bunyan, Watson</td><td>Disciplina, contraste moral</td></tr>
<tr><td>Poetas Cristaos</td><td>Herbert, Milton, Rossetti</td><td>Imagem, sensibilidade, simbolo</td></tr>
<tr><td>Autores Modernos</td><td>Lewis, Tolkien, Chesterton</td><td>Tradicao + sensibilidade contemporanea</td></tr>
<tr><td>Artistas Visuais</td><td>Giotto, Rembrandt, Caravaggio</td><td>Composicao, luz, intencao estetica</td></tr>
</tbody>
</table>
</div>

<div class="tutorial-content-section">
<h3>AGENTE 3: Writer (Redator — Etapa 2)</h3>
<p><strong>Categoria:</strong> Core Pipeline | <strong>Etapa:</strong> 2 — Redacao | <strong>Arquivo:</strong> <code>editorial-squad/skills/writer/SKILL.md</code></p>
<p><strong>Persona:</strong> O Escriba. Transforma pesquisa bruta em conteudo pedagogico usando os 5 Habitos da Gramatica.</p>

<h4>Pre-Requisitos Obrigatorios:</h4>
<ol>
<li>Resolver caminhos do ano</li>
<li>Consultar Plano Pedagogico (extrair titulo, tema, versiculo, progressao)</li>
<li>Verificar termos ja definidos (proibidos)</li>
<li>Titulo da aula DEVE ser exatamente o do Curriculo Macro (fonte de verdade)</li>
</ol>

<h4>Regras de Estilo Obrigatorias:</h4>
<ul>
<li>Voz ativa em todas as frases (NUNCA voz passiva)</li>
<li>Imperativo em todos os enunciados: "Observe", "Complete", "Leia"</li>
<li>Frases com maximo 30 palavras</li>
<li>Paragrafos com maximo 70 palavras</li>
<li>Sem <code>;</code>, <code>:</code>, <code>—</code> — usar <code>,</code> ou <code>.</code></li>
<li>Sem aspas curvas — apenas aspas retas</li>
<li>Sem emojis no corpo do texto</li>
<li>Capitalizacao padrao europeu</li>
</ul>

<h4>Framework dos 5 Habitos:</h4>
<ul>
<li><strong>Definir:</strong> Frase 1 "Reconheca que...", Frase 2 "Observe que...", Frase 3 definicao curta, Frase 4 "Veja o video abaixo." + Accordion com pergunta, link_png, MP3, definicao com negrito, reflexao com "Entenda que..."</li>
<li><strong>Perceber:</strong> 3-4 frases no imperativo + Image Labeled com 2 hotspots</li>
<li><strong>Recordar:</strong> "Ouca e repita a definicao abaixo" + Statement_D com definicao curta (9-10 palavras) + Image Text On</li>
<li><strong>Praticar:</strong> Fill_In com enunciado antes + Atividade extra com PDF</li>
<li><strong>Narrar:</strong> Trecho literario entre aspas retas + atribuicao + 3 perguntas com interrogacao</li>
</ul>
</div>

<div class="tutorial-content-section">
<h3>AGENTE 4: Standardizer (Editor de Estilo — Etapa 3)</h3>
<p><strong>Categoria:</strong> Core Pipeline | <strong>Etapa:</strong> 3 — Formatacao | <strong>Arquivo:</strong> <code>editorial-squad/skills/standardizer/SKILL.md</code></p>
<p><strong>Persona:</strong> O Arquiteto. Transforma o rascunho do Writer em conteudo formatado com Rise Blocks.</p>

<h4>Correcoes Editoriais Proativas (ANTES de aplicar blocos):</h4>
<ol>
<li>Conferir titulo H1 com Curriculo Macro (corrigir se divergente)</li>
<li>REMOVER todos <code>;</code>, <code>:</code>, <code>—</code> — substituir por <code>,</code> ou <code>.</code></li>
<li>CONVERTER aspas curvas para aspas retas</li>
<li>REESCREVER voz passiva para voz ativa</li>
<li>GARANTIR imperativo direto em todas as instrucoes</li>
<li>Verificar limites: 30 palavras/frase, 70 palavras/paragrafo</li>
<li>Aplicar capitalizacao padrao europeu (sub-etapa Capitalizer)</li>
</ol>

<h4>12 Rise Blocks Disponiveis:</h4>
<table class="tutorial-table">
<thead><tr><th>Tag</th><th>Uso</th></tr></thead>
<tbody>
<tr><td><code>[+PARAGRAPH]</code></td><td>Texto corrido</td></tr>
<tr><td><code>[+HEADING]</code></td><td>Subtitulos (NUNCA usar H3)</td></tr>
<tr><td><code>[+ACCORDION]</code></td><td>Definicao expandivel com pergunta, imagem, audio, reflexao</td></tr>
<tr><td><code>[+VIDEO]</code></td><td>Placeholder de video (sempre vazio)</td></tr>
<tr><td><code>[MP3/]</code> <code>[MP3\]</code></td><td>Audio com voice ID (#11L:XXXXXXXX)</td></tr>
<tr><td><code>[+IMAGE_LABELED]</code></td><td>Imagem com 2 hotspots (coordenadas percentuais)</td></tr>
<tr><td><code>[+STATEMENT_D]</code></td><td>Definicao com audio para memorizacao</td></tr>
<tr><td><code>[+IMAGE_TEXT_ON]</code></td><td>Imagem com texto sobreposto e audio</td></tr>
<tr><td><code>[+FILL_IN]</code></td><td>Exercicio de completar lacunas (_____)</td></tr>
<tr><td><code>[+ATTACHMENT]</code></td><td>PDF anexo (@link_pdf@)</td></tr>
<tr><td><code>[+IMAGE_TEXT_ASIDE]</code></td><td>Imagem com texto ao lado (Narrar)</td></tr>
<tr><td><code>[+LIST_NUMBERED]</code></td><td>Lista numerada de perguntas (3 perguntas)</td></tr>
</tbody>
</table>

<h4>Regras Fixas do Output:</h4>
<ul>
<li>Sem cabecalhos de metadados</li>
<li>Sem emojis de secao</li>
<li>Sem separadores <code>---</code> entre secoes</li>
<li>Ordem: Definir → Perceber → Recordar → Praticar → Narrar</li>
<li>Todas as tags <code>[+BLOCO]</code> devem ter <code>[-BLOCO]</code> correspondente</li>
</ul>
</div>

<div class="tutorial-content-section">
<h3>AGENTE 5: Capitalizer (Revisor de Capitalizacao — Etapa 3 sub-passo)</h3>
<p><strong>Categoria:</strong> Specialized | <strong>Etapa:</strong> 3 (sub-passo do Standardizer) | <strong>Arquivo:</strong> <code>editorial-squad/skills/capitalizer/SKILL.md</code></p>
<p><strong>Persona:</strong> Revisor de Capitalizacao. Garante padrao europeu (Acordo Ortografico 1990 / Ciberdúvidas).</p>

<h4>Regras Mestras:</h4>
<ol>
<li><strong>Sentence-case como padrao:</strong> Apenas primeira palavra e nomes proprios com maiuscula.</li>
<li><strong>Excecoes obrigatorias (sempre maiuscula):</strong> Nomes proprios, toponimos (Constantinopla, Roma), titulos institucionais consolidados (Imperio Bizantino, Igreja Catolica), nomes de Deus, livros biblicos, siglas.</li>
<li><strong>Termos descritivos (minuscula):</strong> imperio romano, oriente, ocidente, arte bizantina, mosaico, imperador.</li>
<li><strong>Preposicoes e artigos:</strong> Sempre minuscula no meio de titulos (de, da, do, em, o, a, e).</li>
<li><strong>Consistencia obrigatoria:</strong> Mesmo termo com mesma capitalizacao em TODAS as secoes da aula.</li>
</ol>

<h4>Exemplo Pratico:</h4>
<div class="tutorial-code-block">H1 Correto:  # Imperio Romano do oriente e arte bizantina
H1 Errado:   # Império romano do oriente e a Arte Bizantina

Corpo: "Reconheca que o imperio romano nao desapareceu."
       (minuscula = uso descritivo)

"Imperio Bizantino e a continuacao crista..."
       (maiuscula = nome institucional consolidado)</div>
</div>

<div class="tutorial-content-section">
<h3>AGENTE 6: Reviewer (Revisor de Qualidade — Etapa 4)</h3>
<p><strong>Categoria:</strong> Core Pipeline | <strong>Etapa:</strong> 4 — Revisao/QA | <strong>Arquivo:</strong> <code>editorial-squad/skills/reviewer/SKILL.md</code></p>
<p><strong>Persona:</strong> Editor-Chefe e QA. Garante excelencia tecnica, precisao doutrinal e padronizacao.</p>

<h4>Checklist de Auditoria (13 Categorias):</h4>
<ol>
<li><strong>Titulo H1:</strong> Identico ao Curriculo Macro. Se divergente, REJEITAR.</li>
<li><strong>Estrutura e Escrita:</strong> Voz ativa, imperativo, sem sinais proibidos, limites de texto.</li>
<li><strong>Definir:</strong> 3-4 frases, VIDEO, Accordion com estrutura correta, voice ID, reflexao com "Entenda que..."</li>
<li><strong>Perceber:</strong> Imperativo, IMAGE_LABELED com exatamente 2 hotspots.</li>
<li><strong>Recordar:</strong> Statement_D com definicao curta (9-10 palavras), voice ID.</li>
<li><strong>Praticar:</strong> Fill_In com enunciado antes, 3-4 lacunas, respostas na ultima linha.</li>
<li><strong>Narrar:</strong> IMAGE_TEXT_ASIDE com trecho entre aspas retas (2 paragrafos), 3 perguntas.</li>
<li><strong>Repeticao Consistente:</strong> Definicao identica em 5+ locais.</li>
<li><strong>Fidelidade Pedagogica:</strong> Cumpre objetivos da Matriz, progressao alinhada.</li>
<li><strong>Consistencia Doutrinaria:</strong> Cosmovisao crista reformada, versiculos corretos.</li>
<li><strong>Fact-Checking:</strong> Datas, nomes, obras corretos.</li>
<li><strong>Termo Unico:</strong> Termo nao aparece em aulas anteriores.</li>
<li><strong>Rise Blocks:</strong> Todas tags fechadas, ordem correta, placeholders corretos.</li>
</ol>

<h4>10 Erros Conhecidos da IA (Verificacao Prioritaria):</h4>
<table class="tutorial-table">
<thead><tr><th>#</th><th>Erro</th><th>Verificacao</th></tr></thead>
<tbody>
<tr><td>1</td><td>Accordion com termo repetido</td><td>Definicao direta, sem repetir nome do termo</td></tr>
<tr><td>2</td><td>Matching invertido</td><td>Definicao primeiro, termo depois do [=]</td></tr>
<tr><td>3</td><td>Recordar com definicao longa</td><td>Statement_D deve ter 9-10 palavras</td></tr>
<tr><td>4</td><td>Fill_In sem enunciado</td><td>PARAGRAPH obrigatorio antes</td></tr>
<tr><td>5</td><td>Voz passiva</td><td>Todos enunciados no imperativo ativo</td></tr>
<tr><td>6</td><td>Sinais proibidos</td><td>;, :, — devem ser , ou .</td></tr>
<tr><td>7</td><td>Aspas curvas</td><td>Usar apenas aspas retas</td></tr>
<tr><td>8</td><td>Definicao inconsistente</td><td>Mesma definicao em 5+ locais</td></tr>
<tr><td>9</td><td>Perguntas fora do tema</td><td>Todas relacionadas ao conteudo</td></tr>
<tr><td>10</td><td>1o paragrafo repete titulo</td><td>Complementar, nao repetir</td></tr>
</tbody>
</table>

<h4>Protocolo de Resposta:</h4>
<div class="tutorial-code-block">APROVADO:
[APPROVED_FOR_STEP_5]
Material aprovado.
Checklist: 13/13 categorias | Erros IA: 10/10

REJEITADO:
[REJECTED — RETURN TO STEP X]
Correcoes necessarias:
- Erro de conteudo → volta Etapa 2 (Writer)
- Erro de formatacao → volta Etapa 3 (Standardizer)</div>
</div>

<div class="tutorial-content-section">
<h3>AGENTE 7: Copywriter (Polidor Final — Etapa 5)</h3>
<p><strong>Categoria:</strong> Core Pipeline | <strong>Etapa:</strong> 5 — Polimento | <strong>Arquivo:</strong> <code>editorial-squad/skills/copywriter/SKILL.md</code></p>
<p><strong>Persona:</strong> Polidor Final. Da acabamento final ao conteudo revisado.</p>

<h4>Checklist de Ajustes Finais:</h4>
<ul>
<li><strong>Titulo H1:</strong> Criativo, engajante, capitalizacao europeia</li>
<li><strong>Enunciados:</strong> Claros, imperativo 100%, variacao nos verbos</li>
<li><strong>Accordion Reflexao:</strong> Profunda mas acessivel, "Entenda que..."</li>
<li><strong>Narrar Trecho:</strong> Poetico e elevado, atribuicao completa</li>
<li><strong>Narrar Perguntas:</strong> 3 perguntas abertas, progridem em profundidade</li>
<li><strong>Fluidez Geral:</strong> Transicao natural entre habitos, tom consistente</li>
<li><strong>Checagem Final:</strong> Sem sinais proibidos, aspas retas, sem emojis</li>
</ul>

<h4>Regras:</h4>
<ul>
<li>Problemas menores (titulo, enunciado) → corrigir diretamente</li>
<li>Problemas estruturais → retornar a Etapa 3 ou 4</li>
<li><strong>NUNCA</strong> alterar a definicao do termo (validada pelo Reviewer)</li>
<li><strong>NUNCA</strong> adicionar ou remover blocos Rise</li>
</ul>
</div>

<div class="tutorial-content-section">
<h3>AGENTE 8: Publisher (Publicador — Etapa 7)</h3>
<p><strong>Categoria:</strong> Core Pipeline | <strong>Etapa:</strong> 7 — Publicacao | <strong>Arquivo:</strong> <code>editorial-squad/skills/publisher/SKILL.md</code></p>
<p><strong>Persona:</strong> Distribuidor. Salva a aula localmente e publica no GitHub.</p>

<h4>Etapas de Publicacao:</h4>
<ol>
<li><strong>Salvar Localmente:</strong> <code>[BASE_LOCAL]/[NUMERO_AULA].md</code> (ex: <code>36.3.md</code>)</li>
<li><strong>Registrar Termo:</strong> Marcar termo com check no Curriculo Macro</li>
<li><strong>Push to GitHub:</strong> Via MCP — <code>create_or_update_file</code> no repo <code>bibline/curriculum</code>, branch <code>master</code></li>
<li><strong>Confirmar:</strong> Salvo localmente + Termo registrado + GitHub publicado</li>
</ol>

<h4>Resolucao de Caminhos:</h4>
<table class="tutorial-table">
<thead><tr><th>Ano</th><th>Diretorio Local</th><th>Path GitHub</th></tr></thead>
<tbody>
<tr><td>1o</td><td>1o Ano - ARTE CRISTA PRIMITIVA...</td><td>br/_/1-belas-artes/</td></tr>
<tr><td>2o</td><td>2o Ano - DA CRIACAO ATE A ARTE BIZANTINA/</td><td>br/_/2-belas-artes/</td></tr>
<tr><td>3o</td><td>3o Ano - RENASCIMENTO E REFORMA/</td><td>br/_/3-belas-artes/</td></tr>
<tr><td>4o</td><td>4o Ano - BARROCO ATE O NEOCLASSICISMO/</td><td>br/_/4-belas-artes/</td></tr>
<tr><td>5o</td><td>5o Ano - MANEIRISMO ATE O REALISMO AMERICANO/</td><td>br/_/5-belas-artes/</td></tr>
</tbody>
</table>
</div>

<div class="tutorial-content-section">
<h3>AGENTE 9: Design Thinking (Coordenador de UX)</h3>
<p><strong>Categoria:</strong> Specialized | <strong>Arquivo:</strong> <code>editorial-squad/skills/design-thinking/SKILL.md</code></p>
<p><strong>Persona:</strong> Coordenador de UX e Design Thinking. Lidera processos de design centrado no humano.</p>
<h4>Atribuicoes (5 fases):</h4>
<ul>
<li><strong>Empatia e Pesquisa (Discover):</strong> Entrevistas, surveys, observacao, benchmark, criacao de personas, mapeamento de jornadas do usuario.</li>
<li><strong>Definicao (Define):</strong> Problem statements (Who/What/Why), insights, HMW (How Might We).</li>
<li><strong>Ideacao (Ideate):</strong> Brainstorming (SCAMPER, Crazy 8s), wireframes, priorizacao.</li>
<li><strong>Prototipagem (Prototype):</strong> Prototipos de papel a alta fidelidade, delega UI Designer para visual.</li>
<li><strong>Validacao (Test):</strong> Testes de usabilidade, metricas (tempo, erros, satisfacao), iteracao.</li>
</ul>
<h4>Quando Usar:</strong> "Pesquisa UX", "wireframes", "personas", "jornada do usuario".</p>
</div>

<div class="tutorial-content-section">
<h3>AGENTE 10: UI Designer (Especialista em Design System)</h3>
<p><strong>Categoria:</strong> Specialized | <strong>Arquivo:</strong> <code>editorial-squad/skills/ui-designer/SKILL.md</code></p>
<p><strong>Persona:</strong> UI Designer Senior com expertise em design systems premium, responsivos e acessiveis.</p>
<h4>Atribuicoes:</h4>
<ul>
<li><strong>Design System Premium:</strong> Tokens (colors, typography, spacing, shadows, borders, breakpoints), paleta de cores, tipografia.</li>
<li><strong>Design Responsivo:</strong> Breakpoints (xs:320, sm:480, md:768, lg:1024, xl:1280, xxl:1536), grid 12-colunas, componentes responsivos.</li>
<li><strong>Componentizacao:</strong> Atomic Design (Atoms, Molecules, Organisms, Templates, Pages), props e variantes.</li>
<li><strong>Acessibilidade (WCAG 2.1 AA):</strong> Contraste minimo 4.5:1, foco visivel, labels, ARIA, keyboard navigation, touch targets 44x44px.</li>
</ul>
<h4>Quando Usar:</strong> "criar design system", "criar componentes", "responsividade".</p>
</div>

<div class="tutorial-content-section">
<h3>AGENTE 11: DevOps (Engenheiro DevOps)</h3>
<p><strong>Categoria:</strong> Specialized | <strong>Arquivo:</strong> <code>editorial-squad/skills/devops/SKILL.md</code></p>
<p><strong>Persona:</strong> Engenheiro DevOps. Blindar o ecossistema do repositorio, garantir versionamento leve e estrito.</p>
<h4>Atribuicoes:</h4>
<ul>
<li><strong>Guardiao da Regra de Ouro:</strong> Git NAO e para midia pesada. Apenas texto, historico e conhecimento.</li>
<li><strong>Extensaoes Proibidas:</strong> <code>*.mp4</code>, <code>*.pdf</code>, <code>*.zip</code>, <code>*.mp3</code>, <code>.DS_Store</code>, caches Obsidian.</li>
<li><strong>Executor do Workflow de Publicacao:</strong> Garante passos de Limpeza Profissional quando necessario.</li>
<li><strong>Commits Estruturados:</strong> <code>chore:</code>, <code>content:</code>, <code>fix:</code>.</li>
<li><strong>Limpeza de Emergencia:</strong> <code>git rm -r --cached .</code> → <code>git add .</code> → <code>commit</code> → <code>push --force</code>.</li>
</ul>
</div>

<div class="tutorial-content-section">
<h3>AGENTE 12: Performance Analytics</h3>
<p><strong>Categoria:</strong> Analytics (Vision Board) | <strong>Arquivo:</strong> <code>editorial-squad/skills/performance-analytics/SKILL.md</code></p>
<p><strong>Persona:</strong> Analista de performance e produtividade da equipe editorial.</p>
<h4>Metricas Analisadas:</h4>
<ul>
<li><strong>Individual:</strong> Total de tickets, produzidos, taxa de conclusao, ritmo (tickets/semana).</li>
<li><strong>Por Disciplina:</strong> Tickets por disciplina, meta vs realizado, percentual.</li>
<li><strong>Status do Pipeline:</strong> Backlog, In Progress, In Review, Video, Done/Published.</li>
<li><strong>Ritmo e Velocidade:</strong> Lead time, throughput, capacidade restante, projecao.</li>
</ul>
<h4>Comandos Disponiveis:</h4>
<div class="tutorial-code-block">/performance user Italo-bibline Belas Artes 2
/performance discipline Matematica 2
/performance team
/performance velocity Italo-bibline 4</div>
</div>

<div class="tutorial-content-section">
<h3>AGENTE 13: Vision Progress Engine</h3>
<p><strong>Categoria:</strong> Analytics (Vision Board) | <strong>Arquivo:</strong> <code>editorial-squad/skills/vision-progress-engine/SKILL.md</code></p>
<p><strong>Funcao:</strong> Engine de tracking de progresso para dashboard Vision Board. Calcula percentuais de conclusao, progresso por disciplina/ano, e alimenta os cards de metricas do dashboard.</p>
</div>

<div class="tutorial-content-section">
<h3>AGENTE 14: Vision Bottleneck Detector</h3>
<p><strong>Categoria:</strong> Analytics (Vision Board) | <strong>Arquivo:</strong> <code>editorial-squad/skills/vision-bottleneck-detector/SKILL.md</code></p>
<p><strong>Funcao:</strong> Identifica gargalos no pipeline de producao. Detecta estagios com acúmulo de tickets, agentes sobrecarregados, e semanas paradas. Comando: <code>/bottleneck detect</code>.</p>
</div>

<div class="tutorial-content-section">
<h3>AGENTE 15: Vision GitHub Analyzer</h3>
<p><strong>Categoria:</strong> Analytics (Vision Board) | <strong>Arquivo:</strong> <code>editorial-squad/skills/vision-github-analyzer/SKILL.md</code></p>
<p><strong>Funcao:</strong> Analise de dados GitHub para saude do projeto. Monitora commits, pull requests, issues, e saude geral do repositorio.</p>
</div>

<div class="tutorial-content-section">
<h3>AGENTE 16: Bimester Exam Builder</h3>
<p><strong>Categoria:</strong> Bimester | <strong>Arquivo:</strong> <code>editorial-squad/skills/bimester-exam-builder/SKILL.md</code></p>
<p><strong>Funcao:</strong> Cria exams bimestrais CANVAS_QUIZ de 10 questoes. Usado nas semanas 10, 20, 30, 40.</p>
<h4>Composicao da Prova:</h4>
<ul>
<li>8 questoes das provas semanais (.5) do bimestre</li>
<li>2 questoes autorais do agente</li>
<li>Formato CANVAS_QUIZ para importacao no LMS</li>
</ul>
</div>

<div class="tutorial-content-section">
<h3>AGENTE 17: Bimester Review Builder</h3>
<p><strong>Categoria:</strong> Bimester | <strong>Arquivo:</strong> <code>editorial-squad/skills/bimester-review-builder/SKILL.md</code></p>
<p><strong>Funcao:</strong> Compila reviews bimestrais dos .4 semanais. Usado nas semanas 9, 19, 29, 39.</p>
<h4>Processo:</h4>
<ul>
<li>Coleta todas as revisoes semanais (.4) do bimestre</li>
<li>Consolida flashcards, matching e perguntas</li>
<li>Cria revisao abrangente de todo o conteudo bimestral</li>
</ul>
</div>

<div class="tutorial-content-section">
<h3>AGENTES 18-21: Legacy Agents (Deprecated)</h3>
<p>Estes agentes foram descontinuados mas mantidos por referencia historica:</p>
<table class="tutorial-table">
<thead><tr><th>Agente Legacy</th><th>Funcao Original</th><th>Substituido Por</th></tr></thead>
<tbody>
<tr><td><strong>Exam Builder</strong></td><td>Construtor de quizzes</td><td>Bimester Exam Builder</td></tr>
<tr><td><strong>Review Builder</strong></td><td>Construtor de revisoes</td><td>Bimester Review Builder</td></tr>
<tr><td><strong>Image Link Extractor</strong></td><td>Extrator de imagens</td><td>Sem substituto direto</td></tr>
<tr><td><strong>Image Generator</strong></td><td>Geracao de imagens</td><td>APIs separadas (Pollinations, HuggingFace)</td></tr>
</tbody>
</table>
</div>

<div class="tutorial-content-section">
<h3>Resumo Visual: Mapa de Dependencias entre Skills</h3>
<div class="tutorial-code-block">Orchestrator (diagnostica e delega)
    |
    +-- Researcher --> Writer --> Standardizer --> Reviewer --> Copywriter --> Publisher
          |              |            |               |
          |              |            |               +-- (rejeicao) --> Writer ou Standardizer
          |              |            |
          |              |            +-- Capitalizer (sub-passo obrigatoria)
          |              |
          |              +-- Golden Template (padrao_final_aula.md)
          |
          +-- Doutrina Pedagogica + Guia de Estilo
    |
    +-- Bimester Review Builder (pos X.4 completas)
    |
    +-- Bimester Exam Builder (pos X.5 completas)
    |
    +-- DevOps (quando necessario)</div>
</div>

<div class="tutorial-content-section">
<h3>Tabela de Roteamento Completa (Quem faz o que)</h3>
<table class="tutorial-table">
<thead><tr><th>Demanda do Usuario</th><th>Skill/Workflow</th><th>Invocacao</th></tr></thead>
<tbody>
<tr><td>Criar aula nova</td><td>produce_class.md</td><td>"Crie a aula X.Y, No ano"</td></tr>
<tr><td>Criar revisao (X.4)</td><td>review-builder/SKILL.md</td><td>"Crie a revisao da semana X"</td></tr>
<tr><td>Revisao bimestral</td><td>bimester-review-builder</td><td>"Crie a revisao do bimestre N"</td></tr>
<tr><td>Prova bimestral</td><td>bimester-exam-builder</td><td>"Crie a prova do bimestre N"</td></tr>
<tr><td>Corrigir formatacao Rise</td><td>standardizer/SKILL.md</td><td>@standardizer</td></tr>
<tr><td>Corrigir capitalizacao</td><td>capitalizer/SKILL.md</td><td>@capitalizer</td></tr>
<tr><td>Revisar qualidade</td><td>reviewer/SKILL.md</td><td>@reviewer</td></tr>
<tr><td>Polir texto</td><td>copywriter/SKILL.md</td><td>@copywriter</td></tr>
<tr><td>Subir no GitHub</td><td>devops/SKILL.md</td><td>@devops</td></tr>
<tr><td>Pesquisar conteudo</td><td>researcher/SKILL.md</td><td>@researcher</td></tr>
<tr><td>Publicar arquivo</td><td>publisher/SKILL.md</td><td>@publisher</td></tr>
<tr><td>Status geral</td><td>orchestrator/SKILL.md</td><td>@orchestrator</td></tr>
<tr><td>Design Thinking</td><td>design-thinking/SKILL.md</td><td>@design-thinking</td></tr>
<tr><td>UI/Design System</td><td>ui-designer/SKILL.md</td><td>@ui-designer</td></tr>
<tr><td>Performance</td><td>performance-analytics</td><td>/performance user X</td></tr>
<tr><td>Gargalos</td><td>vision-bottleneck-detector</td><td>/bottleneck detect</td></tr>
</tbody>
</table>
</div>
`},

// ============================================================================
// SECAO 4 — PIPELINE 7 ETAPAS
// ============================================================================
{id:'pipeline',number:4,title:'Pipeline 7 Etapas',icon:'<i class="ph ph-arrows-left-right"></i>',color:'#34d399',content:`
<h2><i class="ph ph-arrows-left-right" style="color:var(--accent-primary);margin-right:0.5rem;"></i> 4. Pipeline Editorial de 7 Etapas</h2>

<div class="tutorial-content-section">
<h3>Visao Geral do Pipeline</h3>
<p>O coracao da producao editorial e o arquivo <code>editorial-squad/workflows/produce_class.md</code>. Toda criacao de aula segue este modelo de linha de montagem em 7 etapas, onde o output de um agente e o input do proximo.</p>
<div class="tutorial-code-block">+-------------+     +-------------+     +-------------+
| 1. PESQUISA |---->| 2. REDACAO  |---->|3. FORMATAcAO|
| (Researcher)|     |  (Writer)   |     |(Standardizer|
+-------------+     +-------------+     +------+------+
                                               |
                    +--------------+            |
                    |              |<-----------+
                    |  4. REVISAO  |
                    |  (Reviewer)  |---- REJECTED? ---> volta 2 ou 3
                    |              |
                    +------+------+
                           | APPROVED
                    +------+------+
                    | 5. POLIMENTO|
                    | (Copywriter)|
                    +------+------+
                           |
                    +------+------+     +-------------+
                    | 6. REGISTRO |---->|7. PUBLICACAO|
                    |  (Termo OK) |     | (Publisher)  |
                    +-------------+     +-------------+</div>
</div>

<div class="tutorial-content-section">
<h3>ETAPA 1 — PESQUISA (Researcher)</h3>
<p><strong>Agente:</strong> Researcher (Investigador)</p>
<p><strong>Input:</strong> Tema da aula + Plano Pedagogico do ano</p>
<p><strong>Output:</strong> <code>research_report.md</code> — relatorio de pesquisa organizado pelos 5 habitos</p>

<h4>Passo a Passo:</h4>
<ol>
<li>Ler a skill <code>editorial-squad/skills/researcher/SKILL.md</code></li>
<li>Consultar o <strong>Plano Pedagogico</strong> do ano para localizar a semana/aula</li>
<li>Consultar o <strong>Curriculo Macro</strong> para identificar termos proibidos (check)</li>
<li>Pesquisar:
<ul>
<li>Definicao Webster 1828 para o termo inedito</li>
<li>Versiculos biblicos relacionados (ARA/ARC)</li>
<li>Obra de arte para o Perceber</li>
<li>Poema/hino para o Recordar</li>
<li>Trecho literario para o Narrar (usar DB de autores da skill)</li>
</ul>
</li>
<li>Compilar relatorio organizado pelos 5 habitos</li>
</ol>

<h4>Regra Principal:</h4>
<p>Fontes primarias: Webster 1828, ARA/ARC, obras classicas. Metodologia Ad Fontes.</p>

<div class="tutorial-info-card">
<strong>Dica:</strong> O Researcher NAO escreve a aula. Ele coleta materia-prima organizada que o Writer vai consumir na Etapa 2. O relatorio deve ter informacoes suficientes para o Writer redigir sem precisar pesquisar.
</div>
</div>

<div class="tutorial-content-section">
<h3>ETAPA 2 — REDACAO (Writer)</h3>
<p><strong>Agente:</strong> Writer (Escriba)</p>
<p><strong>Input:</strong> Relatorio de pesquisa (output da Etapa 1)</p>
<p><strong>Output:</strong> <code>draft_class.md</code> — rascunho da aula completa</p>

<h4>Passo a Passo:</h4>
<ol>
<li>Ler a skill <code>editorial-squad/skills/writer/SKILL.md</code></li>
<li>Consultar o <strong>golden template</strong> <code>editorial-squad/templates/padrao_final_aula.md</code></li>
<li>Consultar a <strong>knowledge base</strong>:
<ul>
<li><code>guia-de-estilo.md</code> — tom de voz, metricas, regras</li>
<li><code>doutrina-pedagogica.md</code> — fundamentacao teologica</li>
</ul>
</li>
<li>Redigir conteudo completo dos 5 habitos baseado no relatorio de pesquisa</li>
<li>Garantir: voz ativa, imperativo, frases ≤ 30 palavras, paragrafos ≤ 70 palavras</li>
<li>Sem <code>;</code>, <code>:</code>, <code>—</code> — substituir por <code>,</code> ou <code>.</code></li>
</ol>

<h4>Regras Criticas:</h4>
<ul>
<li>Titulo H1 DEVE ser EXATAMENTE o do Curriculo Macro (fonte de verdade)</li>
<li>Termo principal NAO pode estar em aulas anteriores (verificar Curriculo Macro)</li>
<li>Definicao de 9-10 palavras no Recordar</li>
<li>Reflexao do Accordion comeca com "Entenda que..."</li>
</ul>

<div class="tutorial-info-card">
<strong>Armadilha Comum:</strong> O Writer muitas vezes repete o termo principal no Accordion ("O que e Catequese? Catequese e..."). O correto e definicao DIRETA: "Catequese e o ensino oral..." — sem repetir o termo como prefixo.
</div>
</div>

<div class="tutorial-content-section">
<h3>ETAPA 3 — FORMATAcAO (Standardizer + Capitalizer)</h3>
<p><strong>Agentes:</strong> Standardizer (Arquiteto) + Capitalizer (sub-etapa)</p>
<p><strong>Input:</strong> Rascunho da aula (output da Etapa 2)</p>
<p><strong>Output:</strong> <code>formatted_class.md</code> — aula com Rise Blocks</p>

<h4>Passo a Passo:</h4>
<ol>
<li>Ler a skill <code>editorial-squad/skills/standardizer/SKILL.md</code></li>
<li>Consultar <code>editorial-squad/knowledge-base/rise-blocks-reference.md</code></li>
<li><strong>Correcoes Editoriais Proativas:</strong>
<ul>
<li>Conferir H1 com Curriculo Macro (corrigir se divergente)</li>
<li>Remover <code>;</code>, <code>:</code>, <code>—</code></li>
<li>Converter aspas curvas para retas</li>
<li>Reescrever voz passiva para ativa</li>
<li>Garantir imperativo direto</li>
<li>Verificar limites de texto</li>
</ul>
</li>
<li><strong>Aplicar capitalizacao padrao europeu</strong> conforme <code>skills/capitalizer/SKILL.md</code></li>
<li>Formatar com Rise Blocks seguindo o mapeamento exato dos 5 habitos</li>
<li>Remover metadados, emojis de secao, separadores <code>---</code></li>
<li>Verificar definicao identica em todos os locais obrigatorios</li>
</ol>

<h4>Mapeamento dos 5 Habitos para Rise Blocks:</h4>
<table class="tutorial-table">
<thead><tr><th>Habito</th><th>Blocks Utilizados</th></tr></thead>
<tbody>
<tr><td><strong>Definir</strong></td><td>PARAGRAPH, VIDEO, HEADING, ACCORDION (com MP3, link_png)</td></tr>
<tr><td><strong>Perceber</strong></td><td>PARAGRAPH, IMAGE_LABELED (2 hotspots)</td></tr>
<tr><td><strong>Recordar</strong></td><td>PARAGRAPH, STATEMENT_D, HEADING, IMAGE_TEXT_ON</td></tr>
<tr><td><strong>Praticar</strong></td><td>HEADING, PARAGRAPH, FILL_IN, ATTACHMENT</td></tr>
<tr><td><strong>Narrar</strong></td><td>HEADING, IMAGE_TEXT_ASIDE, PARAGRAPH, LIST_NUMBERED</td></tr>
</tbody>
</table>
</div>

<div class="tutorial-content-section">
<h3>ETAPA 4 — REVISAO (Reviewer)</h3>
<p><strong>Agente:</strong> Reviewer (Editor-Chefe/QA)</p>
<p><strong>Input:</strong> Aula formatada (output da Etapa 3)</p>
<p><strong>Output:</strong> <code>reviewed_class.md</code> ou rejeicao com log detalhado</p>

<h4>Passo a Passo:</h4>
<ol>
<li>Ler a skill <code>editorial-squad/skills/reviewer/SKILL.md</code></li>
<li>Executar o <strong>checklist de 13 categorias</strong> completo</li>
<li>Verificar os <strong>10 erros conhecidos da IA</strong> (prioritario)</li>
<li>Validar conformidade com o <strong>golden template</strong></li>
<li><strong>Se APROVADO:</strong> Marcar <code>[APPROVED_FOR_STEP_5]</code> e seguir para Etapa 5</li>
<li><strong>Se REJEITADO:</strong> Identificar se erro e de conteudo (volta Etapa 2) ou formatacao (volta Etapa 3)</li>
</ol>

<h4>Feedback Loops:</h4>
<div class="tutorial-code-block">Erro de conteudo/redacao  → volta para Etapa 2 (Writer)
Erro de formatacao/estilo   → volta para Etapa 3 (Standardizer)
Problema grave no Copywriter → volta para Etapa 3 ou 4

LOOP: Se rejeitado, corrigir e ressubmeter ate aprovacao.</div>

<div class="tutorial-info-card">
<strong>Regra Critica:</strong> Violacao da repeticao obrigatoria da definicao (deve aparecer identica em 5+ locais) e motivo de rejeicao automatica na Etapa 4.
</div>
</div>

<div class="tutorial-content-section">
<h3>ETAPA 5 — POLIMENTO (Copywriter)</h3>
<p><strong>Agente:</strong> Copywriter (Polidor Final)</p>
<p><strong>Input:</strong> Aula aprovada (output da Etapa 4)</p>
<p><strong>Output:</strong> <code>final_class.md</code> — aula final polida</p>

<h4>Passo a Passo:</h4>
<ol>
<li>Ler a skill <code>editorial-squad/skills/copywriter/SKILL.md</code></li>
<li>Otimizar titulo da aula (criativo e engajante)</li>
<li>Polir enunciados (variacao de verbos, clareza)</li>
<li>Revisar fluidez geral e transicoes entre habitos</li>
<li>Checagem final de conformidade (sem sinais proibidos, aspas retas, etc.)</li>
</ol>

<h4>Regras:</h4>
<ul>
<li>Problemas menores → corrigir diretamente</li>
<li>Problemas estruturais → retornar a Etapa 3 ou 4</li>
<li><strong>NUNCA</strong> alterar a definicao do termo (validada pelo Reviewer)</li>
<li><strong>NUNCA</strong> adicionar ou remover blocos Rise</li>
</ul>
</div>

<div class="tutorial-content-section">
<h3>ETAPA 6 — REGISTRO NO CURRICULO MACRO</h3>
<p><strong>Agente:</strong> Automatico/Manual (parte do Publisher)</p>
<p><strong>Input:</strong> Aula finalizada</p>
<p><strong>Output:</strong> Curriculo Macro atualizado</p>

<h4>Regra Obrigatoria:</h4>
<p>Executar automaticamente ao final de cada <strong>semana completa</strong> (3 aulas).</p>

<h4>Passo a Passo:</h4>
<ol>
<li>Abrir o <strong>Curriculo Macro</strong> do ano correspondente</li>
<li>Para cada aula finalizada na semana:
<ul>
<li>Localizar a linha <code>- Dia N: [Tema da aula]</code></li>
<li>Adicionar <code> check</code> ao final da linha</li>
</ul>
</li>
<li>Adicionar <code> check</code> ao final do titulo <code>## Semana N</code></li>
<li><strong>Adicionar bloco de termos</strong> logo apos as 3 aulas:
<div class="tutorial-code-block"># Semana N
Termo1 check
Termo2 check
Termo3 check</div>
</li>
<li>Cada termo corresponde ao termo principal do Accordion/Definir daquela aula</li>
<li>Confirmar ao usuario: <code>Semana X: 3/3 aulas + 3 termos marcados check</code></li>
</ol>

<h4>Regra de Sincronizacao Curricular (Manutencao):</h4>
<p>Se voce estiver <strong>modificando/atualizando</strong> uma aula ja existente (em vez de criar uma nova), DEVE obrigatoriamente refletir as mudancas nestes 5 arquivos:</p>
<ol>
<li><code>1 - Curriculo Macro</code>: Se o titulo (H1) da aula mudar</li>
<li><code>2 - Matriz-Curricular-objetivos</code>: Se o objetivo teologico-pedagogico mudar</li>
<li><code>3 - Visao e Plano pedagogico</code>: Se a abordagem da aula mudar</li>
<li><code>4 - Links-para-imagens-perceber</code>: Se a secao Perceber mudar</li>
<li><strong>Aula de Revisao (X.4.md)</strong>: Se alterar definicoes ou atividades do Perceber</li>
</ol>
</div>

<div class="tutorial-content-section">
<h3>ETAPA 7 — PUBLICACAO (Publisher)</h3>
<p><strong>Agente:</strong> Publisher (Distribuidor)</p>
<p><strong>Input:</strong> Aula final (output da Etapa 5)</p>
<p><strong>Output:</strong> Arquivo local + commit GitHub</p>

<h4>Passo a Passo:</h4>
<ol>
<li>Ler a skill <code>editorial-squad/skills/publisher/SKILL.md</code></li>
<li><strong>Salvar localmente:</strong> <code>[BASE_LOCAL]/[NUMERO_AULA].md</code> (ex: <code>36.3.md</code>)</li>
<li><strong>Push para GitHub via MCP</strong> (se disponivel):
<ul>
<li>Repo: <code>bibline/curriculum</code></li>
<li>Branch: <code>master</code></li>
<li>Path: <code>br/_/[ANO]-belas-artes/[NUMERO].md</code></li>
</ul>
</li>
<li><strong>Confirmar ao usuario:</strong> local OK, termo OK, GitHub OK</li>
</ol>
</div>

<div class="tutorial-content-section">
<h3>Estrutura Semanal de Producao</h3>
<p>Cada semana de conteudo segue um padrao fixo de <strong>5 arquivos</strong>:</p>
<table class="tutorial-table">
<thead><tr><th>Arquivo</th><th>Tipo</th><th>Descricao</th><th>Agente</th></tr></thead>
<tbody>
<tr><td><code>X.1.md</code></td><td>Aula regular (Dia 1)</td><td>Primeira aula da semana</td><td>Pipeline 7 etapas</td></tr>
<tr><td><code>X.2.md</code></td><td>Aula regular (Dia 2)</td><td>Segunda aula da semana</td><td>Pipeline 7 etapas</td></tr>
<tr><td><code>X.3.md</code></td><td>Aula regular (Dia 3)</td><td>Terceira aula da semana</td><td>Pipeline 7 etapas</td></tr>
<tr><td><code>X.4.md</code></td><td>Revisao semanal</td><td>Flashcards, matching e questoes</td><td>Review Builder</td></tr>
<tr><td><code>X.5.md</code></td><td>Prova semanal</td><td>Quiz CANVAS com questoes</td><td>Exam Builder</td></tr>
</tbody>
</table>
</div>

<div class="tutorial-content-section">
<h3>Estrutura Bimestral (Ciclos de 10 Semanas)</h3>
<table class="tutorial-table">
<thead><tr><th>Semanas</th><th>Tipo</th><th>Conteudo</th></tr></thead>
<tbody>
<tr><td>1-8, 11-18, 21-28, 31-38</td><td>Conteudo</td><td>8 semanas x 5 arquivos = 40 arquivos por bimestre</td></tr>
<tr><td>9, 19, 29, 39</td><td>Revisao Bimestral</td><td>Compilacao das 8 revisoes semanais (.4)</td></tr>
<tr><td>10, 20, 30, 40</td><td>Prova Bimestral</td><td>CANVAS_QUIZ de 10 questoes (8 das .5 + 2 autorais)</td></tr>
</tbody>
</table>
</div>

<div class="tutorial-content-section">
<h3>Ciclo Completo de uma Semana</h3>
<div class="tutorial-code-block">Aula X.1 --> Aula X.2 --> Aula X.3 --> Revisao X.4 --> Prova X.5
    |              |              |              |              |
    | (Pipeline    | (Pipeline    | (Pipeline    | (review-      | (bimester-
    |  7 etapas)   |  7 etapas)   |  7 etapas)   |  builder)     |  exam-builder)
    v              v              v              v               v
  Publicar       Publicar       Publicar      Publicar        Publicar

Regra de Completude: Uma semana so e considerada completa quando
possui os 5 arquivos (.1, .2, .3, .4, .5) publicados.</div>
</div>

<div class="tutorial-content-section">
<h3>Regra de Idempotencia</h3>
<div class="tutorial-info-card">
<strong>Idempotencia:</strong> O pipeline pode ser re-executado quantas vezes for necessario SEM efeitos colaterais. Se uma aula ja foi publicada e precisa de correcao, basta re-executar o pipeline a partir da etapa onde o erro foi identificado. O Publisher salva localmente e faz commit novamente sem duplicar conteudo.
</div>
</div>

<div class="tutorial-content-section">
<h3>Exemplo Completo: Criando a Aula 5.3 do 3o Ano</h3>
<div class="tutorial-code-block">Comando: "Crie a aula 5.3, 3o ano"

1. ORCHESTRATOR diagnostica:
   → Semana 5 do 3o ano, aula 3 (terceira aula)
   → Diretorio: 3o Ano - RENASCIMENTO E REFORMA/
   → Curriculo Macro localizado

2. RESEARCHER pesquisa:
   → Webster 1828 para o termo inedito
   → Versiculos ARA/ARC relacionados
   → Obra de arte para Perceber
   → Poema para Recordar
   → Trecho literario para Narrar (DB de autores)
   → Output: research_report.md

3. WRITER redige:
   → Consulta golden template + guia de estilo
   → Redige os 5 habitos com conteudo da pesquisa
   → Output: draft_class.md

4. STANDARDIZER formata:
   → Aplica Rise Blocks a cada secao
   → Corrige sinais proibidos, capitalizacao
   → Output: formatted_class.md

5. REVIEWER revisa:
   → Checklist 13 categorias + 10 erros IA
   → Se aprovado: [APPROVED_FOR_STEP_5]
   → Se rejeitado: volta para etapa 2 ou 3

6. COPYWRITE polimento:
   → Otimiza titulos, enunciados, fluidez
   → Output: final_class.md

7. PUBLISHER publica:
   → Salva como 5.3.md no diretorio local
   → Marca termo no Curriculo Macro
   → Push para GitHub via MCP</div>
</div>

<div class="tutorial-content-section">
<h3>Principais Armadilhas do Pipeline</h3>
<table class="tutorial-table">
<thead><tr><th>Armadilha</th><th>Etapa</th><th>Como Evitar</th></tr></thead>
<tbody>
<tr><td>Definicao inconsistente entre secoes</td><td>3-4</td><td>Verificar os 5+ locais obrigatorios</td></tr>
<tr><td>Titulo H1 divergente do Macro</td><td>2-3</td><td>SEMPRE consultar Macro antes de escrever</td></tr>
<tr><td>Voz passiva nos enunciados</td><td>2-4</td><td>Usar checklist de voz ativa</td></tr>
<tr><td>Sinais proibidos (ponto e virgula, etc.)</td><td>2-4</td><td>Standardizer remove proativamente</td></tr>
<tr><td>Termo ja definido em aula anterior</td><td>1-2</td><td>Consultar termos com check no Macro</td></tr>
<tr><td>Definicao longa no Recordar</td><td>2-4</td><td>Limitar a 9-10 palavras</td></tr>
<tr><td>Fill_In sem enunciado antes</td><td>2-4</td><td>PARAGRAPH obrigatoria antes do bloco</td></tr>
<tr><td>Esquecer de sincronizar 5 arquivos</td><td>6</td><td>Executar sync_titles.py apos mudancas</td></tr>
</tbody>
</table>
</div>
`},

// ============================================================================
// SECAO 5 — TEMPLATES E 5 HABITOS
// ============================================================================
{id:'templates',number:5,title:'Templates e 5 Habitos',icon:'<i class="ph ph-notepad"></i>',color:'#ec4899',content:`
<h2><i class="ph ph-notepad" style="color:var(--accent-primary);margin-right:0.5rem;"></i> 5. Golden Template e 5 Habitos da Gramatica</h2>

<div class="tutorial-content-section">
<h3>O Golden Template — padrao_final_aula.md</h3>
<p>O arquivo <code>editorial-squad/templates/padrao_final_aula.md</code> e o <strong>esqueleto oficial de toda aula</strong>. Toda aula publicada DEVE seguir esta estrutura exatamente. O Reviewer valida contra este template na Etapa 4 e rejeita se houver divergencia significativa.</p>

<h4>Localizacao:</h4>
<p><code>editorial-squad/templates/padrao_final_aula.md</code></p>

<h4>Regras Fixas do Golden Template:</h4>
<ol>
<li><strong>Sem cabecalhos de metadados</strong> — nao usar disciplina, modulo, base, fontes, faixa etaria</li>
<li><strong>Sem emojis de secao</strong> — nao usar 🟥🟧🟨🟩🟦📌</li>
<li><strong>Sem separadores <code>---</code></strong> entre secoes</li>
<li><strong>Titulo</strong> comeca com <code>#</code> seguido do nome da aula</li>
<li><strong>Secoes</strong> sao <code>## Definir</code>, <code>## Perceber</code>, <code>## Recordar</code>, <code>## Praticar</code>, <code>## Narrar</code></li>
<li><strong>Definicao consistente</strong> — mesmo conceito aparece no Accordion, Recordar e Praticar</li>
<li><strong>Recordar</strong> — definicao curta de 9-10 palavras</li>
<li><strong>Praticar</strong> — Fill_In usa a definicao do Recordar com <code>_____</code></li>
<li><strong>Narrar</strong> — aspas retas, trecho em 2 paragrafos, atribuicao em linha unica com negrito e italico</li>
<li><strong>Sem <code>;</code>, <code>:</code>, <code>—</code></strong> — usar <code>,</code> ou <code>.</code></li>
<li><strong>Voz ativa e imperativo</strong> em todas as instrucoes</li>
<li><strong>Sem termos em ingles</strong> na versao final</li>
</ol>
</div>

<div class="tutorial-content-section">
<h3>Os 5 Habitos da Gramatica — Estrutura de Cada Aula</h3>
<p>Toda aula regular (.1, .2, .3) e organizada nos <strong>5 Habitos</strong> da Pedagogia do Belo. Cada habito tem uma funcao pedagogica especifica e blocos Rise obrigatorios.</p>

<div class="tutorial-metrics-grid" style="grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));">
<div class="metric-card" style="border-top: 3px solid #2dd4bf;"><div class="metric-value" style="font-size:1.2rem;">Definir</div><div class="metric-label">Conceito central</div></div>
<div class="metric-card" style="border-top: 3px solid #67e8f9;"><div class="metric-value" style="font-size:1.2rem;">Perceber</div><div class="metric-label">Observacao visual</div></div>
<div class="metric-card" style="border-top: 3px solid #f472b6;"><div class="metric-value" style="font-size:1.2rem;">Recordar</div><div class="metric-label">Memorizacao</div></div>
<div class="metric-card" style="border-top: 3px solid #fbbf24;"><div class="metric-value" style="font-size:1.2rem;">Praticar</div><div class="metric-label">Exercicio</div></div>
<div class="metric-card" style="border-top: 3px solid #8b5cf6;"><div class="metric-value" style="font-size:1.2rem;">Narrar</div><div class="metric-label">Contextualizacao</div></div>
</div>
</div>

<div class="tutorial-content-section">
<h3>HABITO 1: Definir (Nomear)</h3>
<p><strong>Funcao:</strong> Apresentar o conceito central da aula. O aluno deve sair desta secao sabendo exatamente o que e o termo novo.</p>
<p><strong>Template:</strong> <code>editorial-squad/templates/defining.md</code></p>

<h4>Estrutura do Bloco:</h4>
<div class="tutorial-code-block">## Definir

[+PARAGRAPH]
Reconheca que [contexto principal da aula].
Observe que [argumento ou reflexao secundaria].
[Definicao curtissima e direta — 9-10 palavras].
Veja o video abaixo.
[-PARAGRAPH]

[+VIDEO][-VIDEO]

[+HEADING]
Atividade
[-HEADING]

[+PARAGRAPH]
Leia a definicao e ouca o audio. [Instrucao no imperativo].
[-PARAGRAPH]

[+ACCORDION]
O que e [Termo]?

@link_png@

[MP3/]
#11L:VOICE_ID_AQUI
[Definicao em portugues — EXATAMENTE a mesma do Recordar]
[MP3\]

[Definicao com palavras-chave em negrito]

Reflexao

[Reflexao teologica curta no imperativo, comecando com "Entenda que..."]

[-ACCORDION]</div>

<h4>Regras Criticas do Definir:</h4>
<ul>
<li>Frase 1: SEMPRE comeca com "Reconheca que..."</li>
<li>Frase 2: SEMPRE comeca com "Observe que..."</li>
<li>Frase 3: Definicao extremamente curta e direta</li>
<li>Frase 4: "Veja o video abaixo." — obrigatoria</li>
<li>Accordion: definicao aparece <strong>3 vezes</strong> (texto no MP3, texto com negrito, e no Recordar)</li>
<li>Reflexao SEMPRE comeca com "Entenda que..."</li>
<li>Voice ID obrigatoria: <code>#11L:XXXXXXXXXXXXXXXXX</code></li>
<li><code>@link_png@</code> vem logo apos a pergunta (antes da definicao)</li>
</ul>

<div class="tutorial-info-card">
<strong>Armadilha Mais Comum:</strong> Colocar a definicao em texto plano ANTES do <code>@link_png@</code> no Accordion. O correto e: Pergunta → <code>@link_png@</code> → MP3 com definicao → definicao com negrito → Reflexao. NUNCA definicao em texto plano antes da imagem.
</div>
</div>

<div class="tutorial-content-section">
<h3>HABITO 2: Perceber (Observar)</h3>
<p><strong>Funcao:</strong> Observar visualmente o conceito. O aluno analisa uma obra de arte relacionada ao tema.</p>
<p><strong>Template:</strong> <code>editorial-squad/templates/perceiving.md</code></p>

<h4>Estrutura do Bloco:</h4>
<div class="tutorial-code-block">## Perceber

[+PARAGRAPH]
[3-4 frases no imperativo descrevendo o que observar na imagem].
[-PARAGRAPH]

[+IMAGE_LABELED]
@link_png@

--

X1 Y1

Titulo do ponto 1

Descricao do ponto 1 no imperativo.

--

X2 Y2

Titulo do ponto 2

Descricao do ponto 2 no imperativo.
[-IMAGE_LABELED]</div>

<h4>Regras Criticas do Perceber:</h4>
<ul>
<li>Paragrafo em imperativo: "Observe...", "Note...", "Repare..."</li>
<li>Exatamente <strong>2 hotspots</strong> com coordenadas percentuais (0-100)</li>
<li>Cada hotspot tem: coordenadas X Y, titulo, descricao imperativa</li>
<li><strong>Nenhum bloco extra</strong> permitido nesta secao</li>
<li>As coordenadas sao percentuais da posicao do label na imagem</li>
</ul>

<h4>Alternancia Permitida (Revisao .4):</h4>
<p>Nas aulas de revisao semanal (.4), o Perceber pode usar <code>TABS</code> ao inves de <code>IMAGE_LABELED</code> para apresentar 2 imagens lado a lado com analise.</p>
</div>

<div class="tutorial-content-section">
<h3>HABITO 3: Recordar (Memorizar)</h3>
<p><strong>Funcao:</strong> Memorizar a definicao. Repeticao e virtude, nao redundancia.</p>
<p><strong>Template:</strong> <code>editorial-squad/templates/remembering.md</code></p>

<h4>Estrutura do Bloco (Variante A — Musica):</h4>
<div class="tutorial-code-block">## Recordar

[+PARAGRAPH]
Ouca e repita a definicao abaixo.
[-PARAGRAPH]

[+STATEMENT_D]
[MP3/]
#11L:VOICE_ID_AQUI
[Definicao CURTA — 9-10 palavras — IDENTICA ao Accordion]
[MP3\]
[Definicao CURTA — mesma frase]
[-STATEMENT_D]

[+HEADING]
Hora de memorizar com musica
[-HEADING]

[+PARAGRAPH]
Clique abaixo para ouvir a musica sobre o tema da aula.
[-PARAGRAPH]

[+IMAGE_TEXT_ON]
@link_png@
@link_mp3@
[Nome da musica]
[-IMAGE_TEXT_ON]</div>

<h4>Estrutura do Bloco (Variante B — Rima, usada no 3o ano):</h4>
<div class="tutorial-code-block">[+HEADING]
Hora de memorizar com rima
[-HEADING]

[+PARAGRAPH]
Clique abaixo para ouvir a rima sobre [tema da aula].
[-PARAGRAPH]

[+STATEMENT_A]
[MP3/]
#11L:VOICE_ID_AQUI
[Titulo da rima]
[Verso 1 rimando com o tema]
[Verso 2]
[Verso 3]
[Verso 4]
[MP3\]
[Titulo da rima]
[Verso 1]
[Verso 2]
[Verso 3]
[Verso 4]
[-STATEMENT_A]</div>

<h4>Regras Criticas do Recordar:</h4>
<ul>
<li>Enunciado: "Ouca e repita a definicao abaixo." — EXATO</li>
<li>Definicao no Statement_D: <strong>9-10 palavras</strong> — IDENTICA a do Accordion</li>
<li>Voice ID presente e consistente por ano</li>
<li>Variante B (rima) e padrao para 3o ano; Variante A (musica) para demais anos</li>
</ul>

<div class="tutorial-info-card">
<strong>Regra de Repeticao Obrigatoria:</strong> A definicao central deve aparecer IDENTICAMENTE em 6 locais: (1) Paragrafo introdutorio Definir, (2) Accordion texto, (3) Accordion audio, (4) Accordion negrito, (5) Statement_D Recordar, (6) Revisao semanal X.4. Violacao = rejeicao automatica.
</div>
</div>

<div class="tutorial-content-section">
<h3>HABITO 4: Praticar (Exercitar)</h3>
<p><strong>Funcao:</strong> Exercitar o conceito. Fixacao atraves de atividades praticas.</p>
<p><strong>Template:</strong> <code>editorial-squad/templates/practicing.md</code></p>

<h4>Estrutura do Bloco:</h4>
<div class="tutorial-code-block">## Praticar

[+HEADING]
Atividade
[-HEADING]

[+PARAGRAPH]
Complete as lacunas para reafirmar a definicao que voce aprendeu.
[-PARAGRAPH]

[+FILL_IN]
[Definicao do Recordar com _____ nas 3-4 lacunas.]
[resposta1, resposta2, resposta3]
[-FILL_IN]

[+HEADING]
Atividade Extra
[-HEADING]

[+PARAGRAPH]
[Instrucao de atividade pratica no imperativo.]
[-PARAGRAPH]

[+ATTACHMENT]
@link_pdf@
[-ATTACHMENT]</div>

<h4>Regras Criticas do Praticar:</h4>
<ul>
<li>Atividade 1 SEMPRE comeca com: "Complete as lacunas para reafirmar a definicao que voce aprendeu."</li>
<li>O bloco <code>FILL_IN</code> contem SOMENTE o conceito com lacunas — NUNCA instrucao</li>
<li>Exatamente <strong>3-4 lacunas</strong> com <code>_____</code> (5 underscores cada)</li>
<li>Respostas na ultima linha, separadas por virgula e espaco, na ordem das lacunas</li>
<li>Alternativas erradas devem ser plausiveis mas claramente incorretas</li>
<li>Resposta correta e extraida da definicao de 9 palavras</li>
<li>Atividade Extra: instrucao no imperativo + PDF attachment</li>
</ul>

<div class="tutorial-info-card">
<strong>Armadilha:</strong> Colocar instrucao DENTRO do bloco FILL_IN. O bloco deve conter SOMENTE a definicao com lacunas. A instrucao vem ANTES, em um bloco PARAGRAPH separado.
</div>
</div>

<div class="tutorial-content-section">
<h3>HABITO 5: Narrar (Contextualizar)</h3>
<p><strong>Funcao:</strong> Contextualizar narrativamente. Conectar o conceito a um trecho literario/poetico com cosmovisao cristã.</p>
<p><strong>Template:</strong> <code>editorial-squad/templates/narrating.md</code></p>

<h4>Estrutura do Bloco (Variante A — IMAGE_TEXT_ASIDE, padrao para 1o, 2o, 4o, 5o ano):</h4>
<div class="tutorial-code-block">## Narrar

[+HEADING]
Leitura
[-HEADING]

[+IMAGE_TEXT_ASIDE]
@link_png@

"[Primeiro paragrafo do trecho literario — conecta tema a verdade biblica.]

[Segundo paragrafo — aprofunda reflexao com linguagem poetica.]"

Trecho inspirado em Referencia Biblica e reflexoes de Autor Cristao, Obra (Contexto)
[-IMAGE_TEXT_ASIDE]

[+HEADING]
Perguntas
[-HEADING]

[+PARAGRAPH]
Responda oralmente as perguntas abaixo sobre o texto.
[-PARAGRAPH]

[+LIST_NUMBERED]
[Pergunta 1 com interrogacao?]

[Pergunta 2 com interrogacao?]

[Pergunta 3 com interrogacao?]
[-LIST_NUMBERED]</div>

<h4>Estrutura do Bloco (Variante B — PARAGRAPH, padrao para 3o ano):</h4>
<p>Igual a Variante A, mas usa <code>[+PARAGRAPH]</code> ao inves de <code>[+IMAGE_TEXT_ASIDE]</code> para o trecho literario.</p>

<h4>Regras Criticas do Narrar:</h4>
<ul>
<li>Trecho literario cristao, puritano ou poetico entre <strong>aspas retas</strong></li>
<li>Trecho dividido em <strong>2 paragrafos</strong> (separados por linha em branco)</li>
<li>Atribuicao em <strong>linha unica</strong> com <strong>negrito</strong> e <em>italico</em></li>
<li>Sempre incluir referencia biblica e autor cristao</li>
<li>3 perguntas com interrogacao</li>
<li>1 linha de espaco entre perguntas (Rise numera automaticamente)</li>
<li>Perguntas relacionadas ao conteudo da aula</li>
<li>Perguntas progridem em profundidade: observacao → interpretacao → aplicacao</li>
</ul>

<h4>DB de Autores para Narrar:</h4>
<table class="tutorial-table">
<thead><tr><th>Categoria</th><th>Autores</th><th>Quando Usar</th></tr></thead>
<tbody>
<tr><td>Pais da Igreja</td><td>Agostinho, Basilio, Gregorio de Nissa, Joao Crisostomo, Irineu, Atanasio</td><td>Fundamento, criacao, beleza, verdade</td></tr>
<tr><td>Puritanos</td><td>John Owen, Richard Baxter, Thomas Watson, John Bunyan, William Gurnall</td><td>Disciplina, contraste moral, forma interior</td></tr>
<tr><td>Poetas Cristaos</td><td>George Herbert, John Milton, Christina Rossetti, Gerard Manley Hopkins</td><td>Imagem, sensibilidade, emocao, simbolo</td></tr>
<tr><td>Autores Modernos</td><td>C.S. Lewis, Tolkien, Chesterton, T.S. Eliot, G.K. Meyer</td><td>Conectar tradicao e sensibilidade contemporanea</td></tr>
<tr><td>Artistas Visuais</td><td>Giotto, Fra Angelico, Caravaggio, Rembrandt, Blake, Friedrich</td><td>Composicao, luz, materialidade, intencao estetica</td></tr>
</tbody>
</table>
</div>

<div class="tutorial-content-section">
<h3>Repeticao Obrigatoria da Definicao — Mapa Visual</h3>
<div class="tutorial-code-block">A mesma definicao de 9-10 palavras aparece em:

1. Definir → Paragrafo introdutorio (final)
   "Reconheca que... Observe que... [Definicao]. Veja o video abaixo."

2. Definir → Accordion (texto simples, dentro do MP3)
   "[MP3/] #11L:xxxx [Definicao] [MP3\]"

3. Definir → Accordion (negrito)
   "[Definicao com palavras-chave em negrito]"

4. Recordar → Statement_D
   "[MP3/] #11L:xxxx [Definicao CURTA] [MP3\]"

5. Praticar → Fill_In (com lacunas)
   "[Definicao com _____ no lugar das respostas]"

6. Revisao Semanal (X.4) → Tabela + Recordar
   Tabela de termos + flashcard de memorizacao

Violacao = REJEICAO AUTOMATICA na Etapa 4 (Reviewer)</div>
</div>

<div class="tutorial-content-section">
<h3>Templates Individuais por Habito</h3>
<p>Alem do Golden Template principal, cada habito tem seu proprio template de referencia:</p>
<table class="tutorial-table">
<thead><tr><th>Template</th><th>Habito</th><th>Orienta</th></tr></thead>
<tbody>
<tr><td><code>defining.md</code></td><td>Definir</td><td>Introducao ao conceito, definicao Webster, etimologia</td></tr>
<tr><td><code>perceiving.md</code></td><td>Perceber</td><td>Observacao visual, perguntas de analise</td></tr>
<tr><td><code>remembering.md</code></td><td>Recordar</td><td>Frase de memorizacao, conexao poetica/musical</td></tr>
<tr><td><code>practicing.md</code></td><td>Praticar</td><td>Atividade pratica, exercicio de fixacao</td></tr>
<tr><td><code>narrating.md</code></td><td>Narrar</td><td>Trecho literario, momento de narracao, perguntas</td></tr>
</tbody>
</table>
</div>

<div class="tutorial-content-section">
<h3>Exemplo Concreto: exemplo_aula_final.md</h3>
<p>O arquivo <code>editorial-squad/templates/exemplo_aula_final.md</code> contem uma implementacao concreta do Golden Template. Use como referencia visual do que uma aula finalizada deve parecer. Nao e o padrao (o padrao e o <code>padrao_final_aula.md</code>), mas sim um exemplo de como o padrao se manifesta na pratica.</p>
</div>

<div class="tutorial-content-section">
<h3>Alternancias de Blocos Permitidas</h3>
<table class="tutorial-table">
<thead><tr><th>Habito</th><th>Contexto</th><th>Opcao A (padrao)</th><th>Opcao B (alternativa)</th></tr></thead>
<tbody>
<tr><td>Perceber</td><td>Revisao .4</td><td>FLASHCARD_GRID / IMAGE</td><td>TABS (2 abas com imagem + texto)</td></tr>
<tr><td>Narrar</td><td>Aula regular</td><td>IMAGE_TEXT_ASIDE</td><td>PARAGRAPH (3o ano)</td></tr>
<tr><td>Recordar</td><td>Aula regular</td><td>IMAGE_TEXT_ON (musica)</td><td>STATEMENT_A (rima)</td></tr>
</tbody>
</table>
<p>O usuario pode solicitar a troca a qualquer momento. O agente deve aplicar a variante escolhida e manter a consistencia ao longo de toda a semana.</p>
</div>
`},

// ============================================================================
// SECAO 6 — WORKFLOWS OPERACIONAIS
// ============================================================================
{id:'workflows',number:6,title:'Workflows Operacionais',icon:'<i class="ph ph-gear"></i>',color:'#f472b6',content:`
<h2><i class="ph ph-gear" style="color:var(--accent-primary);margin-right:0.5rem;"></i> 6. Workflows Operacionais</h2>

<div class="tutorial-content-section">
<h3>Os 3 Workflows Operacionais</h3>
<p>O Trivium Method opera com tres workflows principais que cobrem todo o ciclo de vida editorial:</p>
<table class="tutorial-table">
<thead><tr><th>Workflow</th><th>Arquivo</th><th>Cobertura</th></tr></thead>
<tbody>
<tr><td><strong>produce_class.md</strong></td><td><code>editorial-squad/workflows/produce_class.md</code></td><td>Pipeline completo de criacao de aula (7 etapas)</td></tr>
<tr><td><strong>publish.md</strong></td><td><code>editorial-squad/workflows/publish.md</code></td><td>Versionamento e sincronizacao com GitHub</td></tr>
<tr><td><strong>orchestrate.md</strong></td><td><code>editorial-squad/workflows/orchestrate.md</code></td><td>Ativacao do Diretor Editorial para diagnostico</td></tr>
</tbody>
</table>
</div>

<div class="tutorial-content-section">
<h3>WORKFLOW 1: produce_class.md — Pipeline de Producao de Aula</h3>
<p><strong>Este e o documento mais importante da operacao editorial.</strong> Define o modelo de linha de montagem em 7 etapas.</p>

<h4>Como Invocar:</h4>
<div class="tutorial-code-block">"Crie a aula 36.3, 2o ano"
"Produza a semana 15, 3o ano"
"Crie a aula X.Y, No ano"</div>

<h4>Resolucao de Caminhos (Diretorios por Ano):</h4>
<table class="tutorial-table">
<thead><tr><th>Ano</th><th>Diretorio</th></tr></thead>
<tbody>
<tr><td>1o</td><td><code>1o Ano - ARTE CRISTA PRIMITIVA E ICONES BIZANTINOS/</code></td></tr>
<tr><td>2o</td><td><code>2o Ano - DA CRIACAO ATE A ARTE BIZANTINA/</code></td></tr>
<tr><td>3o</td><td><code>3o Ano - RENASCIMENTO E REFORMA/</code></td></tr>
<tr><td>4o</td><td><code>4o Ano - BARROCO ATE O NEOCLASSICISMO/</code></td></tr>
<tr><td>5o</td><td><code>5o Ano - MANEIRISMO ATE O REALISMO AMERICANO/</code></td></tr>
</tbody>
</table>
<p>Base: <code>Belas Artes - Fase da Gramatica/1 Fase - Gramatica/[Diretorio]/</code></p>

<h4>Workflow Visual Completo:</h4>
<div class="tutorial-code-block">ETAPA 1: PESQUISA (Researcher)
  Input: Tema + Plano Pedagogico
  Output: research_report.md
  Acoes:
  → Ler skill do researcher
  → Consultar Plano Pedagogico
  → Consultar Curriculo Macro (termos proibidos)
  → Pesquisar: Webster 1828, versiculos, arte, poema, trecho literario
  → Compilar por 5 habitos

  |
  v

ETAPA 2: REDACAO (Writer)
  Input: research_report.md
  Output: draft_class.md
  Acoes:
  → Ler skill do writer
  → Consultar golden template
  → Consultar guia de estilo + doutrina pedagogica
  → Redigir conteudo dos 5 habitos
  → Garantir: voz ativa, imperativo, limites de texto

  |
  v

ETAPA 3: FORMATAcAO (Standardizer + Capitalizer)
  Input: draft_class.md
  Output: formatted_class.md
  Acoes:
  → Ler skill do standardizer
  → Consultar rise-blocks-reference.md
  → Correcoes editoriais proativas
  → Aplicar capitalizacao europeia
  → Formatar com Rise Blocks
  → Remover metadados, emojis, separadores

  |
  v

ETAPA 4: REVISAO (Reviewer)
  Input: formatted_class.md
  Output: reviewed_class.md ou rejeicao
  Acoes:
  → Checklist 13 categorias
  → 10 erros conhecidos da IA
  → Validacao golden template
  → APROVADO → [APPROVED_FOR_STEP_5]
  → REJEITADO → volta etapa 2 (conteudo) ou 3 (formato)

  | (aprovado)
  v

ETAPA 5: POLIMENTO (Copywriter)
  Input: reviewed_class.md
  Output: final_class.md
  Acoes:
  → Otimizar titulo
  → Polir enunciados
  → Revisar fluidez
  → Checagem final

  |
  v

ETAPA 6: REGISTRO
  Input: final_class.md
  Output: Curriculo Macro atualizado
  Acoes:
  → Marcar aulas com check
  → Marcar semana com check
  → Adicionar bloco de termos

  |
  v

ETAPA 7: PUBLICACAO (Publisher)
  Input: aula final
  Output: Arquivo local + GitHub commit
  Acoes:
  → Salvar como X.Y.md
  → Push para GitHub via MCP
  → Confirmar ao usuario</div>

<h4>Notas Importantes:</h4>
<ul>
<li>Cada etapa consome o output da anterior (Context Loop)</li>
<li>O fluxo e <strong>idempotente</strong>: pode ser re-executado sem efeitos colaterais</li>
<li>Para uma <strong>semana inteira</strong>, executar 3x (aulas X.1, X.2, X.3) + revisao (X.4) + prova (X.5)</li>
<li>O Reviewer pode rejeitar e mandar de volta — isso e parte normal do fluxo</li>
</ul>
</div>

<div class="tutorial-content-section">
<h3>WORKFLOW 2: publish.md — Versionamento Git</h3>
<p><strong>Arquivo:</strong> <code>editorial-squad/workflows/publish.md</code></p>
<p>Garante que o repositorio sincronize de forma saudavel com o GitHub, prevenindo bloqueio por excesso de tamanho.</p>

<h4>Problemas Resolvidos:</h4>
<ul>
<li>Quebra de push com arquivos grandes (.mp4, .pdf)</li>
<li>Limite rigido de 100MB do GitHub</li>
<li>Repositorio acima de 2GB tornando tudo lento</li>
<li>Falha na sincronizacao misturando notas ativas com midias inutilizadas</li>
</ul>

<h4>Regra de Ouro:</h4>
<div class="tutorial-info-card">
<strong>O Git NAO e para armazenar midia pesada! O Git e exclusivamente para texto, historico de revisoes e gestao de conhecimento puro.</strong>
</div>

<h4>Padrao Ouro do .gitignore:</h4>
<ol>
<li><strong>Ignorar midia por extensao critica:</strong> <code>*.mp4</code>, <code>*.pdf</code>, <code>*.zip</code>, <code>*.mp3</code></li>
<li><strong>Ignorar midias em fluxo (recomendado):</strong> <code>*.png</code>, <code>*.jpg</code>, <code>*.webp</code></li>
<li><strong>Ignorar lixo do framework:</strong> <code>.DS_Store</code>, caches <code>.obsidian/</code></li>
<li><strong>Abrir excecao para conhecimento:</strong> <code>!README.md</code>, <code>!*.md</code>, <code>!*.canvas</code></li>
</ol>

<h4>Limpeza Profissional (quando repo contaminado):</h4>
<div class="tutorial-code-block"># Sincroniza a exclusao e limpa do index (mantendo no disco):
git rm -r --cached .

# Re-adiciona somente os nao ignorados:
git add .

# Registra a alteracao:
git commit -m "chore: Limpeza profissional - removendo arquivos pesados"

# Sobe forcando a limpeza no historico central:
git push origin main --force</div>

<h4>Nomenclatura de Commits:</h4>
<table class="tutorial-table">
<thead><tr><th>Prefixo</th><th>Uso</th></tr></thead>
<tbody>
<tr><td><code>content:</code></td><td>Novo conteudo editorial (aulas, revisoes, provas)</td></tr>
<tr><td><code>fix:</code></td><td>Correcao de erros em conteudo existente</td></tr>
<tr><td><code>chore:</code></td><td>Manutencao tecnica (scripts, .gitignore, limpeza)</td></tr>
</tbody>
</table>
</div>

<div class="tutorial-content-section">
<h3>WORKFLOW 3: orchestrate.md — Ativacao do Orchestrator</h3>
<p><strong>Arquivo:</strong> <code>editorial-squad/workflows/orchestrate.md</code></p>
<p>Atalho para ativar o Orquestrador da Squad e obter direcao sobre o projeto.</p>

<h4>Como Invocar:</h4>
<div class="tutorial-code-block">@orchestrator
/orchestrate
"O que devo fazer agora?"</div>

<h4>Passo a Passo do Orchestrator:</h4>
<ol>
<li>Ler a skill do orquestrador: <code>editorial-squad/skills/orchestrator/SKILL.md</code></li>
<li>Identificar a <strong>Disciplina</strong> e o <strong>Ano</strong> em questao</li>
<li>Ler o <strong>Curriculo Macro</strong> da disciplina/ano correspondente</li>
<li>Executar o <strong>Diagnostico de Progresso</strong>:
<ul>
<li>Contar semanas check completas</li>
<li>Identificar semana em andamento</li>
<li>Identificar proxima semana</li>
</ul>
</li>
<li>Executar a <strong>Priorizacao Inteligente</strong>:
<ul>
<li>Lista ordenada de proximas acoes</li>
</ul>
</li>
<li>Se o usuario tiver demanda especifica, usar a <strong>Tabela de Roteamento</strong> para delegar</li>
<li>Apresentar relatorio final ao usuario</li>
</ol>

<h4>Formato do Relatorio Final:</h4>
<div class="tutorial-code-block">STATUS — [Ano]
Semanas completas: [range]
Em andamento: Semana [N] (detalhes)
Proxima: Semana [N]

PROXIMAS ACOES:
1. [acao prioritaria]
2. [acao secundaria]
3. [acao terciaria]</div>
</div>

<div class="tutorial-content-section">
<h3>Resumo: Quando Usar Cada Workflow</h3>
<table class="tutorial-table">
<thead><tr><th>Situacao</th><th>Workflow</th><th>Comando</th></tr></thead>
<tbody>
<tr><td>Criar uma aula do zero</td><td>produce_class.md</td><td>"Crie a aula X.Y, No ano"</td></tr>
<tr><td>Criar aula de revisao semanal (X.4)</td><td>produce_class.md + review-builder</td><td>"Crie a revisao da semana X"</td></tr>
<tr><td>Criar revisao bimestral</td><td>produce_class.md + bimester-review</td><td>"Revisao do bimestre N"</td></tr>
<tr><td>Criar prova bimestral</td><td>produce_class.md + bimester-exam</td><td>"Prova do bimestre N"</td></tr>
<tr><td>Saber o que fazer</td><td>orchestrate.md</td><td>@orchestrator</td></tr>
<tr><td>Commit e push manual</td><td>publish.md</td><td>@devops</td></tr>
<tr><td>Repo travou com arquivos grandes</td><td>publish.md</td><td>@devops "limpeza"</td></tr>
</tbody>
</table>
</div>
`},

// ============================================================================
// SECAO 7 — DATA SYNC E AUTOMACAO
// ============================================================================
{id:'datasync',number:7,title:'Data Sync e Automacao',icon:'<i class="ph ph-file-py"></i>',color:'#fbbf24',content:`
<h2><i class="ph ph-file-py" style="color:var(--accent-primary);margin-right:0.5rem;"></i> 7. Data Sync e Automacao</h2>

<div class="tutorial-content-section">
<h3>Os 4 Processos de Sincronizacao</h3>
<p>O Trivium Method mantem 4 processos de sincronizacao que garantem consistencia entre todos os sistemas:</p>
</div>

<div class="tutorial-content-section">
<h3>SYNC 1: Vision Board Kanban Sync (Automático — 5 min)</h3>
<p><strong>Arquivos:</strong> <code>src/sync.js</code> + <code>.github/workflows/data-sync.yml</code></p>
<p><strong>Frequencia:</strong> A cada 5 minutos (cron <code>*/5 * * * *</code>)</p>

<h4>Mecanismo:</h4>
<div class="tutorial-code-block">1. GitHub Actions dispara cron job
2. Checkout shallow (fetch-depth: 1)
3. Node src/sync.js executa:
   → Query GitHub Projects via GraphQL
   → Project ID: PVT_kwDODLv1ac4BH1XW
   → Token: VISIONBOARDBIBLINE (PAT com repo + project)
   → Extrai todos os items com paginacao
   → Parse subject de "[Subject]" no titulo
   → Parse year de "Ano N" no titulo
   → Calcula lead_time_days (created_at → closed_at)
4. Gera public/data.json com:
   → last_updated: timestamp
   → total_items: contagem
   → items[]: array de todos os cards
5. Verify: confere se data.json foi criado
6. Commit & Push (atomic diff check):
   → Apenas se dados mudaram
   → Mensagem: "data: sync Kanban - N items (auto-sync)"</div>

<h4>SLA:</h4>
<ul>
<li>Execucao: ~2-3 minutos</li>
<li>Deploy: ~30 segundos</li>
<li>Total: ~3-4 minutos</li>
</ul>

<h4>Dados Extraidos por Item:</h4>
<table class="tutorial-table">
<thead><tr><th>Campo</th><th>Descricao</th></tr></thead>
<tbody>
<tr><td><code>id</code></td><td>ID unico do item no GitHub</td></tr>
<tr><td><code>number</code></td><td>Numero do card</td></tr>
<tr><td><code>title</code></td><td>Titulo completo</td></tr>
<tr><td><code>status</code></td><td>Estagio no pipeline (Backlog, In Progress, etc.)</td></tr>
<tr><td><code>state</code></td><td>Estado (open/closed)</td></tr>
<tr><td><code>assignee</code></td><td>Responsavel</td></tr>
<tr><td><code>labels</code></td><td>Labels (disciplina, ano, etc.)</td></tr>
<tr><td><code>created_at</code></td><td>Data de criacao</td></tr>
<tr><td><code>closed_at</code></td><td>Data de fechamento</td></tr>
<tr><td><code>lead_time_days</code></td><td>Tempo de producao em dias</td></tr>
</tbody>
</table>
</div>

<div class="tutorial-content-section">
<h3>SYNC 2: Title Synchronization (Manual — Quando Titulos Mudam)</h3>
<p><strong>Arquivo:</strong> <code>editorial-squad/scripts/sync_titles.py</code></p>
<p><strong>Fonte da Verdade:</strong> Arquivo <code>1 - Curriculo Macro</code></p>

<h4>O que faz:</h4>
<p>Script MASTER que propaga titulos do Curriculo Macro para TODOS os arquivos downstream:</p>
<ul>
<li><strong>Arquivo 2</strong> (Matriz-Curricular-objetivos) — titulos nas tabelas de aulas</li>
<li><strong>Arquivo 3</strong> (Visao e Plano pedagogico) — titulos nas tabelas de estrutura</li>
<li><strong>Arquivo 6</strong> (Descricoes para tickets) — titulos nas linhas de tarefa</li>
<li><strong>Headers H1</strong> de todos os arquivos <code>.md</code> de aulas individuais</li>
</ul>

<h4>Quando Executar:</h4>
<div class="tutorial-info-card">
<strong>DEVE ser executado apos QUALQUER mudanca nos titulos do Curriculo Macro.</strong> Se voce alterou o H1 de uma aula, o primeiro passo e atualizar o Macro, e o segundo e rodar <code>sync_titles.py</code>.
</div>

<h4>Como Executar:</h4>
<div class="tutorial-code-block">cd "Projeto Bibline Academy/editorial-squad/scripts"
python sync_titles.py</div>

<h4>Fluxo Padrao apos Mudanca no Macro:</h4>
<div class="tutorial-code-block">1. Alterar Curriculo Macro (Arquivo 1)
2. Executar sync_titles.py → propaga para Arquivos 2, 3, 6 e H1s
3. (Opcional) Executar check_matriz.py → verificar alinhamento
4. Commitar e publicar</div>
</div>

<div class="tutorial-content-section">
<h3>SYNC 3: Curriculum Synchronization (Manual — Quando Aulas Existentes Mudam)</h3>
<p>Quando aulas existentes sao modificadas, 5 arquivos devem ser atualizados:</p>
<table class="tutorial-table">
<thead><tr><th>Arquivo</th><th>Gatilho</th></tr></thead>
<tbody>
<tr><td><code>1 - Curriculo Macro</code></td><td>Se o titulo (H1) da aula mudar</td></tr>
<tr><td><code>2 - Matriz-Curricular-objetivos</code></td><td>Se o objetivo teologico-pedagogico mudar</td></tr>
<tr><td><code>3 - Visao e Plano pedagogico</code></td><td>Se a abordagem da aula (Definir/Perceber) mudar</td></tr>
<tr><td><code>4 - Links-para-imagens-perceber</code></td><td>Se a secao Perceber mudar</td></tr>
<tr><td><strong>Aula de Revisao (X.4.md)</strong></td><td>Se alterar definicoes ou atividades</td></tr>
</tbody>
</table>
</div>

<div class="tutorial-content-section">
<h3>SYNC 4: GitHub Issue/Project Sync (Automático via Scripts)</h3>
<p><strong>Scripts:</strong> <code>create_issues.py</code>, <code>update_github_issues_to_year1.py</code>, <code>update_backlog_tickets.py</code>, <code>sync_issues_week13.py</code>, <code>update_fast.py</code></p>
<p><strong>Proposito:</strong> Criar e gerenciar Issues do GitHub como cartoes Kanban para o Vision Board.</p>
<h4>Script update_fast.py:</h4>
<p>Atualiza titulos e bodys das Issues na coluna Backlog do GitHub Projects via GraphQL. Single Source of Truth → Cloud.</p>
</div>

<div class="tutorial-content-section">
<h3>Catalogo Completo de Scripts (18+ Scripts)</h3>

<h4>Scripts Mestres:</h4>
<table class="tutorial-table">
<thead><tr><th>Script</th><th>Funcao</th><th>Le</th><th>Modifica</th></tr></thead>
<tbody>
<tr><td><code>sync_titles.py</code></td><td><strong>MASTER:</strong> Propagacao completa de titulos do Macro</td><td>Curriculo Macro</td><td>Arquivos 2, 3, 6 + H1s</td></tr>
</tbody>
</table>

<h4>Scripts de Auditoria:</h4>
<table class="tutorial-table">
<thead><tr><th>Script</th><th>Funcao</th><th>Modifica?</th></tr></thead>
<tbody>
<tr><td><code>check_matriz.py</code></td><td>Compara Matriz (Arq. 2) com Macro (Arq. 1) e reporta divergencias</td><td>Nao (so leitura)</td></tr>
<tr><td><code>converters/convert_recordar_to_rhyme.py</code></td><td>Identifica quais aulas possuem blocos de musica (pre-conversao)</td><td>Nao (so leitura)</td></tr>
<tr><td><code>check_project_items.py</code></td><td>Audita e lista itens ativos em um ProjectV2 do GitHub</td><td>Nao (so leitura)</td></tr>
</tbody>
</table>

<h4>Scripts Modulares de Sincronizacao:</h4>
<table class="tutorial-table">
<thead><tr><th>Script</th><th>Funcao</th><th>Escopo</th></tr></thead>
<tbody>
<tr><td><code>align_titles.py</code></td><td>Sincroniza titulos de aulas no Arquivo 6 (tickets)</td><td>Apenas linhas de aula X.1, X.2, X.3</td></tr>
<tr><td><code>align_review_titles.py</code></td><td>Sincroniza titulos referenciados em blocos de revisao/prova</td><td>Apenas referencias internas</td></tr>
<tr><td><code>fix_lesson_h1.py</code></td><td>Sincroniza H1 dos arquivos de aula individuais com o Macro</td><td>Apenas headers H1</td></tr>
<tr><td><code>fix_titles.py</code></td><td>Remove sufixos cosmeticos indesejados de titulos</td><td>Formatacao do Arquivo 6</td></tr>
</tbody>
</table>

<h4>Gerador Massivo:</h4>
<table class="tutorial-table">
<thead><tr><th>Script</th><th>Funcao</th><th>Atencao</th></tr></thead>
<tbody>
<tr><td><code>generate_descriptions.py</code></td><td>Regenera completamente o Arquivo 6 a partir de dados hardcoded</td><td><strong>DESTRUTIVO:</strong> sobrescreve tudo</td></tr>
</tbody>
</table>

<h4>Scripts de Conversao e Formatacao:</h4>
<table class="tutorial-table">
<thead><tr><th>Script</th><th>Funcao</th><th>Escopo</th></tr></thead>
<tbody>
<tr><td><code>converters/convert_recordar.py</code></td><td>Converte blocos "musica" para "rima" na secao Recordar</td><td>Aulas .1, .2, .3 do 3o ano</td></tr>
<tr><td><code>formatters/fix_accordion.py</code></td><td>Remove repeticao redundante do termo no Accordion</td><td>Aulas do 4o ano</td></tr>
</tbody>
</table>

<h4>Scripts de Gestao de Tickets no GitHub:</h4>
<table class="tutorial-table">
<thead><tr><th>Script</th><th>Funcao</th><th>Escopo</th></tr></thead>
<tbody>
<tr><td><code>update_fast.py</code></td><td>Atualiza titulos e bodys das Issues no Backlog via GraphQL</td><td>Projetos e Issues remotas</td></tr>
<tr><td><code>check_project_items.py</code></td><td>Audita itens ativos em ProjectV2 do GitHub</td><td>Leitura remota</td></tr>
<tr><td><code>build_year1_tickets.py</code></td><td>Constroi base local estruturada de tickets para carga massiva</td><td>Geracao local (Year 1)</td></tr>
<tr><td><code>create_issues.py</code></td><td>Cria issues no GitHub</td><td>GitHub Projects</td></tr>
<tr><td><code>update_github_issues_to_year1.py</code></td><td>Atualiza issues do Year 1</td><td>GitHub Projects</td></tr>
<tr><td><code>update_backlog_tickets.py</code></td><td>Atualiza tickets do backlog</td><td>GitHub Projects</td></tr>
<tr><td><code>update_year1_tickets.py</code></td><td>Atualiza tickets do Year 1</td><td>GitHub Projects</td></tr>
<tr><td><code>update_tickets_fixed.py</code></td><td>Atualiza tickets corrigidos</td><td>GitHub Projects</td></tr>
<tr><td><code>sync_issues_week13.py</code></td><td>Sincroniza issues para semana 13</td><td>GitHub Projects</td></tr>
</tbody>
</table>
</div>

<div class="tutorial-content-section">
<h3>Fluxos de Execucao dos Scripts</h3>

<h4>Fluxo Padrao (apos mudanca no Macro):</h4>
<div class="tutorial-code-block">1. Alterar Curriculo Macro (Arquivo 1)
2. Executar sync_titles.py → propaga para Arquivos 2, 3, 6 e H1s
3. (Opcional) Executar check_matriz.py → verificar alinhamento
4. Commitar e publicar</div>

<h4>Fluxo de Emergencia (Arquivo 6 corrompido):</h4>
<div class="tutorial-code-block">1. Executar generate_descriptions.py → reconstroi Arquivo 6 do zero
2. Executar align_titles.py + align_review_titles.py → sincronizar titulos
3. Executar fix_titles.py → limpar formatacao
4. Commitar e publicar</div>

<h4>Fluxo de Conversao (mudanca de formato):</h4>
<div class="tutorial-code-block">1. Executar convert_recordar_to_rhyme.py → auditar escopo
2. Executar convert_recordar.py → converter musica para rima
3. Executar fix_accordion.py → normalizar definicoes
4. Commitar e publicar</div>
</div>

<div class="tutorial-content-section">
<h3>GitHub Actions — Workflows CI/CD</h3>

<h4>Workflow 1: deploy-pages.yml</h4>
<table class="tutorial-table">
<thead><tr><th>Propriedade</th><th>Valor</th></tr></thead>
<tbody>
<tr><td>Trigger</td><td>Push para main (paths: *.html, public/**) + manual</td></tr>
<tr><td>Jobs</td><td>Build (valida HTML/JS) → Deploy (upload pages)</td></tr>
<tr><td>Output URL</td><td>https://italogabriel-lab.github.io/Projeto-Editorial-Education/</td></tr>
<tr><td>Concurrency</td><td>Grupo github-pages-deploy, cancela execucoes anteriores</td></tr>
</tbody>
</table>

<h4>Workflow 2: data-sync.yml</h4>
<table class="tutorial-table">
<thead><tr><th>Propriedade</th><th>Valor</th></tr></thead>
<tbody>
<tr><td>Trigger</td><td>Cron a cada 5 minutos (*/5 * * * *) + manual</td></tr>
<tr><td>Token</td><td>VISIONBOARDBIBLINE (PAT com repo + project)</td></tr>
<tr><td>Project ID</td><td>PVT_kwDODLv1ac4BH1XW ("Bibline Aulas")</td></tr>
<tr><td>Jobs</td><td>Checkout → Sync (GraphQL) → Verify → Commit & Push</td></tr>
<tr><td>SLA</td><td>~3-4 minutos total</td></tr>
</tbody>
</table>
</div>
`},

// ============================================================================
// SECAO 8 — UI PAGES E DASHBOARD
// ============================================================================
{id:'ui',number:8,title:'UI Pages e Dashboard',icon:'<i class="ph ph-desktop"></i>',color:'#06b6d4',content:`
<h2><i class="ph ph-desktop" style="color:var(--accent-primary);margin-right:0.5rem;"></i> 8. UI Pages e Dashboard</h2>

<div class="tutorial-content-section">
<h3>Vision Board Dashboard — Visao Geral</h3>
<p>O Vision Board e o dashboard central do projeto, deployado via GitHub Pages + Vercel. Ele consome dados do <code>public/data.json</code> (gerado pelo sync automatico a cada 5 minutos) e apresenta metricas em tempo real do Kanban.</p>
<p><strong>URL Base:</strong> <code>https://italogabriel-lab.github.io/Projeto-Editorial-Education/</code></p>
</div>

<div class="tutorial-content-section">
<h3>As 6 Paginas do Dashboard</h3>
<table class="tutorial-table">
<thead><tr><th>Pagina</th><th>URL</th><th>Funcao</th></tr></thead>
<tbody>
<tr><td><strong>Home</strong></td><td><code>/</code></td><td>Landing page com overview do projeto, links rapidos, apresentacao</td></tr>
<tr><td><strong>Overview Geral</strong></td><td><code>/index.html</code></td><td>Dashboard principal mostrando todos os dados do Kanban de data.json. Cards, graficos, filtros por status, disciplina, ano.</td></tr>
<tr><td><strong>Metas (Curriculo)</strong></td><td><code>/metas.html</code></td><td>Tracking de metas do curriculo. Visao geral de progresso por disciplina e ano. Comparacao meta vs realizado.</td></tr>
<tr><td><strong>Metas (Disciplinas)</strong></td><td><code>/metas-disciplinas.html</code></td><td>Metas baseadas em disciplina com <strong>Year Health Feature</strong> (4 status levels: Completado, Saudavel, Atencao, Critico). Clique em cards de disciplina → ano → saude completa.</td></tr>
<tr><td><strong>Videos Pipeline</strong></td><td><code>/videos.html</code></td><td>Tracking de pipeline de producao de videos. Status de cada video por disciplina/ano/semana.</td></tr>
<tr><td><strong>Agent Command Center</strong></td><td><code>/agent-command-center.html</code></td><td>UI premium de 5300+ linhas mostrando todos os 22 agentes, workflow visualization, performance de equipe, status do pipeline. Inclui Tutorial Viewer (esta documentacao).</td></tr>
</tbody>
</table>
</div>

<div class="tutorial-content-section">
<h3>Vision Board — Funcionalidades do Overview</h3>
<ul>
<li><strong>Filtros:</strong> Por status (Backlog, In Progress, In Review, Video, Done/Published), por disciplina, por ano</li>
<li><strong>Metricas:</strong> Total de items, percentual por status, lead time medio</li>
<li><strong>Cards:</strong> Cada item do Kanban renderizado como card com titulo, status, assignee, labels</li>
<li><strong>Atualizacao:</strong> Dados atualizados automaticamente a cada 5 minutos via sync</li>
</ul>
</div>

<div class="tutorial-content-section">
<h3>Year Health Feature (metas-disciplinas.html)</h3>
<p>Funcionalidade avancada que calcula a saude de cada ano de cada disciplina com base na producao real vs esperada.</p>

<h4>4 Niveis de Status:</h4>
<table class="tutorial-table">
<thead><tr><th>Status</th><th>Icon</th><th>Criterio</th><th>Significado</th></tr></thead>
<tbody>
<tr><td><strong>Completado</strong></td><td>✅</td><td>Meta atingida (producao real >= meta esperada)</td><td>Meta concluida! Parabens equipe!</td></tr>
<tr><td><strong>Saudavel</strong></td><td>🌟</td><td>No ritmo certo (producao acompanha tempo decorrido)</td><td>Producao dentro do esperado para o tempo</td></tr>
<tr><td><strong>Atencao</strong></td><td>⚠️</td><td>Ritmo lento (producao abaixo do esperado)</td><td>Precisa acelerar para atingir meta</td></tr>
<tr><td><strong>Critico</strong></td><td>🔴</td><td>Atrasado (producao muito abaixo do esperado)</td><td>Acao imediata necessaria</td></tr>
</tbody>
</table>

<h4>Metricas Exibidas ao Clicar em um Ano:</h4>
<ul>
<li>Status alert (color-coded com emoji e cor)</li>
<li>Producao total do ano</li>
<li>Meta total do ano (168 aulas)</li>
<li>Percentual de conclusao</li>
<li>Ritmo de producao (aulas/semana)</li>
<li>Projecao de conclusao baseada no ritmo atual</li>
<li>Acoes recomendadas automaticamente</li>
</ul>

<h4>Como Usar:</h4>
<ol>
<li>Acesse <code>/metas-disciplinas.html</code></li>
<li>Clique em qualquer card de disciplina (História, Ciências, Belas Artes, etc.)</li>
<li>Clique em qualquer card de ano (1º Ano, 2º Ano, etc.)</li>
<li>Visualize o dashboard de saude completo com metricas detalhadas</li>
</ol>
</div>

<div class="tutorial-content-section">
<h3>Agent Command Center (agent-command-center.html)</h3>
<p>A pagina mais completa do projeto — 5300+ linhas de UI premium.</p>

<h4>Funcionalidades:</h4>
<ul>
<li><strong>Agent Grid:</strong> Todos os 22 agentes organizados por categoria (Core, Specialized, Analytics, Bimester, Legacy)</li>
<li><strong>Workflow Visualization:</strong> Diagrama visual das 7 etapas do pipeline</li>
<li><strong>Performance de Equipe:</strong> Metricas de produtividade individual e coletiva</li>
<li><strong>Status do Pipeline:</strong> Visao em tempo real de cada estagio</li>
<li><strong>Comandos Expansiveis:</strong> Cada agente mostra comandos com prompts clicaveis e copiateis</li>
<li><strong>Tutorial Viewer:</strong> Esta documentacao integrada como modal de tutorial com navegacao por secoes</li>
<li><strong>Search e Filtros:</strong> Busca por nome, categoria, comando</li>
<li><strong>Temas:</strong> Dark/Light mode toggle</li>
</ul>

<h4>Design System do Command Center:</h4>
<ul>
<li>Tipografia: Inter (sans-serif) + JetBrains Mono (code)</li>
<li>Cores: Cyan (#2dd4bf), Purple (#8b5cf6), Pink (#f472b6), Amber (#fbbf24)</li>
<li>Categorias com cores distintas: Core (green), Specialized (cyan), Analytics (rose), Bimester (purple), Legacy (slate)</li>
<li>Efeitos: Glassmorphism, gradientes, glow, animacoes de hover</li>
<li>Responsivo: Funciona em mobile, tablet e desktop</li>
</ul>
</div>

<div class="tutorial-content-section">
<h3>Como os Dados Fluem para o Dashboard</h3>
<div class="tutorial-code-block">GitHub Projects Kanban (bibline/org)
         |
         | GraphQL API query via PAT
         | Project ID: PVT_kwDODLv1ac4BH1XW
         v
GitHub Actions (data-sync.yml)
         |
         | node src/sync.js
         | Parse: subject, year, status, assignee, labels
         | Calcula: lead_time_days
         v
public/data.json
{
  "last_updated": "2026-04-09T...",
  "total_items": 342,
  "items": [
    { id, number, title, status, state,
      assignee, labels, created_at,
      closed_at, lead_time_days,
      subject, year }
  ]
}
         |
         | app.js, metas.js, videos.js
         | leem data.json e renderizam
         v
Dashboard Pages (HTML + JS)
         |
         | Renderiza cards, graficos, metricas
         | Year Health calcula status
         | Filtros e interacoes
         v
Usuario ve tudo no navegador</div>
</div>

<div class="tutorial-content-section">
<h3>Links Rapidos de Todas as Paginas</h3>
<div class="tutorial-code-block">Home:                   https://...github.io/Projeto-Editorial-Education/
Overview:               https://...github.io/Projeto-Editorial-Education/index.html
Metas:                  https://...github.io/Projeto-Editorial-Education/metas.html
Metas Disciplinas:      https://...github.io/Projeto-Editorial-Education/metas-disciplinas.html
Videos Pipeline:        https://...github.io/Projeto-Editorial-Education/videos.html
Agent Command Center:   https://...github.io/Projeto-Editorial-Education/agent-command-center.html

GitHub Repo:            https://github.com/italogabriel-lab/Projeto-Editorial-Education
GitHub Actions:         https://github.com/italogabriel-lab/Projeto-Editorial-Education/actions
Kanban Project:         https://github.com/orgs/bibline/projects/2/views/1</div>
</div>

<div class="tutorial-content-section">
<h3>Dica: Cache Bust</h3>
<div class="tutorial-info-card">
Se as mudancas nao aparecerem no dashboard, faca hard refresh: <strong>Ctrl+Shift+R</strong> (Linux/Windows) ou <strong>Cmd+Shift+R</strong> (Mac). Tambem pode adicionar version parameter na URL: <code>?v=2</code>.
</div>
</div>
`},

// ============================================================================
// SECAO 9 — KNOWLEDGE BASE
// ============================================================================
{id:'knowledge',number:9,title:'Knowledge Base',icon:'<i class="ph ph-book-open"></i>',color:'#a78bfa',content:`
<h2><i class="ph ph-book-open" style="color:var(--accent-primary);margin-right:0.5rem;"></i> 9. Knowledge Base — Base de Conhecimento</h2>

<div class="tutorial-content-section">
<h3>Visao Geral da Knowledge Base</h3>
<p>A Knowledge Base e o conjunto de documentos que fundamentam TODAS as decisoes editoriais do Trivium Method. Cada agente consulta estes documentos durante sua operacao. Sem a KB, os agentes nao teriam padroes consistentes.</p>

<h4>Documentos Principais (editorial-squad/knowledge-base/):</h4>
<table class="tutorial-table">
<thead><tr><th>Documento</th><th>Linhas</th><th>Funcao</th><th>Quem Consulta</th></tr></thead>
<tbody>
<tr><td><code>visao-geral-fluxo-editorial.md</code></td><td>572</td><td>Mapa editorial master — regras de pipeline, sincronizacao, scripts</td><td>Todos os agentes</td></tr>
<tr><td><code>doutrina-pedagogica.md</code></td><td>~100</td><td>Base teologica e filosofica — Trivium, Cosmovisao Crista</td><td>Researcher, Writer, Reviewer</td></tr>
<tr><td><code>guia-de-estilo.md</code></td><td>~120</td><td>Guia de estilo — tom de voz, metricas, pontuacao proibida</td><td>Writer, Standardizer, Reviewer</td></tr>
<tr><td><code>rise-blocks-reference.md</code></td><td>~200</td><td>Dicionario de sintaxe de blocos Rise 360 (12 blocos)</td><td>Standardizer, Reviewer</td></tr>
<tr><td><code>relatorio-vision-board-projeto.md</code></td><td>~50</td><td>Relatorio do projeto Vision Board</td><td>Analytics Agents</td></tr>
</tbody>
</table>

<h4>Documentos Expandidos (Base de Conhecimento/2-Base de Conhecimento/):</h4>
<table class="tutorial-table">
<thead><tr><th>Documento</th><th>Conteudo</th></tr></thead>
<tbody>
<tr><td><code>Referencias Literarias e Livros Vivos.md</code></td><td>DB de autores cristoes e obras para secao Narrar</td></tr>
<tr><td><code>Obras de Arte e Autores Classicos.md</code></td><td>DB de obras de arte para secao Perceber</td></tr>
<tr><td><code>Pontos de Atencao para Revisao.md</code></td><td>Regras fixas de revisao</td></tr>
<tr><td><code>Principais erros da IA.md</code></td><td>10 erros conhecidos da IA com o conteudo</td></tr>
<tr><td><code>13-Style conventions.md</code></td><td>Convencoes de escrita detalhadas</td></tr>
<tr><td><code>12-Structuring the content.md</code></td><td>Estrutura por habito</td></tr>
<tr><td><code>14-Structuring the Review.md</code></td><td>Formato de revisao semanal</td></tr>
</tbody>
</table>
</div>

<div class="tutorial-content-section">
<h3>Style Guide (guia-de-estilo.md) — Resumo Completo</h3>

<h4>Tom de Voz:</h4>
<ul>
<li><strong>Virtuoso e elevado</strong>, porem acessivel para criancas de 7 a 11 anos</li>
<li>Didatico sem ser infantilizado. Respeitoso sem ser inacessivel.</li>
<li>Use analogias ricas e referencias a grandes autores ou obras de arte.</li>
<li>Dirija-se ao aluno usando <strong>"voce"</strong> ou <strong>"seu"</strong></li>
<li><strong>Proibido:</strong> linguagem excessivamente infantilizada, girias modernas, ironia</li>
<li><strong>Obrigatorio:</strong> clareza na exposicao e beleza na forma</li>
<li>Tom biblico, robusto, respeitoso. Zero traços de passiva, gerundio excessivo.</li>
</ul>

<h4>Regras de Escrita Obrigatorias:</h4>
<table class="tutorial-table">
<thead><tr><th>Regra</th><th>Detalhe</th></tr></thead>
<tbody>
<tr><td><strong>Voz e Tempo</strong></td><td>Tempo presente, voz ativa. NUNCA voz passiva. Imperativo direto em enunciados.</td></tr>
<tr><td><strong>Sinais Proibidos</strong></td><td><code>;</code> (ponto e virgula), <code>:</code> (dois pontos no corpo), <code>—</code> (travessao). Usar <code>,</code> ou <code>.</code></td></tr>
<tr><td><strong>Aspas</strong></td><td>Somente aspas retas <code>" "</code>. Usadas SOMENTE no trecho literario do Narrar.</td></tr>
<tr><td><strong>Emojis</strong></td><td>NUNCA no corpo do texto</td></tr>
<tr><td><strong>Limite de Frases</strong></td><td>Maximo 30 palavras por frase</td></tr>
<tr><td><strong>Limite de Paragrafos</strong></td><td>Maximo 70 palavras por paragrafo</td></tr>
<tr><td><strong>Primeiro Paragrafo</strong></td><td>NUNCA repete o conteudo do titulo ou subtitulo</td></tr>
<tr><td><strong>Negrito</strong></td><td>Apenas para destacar termos-chave na terceira repeticao do accordion</td></tr>
</tbody>
</table>

<h4>Capitalizacao (Padrao Europeu):</h4>
<ul>
<li><strong>Sentence-case</strong> como padrao: maiuscula apenas na primeira palavra e nomes proprios</li>
<li><strong>Nomes proprios</strong> (Constantinopla, Bizancio, Justiniano) → sempre maiuscula</li>
<li><strong>Nomes institucionais consolidados</strong> (Imperio Bizantino, Igreja Catolica) → maiuscula</li>
<li><strong>Termos descritivos/genereicos</strong> (imperio romano, oriente, arte bizantina) → minuscula</li>
<li><strong>Preposicoes e artigos</strong> (de, da, do, em, o, a, e) → minuscula no meio de titulos</li>
<li><strong>Consistencia obrigatoria</strong>: mesmo termo com mesma capitalizacao em todas as secoes</li>
</ul>

<h4>Versiculos:</h4>
<ul>
<li>Preferencialmente ARA ou ARC</li>
<li>Formato completo: "Texto do versiculo" — Referencia (ex: Proverbios 22:29)</li>
<li>No IMAGE_TEXT_ON, formato curto: "Texto resumido — Referencia"</li>
</ul>
</div>

<div class="tutorial-content-section">
<h3>Doutrina Pedagogica (doutrina-pedagogica.md) — Resumo</h3>

<h4>O Trivium:</h4>
<table class="tutorial-table">
<thead><tr><th>Fase</th><th>Idade</th><th>Foco</th><th>Descricao</th></tr></thead>
<tbody>
<tr><td><strong>Gramatica</strong></td><td>7-11 anos</td><td>Fatos e Definicoes</td><td>Memorizacao, observacao, vocabulario. TODAS as aulas atuais estao aqui.</td></tr>
<tr><td>Logica</td><td>12-14 anos</td><td>Relacoes e Argumentos</td><td>Conectar ideias, questionar, debater</td></tr>
<tr><td>Retorica</td><td>15-18 anos</td><td>Expressao e Persuasao</td><td>Articular, defender, criar</td></tr>
</tbody>
</table>

<h4>Implicacoes para a Fase da Gramatica:</h4>
<ol>
<li><strong>Memorizacao</strong> e a atividade cognitiva central — definicoes, versiculos, vocabulario.</li>
<li><strong>Observacao</strong> precede a analise — primeiro ver, depois entender.</li>
<li><strong>Repeticao</strong> e virtude, nao redundancia — o mesmo conceito em multiplas formas.</li>
<li><strong>Narrativa</strong> e a forma mais natural de aprendizagem — historias fixam conhecimento.</li>
<li><strong>Vocabulario</strong> e construido progressivamente — cada aula introduz 1 termo novo.</li>
</ol>

<h4>Cosmovisao Crista Reformada — 6 Principios:</h4>
<ol>
<li><strong>Toda arte expressa uma cosmovisao</strong> — consciente ou inconscientemente.</li>
<li><strong>A beleza e dom de Deus</strong> — nao e construcao humana arbitraria.</li>
<li><strong>O cristao nao teme a arte</strong> — avalia com discernimento (Filipenses 4:8).</li>
<li><strong>A criacao proclama a glória de Deus</strong> — Salmo 19:1.</li>
<li><strong>Provar tudo, reter o que e bom</strong> — 1 Tessalonicenses 5:21.</li>
<li><strong>A arte nao e sagrada, somente Deus e santo</strong> — Exodo 20:4-5, Isaias 42:8.</li>
</ol>

<h4>A Pedagogia do Belo:</h4>
<ul>
<li>A beleza atrai antes de instruir</li>
<li>A virtude e mais aprendida por admiracao do que por imposicao</li>
<li>A arte e linguagem universal que fala ao coracao antes de falar a mente</li>
<li>O belo, o verdadeiro e o bom sao transcendentais inseparaveis</li>
</ul>
</div>

<div class="tutorial-content-section">
<h3>Rise Blocks Reference (rise-blocks-reference.md) — Os 12 Blocos</h3>
<p>Referencia completa de sintaxe para cada bloco Rise 360 usado nas aulas:</p>
<table class="tutorial-table">
<thead><tr><th>Bloco</th><th>Tag</th><th>Uso Principal</th></tr></thead>
<tbody>
<tr><td>Paragraph</td><td><code>[+PARAGRAPH]...[-PARAGRAPH]</code></td><td>Texto corrido (introducoes, enunciados, instrucoes)</td></tr>
<tr><td>Heading</td><td><code>[+HEADING]...[-HEADING]</code></td><td>Subtitulos dentro de habitos (NUNCA usar H3 markdown)</td></tr>
<tr><td>Video</td><td><code>[+VIDEO][-VIDEO]</code></td><td>Placeholder para video (sempre vazio)</td></tr>
<tr><td>Accordion</td><td><code>[+ACCORDION]...[-ACCORDION]</code></td><td>Definicao expandivel com pergunta, imagem, audio, reflexao</td></tr>
<tr><td>Image Labeled</td><td><code>[+IMAGE_LABELED]...[-IMAGE_LABELED]</code></td><td>Imagem com 2 hotspots rotulados (coordenadas percentuais)</td></tr>
<tr><td>Statement D</td><td><code>[+STATEMENT_D]...[-STATEMENT_D]</code></td><td>Bloco de declaracao com audio para memorizacao</td></tr>
<tr><td>Image Text On</td><td><code>[+IMAGE_TEXT_ON]...[-IMAGE_TEXT_ON]</code></td><td>Imagem com texto sobreposto e audio (versiculos musicais)</td></tr>
<tr><td>Fill In</td><td><code>[+FILL_IN]...[-FILL_IN]</code></td><td>Exercicio de completar lacunas (3-4 lacunas com _____)</td></tr>
<tr><td>Attachment</td><td><code>[+ATTACHMENT]...[-ATTACHMENT]</code></td><td>Placeholder para arquivo anexo (PDF de atividade)</td></tr>
<tr><td>Image Text Aside</td><td><code>[+IMAGE_TEXT_ASIDE]...[-IMAGE_TEXT_ASIDE]</code></td><td>Imagem com texto narrativo ao lado (secao Narrar)</td></tr>
<tr><td>List Numbered</td><td><code>[+LIST_NUMBERED]...[-LIST_NUMBERED]</code></td><td>Lista numerada de 3 perguntas</td></tr>
<tr><td>Tabs</td><td><code>[+TABS]...[-TABS]</code></td><td>Bloco com 2 abas nomeadas (Perceber de revisao)</td></tr>
</tbody>
</table>

<h4>Placeholders de Midia:</h4>
<table class="tutorial-table">
<thead><tr><th>Placeholder</th><th>Significado</th></tr></thead>
<tbody>
<tr><td><code>@link_png@</code></td><td>Imagem a ser inserida</td></tr>
<tr><td><code>@link_mp3@</code></td><td>Audio a ser inserido</td></tr>
<tr><td><code>@link_pdf@</code></td><td>PDF de atividade</td></tr>
</tbody>
</table>
</div>

<div class="tutorial-content-section">
<h3>Visao Geral do Fluxo Editorial (572 linhas)</h3>
<p>O documento <code>visao-geral-fluxo-editorial.md</code> e o <strong>documento mais importante</strong> do projeto. Contem:</p>
<ul>
<li>Arquitetura geral do ecossistema (5 camadas)</li>
<li>Detalhe completo do pipeline de 7 etapas</li>
<li>Estrutura semanal de producao (5 arquivos/semana)</li>
<li>Estrutura bimestral (ciclos de 10 semanas)</li>
<li>Catalogo completo de especialistas e skills</li>
<li>Mapa de dependencias entre skills</li>
<li>Base de conhecimento completa</li>
<li>Os 5 Habitos da Gramatica com estrutura detalhada de cada bloco</li>
<li>Regra de repeticao obrigatoria da definicao (6 locais)</li>
<li>Estrutura curricular e regras de sincronizacao</li>
<li>Regra de Ouro (Curriculo Macro como fonte da verdade)</li>
<li>Automacao: todos os scripts Python catalogados</li>
<li>Fluxos de execucao dos scripts</li>
<li>Alternancia de blocos permitidas</li>
<li>Gestao de repositorio (publish.md + DevOps)</li>
<li>Progressao curricular por ano</li>
<li>Mapa completo de conexoes</li>
<li>Tabela de roteamento</li>
</ul>

<div class="tutorial-info-card">
<strong>Dica:</strong> Se voce tiver tempo para ler apenas UM documento do projeto, leia o <code>visao-geral-fluxo-editorial.md</code>. Ele contem praticamente tudo que voce precisa saber para operar o Trivium Method.
</div>
</div>

<div class="tutorial-content-section">
<h3>Progressao Curricular por Ano</h3>
<table class="tutorial-table">
<thead><tr><th>Ano</th><th>Volume</th><th>Periodo Artistico</th><th>Semanas</th><th>Status</th></tr></thead>
<tbody>
<tr><td><strong>1o Ano</strong></td><td>—</td><td>Introducao a Linguagem Visual e Elementos da Arte</td><td>40</td><td>Nao iniciado</td></tr>
<tr><td><strong>2o Ano</strong></td><td>Vol. 1</td><td>Da Criacao ate a Arte Bizantina</td><td>38</td><td>Producao completa</td></tr>
<tr><td><strong>3o Ano</strong></td><td>Vol. 2</td><td>Arte Crista Oriental ate o Renascimento do Norte</td><td>38+</td><td>Producao completa (.4 e .5)</td></tr>
<tr><td><strong>4o Ano</strong></td><td>Vol. 3</td><td>Impressionismo ate a Arte Contemporanea</td><td>40</td><td>Producao completa (.4)</td></tr>
<tr><td><strong>5o Ano</strong></td><td>Vol. 4</td><td>Maneirismo ate o Realismo Americano</td><td>40</td><td>Parcialmente produzido</td></tr>
</tbody>
</table>
</div>
`},

// ============================================================================
// SECAO 10 — FLUXO DIARIO DE TRABALHO
// ============================================================================
{id:'workflow',number:10,title:'Fluxo Diario de Trabalho',icon:'<i class="ph ph-compass"></i>',color:'#14b8a6',content:`
<h2><i class="ph ph-compass" style="color:var(--accent-primary);margin-right:0.5rem;"></i> 10. Fluxo Diario de Trabalho</h2>

<div class="tutorial-content-section">
<h3>Rotina Diaria Completa</h3>
<p>Este e o fluxo passo-a-passo que um operador do Trivium Method deve seguir em um dia tipico de trabalho editorial.</p>

<h4>Manha — Diagnostico e Planejamento (15 min)</h4>
<div class="tutorial-code-block">PASSO 1: Abrir o Dashboard
URL: https://italogabriel-lab.github.io/Projeto-Editorial-Education/
Verificar: Metricas gerais, status dos cards, progresso

PASSO 2: Abrir o Agent Command Center
URL: .../agent-command-center.html
Verificar: Status de cada agente, gargalos, performance

PASSO 3: Abrir o Vision Board de Metas por Disciplina
URL: .../metas-disciplinas.html
Verificar: Year Health de cada disciplina/ano
Acao: Identificar anos criticos (🔴) que precisam de atencao

PASSO 4: Invocar o Orchestrator
Comando: @orchestrator "Status do [ano/disciplina]"
Output: Relatorio de progresso + proximas acoes priorizadas</div>
</div>

<div class="tutorial-content-section">
<h4>Durante o Dia — Execucao do Pipeline</h4>
<div class="tutorial-code-block">PASSO 5: Executar o Pipeline de Producao

Para cada aula nova:
  Comando: "Crie a aula X.Y, No ano"

  O fluxo automatico:
  1. Orchestrator diagnostica e delega
  2. Researcher pesquisa (Webster 1828, versiculos, arte, poemas)
  3. Writer redige (5 habitos, golden template, guia de estilo)
  4. Standardizer formata (Rise Blocks, capitalizacao)
  5. Reviewer revisa (13 categorias + 10 erros IA)
     → Se aprovado: continua
     → Se rejeitado: volta para etapa 2 ou 3
  6. Copywriter polimento final
  7. Publisher salva local + GitHub

Para revisoes semanais (X.4):
  Comando: "Crie a revisao da semana X"
  Agente: Review Builder

Para provas bimestrais:
  Comando: "Crie a prova do bimestre N"
  Agente: Bimester Exam Builder</div>
</div>

<div class="tutorial-content-section">
<h4>Final do Dia — Sincronizacao e Commit (10 min)</h4>
<div class="tutorial-code-block">PASSO 6: Sincronizar Titulos (se houve mudancas)
cd "Projeto Bibline Academy/editorial-squad/scripts"
python sync_titles.py
# Propaga titulos do Macro para todos os arquivos

PASSO 7: Verificar Sincronizacao
python check_matriz.py
# Compara Matriz vs Macro e reporta divergencias

PASSO 8: Commit e Push
cd /caminho/do/repo
git status
git add -A
git commit -m "content: aulas X.Y-X.Z do 3o ano"
git push origin main

PASSO 9: Confirmar Deploy
Verificar: GitHub Actions → Deploy to GitHub Pages
URL: https://italogabriel-lab.github.io/Projeto-Editorial-Education/</div>
</div>

<div class="tutorial-content-section">
<h3>Comandos Mais Usados — Referencia Rapida</h3>

<h4>Producao de Conteudo:</h4>
<table class="tutorial-table">
<thead><tr><th>Comando</th><th>Agente</th><th>Resultado</th></tr></thead>
<tbody>
<tr><td><code>@orchestrator "Status do 3o ano"</code></td><td>Orchestrator</td><td>Diagnostico completo</td></tr>
<tr><td><code>"Crie a aula 5.3, 3o ano"</code></td><td>Pipeline 7 etapas</td><td>Aula completa publicada</td></tr>
<tr><td><code>"Produza a semana 15, 3o ano"</code></td><td>Pipeline 7 etapas x5</td><td>Semana completa (3 aulas + review + quiz)</td></tr>
<tr><td><code>"Crie a revisao da semana 7"</code></td><td>Review Builder</td><td>Revisao semanal X.4</td></tr>
<tr><td><code>"Crie a prova do bimestre 2"</code></td><td>Bimester Exam Builder</td><td>Prova bimestral CANVAS_QUIZ</td></tr>
</tbody>
</table>

<h4>Correcao e Padronizacao:</h4>
<table class="tutorial-table">
<thead><tr><th>Comando</th><th>Agente</th><th>Resultado</th></tr></thead>
<tbody>
<tr><td><code>@standardizer "formate aula 5.3"</code></td><td>Standardizer</td><td>Rise Blocks aplicados</td></tr>
<tr><td><code>@capitalizer "corrija capitalizacao"</code></td><td>Capitalizer</td><td>Padrao europeu aplicado</td></tr>
<tr><td><code>@reviewer "revise aula 5.3"</code></td><td>Reviewer</td><td>Checklist 13 categorias</td></tr>
<tr><td><code>@copywriter "polir aula 5.3"</code></td><td>Copywriter</td><td>Otimizacao de titulos e fluidez</td></tr>
</tbody>
</table>

<h4>Analytics e Performance:</h4>
<table class="tutorial-table">
<thead><tr><th>Comando</th><th>Resultado</th></tr></thead>
<tbody>
<tr><td><code>/performance user Italo-bibline Belas Artes 2</code></td><td>Relatorio individual</td></tr>
<tr><td><code>/performance discipline Matematica 2</code></td><td>Relatorio por disciplina</td></tr>
<tr><td><code>/performance team</code></td><td>Relatorio da equipe</td></tr>
<tr><td><code>/performance velocity Italo-bibline 4</code></td><td>Velocidade nas ultimas 4 semanas</td></tr>
<tr><td><code>/bottleneck detect</code></td><td>Gargalos no pipeline</td></tr>
</tbody>
</table>

<h4>DevOps e Publicacao:</h4>
<table class="tutorial-table">
<thead><tr><th>Comando</th><th>Agente</th><th>Resultado</th></tr></thead>
<tbody>
<tr><td><code>@publisher "publicar aula 5.3"</code></td><td>Publisher</td><td>Salva local + GitHub commit</td></tr>
<tr><td><code>@devops "push"</code></td><td>DevOps</td><td>Versionamento Git</td></tr>
<tr><td><code>@devops "cleanup"</code></td><td>DevOps</td><td>Limpeza de repo</td></tr>
<tr><td><code>@devops "limpeza profissional"</code></td><td>DevOps</td><td>git rm --cached + add + commit</td></tr>
</tbody>
</table>

<h4>Scripts de Automacao:</h4>
<table class="tutorial-table">
<thead><tr><th>Comando</th><th>Resultado</th></tr></thead>
<tbody>
<tr><td><code>python sync_titles.py</code></td><td>Sincroniza titulos do Macro → todos os arquivos</td></tr>
<tr><td><code>python check_matriz.py</code></td><td>Audita Matriz vs Macro</td></tr>
<tr><td><code>python fix_lesson_h1.py</code></td><td>Corrige headers H1 das aulas</td></tr>
<tr><td><code>python fix_titles.py</code></td><td>Limpa sufixos cosmeticos</td></tr>
<tr><td><code>python generate_descriptions.py</code></td><td>Regenera arquivo de descricoes (DESTRUTIVO)</td></tr>
<tr><td><code>python align_titles.py</code></td><td>Alinha titulos em tickets</td></tr>
<tr><td><code>python align_review_titles.py</code></td><td>Alinha referencias de review</td></tr>
</tbody>
</table>
</div>

<div class="tutorial-content-section">
<h3>Resolucao de Problemas (Troubleshooting)</h3>

<h4>Problema: Reviewer rejeitou a aula</h4>
<div class="tutorial-code-block">Sintoma: [REJECTED — RETURN TO STEP X]
Causa: Erro em uma das 13 categorias ou 10 erros IA

Solucao:
1. Ler o log de rejeicao detalhado
2. Identificar se e erro de conteudo (volta etapa 2) ou formatacao (volta etapa 3)
3. Corrigir o problema especifico
4. Rode o pipeline novamente a partir da etapa correta</div>

<h4>Problema: Titulos desalinhados entre arquivos</h4>
<div class="tutorial-code-block">Sintoma: H1 da aula nao bate com Curriculo Macro
Causa: Titulo foi alterado no Macro mas nao propagado

Solucao:
1. Confirmar que o Macro tem o titulo correto
2. Executar: python sync_titles.py
3. Verificar: python check_matriz.py
4. Commitar as mudancas</div>

<h4>Problema: Push do Git falha com "Large files detected"</h4>
<div class="tutorial-code-block">Sintoma: Erro GH001 - Large files detected
Causa: Arquivos de midia (.mp4, .pdf, .png) foram adicionados ao repo

Solucao:
1. Verificar .gitignore inclui extensoes proibidas
2. Executar limpeza profissional:
   git rm -r --cached .
   git add .
   git commit -m "chore: Limpeza profissional"
   git push origin main --force
3. Para evitar: @devops antes de qualquer push com midia</div>

<h4>Problema: Definicoes inconsistentes entre secoes</h4>
<div class="tutorial-code-block">Sintoma: Definicao no Accordion != Recordar != Praticar
Causa: Writer ou Standardizer nao verificou consistencia

Solucao:
1. Identificar todas as ocorrencias da definicao
2. Corrigir para que sejam IDENTICAS em todos os 5+ locais
3. Re-executar pipeline a partir da Etapa 3
4. Revisar novamente</div>

<h4>Problema: Dashboard nao atualiza</h4>
<div class="tutorial-code-block">Sintoma: Dados no Vision Board estao desatualizados
Causa: Sync automatico pode ter falhado ou cache do navegador

Solucao:
1. Hard refresh: Ctrl+Shift+R
2. Verificar GitHub Actions → Vision Board Live Sync
3. Se necessario, disparar sync manual: Actions → Run workflow
4. Verificar se public/data.json foi atualizado</div>
</div>

<div class="tutorial-content-section">
<h3>Melhores Praticas</h3>
<ol>
<li><strong>Sempre comece pelo Orchestrator.</strong> Ele te diz exatamente o que fazer e em que ordem.</li>
<li><strong>Nunca pule etapas do pipeline.</strong> Cada etapa existe por uma razao. Pular = problemas na revisao.</li>
<li><strong>Consulte o Curriculo Macro ANTES de qualquer coisa.</strong> Ele e a fonte da verdade para titulos e termos.</li>
<li><strong>Execute sync_titles.py apos QUALQUER mudanca de titulo.</strong> Nao espere o problema se multiplicar.</li>
<li><strong>Verifique consistencia da definicao em todos os locais.</strong> O erro mais comum e definicao inconsistente.</li>
<li><strong>Use o Reviewer proativamente.</strong> Nao espere o Publisher descobrir erros. revise antes de publicar.</li>
<li><strong>Commite frequentemente.</strong> Commits pequenos sao mais faceis de reverter que commits gigantes.</li>
<li><strong>Mantenha o .gitignore atualizado.</strong> Midia pesada no Git = repo lento e instavel.</li>
<li><strong>Documente decisoes importantes.</strong> Se mudou uma regra, atualize o visao-geral-fluxo-editorial.md.</li>
<li><strong>Monitore o Year Health.</strong> Identifique anos criticos antes que virem emergencies.</li>
</ol>
</div>

<div class="tutorial-content-section">
<h3>Armadihas Comuns — O que NAO Fazer</h3>
<table class="tutorial-table">
<thead><tr><th>Nao Faca</th><th>Por Que</th><th>Faca Isso</th></tr></thead>
<tbody>
<tr><td>Criar titulo criativo diferente do Macro</td><td>Quebra sincronizacao curricular</td><td>Usar EXATAMENTE o titulo do Curriculo Macro</td></tr>
<tr><td>Pular a etapa de pesquisa</td><td>Conteudo sem base academica</td><td>Sempre usar Researcher antes do Writer</td></tr>
<tr><td>Ignorar o guia de estilo</td><td>Inconsistencia de tom e formatacao</td><td>Consultar guia-de-estilo.md antes de escrever</td></tr>
<tr><td>Colocar instrucao dentro do FILL_IN</td><td>Erro automatico na revisao</td><td>Instrucao em PARAGRAPH antes do bloco</td></tr>
<tr><td>Usar voz passiva</td><td>Violacao direta do guia de estilo</td><td>Sempre imperativo ativo: "Observe", "Complete"</td></tr>
<tr><td>Esquecer de sincronizar 5 arquivos</td><td>Curriculo desatualizado</td><td>Executar sync_titles.py apos mudancas</td></tr>
<tr><td>Commitar midia pesada no Git</td><td>Repo lento, push falha</td><td>Usar .gitignore, manter apenas texto</td></tr>
<tr><td>Definicao diferente no Accordion e Recordar</td><td>Rejeicao automatica do Reviewer</td><td>Verificar consistencia em todos os 5+ locais</td></tr>
<tr><td>Comeecar semana nova sem completar a anterior</td><td>Trabalho incompleto acumulado</td><td>Completar semanas parciais primeiro</td></tr>
<tr><td>Ignorar o Year Health</td><td>Meta perdida sem aviso</td><td>Monitorar metas-disciplinas.html semanalmente</td></tr>
</tbody>
</table>
</div>

<div class="tutorial-content-section">
<h3>Checklist Diario do Operador</h3>
<div class="tutorial-code-block">MANHA:
[ ] Abrir Dashboard e verificar metricas gerais
[ ] Abrir Agent Command Center e verificar agentes
[ ] Verificar Year Health de todas as disciplinas
[ ] Invocar Orchestrator para diagnostico e priorizacao

DURANTE O DIA:
[ ] Executar pipelines de producao conforme prioridade
[ ] Revisar aulas aprovadas antes de publicar
[ ] Sincronizar titulos se houve mudancas
[ ] Resolver rejeicoes do Reviewer

FINAL DO DIA:
[ ] Verificar consistencia de definicoes
[ ] Executar sync_titles.py (se necessario)
[ ] Commitar todas as mudancas
[ ] Push para main
[ ] Confirmar deploy no GitHub Pages
[ ] Registrar progresso (check no Curriculo Macro)</div>
</div>

<div class="tutorial-content-section">
<h3>Links Essenciais para Bookmark</h3>
<table class="tutorial-table">
<thead><tr><th>Recurso</th><th>URL</th></tr></thead>
<tbody>
<tr><td><strong>Vision Board (Dashboard)</strong></td><td><code>https://italogabriel-lab.github.io/Projeto-Editorial-Education/</code></td></tr>
<tr><td><strong>Agent Command Center</strong></td><td><code>https://.../agent-command-center.html</code></td></tr>
<tr><td><strong>Metas por Disciplina + Year Health</strong></td><td><code>https://.../metas-disciplinas.html</code></td></tr>
<tr><td><strong>Videos Pipeline</strong></td><td><code>https://.../videos.html</code></td></tr>
<tr><td><strong>GitHub Repository</strong></td><td><code>https://github.com/italogabriel-lab/Projeto-Editorial-Education</code></td></tr>
<tr><td><strong>GitHub Actions</strong></td><td><code>https://github.com/italogabriel-lab/.../actions</code></td></tr>
<tr><td><strong>Kanban Project</strong></td><td><code>https://github.com/orgs/bibline/projects/2/views/1</code></td></tr>
</tbody>
</table>
</div>

<div class="tutorial-content-section">
<h3>Conclusao</h3>
<p>O Trivium Method e um sistema completo e sofisticado, mas que se torna simples quando voce entende seus padroes:</p>
<ul>
<li><strong>7 etapas</strong> que sempre seguem a mesma sequencia</li>
<li><strong>5 habitos</strong> que sempre seguem a mesma estrutura</li>
<li><strong>1 fonte da verdade</strong> (Curriculo Macro) que governa todos os titulos</li>
<li><strong>22 agentes</strong> cada com uma responsabilidade clara</li>
<li><strong>4 processos de sync</strong> que mantem tudo consistente</li>
<li><strong>1 dashboard</strong> que mostra tudo em tempo real</li>
</ul>
<p>Domine estes padroes e voce dominara o framework. Consulte esta documentacao sempre que precisar de referencia. Ela foi projetada para ser sua fonte unica de verdade operacional.</p>

<div class="tutorial-info-card" style="text-align: center; margin-top: 2rem;">
<p style="font-size: 1.1rem; margin-bottom: 0.5rem;"><em>"Portanto, meus amados irmaos, sede firmes, inabalaveis e sempre abundantes na obra do Senhor, sabendo que o vosso trabalho nao e vao no Senhor."</em></p>
<p style="color: var(--text-muted);">— 1 Corintios 15:58</p>
</div>
</div>
`}

]; // fim do array tutorialSections
