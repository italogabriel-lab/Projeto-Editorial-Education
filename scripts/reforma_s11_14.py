import os, re

BASE = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto - Bibline Academy ( Produção de Aulas)/Belas Artes - Fase da Gramática/1 Fase - Gramática/1º Ano - Introdução à Linguagem Visual e aos Elementos da Arte"

# (semana, aula, old_def, new_def, old_para_plain, new_para_plain, new_para_bold, fill_in, fill_answer)
AULAS = [
# Semana 11
(11,1,"Cor primária inicia misturas e ajuda outras cores a nascer.","Cor primária é a cor que existe por si mesma e cria misturas de novas cores.",
 "A cor primária é a cor que não nasce de nenhuma mistura e inicia o ciclo das cores.",
 "A cor primária é a cor que não vem de nenhuma mistura e existe sozinha na paleta.",
 "A **cor primária** é a cor que não vem de nenhuma mistura e existe sozinha na paleta.",
 "_____ é a cor que existe por si mesma e cria misturas de novas cores.","Cor primária"),
(11,2,"Cor primária inicia misturas e ajuda outras cores a nascer.","Cor primária é a cor que existe por si mesma e cria misturas de novas cores.",
 "A cor primária inicia misturas que criam novas cores a partir do vermelho, do azul e do amarelo.",
 "A cor primária faz misturas quando se combina com outra cor primária.",
 "A **cor primária** faz **misturas** quando se combina com outra cor primária.",
 "Cor primária é a cor que existe por si mesma e cria _____ de novas cores.","misturas"),
(11,3,"Cor primária inicia misturas e ajuda outras cores a nascer.","Cor primária é a cor que existe por si mesma e cria misturas de novas cores.",
 "A cor primária ajuda outras cores a nascer quando duas ou mais se combinam.",
 "A cor primária dá origem a novas cores quando duas ou mais se combinam.",
 "A **cor primária** dá origem a novas **cores** quando duas ou mais se combinam.",
 "Cor primária é a cor que existe por si mesma e cria misturas de novas _____.","cores"),
# Semana 12
(12,1,"Cor expressiva mostra sentimentos com beleza, ordem e cuidado.","Cor expressiva é a cor escolhida para revelar sentimentos com beleza e cuidado.",
 "A cor expressiva mostra sentimentos com beleza e ordem quando é escolhida com cuidado.",
 "A cor expressiva é a cor que o artista escolhe para revelar sentimentos com beleza e cuidado.",
 "A **cor expressiva** é a cor que o artista escolhe para revelar sentimentos com beleza e cuidado.",
 "_____ é a cor escolhida para revelar sentimentos com beleza e cuidado.","Cor expressiva"),
(12,2,"Cor expressiva mostra sentimentos com beleza, ordem e cuidado.","Cor expressiva é a cor escolhida para revelar sentimentos com beleza e cuidado.",
 "A cor expressiva comunica sentimentos diferentes conforme a cor que o artista escolhe.",
 "A cor expressiva revela sentimentos diferentes conforme a cor que o artista escolhe.",
 "A **cor expressiva** revela **sentimentos** diferentes conforme a cor que o artista escolhe.",
 "Cor expressiva é a cor escolhida para revelar _____ com beleza e cuidado.","sentimentos"),
(12,3,"Cor expressiva mostra sentimentos com beleza, ordem e cuidado.","Cor expressiva é a cor escolhida para revelar sentimentos com beleza e cuidado.",
 "A cor expressiva usa cores quentes e frias com cuidado para mostrar sentimentos com beleza.",
 "A cor expressiva usa cores quentes e frias com cuidado para revelar sentimentos com beleza.",
 "A **cor expressiva** usa cores quentes e frias com **cuidado** para revelar sentimentos com beleza.",
 "Cor expressiva é a cor escolhida para revelar sentimentos com beleza e _____.","cuidado"),
# Semana 13
(13,1,"Cor musical acompanha o som e expressa sentimento na arte.","Cor musical é a cor que nasce do som e revela o sentimento da música na arte.",
 "A cor musical une escuta e observação ao conectar o som às escolhas de cor.",
 "A cor musical é a cor que o artista escolhe ao ouvir música e deixar o som guiar a imagem.",
 "A **cor musical** é a cor que o artista escolhe ao ouvir música e deixar o som guiar a imagem.",
 "_____ é a cor que nasce do som e revela o sentimento da música na arte.","Cor musical"),
(13,2,"Cor musical acompanha o som e expressa sentimento na arte.","Cor musical é a cor que nasce do som e revela o sentimento da música na arte.",
 "A cor musical acompanha o som e transforma a escuta em gesto e cor no papel.",
 "A cor musical nasce do som quando a escuta se transforma em gesto e cor no papel.",
 "A **cor musical** nasce do **som** quando a escuta se transforma em gesto e cor no papel.",
 "Cor musical é a cor que nasce do _____ e revela o sentimento da música na arte.","som"),
(13,3,"Cor musical acompanha o som e expressa sentimento na arte.","Cor musical é a cor que nasce do som e revela o sentimento da música na arte.",
 "A cor musical expressa sentimento quando a cor escolhida nasce do que a música provoca.",
 "A cor musical revela o sentimento quando a cor escolhida nasce do que a música provoca.",
 "A **cor musical** revela o **sentimento** quando a cor escolhida nasce do que a música provoca.",
 "Cor musical é a cor que nasce do som e revela o _____ da música na arte.","sentimento"),
# Semana 14
(14,1,"Luz muda as cores do dia e da noite com beleza.","Luz é a claridade que Deus criou para revelar as cores do dia e da noite.",
 "A luz muda as cores do dia e da noite ao iluminar a criação com beleza.",
 "A luz é a claridade que Deus criou e que revela as formas e as cores na criação.",
 "A **luz** é a claridade que Deus criou e que revela as formas e as cores na criação.",
 "_____ é a claridade que Deus criou para revelar as cores do dia e da noite.","Luz"),
(14,2,"Luz muda as cores do dia e da noite com beleza.","Luz é a claridade que Deus criou para revelar as cores do dia e da noite.",
 "A luz revela cores diferentes conforme o momento do dia e a posição do sol.",
 "A luz revela cores diferentes conforme o momento do dia e a posição do sol.",
 "A **luz** revela **cores** diferentes conforme o momento do dia e a posição do sol.",
 "Luz é a claridade que Deus criou para revelar as _____ do dia e da noite.","cores"),
(14,3,"Luz muda as cores do dia e da noite com beleza.","Luz é a claridade que Deus criou para revelar as cores do dia e da noite.",
 "A luz mostra as cores da noite com tons escuros e suaves que cobrem a criação.",
 "A luz revela as cores da noite com tons escuros e suaves que cobrem a criação.",
 "A **luz** revela as cores da **noite** com tons escuros e suaves que cobrem a criação.",
 "Luz é a claridade que Deus criou para revelar as cores do dia e da _____.","noite"),
]

def patch_file(path, old_def, new_def, old_para_plain, new_para_plain, new_para_bold, fill_in, fill_answer):
    with open(path, encoding="utf-8") as f:
        txt = f.read()
    
    old_def_bold = f"**{old_def}**"
    new_def_bold = f"**{new_def}**"
    
    # definição bold → nova bold
    txt = txt.replace(old_def_bold, new_def_bold)
    # definição plain → nova plain
    txt = txt.replace(old_def, new_def)
    
    # parágrafo plain → novo plain (Accordion MP3 e Narrar antes de [MP3\])
    txt = txt.replace(old_para_plain, new_para_plain)
    
    # parágrafo bold → novo bold (Definir linha 9 e Accordion/Narrar após [MP3\])
    old_para_bold = re.sub(r'\*\*(.+?)\*\*', lambda m: m.group(1), new_para_bold)
    # substituir a versão com bold que já existia
    # A versão bold existente: identifica pelo padrão com **termo** e **kw**
    # Mais seguro: substituir old_para com bold pelo new_para_bold
    # A versão bold antiga era: old_para_plain com bold no termo
    # Vamos usar regex para encontrar a versão bold do old_para
    old_para_bold_pattern = re.escape(old_para_plain).replace(re.escape("A **"), "A \\*\\*").replace(re.escape("O **"), "O \\*\\*")
    # Abordagem mais simples: substituir qualquer linha que contenha old_para_plain (com ou sem bold)
    for line in txt.split("\n"):
        stripped = re.sub(r'\*\*(.+?)\*\*', r'\1', line)
        if stripped.strip() == old_para_plain.strip() and "**" in line:
            txt = txt.replace(line, new_para_bold)
            break
    
    # fill_in: substituir a linha com _____ dentro do bloco FILL_IN
    lines = txt.split("\n")
    in_fill = False
    new_lines = []
    replaced_fill = False
    replaced_answer = False
    for i, line in enumerate(lines):
        if "[+FILL_IN]" in line:
            in_fill = True
            replaced_fill = False
            replaced_answer = False
            new_lines.append(line)
            continue
        if "[-FILL_IN]" in line:
            in_fill = False
        if in_fill and "_____" in line and not replaced_fill:
            new_lines.append(fill_in)
            replaced_fill = True
            continue
        if in_fill and replaced_fill and not replaced_answer and line.strip() and "[-FILL_IN]" not in line and "[" not in line:
            new_lines.append(fill_answer)
            replaced_answer = True
            continue
        new_lines.append(line)
    txt = "\n".join(new_lines)
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(txt)
    return True

modified = 0
errors = []
for row in AULAS:
    sem, aula, old_def, new_def, old_para, new_para_plain, new_para_bold, fill_in, fill_answer = row
    fname = f"{sem}.{aula}.md"
    fpath = os.path.join(BASE, fname)
    try:
        patch_file(fpath, old_def, new_def, old_para, new_para_plain, new_para_bold, fill_in, fill_answer)
        modified += 1
        print(f"✔ {fname}")
    except Exception as e:
        errors.append((fname, str(e)))
        print(f"✗ {fname}: {e}")

print(f"\nModificados: {modified} | Erros: {len(errors)}")
