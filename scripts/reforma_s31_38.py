import os, re

BASE = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto - Bibline Academy ( Produção de Aulas)/Belas Artes - Fase da Gramática/1 Fase - Gramática/1º Ano - Introdução à Linguagem Visual e aos Elementos da Arte"

AULAS = [
# Semana 31
(31,1,"Esperança olha para a beleza prometida por Deus com alegria.","Esperança é a certeza da beleza prometida por Deus que inspira a arte.",
 "A esperança olha para a beleza prometida por Deus e inspira a arte com alegria e reverência.",
 "A esperança é a certeza da beleza prometida por Deus que inspira a arte com alegria e reverência.",
 "A **esperança** é a certeza da beleza prometida por Deus que inspira a arte com alegria e reverência.",
 "_____ é a certeza da beleza prometida por Deus que inspira a arte.","Esperança"),
(31,2,"Esperança olha para a beleza prometida por Deus com alegria.","Esperança é a certeza da beleza prometida por Deus que inspira a arte.",
 "A esperança olha para a beleza dos anjos e do céu e a transforma em imagem com tinta e papel.",
 "A esperança é a certeza da beleza dos anjos e do céu que o artista transforma em imagem.",
 "A **esperança** é a certeza da **beleza** dos anjos e do céu que o artista transforma em imagem.",
 "Esperança é a certeza da _____ prometida por Deus que inspira a arte.","beleza"),
(31,3,"Esperança olha para a beleza prometida por Deus com alegria.","Esperança é a certeza da beleza prometida por Deus que inspira a arte.",
 "A esperança contempla a promessa de Deus com alegria ao desenhar a visão do céu.",
 "A esperança é a certeza da promessa de Deus que inspira a visão do céu com alegria.",
 "A **esperança** é a certeza da promessa de Deus que inspira a visão do céu com **alegria**.",
 "Esperança é a certeza da beleza prometida por Deus que inspira a arte com _____.","alegria"),
# Semana 32
(32,1,"Criação mostra Deus formando luz, céus e águas com poder.","Criação é a obra de Deus que formou luz, céus e águas do nada.",
 "A criação mostra Deus formando luz, céus e águas com poder e ordem.",
 "A criação é a obra de Deus que formou luz, céus e águas do nada com poder e ordem.",
 "A **criação** é a obra de Deus que formou luz, céus e águas do nada com poder e ordem.",
 "_____ é a obra de Deus que formou luz, céus e águas do nada.","Criação"),
(32,2,"Criação mostra Deus formando luz, céus e águas com poder.","Criação é a obra de Deus que formou luz, céus e águas do nada.",
 "A criação começa com a luz que Deus separou das trevas no primeiro dia.",
 "A criação é a obra que começa com a luz que Deus separou das trevas no primeiro dia.",
 "A **criação** é a obra que começa com a **luz** que Deus separou das trevas no primeiro dia.",
 "Criação é a obra de Deus que formou _____, céus e águas do nada.","luz"),
(32,3,"Criação mostra Deus formando luz, céus e águas com poder.","Criação é a obra de Deus que formou luz, céus e águas do nada.",
 "A criação mostra as águas que Deus reuniu em mares e rios com poder e ordem.",
 "A criação é a obra que reuniu as águas em mares e rios com poder e ordem de Deus.",
 "A **criação** é a obra que reuniu as **águas** em mares e rios com poder e ordem de Deus.",
 "Criação é a obra de Deus que formou luz, céus e _____ do nada.","águas"),
# Semana 33
(33,1,"Vida criada mostra terra, luminares e seres vivos em ordem.","Vida criada é o conjunto de seres que Deus chamou à existência com ordem.",
 "A vida criada mostra terra, luminares e seres vivos em harmonia na criação de Deus.",
 "A vida criada é o conjunto de terra, luminares e seres vivos que Deus chamou à existência.",
 "A **vida criada** é o conjunto de terra, luminares e seres vivos que Deus chamou à existência.",
 "_____ é o conjunto de seres que Deus chamou à existência com ordem.","Vida criada"),
(33,2,"Vida criada mostra terra, luminares e seres vivos em ordem.","Vida criada é o conjunto de seres que Deus chamou à existência com ordem.",
 "A vida criada inclui a terra que Deus formou junto com o sol, a lua e as estrelas.",
 "A vida criada é o conjunto que inclui a terra formada por Deus com o sol, a lua e as estrelas.",
 "A **vida criada** é o conjunto que inclui a **terra** formada por Deus com o sol, a lua e as estrelas.",
 "Vida criada é o conjunto de _____ que Deus chamou à existência com ordem.","seres"),
(33,3,"Vida criada mostra terra, luminares e seres vivos em ordem.","Vida criada é o conjunto de seres que Deus chamou à existência com ordem.",
 "A vida criada revela os seres vivos como peixes e aves que Deus chamou à existência.",
 "A vida criada é o conjunto dos seres vivos como peixes e aves que Deus chamou à existência.",
 "A **vida criada** é o conjunto dos **seres** vivos como peixes e aves que Deus chamou à existência.",
 "Vida criada é o conjunto de seres que Deus chamou à existência com _____.","ordem"),
# Semana 34
(34,1,"Descanso lembra que Deus completou sua obra com perfeição.","Descanso é o sinal de que Deus completou sua obra com perfeição.",
 "O descanso lembra que Deus completou sua obra com perfeição e alegria.",
 "O descanso é o sinal de que Deus completou sua obra com perfeição e alegria no sétimo dia.",
 "O **descanso** é o sinal de que Deus completou sua obra com perfeição e alegria no sétimo dia.",
 "_____ é o sinal de que Deus completou sua obra com perfeição.","Descanso"),
(34,2,"Descanso lembra que Deus completou sua obra com perfeição.","Descanso é o sinal de que Deus completou sua obra com perfeição.",
 "O descanso lembra que Deus completou a criação dos animais e do ser humano com perfeição.",
 "O descanso é o sinal de que Deus completou a criação dos animais e do ser humano com perfeição.",
 "O **descanso** é o sinal de que **Deus** completou a criação dos animais e do ser humano com perfeição.",
 "Descanso é o sinal de que _____ completou sua obra com perfeição.","Deus"),
(34,3,"Descanso lembra que Deus completou sua obra com perfeição.","Descanso é o sinal de que Deus completou sua obra com perfeição.",
 "O descanso lembra que Deus completou sua obra com perfeição ao criar um painel completo da criação.",
 "O descanso é o sinal de que Deus completou sua obra com perfeição ao criar o painel completo.",
 "O **descanso** é o sinal de que Deus completou sua obra com **perfeição** ao criar o painel completo.",
 "Descanso é o sinal de que Deus completou sua obra com _____.","perfeição"),
# Semana 35
(35,1,"Arte e música expressam beleza com som, cor e movimento.","Arte e música são expressões da beleza que Deus deu ao ser humano.",
 "A arte e música expressam beleza com som, cor e movimento de forma integrada.",
 "A arte e música são expressões da beleza que Deus deu com som, cor e movimento integrados.",
 "A **arte e música** são expressões da beleza que Deus deu com som, cor e movimento integrados.",
 "_____ são expressões da beleza que Deus deu ao ser humano.","Arte e música"),
(35,2,"Arte e música expressam beleza com som, cor e movimento.","Arte e música são expressões da beleza que Deus deu ao ser humano.",
 "A arte e música expressam beleza ao usar a cor para retratar o que a música provoca no ouvinte.",
 "A arte e música são expressões da beleza que usam a cor para retratar o que a música provoca.",
 "A **arte e música** são expressões da beleza que usam a **cor** para retratar o que a música provoca.",
 "Arte e música são expressões da beleza que Deus deu com som, _____ e movimento.","cor"),
(35,3,"Arte e música expressam beleza com som, cor e movimento.","Arte e música são expressões da beleza que Deus deu ao ser humano.",
 "A arte e música expressam beleza com movimento quando o pincel dança ao ritmo do som.",
 "A arte e música são expressões da beleza com movimento quando o pincel dança ao ritmo do som.",
 "A **arte e música** são expressões da beleza com **movimento** quando o pincel dança ao ritmo do som.",
 "Arte e música são expressões da beleza que Deus deu com som, cor e _____.","movimento"),
# Semana 36
(36,1,"Imagem musical mostra o que o som faz nascer na imaginação.","Imagem musical é a imagem que nasce do que o som provoca na imaginação.",
 "A imagem musical mostra o que o som faz nascer na imaginação de quem ouve.",
 "A imagem musical é a imagem que nasce do que o som provoca na imaginação de quem ouve.",
 "A **imagem musical** é a imagem que nasce do que o som provoca na imaginação de quem ouve.",
 "_____ é a imagem que nasce do que o som provoca na imaginação.","Imagem musical"),
(36,2,"Imagem musical mostra o que o som faz nascer na imaginação.","Imagem musical é a imagem que nasce do que o som provoca na imaginação.",
 "A imagem musical nasce do som quando os olhos escutam e transformam a melodia em forma e cor.",
 "A imagem musical é a imagem que nasce do som quando os olhos transformam a melodia em forma e cor.",
 "A **imagem musical** é a imagem que nasce do **som** quando os olhos transformam a melodia em forma e cor.",
 "Imagem musical é a imagem que nasce do que o _____ provoca na imaginação.","som"),
(36,3,"Imagem musical mostra o que o som faz nascer na imaginação.","Imagem musical é a imagem que nasce do que o som provoca na imaginação.",
 "A imagem musical revela o que o som faz nascer na imaginação ao transformar uma música favorita em obra visual.",
 "A imagem musical é a imagem que o som faz nascer na imaginação ao transformar música em obra visual.",
 "A **imagem musical** é a imagem que o som faz nascer na **imaginação** ao transformar música em obra visual.",
 "Imagem musical é a imagem que nasce do que o som provoca na _____.","imaginação"),
# Semana 37
(37,1,"Encanto ajuda o olhar a perceber beleza nas obras de arte.","Encanto é o estado do olhar que percebe beleza nas obras de arte.",
 "O encanto ajuda o olhar a perceber beleza nas obras de arte com atenção e cuidado.",
 "O encanto é o estado do olhar que percebe beleza nas obras de arte com atenção e cuidado.",
 "O **encanto** é o estado do olhar que percebe beleza nas obras de arte com atenção e cuidado.",
 "_____ é o estado do olhar que percebe beleza nas obras de arte.","Encanto"),
(37,2,"Encanto ajuda o olhar a perceber beleza nas obras de arte.","Encanto é o estado do olhar que percebe beleza nas obras de arte.",
 "O encanto ajuda o olhar a perceber a beleza dos girassóis de Van Gogh com cores vivas e movimento.",
 "O encanto é o estado do olhar que percebe a beleza dos girassóis de Van Gogh com cores vivas.",
 "O **encanto** é o estado do olhar que percebe a **beleza** dos girassóis de Van Gogh com cores vivas.",
 "Encanto é o estado do olhar que percebe _____ nas obras de arte.","beleza"),
(37,3,"Encanto ajuda o olhar a perceber beleza nas obras de arte.","Encanto é o estado do olhar que percebe beleza nas obras de arte.",
 "O encanto ajuda o olhar a perceber beleza nas obras de Paul Klee com formas e cores alegres.",
 "O encanto é o estado do olhar que percebe beleza nas obras de Paul Klee com formas e cores alegres.",
 "O **encanto** é o estado do olhar que percebe beleza nas **obras** de Paul Klee com formas e cores alegres.",
 "Encanto é o estado do olhar que percebe beleza nas _____ de arte.","obras"),
# Semana 38
(38,1,"Observação atenta vê detalhes e responde com gratidão.","Observação é o olhar atento que descobre detalhes na obra de arte.",
 "A observação atenta vê detalhes que passariam despercebidos e responde com gratidão.",
 "A observação é o olhar atento que descobre detalhes que passariam despercebidos na obra.",
 "A **observação** é o olhar atento que descobre detalhes que passariam despercebidos na obra.",
 "_____ é o olhar atento que descobre detalhes na obra de arte.","Observação"),
(38,2,"Observação atenta vê detalhes e responde com gratidão.","Observação é o olhar atento que descobre detalhes na obra de arte.",
 "A observação atenta percebe detalhes como cores, texturas e formas escondidas no quadro.",
 "A observação é o olhar que percebe detalhes como cores, texturas e formas no quadro.",
 "A **observação** é o olhar que percebe **detalhes** como cores, texturas e formas no quadro.",
 "Observação é o olhar atento que descobre _____ na obra de arte.","detalhes"),
(38,3,"Observação atenta vê detalhes e responde com gratidão.","Observação é o olhar atento que descobre detalhes na obra de arte.",
 "A observação atenta responde com gratidão ao perceber a beleza na obra que tocou o coração.",
 "A observação é o olhar que responde com gratidão ao perceber a beleza na obra que tocou o coração.",
 "A **observação** é o olhar que responde com **gratidão** ao perceber a beleza na obra que tocou o coração.",
 "Observação é o olhar atento que descobre detalhes na obra com _____.","gratidão"),
]

def patch_file(path, old_def, new_def, old_para_plain, new_para_plain, new_para_bold, fill_in, fill_answer):
    with open(path, encoding="utf-8") as f:
        txt = f.read()
    txt = txt.replace(f"**{old_def}**", f"**{new_def}**")
    txt = txt.replace(old_def, new_def)
    txt = txt.replace(old_para_plain, new_para_plain)
    for line in txt.split("\n"):
        stripped = re.sub(r'\*\*(.+?)\*\*', r'\1', line)
        if stripped.strip() == old_para_plain.strip() and "**" in line:
            txt = txt.replace(line, new_para_bold); break
    lines = txt.split("\n")
    in_fill, rf, ra = False, False, False
    new_lines = []
    for line in lines:
        if "[+FILL_IN]" in line:
            in_fill=True; rf=False; ra=False; new_lines.append(line); continue
        if "[-FILL_IN]" in line: in_fill=False
        if in_fill and "_____" in line and not rf:
            new_lines.append(fill_in); rf=True; continue
        if in_fill and rf and not ra and line.strip() and "[" not in line:
            new_lines.append(fill_answer); ra=True; continue
        new_lines.append(line)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))

for row in AULAS:
    sem, aula, old_def, new_def, old_para, new_para_plain, new_para_bold, fill_in, fill_answer = row
    fpath = os.path.join(BASE, f"{sem}.{aula}.md")
    try:
        patch_file(fpath, old_def, new_def, old_para, new_para_plain, new_para_bold, fill_in, fill_answer)
        print(f"✔ {sem}.{aula}.md")
    except Exception as e:
        print(f"✗ {sem}.{aula}.md: {e}")
