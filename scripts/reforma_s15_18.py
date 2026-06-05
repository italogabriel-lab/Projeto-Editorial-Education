import os, re

BASE = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto - Bibline Academy ( Produção de Aulas)/Belas Artes - Fase da Gramática/1 Fase - Gramática/1º Ano - Introdução à Linguagem Visual e aos Elementos da Arte"

AULAS = [
# Semana 15
(15,1,"Textura mostra se a superfície parece lisa, áspera ou marcada.","Textura é a qualidade da superfície que parece lisa, áspera ou marcada.",
 "A textura mostra como uma superfície parece ao toque e à vista.",
 "A textura é a qualidade da superfície que parece lisa, áspera ou marcada ao olho e ao toque.",
 "A **textura** é a qualidade da superfície que parece lisa, áspera ou marcada ao olho e ao toque.",
 "_____ é a qualidade da superfície que parece lisa, áspera ou marcada.","Textura"),
(15,2,"Textura mostra se a superfície parece lisa, áspera ou marcada.","Textura é a qualidade da superfície que parece lisa, áspera ou marcada.",
 "A textura revela superfícies lisas quando o material não tem marcas nem irregularidades.",
 "A textura é lisa quando a superfície não tem marcas nem irregularidades.",
 "A **textura** é **lisa** quando a superfície não tem marcas nem irregularidades.",
 "Textura é a qualidade da superfície que parece _____, áspera ou marcada.","lisa"),
(15,3,"Textura mostra se a superfície parece lisa, áspera ou marcada.","Textura é a qualidade da superfície que parece lisa, áspera ou marcada.",
 "A textura da areia e das folhas deixa superfícies marcadas com padrões únicos.",
 "A textura da areia e das folhas é marcada com padrões únicos que cada material deixa.",
 "A **textura** da areia e das folhas é **marcada** com padrões únicos que cada material deixa.",
 "Textura é a qualidade da superfície que parece lisa, áspera ou _____.","marcada"),
# Semana 16
(16,1,"Textura expressiva comunica sentimento por marcas, massas e materiais.","Textura expressiva é a textura criada com marcas, massas e materiais na arte.",
 "A textura expressiva usa marcas e materiais para comunicar sentimento na arte.",
 "A textura expressiva é a textura que o artista faz com marcas e materiais para revelar sentimento na obra.",
 "A **textura expressiva** é a textura que o artista faz com marcas e materiais para revelar sentimento na obra.",
 "_____ é a textura criada com marcas, massas e materiais na arte.","Textura expressiva"),
(16,2,"Textura expressiva comunica sentimento por marcas, massas e materiais.","Textura expressiva é a textura criada com marcas, massas e materiais na arte.",
 "A textura expressiva se forma com massas que deixam marcas espessas e com volume.",
 "A textura expressiva é feita com massas que deixam marcas espessas e com volume na obra.",
 "A **textura expressiva** é feita com **massas** que deixam marcas espessas e com volume na obra.",
 "Textura expressiva é a textura criada com marcas, _____ e materiais na arte.","massas"),
(16,3,"Textura expressiva comunica sentimento por marcas, massas e materiais.","Textura expressiva é a textura criada com marcas, massas e materiais na arte.",
 "A textura expressiva usa materiais naturais que deixam marcas únicas no papel.",
 "A textura expressiva usa materiais naturais que deixam marcas únicas e com sentimento no papel.",
 "A **textura expressiva** usa **materiais** naturais que deixam marcas únicas e com sentimento no papel.",
 "Textura expressiva é a textura criada com marcas, massas e _____ na arte.","materiais"),
# Semana 17
(17,1,"Espaço organiza fundo, borda e centro dentro do papel.","Espaço é a área do papel dividida em fundo, borda e centro.",
 "O espaço organiza o papel em fundo, borda e centro para que cada parte tenha o seu lugar.",
 "O espaço é a área do papel que o artista divide em fundo, borda e centro para organizar a obra.",
 "O **espaço** é a área do papel que o artista divide em fundo, borda e centro para organizar a obra.",
 "_____ é a área do papel dividida em fundo, borda e centro.","Espaço"),
(17,2,"Espaço organiza fundo, borda e centro dentro do papel.","Espaço é a área do papel dividida em fundo, borda e centro.",
 "O espaço começa pelo fundo que preenche a área atrás das figuras principais.",
 "O espaço começa pelo fundo que preenche a área atrás das figuras principais.",
 "O **espaço** começa pelo **fundo** que preenche a área atrás das figuras principais.",
 "Espaço é a área do papel dividida em _____, borda e centro.","fundo"),
(17,3,"Espaço organiza fundo, borda e centro dentro do papel.","Espaço é a área do papel dividida em fundo, borda e centro.",
 "O espaço organiza figuras pelo centro ao colocar o maior elemento no meio do papel.",
 "O espaço tem o centro como o lugar onde o artista coloca o elemento principal da obra.",
 "O **espaço** tem o **centro** como o lugar onde o artista coloca o elemento principal da obra.",
 "Espaço é a área do papel dividida em fundo, borda e _____.","centro"),
# Semana 18
(18,1,"Respiro equilibra espaço cheio e vazio para ordenar o desenho.","Respiro é o espaço vazio que dá clareza ao desenho cheio.",
 "O respiro equilibra o cheio e o vazio para que a imagem tenha ordem e clareza.",
 "O respiro é o espaço vazio que o artista deixa para que a imagem tenha ordem e clareza.",
 "O **respiro** é o espaço vazio que o artista deixa para que a imagem tenha ordem e clareza.",
 "_____ é o espaço vazio que dá clareza ao desenho cheio.","Respiro"),
(18,2,"Respiro equilibra espaço cheio e vazio para ordenar o desenho.","Respiro é o espaço vazio que dá clareza ao desenho cheio.",
 "O respiro equilibra o espaço ao deixar partes livres ao redor dos elementos do desenho.",
 "O respiro é o espaço livre ao redor dos elementos que equilibra o cheio e o vazio.",
 "O **respiro** é o **espaço** livre ao redor dos elementos que equilibra o cheio e o vazio.",
 "Respiro é o _____ vazio que dá clareza ao desenho cheio.","espaço"),
(18,3,"Respiro equilibra espaço cheio e vazio para ordenar o desenho.","Respiro é o espaço vazio que dá clareza ao desenho cheio.",
 "O respiro equilibra o cheio e o vazio ao organizar formas com espaço entre elas.",
 "O respiro é o espaço vazio entre as formas que organiza a imagem da cidade no papel.",
 "O **respiro** é o espaço **vazio** entre as formas que organiza a imagem da cidade no papel.",
 "Respiro é o espaço _____ que dá clareza ao desenho cheio.","vazio"),
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
            txt = txt.replace(line, new_para_bold)
            break
    lines = txt.split("\n")
    in_fill, replaced_fill, replaced_answer = False, False, False
    new_lines = []
    for line in lines:
        if "[+FILL_IN]" in line:
            in_fill = True; replaced_fill = False; replaced_answer = False
            new_lines.append(line); continue
        if "[-FILL_IN]" in line:
            in_fill = False
        if in_fill and "_____" in line and not replaced_fill:
            new_lines.append(fill_in); replaced_fill = True; continue
        if in_fill and replaced_fill and not replaced_answer and line.strip() and "[" not in line:
            new_lines.append(fill_answer); replaced_answer = True; continue
        new_lines.append(line)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))

for row in AULAS:
    sem, aula, old_def, new_def, old_para, new_para_plain, new_para_bold, fill_in, fill_answer = row
    fname = f"{sem}.{aula}.md"
    fpath = os.path.join(BASE, fname)
    try:
        patch_file(fpath, old_def, new_def, old_para, new_para_plain, new_para_bold, fill_in, fill_answer)
        print(f"✔ {fname}")
    except Exception as e:
        print(f"✗ {fname}: {e}")
