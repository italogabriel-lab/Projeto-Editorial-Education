Agora preciso que você faça a criação de tickets dentro de um quadro Kanban no GitHub.

🔹 Projeto Kanban:
[COLE A URL DO PROJETO AQUI]

🔹 Autenticação:
Utilize a chave de acesso armazenada no arquivo `.env` do usuário:
- USER: [NOME DO USUÁRIO]
- TOKEN: [NOME DA VARIÁVEL DO TOKEN]

Passos:
1. Identifique corretamente a chave no `.env`
2. Verifique se o token possui permissões necessárias (projects, issues, repo)
3. Prepare a execução para criação dos tickets

🔹 Configuração dos Tickets:
- Disciplina: [NOME DA DISCIPLINA]
- Série/Ano: [ANO/SÉRIE]
- Assignee: @[USUÁRIO RESPONSÁVEL]
- Status inicial: [STATUS - ex: Backlog]
- Total de tickets a serem criados: [QUANTIDADE]

🔹 Fonte de Dados:
Utilize como base o seguinte arquivo para extrair as informações dos tickets:
- Arquivo: [NOME DO ARQUIVO]

🔹 Objetivo:
Criar todos os tickets no projeto Kanban com base nas informações do arquivo, garantindo:
- Títulos organizados e padronizados
- Descrições claras (quando aplicável)
- Associação correta ao responsável
- Status inicial definido corretamente

🔹 Observações:
- Validar duplicações antes de criar novos tickets
- Garantir consistência nos nomes dos tickets
- Seguir um padrão claro de nomenclatura (ex: Disciplina - Ano - Tema)

Execute o processo de forma estruturada e segura.


### Exemplo de uso 

Projeto: https://github.com/orgs/bibline/projects/2/views/1
USER: Italo-bibline
TOKEN: GITHUB_TOKEN_CLASSIC 
Disciplina: Matemática
Ano: 5º ano
Assignee: @walmirfeijo
Status: Backlog
Total: 128
Arquivo: matemática 5 ano

