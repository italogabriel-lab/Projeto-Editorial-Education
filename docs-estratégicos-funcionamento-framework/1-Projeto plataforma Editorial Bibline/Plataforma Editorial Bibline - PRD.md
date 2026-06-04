# PRD — Plataforma Editorial Bibline

**Versão:** 1.0
**Data:** 2026-06-04
**Status:** Em definição

---

## 1. Visão geral

A Plataforma Editorial Bibline é uma ferramenta web interna para a equipe de produção de conteúdo didático da Bibline. Ela centraliza as regras editoriais, os templates pedagógicos e o pipeline de criação de aulas, eliminando a dependência de código bruto e de prompts manuais para cada membro da equipe.

O objetivo é que professores e editores consigam gerar o esqueleto completo de uma aula, em formato markdown padronizado, apenas preenchendo os campos de alto nível, como disciplina, ano escolar e tema. Todo o restante, estrutura de blocos Rise, definições por fase do Trivium, progressão pedagógica e formatação, é tratado pela plataforma.

---

## 2. Problema

Hoje a produção de aulas depende de:

- Conhecimento profundo dos templates markdown e da sintaxe Rise Blocks.
- Memorização das regras editoriais e das abordagens pedagógicas por fase.
- Uso direto de agentes de IA sem proteção contra alucinações ou desvios de padrão.
- Revisões manuais frequentes para garantir conformidade com o método Trivium.

Isso gera retrabalho, inconsistências entre aulas e dependência de poucos membros com domínio técnico do framework.

---

## 3. Público-alvo

| Perfil | Necessidade principal |
|---|---|
| Professor conteudista | Inserir o tema e receber a estrutura da aula pronta |
| Editor pedagógico | Validar conformidade com o método e ajustar blocos |
| Coordenador de currículo | Monitorar progresso semanal e bimestral |

---

## 4. Proposta de valor

> A Bibline Editorial Platform é o Canva da produção de aulas clássicas cristãs reformadas. A equipe insere o tema, a plataforma entrega o esqueleto da aula em markdown, pronto para aplicar no GitHub.

---

## 5. Funcionalidades principais

### 5.1 Gerador de aulas

- Seleção de disciplina, ano escolar, semana e número da aula (x.1, x.2, x.3).
- Campo para o tema central da aula.
- Campo para importação do currículo macro da semana.
- Geração automática de todos os blocos da aula no template Rise Blocks padrão.
- Exportação do arquivo `.md` final pronto para publicação.

### 5.2 Base de conhecimento editorial

- Regras editoriais por fase do Trivium (Gramática, Dialética, Retórica).
- Definições padrão de cada disciplina por ano escolar.
- Glossário de termos pedagógicos e seus usos corretos.
- Templates de aulas, revisões semanais e provas.

### 5.3 Validador de conformidade

- Verificação automática de estrutura do arquivo gerado.
- Alertas para desvios de padrão, como definição curta ausente, fill-in incorreto ou pergunta do Narrar fora do formato válido.
- Score de conformidade com o template padrão.

### 5.4 Painel de progresso curricular

- Visualização do currículo macro por ano e bimestre.
- Status de produção por aula: rascunho, revisão, publicado.
- Indicadores de consistência semanal entre x.1, x.2, x.3 e x.4.

### 5.5 Exportação e publicação

- Download do arquivo markdown individual.
- Integração com GitHub para publicação direta no repositório do projeto.
- Log de versões por aula.

---

## 6. Fluxo de criação de uma aula

```
1. Membro da equipe acessa a plataforma.
2. Seleciona: disciplina > ano escolar > semana > aula (x.1, x.2 ou x.3).
3. Insere o tema central e, se disponível, cola o currículo macro da semana.
4. A plataforma preenche automaticamente:
   - Definição curta padronizada para a semana.
   - Progressão de palavras-chave entre x.1, x.2 e x.3.
   - Blocos Rise: Definir, Perceber, Recordar, Praticar, Narrar.
   - Fill-In progressivo com lacuna correta para a aula.
   - Pergunta do Narrar no formato válido.
   - Pergunta do Multiple com distrator temático.
5. Editor revisa os campos gerados e ajusta o parágrafo livre.
6. Plataforma valida conformidade com o template.
7. Exportação do arquivo .md final.
```

---

## 7. Regras editoriais integradas à plataforma

A plataforma deve ter as seguintes regras gravadas como lógica interna, não como instruções de prompt:

- Definição curta: 8 a 12 palavras, verbo ser no presente, foco ontológico (o que é, não o que faz).
- Definição idêntica nas três aulas da semana e em todos os blocos da mesma aula.
- Parágrafo livre: uma única frase direta, sem segunda frase genérica.
- Fill-In progressivo: mesma frase-base da definição curta nas três aulas, com lacuna na palavra-chave específica de cada aula.
- Pergunta do Narrar: derivada do parágrafo livre, no formato "O que X faz?", "Como X aparece?", "Onde X está?", ou "Para que X serve?".
- Pergunta do Multiple: específica por aula, nunca genérica como "O que estudamos?".
- Narrar espelha literalmente o Definir, sem frases adicionais.
- Revisão x.4: uma definição curta da semana, três Multiples derivadas das aulas x.1, x.2 e x.3.

---

## 8. Abordagem pedagógica por fase do Trivium

A plataforma adapta a linguagem, os exemplos e a profundidade dos blocos de acordo com a fase do Trivium de cada ano escolar.

### Fase da Gramática (anos 1 a 4)

Foco: nomear, observar e memorizar o que as coisas são.

- Definições ontológicas simples: "X é Y."
- Exemplos concretos e visuais.
- Atividades de repetição e memorização.
- Perguntas diretas com resposta explícita no texto.
- Sem inferências, abstrações ou comparações complexas.

### Fase da Dialética (anos 5 a 8)

Foco: comparar, diferenciar e relacionar conceitos.

- Definições que estabelecem gênero e diferença específica.
- Perguntas que exigem relação entre conceitos.
- Atividades de análise e argumentação simples.
- Uso de exemplos que contrastam casos semelhantes.

### Fase da Retórica (anos 9 a 12)

Foco: expressar, defender e aplicar o conhecimento com clareza e elegância.

- Definições precisas com fundamentação histórica e teológica.
- Produção textual argumentativa.
- Aplicação dos conceitos em contextos reais e culturais.
- Pesquisa em fontes primárias (Ad Fontes).

---

## 9. Restrições e requisitos não funcionais

- A plataforma não substitui a revisão humana do editor pedagógico.
- Nenhuma aula pode ser publicada sem validação de conformidade aprovada.
- O arquivo markdown gerado deve ser idêntico ao produzido manualmente pelo template padrão.
- A plataforma deve operar offline para edição e apenas requerer conexão para publicação no GitHub.
- Interface em português, sem jargão técnico desnecessário.

---

## 10. Integrações

| Sistema | Finalidade |
|---|---|
| GitHub | Publicação e versionamento das aulas |
| Trivium Method Editorial framework | Fonte de verdade de templates e regras |
| Currículo Macro (arquivos .md do repositório) | Importação automática de temas e termos por semana |

---

## 11. Critérios de sucesso

- Um professor sem conhecimento de markdown consegue gerar uma aula conforme em menos de 20 minutos.
- 95% das aulas geradas passam na validação de conformidade sem edição estrutural.
- Tempo de revisão editorial por aula cai de 60 minutos para menos de 15 minutos.
- Zero alucinações de estrutura, ou seja, todos os blocos obrigatórios sempre presentes no arquivo gerado.

---

## 12. Fora do escopo (v1)

- Geração de imagens ou áudios.
- Aplicativo mobile.
- Portal para alunos ou pais.
- Integração com plataformas de LMS externas.
- Edição colaborativa em tempo real.

---

## 13. Referências

- `AGENTS.md` — regras editoriais e pipeline de produção.
- `trivium-method-editorial/templates/padrao_final_aula.md` — template golden.
- `trivium-method-editorial/knowledge-base/` — base de conhecimento pedagógico.
- `docs-estratégicos-funcionamento-framework/1-Projeto plataforma Editorial Bibline/Contexto sobre a abordagem pedagogica em cada fase e como conceituar.md` — fundamentos do Trivium para conceituação.
