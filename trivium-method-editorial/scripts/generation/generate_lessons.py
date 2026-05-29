#!/usr/bin/env python3
"""
generate_lessons.py — Gerador de aulas no padrão Trivium Method Editorial

Uso:
    # Gerar todas as aulas da semana (x.1, x.2, x.3, x.4)
    python generate_lessons.py dados_semana3.yaml

    # Gerar apenas uma aula específica
    python generate_lessons.py dados_semana3.yaml --apenas x1
    python generate_lessons.py dados_semana3.yaml --apenas x2
    python generate_lessons.py dados_semana3.yaml --apenas x3
    python generate_lessons.py dados_semana3.yaml --apenas revisao

    # Especificar diretório de saída
    python generate_lessons.py dados_semana3.yaml --saida ./output

    # Gerar arquivo YAML de exemplo preenchido
    python generate_lessons.py --exemplo > dados_semana_exemplo.yaml

Requisitos:
    pip install pyyaml

Compatibilidade:
    Anos 1, 2 e 3 do padrão Trivium Method Editorial (Belas Artes e outras
    disciplinas com o mesmo template de 5 hábitos: Definir, Perceber,
    Recordar, Praticar e Narrar).

Diferenças por ano:
    Ano 1 : 2 opções no [+MULTIPLE] (1 correta + 1 distrator)
    Ano 2 : 3 opções no [+MULTIPLE] (1 correta + 2 distratores)
    Ano 3 : 3 opções + Narrar usa [+PARAGRAPH]+[+IMAGE] em vez de [+IMAGE_TEXT_ASIDE]

Padrões editoriais aplicados automaticamente:
    - Definição curta idêntica em Definir, Accordion, Recordar e Narrar
    - Accordion plain (sem negrito) antes de [MP3\\] e bold depois
    - Narrar espelha literalmente o Definir (plain antes, bold depois)
    - Legendas do IMAGE_LABELED na revisão copiadas das aulas x.1, x.2, x.3
    - Fill-In da revisão com lacuna na palavra-chave correta
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Erro: PyYAML não instalado. Execute: pip install pyyaml")
    sys.exit(1)


# ─────────────────────────────────────────────────────────────────────────────
# Constantes de marcação Rise Blocks
# ─────────────────────────────────────────────────────────────────────────────

MP3_ABRIR = "[MP3/]"
MP3_FECHAR = r"[MP3\]"


# ─────────────────────────────────────────────────────────────────────────────
# Utilitários de texto
# ─────────────────────────────────────────────────────────────────────────────

def aplicar_negrito(texto: str, palavras: list) -> str:
    """
    Aplica **negrito** às palavras/frases listadas no texto.
    Frases mais longas são processadas primeiro para evitar sobreposições.
    A substituição preserva o caso original do texto.
    """
    if not palavras:
        return texto
    resultado = texto
    for kw in sorted(palavras, key=len, reverse=True):
        def _repl(m, kw=kw):
            return f"**{m.group()}**"
        resultado = re.sub(re.escape(kw), _repl, resultado, flags=re.IGNORECASE)
    return resultado


def primeira_minuscula(texto: str) -> str:
    """Converte a primeira letra para minúscula (usado no Definir da revisão)."""
    if not texto:
        return texto
    return texto[0].lower() + texto[1:]


# ─────────────────────────────────────────────────────────────────────────────
# Gerador de aula regular (x.1, x.2 ou x.3)
# ─────────────────────────────────────────────────────────────────────────────

def gerar_aula(config: dict, semana: dict, chave: str) -> str:
    """
    Gera o conteúdo markdown de uma aula regular.
    chave: 'x1' | 'x2' | 'x3'
    """
    aula = semana["aulas"][chave]
    ano = config.get("ano", 1)
    hash_audio = config.get("audio_hash", "0b12d715e4c741399594fccb12d4bbe2")
    definicao = semana["definicao_curta"]
    musica = semana["nome_musica"]

    titulo = aula["titulo"]
    accordion_titulo = aula.get("accordion_titulo", titulo)
    palavras_negrito = aula.get("palavras_negrito", [])

    paragrafo_plain = aula["paragrafo_plain"]
    paragrafo_bold = aplicar_negrito(paragrafo_plain, palavras_negrito)

    perceber_frase = aula["perceber_frase"]
    hotspot_coords = aula["perceber_hotspot_coords"]
    hotspot_legenda = aula["perceber_hotspot_legenda"]

    fill_frase = aula["fill_in_frase"]
    fill_resposta = aula["fill_in_resposta"]

    multiple_pergunta = aula["multiple_pergunta"]
    multiple_correta = aula["multiple_resposta_correta"]
    distratores = aula.get("multiple_distratores", [])

    instrucao = aula["atividade_instrucao"]
    narrar_pergunta = aula["narrar_pergunta"]

    L = []  # linhas do arquivo

    # ── Definir ───────────────────────────────────────────────────────────────
    L += [
        f"# {titulo}",
        "",
        "## Definir",
        "",
        "[+PARAGRAPH]",
        "",
        f"**{definicao}**",
        "",
        paragrafo_bold,
        "",
        "Veja o vídeo abaixo.",
        "",
        "[-PARAGRAPH]",
        "",
        "[+VIDEO][-VIDEO]",
        "",
        "[+HEADING]",
        "",
        "Atividade",
        "",
        "[-HEADING]",
        "",
        "[+PARAGRAPH]",
        "",
        "Leia a definição e ouça o áudio clicando abaixo.",
        "",
        "[-PARAGRAPH]",
        "",
        "[+ACCORDION]",
        "",
        accordion_titulo,
        "",
        "@link_png@",
        "",
        MP3_ABRIR,
        "",
        f"#FSH:{hash_audio}",
        "",
        definicao,
        "",
        paragrafo_plain,
        "",
        MP3_FECHAR,
        "",
        f"**{definicao}**",
        "",
        paragrafo_bold,
        "",
        "[-ACCORDION]",
        "",
    ]

    # ── Perceber ──────────────────────────────────────────────────────────────
    L += [
        "## Perceber",
        "",
        "[+PARAGRAPH]",
        "",
        perceber_frase,
        "",
        "[-PARAGRAPH]",
        "",
        "[+IMAGE_LABELED]",
        "",
        "@link_png@",
        "",
        "--",
        "",
        hotspot_coords,
        "",
        hotspot_legenda,
        "",
        "[-IMAGE_LABELED]",
        "",
    ]

    # ── Recordar ──────────────────────────────────────────────────────────────
    L += [
        "## Recordar",
        "",
        "[+PARAGRAPH]",
        "",
        "Ouça e repita a definição abaixo.",
        "",
        "[-PARAGRAPH]",
        "",
        "[+STATEMENT_D]",
        "",
        MP3_ABRIR,
        "",
        f"#FSH:{hash_audio}",
        "",
        definicao,
        "",
        MP3_FECHAR,
        "",
        definicao,
        "",
        "[-STATEMENT_D]",
        "",
        "[+HEADING]",
        "",
        "Hora de memorizar com música",
        "",
        "[-HEADING]",
        "",
        "[+PARAGRAPH]",
        "",
        "Clique abaixo para ouvir a música.",
        "",
        "[-PARAGRAPH]",
        "",
        "[+IMAGE_TEXT_ON]",
        "",
        "@link_png@",
        "",
        "@link_mp3@",
        "",
        musica,
        "",
        "[-IMAGE_TEXT_ON]",
        "",
    ]

    # ── Praticar ──────────────────────────────────────────────────────────────
    L += [
        "## Praticar",
        "",
        "[+HEADING]",
        "",
        "Atividade 1",
        "",
        "[-HEADING]",
        "",
        "[+PARAGRAPH]",
        "",
        "Complete a definição abaixo com a palavra correta.",
        "",
        "[-PARAGRAPH]",
        "",
        "[+FILL_IN]",
        "",
        fill_frase,
        "",
        fill_resposta,
        "",
        "[-FILL_IN]",
        "",
        "[+HEADING]",
        "",
        "Atividade 2",
        "",
        "[-HEADING]",
        "",
        "[+MULTIPLE]",
        "",
        multiple_pergunta,
        "",
    ]

    if ano == 1:
        # Ano 1: 2 opções (1 correta + 1 distrator)
        L.append(f"{multiple_correta} [=] true")
        if distratores:
            L.append(f"{distratores[0]} [=]")
    else:
        # Anos 2 e 3: 3 opções (1 correta + até 2 distratores)
        L.append(f"{multiple_correta} [=] true")
        for d in distratores[:2]:
            L.append(f"{d} [=]")

    L += [
        "",
        "[-MULTIPLE]",
        "",
        "[+HEADING]",
        "",
        "Atividade Extra",
        "",
        "[-HEADING]",
        "",
        "[+PARAGRAPH]",
        "",
        "Acesse o PDF abaixo e faça a atividade com atenção.",
        "",
        "[-PARAGRAPH]",
        "",
        "[+ACTIVITY_WORKSHEET]",
        "",
        f"INSTRUCTION={instrucao}",
        "",
        "[-ACTIVITY_WORKSHEET]",
        "",
    ]

    # ── Narrar ────────────────────────────────────────────────────────────────
    L += [
        "## Narrar",
        "",
        "[+HEADING]",
        "",
        "Leitura",
        "",
        "[-HEADING]",
        "",
    ]

    if ano == 3:
        # Ano 3: [+PARAGRAPH] com o texto + [+IMAGE] separado antes das perguntas
        L += [
            "[+PARAGRAPH]",
            "",
            f"**{definicao}**",
            "",
            paragrafo_bold,
            "",
            "[-PARAGRAPH]",
            "",
            "[+IMAGE]",
            "",
            "@link_png@",
            "",
            "[-IMAGE]",
            "",
        ]
    else:
        # Anos 1 e 2: [+IMAGE_TEXT_ASIDE] com áudio — espelho literal do Definir
        L += [
            "[+IMAGE_TEXT_ASIDE]",
            "",
            "@link_png@",
            "",
            MP3_ABRIR,
            "",
            f"#FSH:{hash_audio}",
            "",
            definicao,
            "",
            paragrafo_plain,
            "",
            MP3_FECHAR,
            "",
            f"**{definicao}**",
            "",
            paragrafo_bold,
            "",
            "[-IMAGE_TEXT_ASIDE]",
            "",
        ]

    L += [
        "[+HEADING]",
        "",
        "Pergunta",
        "",
        "[-HEADING]",
        "",
        "[+PARAGRAPH]",
        "",
        "Responda oralmente a pergunta abaixo sobre o texto.",
        "",
        "[-PARAGRAPH]",
        "",
        "[+LIST_NUMBERED]",
        "",
        narrar_pergunta,
        "",
        "[-LIST_NUMBERED]",
    ]

    return "\n".join(L) + "\n"


# ─────────────────────────────────────────────────────────────────────────────
# Gerador de revisão semanal (x.4)
# ─────────────────────────────────────────────────────────────────────────────

def gerar_revisao(config: dict, semana: dict) -> str:
    """
    Gera o conteúdo markdown da revisão semanal (x.4).
    As legendas do IMAGE_LABELED são copiadas automaticamente das aulas x.1, x.2 e x.3.
    """
    hash_audio = config.get("audio_hash", "0b12d715e4c741399594fccb12d4bbe2")
    definicao = semana["definicao_curta"]
    musica = semana["nome_musica"]
    revisao = semana["revisao"]

    # Legendas copiadas literalmente das aulas originais (regra editorial)
    legenda_x1 = semana["aulas"]["x1"]["perceber_hotspot_legenda"]
    legenda_x2 = semana["aulas"]["x2"]["perceber_hotspot_legenda"]
    legenda_x3 = semana["aulas"]["x3"]["perceber_hotspot_legenda"]

    fill_frase = revisao["fill_in_frase"]
    fill_resposta = revisao["fill_in_resposta"]
    multiples = revisao["multiples"]

    # Na revisão, a definição aparece com primeira letra minúscula (meio de frase)
    definicao_lower = primeira_minuscula(definicao)

    L = [
        "# Revisão",
        "",
        "## Definir",
        "",
        "[+PARAGRAPH]",
        "",
        f"Nesta semana estudamos que **{definicao_lower}**",
        "",
        "[-PARAGRAPH]",
        "",
        "[+HEADING]",
        "",
        "Atividade",
        "",
        "[-HEADING]",
        "",
        "[+IMAGE_TEXT_ON]",
        "",
        "@link_png@",
        "",
        "@link_mp3@",
        "",
        musica,
        "",
        "[-IMAGE_TEXT_ON]",
        "",
        "## Perceber",
        "",
        "[+PARAGRAPH]",
        "",
        "Observe as imagens que estudamos durante a semana.",
        "",
        "[-PARAGRAPH]",
        "",
        "[+HEADING]",
        "",
        "Atividade",
        "",
        "[-HEADING]",
        "",
        "[+IMAGE_LABELED]",
        "",
        "@link_png@",
        "",
        "--",
        "",
        "20 50",
        "",
        legenda_x1,       # cópia literal de x.1
        "",
        "--",
        "",
        "50 50",
        "",
        legenda_x2,       # cópia literal de x.2
        "",
        "--",
        "",
        "80 50",
        "",
        legenda_x3,       # cópia literal de x.3
        "",
        "[-IMAGE_LABELED]",
        "",
        "## Recordar",
        "",
        "[+PARAGRAPH]",
        "",
        "Recorde agora o fato aprendido durante a semana.",
        "",
        "[-PARAGRAPH]",
        "",
        "[+HEADING]",
        "",
        "Atividade",
        "",
        "[-HEADING]",
        "",
        "[+STATEMENT_D]",
        "",
        MP3_ABRIR,
        "",
        f"#FSH:{hash_audio}",
        "",
        definicao,
        "",
        MP3_FECHAR,
        "",
        definicao,
        "",
        "[-STATEMENT_D]",
        "",
        "## [QUIZ] Praticar",
        "",
        "[+FILL_IN]",
        "",
        fill_frase,
        "",
        fill_resposta,
        "",
        "[-FILL_IN]",
        "",
    ]

    # 3 perguntas de múltipla escolha (uma por aula)
    for m in multiples:
        pergunta = m["pergunta"]
        correta = m["resposta_correta"]
        distratores = m.get("distratores", [])

        L += [
            "[+MULTIPLE]",
            "",
            pergunta,
            "",
            f"{correta} [=] true",
        ]
        for d in distratores:
            L.append(f"{d} [=]")

        L += ["", "[-MULTIPLE]", ""]

    # Narrar
    L += [
        "## Narrar",
        "",
        "[+PARAGRAPH]",
        "",
        "Agora é hora de contar exatamente o fato que você aprendeu esta semana.",
        "",
        "[-PARAGRAPH]",
    ]

    return "\n".join(L) + "\n"


# ─────────────────────────────────────────────────────────────────────────────
# Validação do YAML
# ─────────────────────────────────────────────────────────────────────────────

CAMPOS_OBRIGATORIOS_AULA = [
    "titulo",
    "accordion_titulo",
    "paragrafo_plain",
    "palavras_negrito",
    "perceber_frase",
    "perceber_hotspot_coords",
    "perceber_hotspot_legenda",
    "fill_in_frase",
    "fill_in_resposta",
    "multiple_pergunta",
    "multiple_resposta_correta",
    "multiple_distratores",
    "atividade_instrucao",
    "narrar_pergunta",
]


def validar(data: dict) -> list:
    """Retorna lista de erros de validação. Lista vazia = dados válidos."""
    erros = []

    if "config" not in data:
        erros.append("'config' ausente no YAML.")
    if "semana" not in data:
        erros.append("'semana' ausente no YAML.")
        return erros

    semana = data["semana"]
    for campo in ["numero", "definicao_curta", "nome_musica", "aulas", "revisao"]:
        if campo not in semana:
            erros.append(f"'semana.{campo}' ausente.")

    for chave in ["x1", "x2", "x3"]:
        if chave not in semana.get("aulas", {}):
            erros.append(f"Aula '{chave}' ausente em 'semana.aulas'.")
            continue
        aula = semana["aulas"][chave]
        for campo in CAMPOS_OBRIGATORIOS_AULA:
            if campo not in aula:
                erros.append(f"'{campo}' ausente em 'semana.aulas.{chave}'.")

    revisao = semana.get("revisao", {})
    for campo in ["fill_in_frase", "fill_in_resposta", "multiples"]:
        if campo not in revisao:
            erros.append(f"'revisao.{campo}' ausente.")

    n_multiples = len(revisao.get("multiples", []))
    if n_multiples != 3:
        erros.append(
            f"'revisao.multiples' deve ter exatamente 3 itens (um por aula). "
            f"Encontrado: {n_multiples}."
        )

    return erros


# ─────────────────────────────────────────────────────────────────────────────
# YAML de exemplo
# ─────────────────────────────────────────────────────────────────────────────

EXEMPLO_YAML = """\
# ──────────────────────────────────────────────────────────────────────────────
# ARQUIVO DE DADOS DA SEMANA — Trivium Method Editorial
# Gerado com: python generate_lessons.py --exemplo
#
# Instrução de uso:
#   1. Copie este arquivo e renomeie: dados_semana3.yaml
#   2. Preencha todos os campos com o conteúdo da semana
#   3. Execute: python generate_lessons.py dados_semana3.yaml
#
# O script gera automaticamente:
#   - 3.1.md, 3.2.md, 3.3.md  (aulas regulares)
#   - 3.4.md                   (revisão semanal)
#
# As legendas do IMAGE_LABELED da revisão são copiadas das aulas x.1, x.2, x.3.
# ──────────────────────────────────────────────────────────────────────────────

config:
  ano: 1                                           # 1, 2 ou 3
  audio_hash: "0b12d715e4c741399594fccb12d4bbe2"  # hash FSH — mesmo para todas as aulas da semana
  diretorio_saida: "./output_semana3"              # pasta onde os arquivos .md serão salvos

semana:
  numero: 3
  definicao_curta: "O ponto representa o começo de uma obra de arte."
  nome_musica: "O ponto começa a arte"

  # ── Aulas da semana ────────────────────────────────────────────────────────
  aulas:

    # x.1 — Coração da semana: define o TERMO central e a definição
    # Negrito: somente o TERMO
    x1:
      titulo: "O ponto no desenho"
      accordion_titulo: "O ponto começa a arte"
      paragrafo_plain: "Você observa pontos na obra de arte e percebe como um pequeno sinal pode começar uma imagem."
      palavras_negrito:
        - "pontos"
      perceber_frase: "Observe a imagem e veja como um ponto pode iniciar uma obra de arte simples."
      perceber_hotspot_coords: "40 45"
      perceber_hotspot_legenda: "Obra de arte com pontos"
      fill_in_frase: "O _____ representa o começo de uma obra de arte."
      fill_in_resposta: "ponto"
      multiple_pergunta: "O que o ponto representa?"
      multiple_resposta_correta: "O começo de uma obra de arte."
      multiple_distratores:
        - "Apenas manchas sem forma."          # ano 1: 1 distrator; ano 2+: até 2
      atividade_instrucao: "Faça uma imagem simples começando com um ponto e observe como a obra de arte nasce desse sinal."
      narrar_pergunta: "O que o ponto representa?"

    # x.2 — Subtópico 1: desdobramento do tema de x.1
    # Negrito: TERMO + KW2 (= resposta do fill-in)
    x2:
      titulo: "O ponto como começo"
      accordion_titulo: "O ponto como começo"
      paragrafo_plain: "Você aprende que o ponto pode ser o começo de uma obra de arte, porque toda imagem nasce de um pequeno sinal."
      palavras_negrito:
        - "ponto"
        - "começo"
      perceber_frase: "Observe a imagem e veja como um ponto pode ser o começo de uma obra de arte."
      perceber_hotspot_coords: "45 45"
      perceber_hotspot_legenda: "Ponto como começo"
      fill_in_frase: "O ponto representa o _____ de uma obra de arte."
      fill_in_resposta: "começo"
      multiple_pergunta: "O que o ponto pode ser em uma obra de arte?"
      multiple_resposta_correta: "O começo de uma obra de arte."
      multiple_distratores:
        - "O fim de toda imagem."
      atividade_instrucao: "Comece um desenho com pontos e depois observe como a imagem aparece com ordem."
      narrar_pergunta: "O que o ponto pode ser em uma obra de arte?"

    # x.3 — Subtópico 2: fecha a progressão da semana
    # Negrito: TERMO + KW3 (= resposta do fill-in)
    x3:
      titulo: "O ponto como padrão"
      accordion_titulo: "O ponto na obra de arte"
      paragrafo_plain: "Você usa o ponto na obra de arte para marcar lugares, criar detalhes e organizar a imagem com cuidado."
      palavras_negrito:
        - "ponto"
        - "obra de arte"
      perceber_frase: "Observe a imagem e veja o ponto marcando partes da obra de arte com cuidado."
      perceber_hotspot_coords: "50 45"
      perceber_hotspot_legenda: "Ponto na obra de arte"
      fill_in_frase: "O ponto representa o começo de uma _____."
      fill_in_resposta: "obra de arte"
      multiple_pergunta: "Para que você usa o ponto na obra de arte?"
      multiple_resposta_correta: "Para marcar lugares e criar detalhes."
      multiple_distratores:
        - "Para apagar toda a imagem."
      atividade_instrucao: "Marque lugares com pontos em uma obra de arte e organize a imagem com cuidado."
      narrar_pergunta: "Para que você usa o ponto na obra de arte?"

  # ── Revisão semanal (x.4) ──────────────────────────────────────────────────
  # As legendas do IMAGE_LABELED são copiadas automaticamente de x.1, x.2, x.3.
  # As 3 perguntas devem cobrir um ângulo de cada aula da semana.
  revisao:
    fill_in_frase: "O ponto representa o começo de uma _____."
    fill_in_resposta: "obra de arte"
    multiples:
      - pergunta: "O que o ponto representa?"                     # ângulo de x.1
        resposta_correta: "O começo de uma obra de arte."
        distratores:
          - "Apenas rabiscos sem cuidado."
          - "Somente linhas apagadas."
      - pergunta: "O que o ponto pode ser em uma obra de arte?"   # ângulo de x.2
        resposta_correta: "O começo de uma obra de arte."
        distratores:
          - "Apenas um erro no papel."
          - "Somente o fim da imagem."
      - pergunta: "Para que você usa o ponto na obra de arte?"    # ângulo de x.3
        resposta_correta: "Para marcar lugares e criar detalhes."
        distratores:
          - "Para esconder toda a imagem."
          - "Para tirar a ordem do desenho."
"""


# ─────────────────────────────────────────────────────────────────────────────
# CLI principal
# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Gera aulas no padrão Trivium Method Editorial a partir de um arquivo YAML.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemplos:\n"
            "  python generate_lessons.py dados_semana3.yaml\n"
            "  python generate_lessons.py dados_semana3.yaml --apenas x1\n"
            "  python generate_lessons.py dados_semana3.yaml --saida ./output\n"
            "  python generate_lessons.py --exemplo > dados_semana_exemplo.yaml\n"
        ),
    )
    parser.add_argument(
        "arquivo_yaml",
        nargs="?",
        help="Arquivo YAML com os dados da semana.",
    )
    parser.add_argument(
        "--apenas",
        choices=["x1", "x2", "x3", "revisao", "todas"],
        default="todas",
        help="Gerar apenas uma aula específica (padrão: todas).",
    )
    parser.add_argument(
        "--saida",
        help="Sobrescreve o diretório de saída definido no YAML.",
    )
    parser.add_argument(
        "--exemplo",
        action="store_true",
        help="Imprime um arquivo YAML de exemplo preenchido e sai.",
    )
    args = parser.parse_args()

    if args.exemplo:
        print(EXEMPLO_YAML, end="")
        return

    if not args.arquivo_yaml:
        parser.print_help()
        sys.exit(1)

    # ── Carrega o YAML ────────────────────────────────────────────────────────
    caminho_yaml = Path(args.arquivo_yaml)
    if not caminho_yaml.exists():
        print(f"Erro: arquivo '{caminho_yaml}' não encontrado.")
        sys.exit(1)

    with open(caminho_yaml, encoding="utf-8") as f:
        data = yaml.safe_load(f)

    # ── Valida ────────────────────────────────────────────────────────────────
    erros = validar(data)
    if erros:
        print(f"Erros encontrados em '{caminho_yaml}':")
        for e in erros:
            print(f"  • {e}")
        sys.exit(1)

    config = data["config"]
    semana = data["semana"]
    numero = semana["numero"]

    # ── Diretório de saída ────────────────────────────────────────────────────
    dir_saida_str = args.saida or config.get("diretorio_saida", f"./output_semana{numero}")
    dir_saida = Path(dir_saida_str)
    dir_saida.mkdir(parents=True, exist_ok=True)

    # ── Mapa de geradores ─────────────────────────────────────────────────────
    geradores = {
        "x1":      (f"{numero}.1.md",  lambda: gerar_aula(config, semana, "x1")),
        "x2":      (f"{numero}.2.md",  lambda: gerar_aula(config, semana, "x2")),
        "x3":      (f"{numero}.3.md",  lambda: gerar_aula(config, semana, "x3")),
        "revisao": (f"{numero}.4.md",  lambda: gerar_revisao(config, semana)),
    }

    alvos = ["x1", "x2", "x3", "revisao"] if args.apenas == "todas" else [args.apenas]

    print(f"Gerando semana {numero} — {semana['definicao_curta']}")
    print(f"Destino: {dir_saida.resolve()}\n")

    for alvo in alvos:
        nome_arquivo, gerar = geradores[alvo]
        conteudo = gerar()
        caminho = dir_saida / nome_arquivo
        caminho.write_text(conteudo, encoding="utf-8")
        print(f"  ✓ {nome_arquivo}")

    print(f"\n{len(alvos)} arquivo(s) gerado(s).")


if __name__ == "__main__":
    main()
