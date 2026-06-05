import os, re

BASE = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto - Bibline Academy ( Produção de Aulas)/Belas Artes - Fase da Gramática/1 Fase - Gramática/1º Ano - Introdução à Linguagem Visual e aos Elementos da Arte"

AULAS = [
# Semana 21
(21,1,"Direção guia o olhar e conduz a história na imagem.","Direção é o caminho que o olhar segue dentro da imagem.",
 "A direção guia o olhar e mostra para onde a história da imagem se move.",
 "A direção é o caminho que o olhar segue dentro da imagem ao percorrer linhas, formas e figuras.",
 "A **direção** é o caminho que o olhar segue dentro da imagem ao percorrer linhas, formas e figuras.",
 "_____ é o caminho que o olhar segue dentro da imagem.","Direção"),
(21,2,"Direção guia o olhar e conduz a história na imagem.","Direção é o caminho que o olhar segue dentro da imagem.",
 "A direção guia o olhar ao usar setas e linhas que mostram para onde olhar primeiro.",
 "A direção é o caminho que setas e linhas mostram para o olhar seguir na imagem.",
 "A **direção** é o caminho que setas e linhas mostram para o **olhar** seguir na imagem.",
 "Direção é o caminho que o _____ segue dentro da imagem.","olhar"),
(21,3,"Direção guia o olhar e conduz a história na imagem.","Direção é o caminho que o olhar segue dentro da imagem.",
 "A direção conduz a história ao criar caminhos com o pincel que orientam os olhos.",
 "A direção é o caminho que o pincel cria para conduzir a história pelos olhos do observador.",
 "A **direção** é o caminho que o pincel cria para conduzir a **história** pelos olhos do observador.",
 "Direção é o caminho que o olhar segue dentro da _____.","imagem"),
# Semana 22
(22,1,"Equilíbrio organiza partes diferentes para a obra ficar firme e bela.","Equilíbrio é a ordem entre as partes da obra que a deixa firme e bela.",
 "O equilíbrio organiza partes diferentes para que a obra fique firme e bela.",
 "O equilíbrio é a ordem entre as partes da obra que a deixa firme e bela aos olhos.",
 "O **equilíbrio** é a ordem entre as partes da obra que a deixa firme e bela aos olhos.",
 "_____ é a ordem entre as partes da obra que a deixa firme e bela.","Equilíbrio"),
(22,2,"Equilíbrio organiza partes diferentes para a obra ficar firme e bela.","Equilíbrio é a ordem entre as partes da obra que a deixa firme e bela.",
 "O equilíbrio organiza partes simétricas ao dobrar o papel e repetir as formas.",
 "O equilíbrio é a ordem entre as partes simétricas ao dobrar o papel e repetir as formas.",
 "O **equilíbrio** é a ordem entre as **partes** simétricas ao dobrar o papel e repetir as formas.",
 "Equilíbrio é a ordem entre as _____ da obra que a deixa firme e bela.","partes"),
(22,3,"Equilíbrio organiza partes diferentes para a obra ficar firme e bela.","Equilíbrio é a ordem entre as partes da obra que a deixa firme e bela.",
 "O equilíbrio da simetria deixa a obra firme ao espelhar formas de um lado para o outro.",
 "O equilíbrio da simetria é a ordem que deixa a obra firme ao espelhar formas de um lado ao outro.",
 "O **equilíbrio** da simetria é a ordem que deixa a obra **firme** ao espelhar formas de um lado ao outro.",
 "Equilíbrio é a ordem entre as partes da obra que a deixa _____ e bela.","firme"),
# Semana 23
(23,1,"Composição une ponto, linha, forma, cor e espaço com ordem.","Composição é o arranjo de ponto, linha, forma, cor e espaço em uma obra de arte.",
 "A composição une todos os elementos visuais em uma obra com ordem e beleza.",
 "A composição é o arranjo de ponto, linha, forma, cor e espaço que forma uma obra com ordem e beleza.",
 "A **composição** é o arranjo de ponto, linha, forma, cor e espaço que forma uma obra com ordem e beleza.",
 "_____ é o arranjo de ponto, linha, forma, cor e espaço em uma obra de arte.","Composição"),
(23,2,"Composição une ponto, linha, forma, cor e espaço com ordem.","Composição é o arranjo de ponto, linha, forma, cor e espaço em uma obra de arte.",
 "A composição une forma e cor para criar um quadro com equilíbrio e harmonia.",
 "A composição é o arranjo de forma e cor que cria um quadro com equilíbrio e harmonia.",
 "A **composição** é o arranjo de **forma** e cor que cria um quadro com equilíbrio e harmonia.",
 "Composição é o arranjo de ponto, linha, _____, cor e espaço em uma obra de arte.","forma"),
(23,3,"Composição une ponto, linha, forma, cor e espaço com ordem.","Composição é o arranjo de ponto, linha, forma, cor e espaço em uma obra de arte.",
 "A composição usa ponto, linha e espaço para criar obras com ordem e sentido.",
 "A composição é o arranjo de ponto, linha e espaço que dá ordem e sentido à obra.",
 "A **composição** é o arranjo de ponto, linha e **espaço** que dá ordem e sentido à obra.",
 "Composição é o arranjo de ponto, linha, forma, cor e _____ em uma obra de arte.","espaço"),
# Semana 24
(24,1,"Forma simples ajuda o desenho a nascer com clareza e ordem.","Forma simples é a figura de círculo, quadrado ou triângulo que está na origem do desenho.",
 "A forma simples ajuda o desenho a nascer com clareza ao usar círculos, quadrados e triângulos.",
 "A forma simples é a figura de círculo, quadrado ou triângulo que está na origem de todo desenho.",
 "A **forma simples** é a figura de círculo, quadrado ou triângulo que está na origem de todo desenho.",
 "_____ é a figura de círculo, quadrado ou triângulo que está na origem do desenho.","Forma simples"),
(24,2,"Forma simples ajuda o desenho a nascer com clareza e ordem.","Forma simples é a figura de círculo, quadrado ou triângulo que está na origem do desenho.",
 "A forma simples ajuda o desenho a nascer quando o círculo vira cabeça, olho ou corpo.",
 "A forma simples é a origem do desenho quando o círculo vira cabeça, olho ou corpo.",
 "A **forma simples** é a origem do **desenho** quando o círculo vira cabeça, olho ou corpo.",
 "Forma simples é a figura de círculo, quadrado ou triângulo que está na origem do _____.","desenho"),
(24,3,"Forma simples ajuda o desenho a nascer com clareza e ordem.","Forma simples é a figura de círculo, quadrado ou triângulo que está na origem do desenho.",
 "A forma simples permite o desenho nascer com clareza ao usar triângulos e quadrados para criar casas.",
 "A forma simples é a origem de toda figura com clareza ao usar triângulos e quadrados na casa.",
 "A **forma simples** é a origem de toda figura com **clareza** ao usar triângulos e quadrados na casa.",
 "Forma simples é a figura de círculo, quadrado ou triângulo que está na origem com _____.","clareza"),
# Semana 25
(25,1,"Personagem transforma formas simples em figuras com expressão.","Personagem é a figura com rosto, corpo e expressão que o artista cria.",
 "O personagem transforma formas simples em figuras com expressão e vida.",
 "O personagem é a figura com rosto, corpo e expressão que o artista cria com formas simples.",
 "O **personagem** é a figura com rosto, corpo e expressão que o artista cria com formas simples.",
 "_____ é a figura com rosto, corpo e expressão que o artista cria.","Personagem"),
(25,2,"Personagem transforma formas simples em figuras com expressão.","Personagem é a figura com rosto, corpo e expressão que o artista cria.",
 "O personagem transforma formas simples em figuras que ganham rosto, corpo e movimento.",
 "O personagem é a figura que ganha rosto, corpo e movimento quando o artista dá vida à forma.",
 "O **personagem** é a **figura** que ganha rosto, corpo e movimento quando o artista dá vida à forma.",
 "Personagem é a _____ com rosto, corpo e expressão que o artista cria.","figura"),
(25,3,"Personagem transforma formas simples em figuras com expressão.","Personagem é a figura com rosto, corpo e expressão que o artista cria.",
 "O personagem inventado mostra expressão quando o artista dá forma, cor e traço únicos ao ser criado.",
 "O personagem inventado é a figura com expressão única que o artista cria com forma, cor e traço.",
 "O **personagem** inventado é a figura com **expressão** única que o artista cria com forma, cor e traço.",
 "Personagem é a figura com rosto, corpo e _____ que o artista cria.","expressão"),
# Semana 26
(26,1,"Mundo desenhado mostra lugares queridos com ordem, beleza e gratidão.","Mundo desenhado é a imagem dos lugares queridos feita com ordem e beleza.",
 "O mundo desenhado mostra lugares queridos com ordem, beleza e cuidado no papel.",
 "O mundo desenhado é a imagem dos lugares queridos que o artista faz com ordem, beleza e cuidado.",
 "O **mundo desenhado** é a imagem dos lugares queridos que o artista faz com ordem, beleza e cuidado.",
 "_____ é a imagem dos lugares queridos feita com ordem e beleza.","Mundo desenhado"),
(26,2,"Mundo desenhado mostra lugares queridos com ordem, beleza e gratidão.","Mundo desenhado é a imagem dos lugares queridos feita com ordem e beleza.",
 "O mundo desenhado mostra lugares queridos como a casa, a escola e o quintal com carinho.",
 "O mundo desenhado é a imagem dos lugares queridos como a casa, a escola e o quintal.",
 "O **mundo desenhado** é a imagem dos **lugares** queridos como a casa, a escola e o quintal.",
 "Mundo desenhado é a imagem dos _____ queridos feita com ordem e beleza.","lugares"),
(26,3,"Mundo desenhado mostra lugares queridos com ordem, beleza e gratidão.","Mundo desenhado é a imagem dos lugares queridos feita com ordem e beleza.",
 "O mundo desenhado expressa gratidão ao registrar o cantinho favorito com beleza e cuidado.",
 "O mundo desenhado é a imagem do cantinho favorito feita com beleza e gratidão pelo lugar.",
 "O **mundo desenhado** é a imagem do cantinho favorito feita com beleza e **gratidão** pelo lugar.",
 "Mundo desenhado é a imagem dos lugares queridos feita com ordem e _____.","beleza"),
# Semana 27
(27,1,"Lugar desenhado mostra espaços e histórias com formas e cores.","Lugar desenhado é a imagem de um espaço real feita com formas e cores.",
 "O lugar desenhado mostra espaços e histórias com formas e cores que revelam a identidade do lugar.",
 "O lugar desenhado é a imagem de um espaço real que o artista retrata com formas e cores.",
 "O **lugar desenhado** é a imagem de um espaço real que o artista retrata com formas e cores.",
 "_____ é a imagem de um espaço real feita com formas e cores.","Lugar desenhado"),
(27,2,"Lugar desenhado mostra espaços e histórias com formas e cores.","Lugar desenhado é a imagem de um espaço real feita com formas e cores.",
 "O lugar desenhado usa formas verticais e horizontais para retratar a Igreja com torres e arcos.",
 "O lugar desenhado é a imagem da Igreja com formas verticais e horizontais de torres e arcos.",
 "O **lugar desenhado** é a imagem da Igreja com **formas** verticais e horizontais de torres e arcos.",
 "Lugar desenhado é a imagem de um espaço real feita com _____ e cores.","formas"),
(27,3,"Lugar desenhado mostra espaços e histórias com formas e cores.","Lugar desenhado é a imagem de um espaço real feita com formas e cores.",
 "O lugar desenhado usa cores vivas para mostrar a alegria do parquinho e da brincadeira.",
 "O lugar desenhado é a imagem do parquinho feita com cores vivas que revelam alegria.",
 "O **lugar desenhado** é a imagem do parquinho feita com **cores** vivas que revelam alegria.",
 "Lugar desenhado é a imagem de um espaço real feita com formas e _____.","cores"),
# Semana 28
(28,1,"História inspira imagens que ajudam a lembrar fatos importantes.","História é o relato de fatos reais que o artista transforma em imagem.",
 "A história inspira imagens que ajudam a criança a lembrar fatos importantes com beleza.",
 "A história é o relato de fatos reais que o artista transforma em imagem para lembrar com beleza.",
 "A **história** é o relato de fatos reais que o artista transforma em imagem para lembrar com beleza.",
 "_____ é o relato de fatos reais que o artista transforma em imagem.","História"),
(28,2,"História inspira imagens que ajudam a lembrar fatos importantes.","História é o relato de fatos reais que o artista transforma em imagem.",
 "A história inspira imagens que retratam a arca e os animais de Noé com detalhes visuais.",
 "A história é o relato que se transforma em imagens da arca e dos animais de Noé.",
 "A **história** é o relato que se transforma em **imagens** da arca e dos animais de Noé.",
 "História é o relato de fatos reais que o artista transforma em _____.","imagem"),
(28,3,"História inspira imagens que ajudam a lembrar fatos importantes.","História é o relato de fatos reais que o artista transforma em imagem.",
 "A história ajuda a lembrar fatos importantes ao transformar o jardim da criação em imagem.",
 "A história é o relato dos fatos da criação que o artista transforma no jardim em imagem.",
 "A **história** é o relato dos **fatos** da criação que o artista transforma no jardim em imagem.",
 "História é o relato de _____ reais que o artista transforma em imagem.","fatos"),
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
