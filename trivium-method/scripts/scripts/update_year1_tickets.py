import re

tickets_file = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto Bibline Academy/Belas Artes - Fase da Gramática/1 Fase - Gramática/1º Ano/Estrutura Curricular - 1º ANO/6 - Descrições para tickets - 1º ANO.md"

with open(tickets_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all occurrences of:
# [Belas artes] - Ano 1 - X.Y Título
# with
# [Belas artes] - Ano 1 - X.Y Título
# Wait, the prompt says the current format is:
# [Belas artes] - Ano 1 - 1.1 A essência da arte
# Oh, the user says:
# "esses 3 tickets ficam no llugar dos tickets
# [Belas artes] - Ano 3 - 11.1 Arte Islâmica e as formas de arte
# [Belas artes] - Ano 1 - 1.1 A essência da arte
# faça esse teste e entenda o fluxo que eu pretendo fazer com todos os tickets que estão sem descrição do 3 ano , e depois eu vou fazer essa mudança em todos os tickets para ter os tickets atualizados para o 1 ano"
