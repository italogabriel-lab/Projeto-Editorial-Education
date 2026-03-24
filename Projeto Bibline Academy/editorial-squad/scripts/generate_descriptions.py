#!/usr/bin/env python3
"""
GERADOR MASSIVO: Reconstrói o arquivo 6 (Descrições para tickets) inteiro, incluindo provas e bimestres, do zero. 
Uso: Criação original ou regeneração profunda (sobrescreve tudo).
"""
import re

# Read original file
with open("/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto Bibline Academy/Belas Artes - Fase da Gramática/1 Fase - Gramática/3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE/Estrutura Curricular - 3º ANO/6 - Descrições para tickets - 3º ANO.md", "r") as f:
    content = f.read()

# Data structure: week_num -> (week_theme, [(lesson_id, lesson_title), ...])
weeks = {
    1: ("Arte Bizantina: o Império e a fé", [
        ("1.1", "Império Romano do oriente e arte bizantina"),
        ("1.2", "Constantinopla como centro"),
        ("1.3", "Cristianismo e transformação da arte pública"),
    ]),
    2: ("Arte Bizantina: teologia visual", [
        ("2.1", "Cristo como centro da arte"),
        ("2.2", "Arte como ensino da fé"),
        ("2.3", "Ornamentação litúrgica"),
    ]),
    3: ("Arte Bizantina: materiais e técnicas", [
        ("3.1", "Mosaicos em ouro"),
        ("3.2", "Têmpera sobre madeira"),
        ("3.3", "Afrescos bizantinos"),
    ]),
    4: ("Arte Bizantina: forma e arquitetura", [
        ("4.1", "Frontalidade e hierarquia"),
        ("4.2", "Fundo dourado e eternidade"),
        ("4.3", "Igrejas centralizadas"),
    ]),
    5: ("Arte Bizantina: obras e legado", [
        ("5.1", "Mosaicos de Ravena"),
        ("5.2", "A cúpula que toca o céu"),
        ("5.3", "Legado e influência medieval"),
    ]),
    6: ("Iconoclastia: a crise das imagens", [
        ("6.1", "Conflitos religiosos por causa das imagens"),
        ("6.2", "A imagem entre o ensino e o ídolo"),
        ("6.3", "Defesa dos ícones"),
    ]),
    7: ("Iconoclastia: destruição e restauração", [
        ("7.1", "Destruição dos ícones"),
        ("7.2", "Restauração e produção padronizada"),
        ("7.3", "Estilo rígido e simbólico"),
    ]),
    8: ("Iconoclastia: legado teológico", [
        ("8.1", "A pintura que venceu a escultura"),
        ("8.2", "A imagem que renasceu mais forte"),
        ("8.3", "O lugar correto da imagem"),
    ]),
    11: ("Arte Islâmica: contexto e cosmovisão", [
        ("11.1", "A arte que nasceu no deserto"),
        ("11.2", "Impérios que moldaram a beleza"),
        ("11.3", "A arte sem rosto humano"),
    ]),
    12: ("Arte Islâmica: ornamentação e materiais", [
        ("12.1", "A beleza que substitui o rosto"),
        ("12.2", "Letras que se tornaram arte"),
        ("12.3", "A linguagem infinita das formas"),
    ]),
    13: ("Arte Islâmica: forma e composição", [
        ("13.1", "O desenho que nunca termina"),
        ("13.2", "O espelho perfeito da ordem"),
        ("13.3", "A voz silenciosa da repetição"),
    ]),
    14: ("Arte Islâmica: arquitetura", [
        ("14.1", "O lugar dedicado à oração"),
        ("14.2", "A beleza sem estátuas"),
        ("14.3", "O oceano azul de Istambul"),
    ]),
    15: ("Arte Islâmica: obras e legado", [
        ("15.1", "A joia de Granada"),
        ("15.2", "A arte que cruzou fronteiras"),
        ("15.3", "Examina tudo, retém o bom"),
    ]),
    16: ("Arte Românica: contexto e cosmovisão", [
        ("16.1", "A fé que construiu fortalezas"),
        ("16.2", "O caminho devocional do peregrino"),
        ("16.3", "O sermão esculpido na pedra"),
    ]),
    17: ("Arte Românica: materiais e forma", [
        ("17.1", "Paredes que falam de Deus"),
        ("17.2", "Capitéis que contam histórias"),
        ("17.3", "A força da pedra e da forma"),
    ]),
    18: ("Arte Românica: arquitetura e legado", [
        ("18.1", "A fortaleza de Deus em Cluny"),
        ("18.2", "A página iluminada pela fé"),
        ("18.3", "Herança que ecoa nos séculos"),
    ]),
    21: ("Arte Gótica: contexto e cosmovisão", [
        ("21.1", "A cidade que ergueu catedrais"),
        ("21.2", "A fé que saiu do claustro"),
        ("21.3", "A luz que entrou pela pedra"),
    ]),
    22: ("Arte Gótica: função e materiais", [
        ("22.1", "A arte que inspira adoração"),
        ("22.2", "A Bíblia pintada em vidro"),
        ("22.3", "O arco que alcança o céu"),
    ]),
    23: ("Arte Gótica: forma e composição", [
        ("23.1", "A pedra que sustenta a pedra"),
        ("23.2", "A agulha que costura terra e céu"),
        ("23.3", "A rosa que conta a redenção"),
    ]),
    24: ("Arte Gótica: arquitetura e escultura", [
        ("24.1", "O rosto que ganha vida na pedra"),
        ("24.2", "O olhar que comove e converte"),
        ("24.3", "O pincel que anunciou o Renascimento"),
    ]),
    25: ("Arte Gótica: obras e legado", [
        ("25.1", "A joia de vidro e pedra"),
        ("25.2", "A capela feita só de luz"),
        ("25.3", "A ponte entre dois mundos"),
    ]),
    26: ("Pré-Renascimento do Norte: contexto e cosmovisão", [
        ("26.1", "O mercador e o pintor"),
        ("26.2", "A tinta que brilha como joia"),
        ("26.3", "O espelho da criação"),
    ]),
    27: ("Pré-Renascimento do Norte: materiais e forma", [
        ("27.1", "O altar que deslumbra o mundo"),
        ("27.2", "O símbolo escondido no detalhe"),
        ("27.3", "O rosto do homem comum"),
    ]),
    28: ("Pré-Renascimento do Norte: obras e legado", [
        ("28.1", "A descida da cruz que nos faz chorar"),
        ("28.2", "A cidade santa pintada no painel"),
        ("28.3", "A lupa e a verdade"),
    ]),
    31: ("Renascimento do Norte: contexto e cosmovisão", [
        ("31.1", "A mente que busca Deus nos livros"),
        ("31.2", "A revolução da tinta e da prensa"),
        ("31.3", "O cavaleiro entre a morte e o diabo"),
    ]),
    32: ("Renascimento do Norte: função e cosmovisão", [
        ("32.1", "O artista que se pintou como Cristo"),
        ("32.2", "O martelo que mudou o mundo e a arte"),
        ("32.3", "O pintor dos reis e da verdade"),
    ]),
    33: ("Renascimento do Norte: materiais e forma", [
        ("33.1", "O pintor da Reforma"),
        ("33.2", "O jardim dos pesadelos e das verdades"),
        ("33.3", "O pintor dos camponeses e das estações"),
    ]),
    34: ("Renascimento do Norte: artistas", [
        ("34.1", "A janela para a criação"),
        ("34.2", "A mesa posta que lembra a morte"),
        ("34.3", "A lupa contra o telescópio"),
    ]),
    35: ("Renascimento do Norte: legado", [
        ("35.1", "A teimosia da beleza verdadeira"),
        ("35.2", "O ofício que glorifica o Criador"),
        ("35.3", "A linha de ouro que une tudo"),
    ]),
    36: ("Consolidação: visão panorâmica (parte 1)", [
        ("36.1", "A balança do discernimento"),
        ("36.2", "A vocação do artista e a glória de Deus"),
        ("36.3", "A beleza que aponta para o Belo"),
    ]),
    37: ("Consolidação: conexões e contrastes", [
        ("37.1", "O que a arte me ensinou sobre Deus"),
        ("37.2", "A gratidão pelo dom de ver"),
        ("37.3", "O próximo capítulo da grande história"),
    ]),
    38: ("Encerramento do Volume 2", [
        ("38.1", "O museu do coração"),
        ("38.2", "A coroa e o serviço"),
        ("38.3", "Soli Deo Gloria"),
    ]),
}

# Utility functions for generating text blocks

def generate_weekly_review_desc(week_num):
    """Generate weekly review description content."""
    theme, lessons = weeks[week_num]
    lines = [f"Revisar os conhecimentos das aulas da semana {week_num}\n"]
    lines.append(f"## {week_num}ª Semana: **{theme}**\n")
    for lid, ltitle in lessons:
        lines.append(f"- {lid} {ltitle}\n")
    return "\n".join(lines)

def generate_weekly_exam_desc(week_num):
    """Generate weekly exam description content."""
    theme, lessons = weeks[week_num]
    lines = [f"Avaliar os conhecimentos das aulas da semana {week_num}\n"]
    lines.append(f"## {week_num}ª Semana: **{theme}**\n")
    for lid, ltitle in lessons:
        lines.append(f"- {lid} {ltitle}\n")
    return "\n".join(lines)


# Process the file line by line
lines = content.split('\n')
new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    
    # Check for weekly review pattern: [Belas artes] - Ano 3 - X.4 Revisão
    review_match = re.match(r'^\[Belas artes\] - Ano 3 - (\d+)\.4 Revisão', line)
    exam_match = re.match(r'^\[Belas artes\] - Ano 3 - (\d+)\.5 Provas?', line)
    
    if review_match:
        week_num = int(review_match.group(1))
        if week_num in weeks:
            # Write the title line
            new_lines.append(line)
            i += 1
            # Skip to after "# Description" line
            while i < len(lines) and not lines[i].startswith('# Description'):
                new_lines.append(lines[i])
                i += 1
            if i < len(lines):
                new_lines.append(lines[i])  # "# Description"
                i += 1
            # Skip the old content until next ---
            while i < len(lines) and lines[i].strip() != '---':
                i += 1
            # Insert new content
            new_lines.append("")
            new_lines.append(generate_weekly_review_desc(week_num))
            # The --- will be added by the main loop
        else:
            new_lines.append(line)
            i += 1
    elif exam_match:
        week_num = int(exam_match.group(1))
        if week_num in weeks:
            # Write the title line
            new_lines.append(line)
            i += 1
            # Skip to after "# Description" line
            while i < len(lines) and not lines[i].startswith('# Description'):
                new_lines.append(lines[i])
                i += 1
            if i < len(lines):
                new_lines.append(lines[i])  # "# Description"
                i += 1
            # Skip the old content until next ---
            while i < len(lines) and lines[i].strip() != '---':
                i += 1
            # Insert new content
            new_lines.append("")
            new_lines.append(generate_weekly_exam_desc(week_num))
            # The --- will be added by the main loop
        else:
            new_lines.append(line)
            i += 1
    else:
        new_lines.append(line)
        i += 1

# Now we need to add bimestral entries
# They should go after the last week of each bimester
# Bimesters: 
# After week 8 (before week 11): Semana 9 (Revisão) + Semana 10 (Prova)
# After week 18 (before week 21): Semana 19 (Revisão) + Semana 20 (Prova)
# After week 28 (before week 31): Semana 29 (Revisão) + Semana 30 (Prova)
# After week 38 (at end): Semana 39 (Revisão Final) + Semana 40 (Prova Final)

# Configuration for bimesters is defined implicitly during generation.
def generate_bimestral_section(bim_num, week_list, module_name, is_final=False):
    """Generate a full bimestral review + exam section."""
    lines_out = []
    
    rev_prefix = "Revisão Final" if is_final else f"Revisão do {bim_num}º Bimestre"
    exam_prefix = "Prova Final" if is_final else f"Prova do {bim_num}º Bimestre"
    rev_week = 39 if is_final else (bim_num * 10 - 1)
    exam_week = 40 if is_final else (bim_num * 10)
    
    # Compute actual review/exam week numbers
    if bim_num == 1:
        rev_week, exam_week = 9, 10
    elif bim_num == 2:
        rev_week, exam_week = 19, 20
    elif bim_num == 3:
        rev_week, exam_week = 29, 30
    elif bim_num == 4:
        rev_week, exam_week = 39, 40
    
    rev_title_suffix = f"Revisão do {module_name}" if not is_final else "Revisão Final"
    exam_title_suffix = f"Prova do {module_name}" if not is_final else "Prova Final"
    
    # Review section
    lines_out.append(f"## Semana {rev_week} – {rev_title_suffix}")
    lines_out.append("")
    lines_out.append("---")
    lines_out.append("")
    lines_out.append(f"[Belas artes] - Ano 3 - Semana {rev_week} - {rev_title_suffix}")
    lines_out.append("")
    lines_out.append("# Description")
    lines_out.append("")
    lines_out.append(f"# {rev_prefix}")
    lines_out.append("")
    
    for wn in week_list:
        theme, lessons = weeks[wn]
        lines_out.append(f"## {wn}ª Semana: **{theme}**")
        lines_out.append("")
        for lid, ltitle in lessons:
            lines_out.append(f"- {lid} {ltitle}")
            lines_out.append("")
    
    lines_out.append("---")
    lines_out.append("")
    
    # Exam section
    lines_out.append(f"## Semana {exam_week} – {exam_title_suffix}")
    lines_out.append("")
    lines_out.append("---")
    lines_out.append("")
    lines_out.append(f"[Belas artes] - Ano 3 - Semana {exam_week} - {exam_title_suffix}")
    lines_out.append("")
    lines_out.append("# Description")
    lines_out.append("")
    lines_out.append(f"# {exam_prefix}")
    lines_out.append("")
    
    for wn in week_list:
        theme, lessons = weeks[wn]
        lines_out.append(f"## {wn}ª Semana: **{theme}**")
        lines_out.append("")
        for lid, ltitle in lessons:
            lines_out.append(f"- {lid} {ltitle}")
            lines_out.append("")
    
    lines_out.append("---")
    lines_out.append("")
    
    return lines_out


# Now insert bimestral sections into the content
# Strategy: find the locations where each bimester break should go
result = "\n".join(new_lines)

# Insert bimestral sections at the right points
# After week 8.5 section (before "## Semana 11"), insert Bimestral 1
# After week 18.5 section (before "## Semana 21"), insert Bimestral 2
# After week 28.5 section (before "## Semana 31"), insert Bimestral 3
# After week 38.5 section (at end of file), insert Bimestral 4

insertions = [
    ("## Semana 11", generate_bimestral_section(1, [1,2,3,4,5,6,7,8], "Módulo 1")),
    ("## Semana 21", generate_bimestral_section(2, [11,12,13,14,15,16,17,18], "Módulo 2")),
    ("## Semana 31", generate_bimestral_section(3, [21,22,23,24,25,26,27,28], "Módulo 3")),
]

result_lines = result.split('\n')
final_lines = []
for line in result_lines:
    for marker, section_lines in insertions:
        if line.strip().startswith(marker):
            final_lines.extend(section_lines)
            break
    final_lines.append(line)

# Add bimestral 4 at end
final_lines.append("")
bim4_lines = generate_bimestral_section(4, [31,32,33,34,35,36,37,38], "Volume 2", is_final=True)
final_lines.extend(bim4_lines)

output = "\n".join(final_lines)

# Write output
output_path = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto Bibline Academy/Belas Artes - Fase da Gramática/1 Fase - Gramática/3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE/Estrutura Curricular - 3º ANO/6 - Descrições para tickets - 3º ANO.md"
with open(output_path, "w") as f:
    f.write(output)

print(f"File written successfully. Total lines: {len(final_lines)}")
