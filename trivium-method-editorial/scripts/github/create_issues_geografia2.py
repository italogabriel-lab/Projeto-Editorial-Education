#!/usr/bin/env python3
"""
Cria tickets de [Geografia] - Ano 2 no GitHub Projects (Kanban Bibline Aulas).

Lê o arquivo de referência geografia-2-ano-tickets.md e cria cada ticket como
issue no repositório bibline/curriculum, adicionando ao Project e configurando
o status como Backlog.

Token: GITHUB_TOKEN_CLASSIC_KANBAN_BIBLINE_AULAS (User: Italo-bibline)

Uso:
    python3 create_issues_geografia2.py           # dry-run (só lista os tickets)
    python3 create_issues_geografia2.py --apply   # cria os tickets no GitHub
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path


# ─── Configurações ────────────────────────────────────────────────────────────

ROOT = Path(__file__).resolve().parents[3]
ENV_PATH = ROOT / ".env"

REFERENCE_FILE = (
    ROOT
    / "Projeto - Bibline Academy ( Produção de Aulas)"
    / "Criação de tickets Equipe - Kanban Github"
    / "Em-Progresso"
    / "geografia-2-ano-tickets.md"
)

TOKEN_NAME    = "GITHUB_TOKEN_CLASSIC_KANBAN_BIBLINE_AULAS"
REPO          = "bibline/curriculum"
PROJECT_ID    = "PVT_kwDODLv1ac4BH1XW"
STATUS_FIELD  = "PVTSSF_lADODLv1ac4BH1XWzg4eN1w"
BACKLOG_OPT   = "f75ad846"
ASSIGNEE      = "Decioayres"
SLEEP_BETWEEN = 1.2   # segundos entre criações


# ─── Carrega token ────────────────────────────────────────────────────────────

def load_token() -> str:
    if not ENV_PATH.exists():
        raise SystemExit(f"❌ Arquivo .env não encontrado: {ENV_PATH}")
    for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
        if line.startswith(f"{TOKEN_NAME}="):
            token = line.split("=", 1)[1].strip()
            if token:
                return token
    raise SystemExit(f"❌ Token {TOKEN_NAME} não encontrado em {ENV_PATH}")


# ─── Parsing do arquivo de referência ────────────────────────────────────────

def parse_tickets() -> list[tuple[str, str]]:
    """
    Retorna lista de (title, body) lendo o arquivo de referência.

    Cada bloco tem a forma:
        [Geografia] - Ano 2 - XX.X Título (update)

        # Description

        Texto da descrição.

        ---
    """
    if not REFERENCE_FILE.exists():
        raise SystemExit(f"❌ Arquivo de referência não encontrado:\n  {REFERENCE_FILE}")

    content = REFERENCE_FILE.read_text(encoding="utf-8")

    # Extrai blocos separados por ---
    blocks = content.split("\n---\n")

    ticket_re = re.compile(
        r"^\[Geografia\] - Ano 2 - (.+?)\n\n# Description\n\n(.+?)$",
        re.DOTALL,
    )

    tickets: list[tuple[str, str]] = []
    for block in blocks:
        block = block.strip()
        m = ticket_re.match(block)
        if m:
            id_title    = m.group(1).strip()
            description = m.group(2).strip()
            full_title  = f"[Geografia] - Ano 2 - {id_title}"
            body        = f"# Description\n\n{description}"
            tickets.append((full_title, body))

    return tickets


# ─── Chamadas à API do GitHub via gh CLI ─────────────────────────────────────

def gh_api(path: str, method: str, payload: dict, env: dict) -> dict | None:
    """Chama a REST API do GitHub via gh CLI com payload JSON."""
    cmd = ["gh", "api", path, "-X", method, "--input", "-"]
    result = subprocess.run(
        cmd,
        input=json.dumps(payload),
        text=True,
        capture_output=True,
        env=env,
        check=False,
    )
    if result.returncode != 0:
        print(f"    ✗ REST API error [{path}]: {result.stderr.strip()}")
        return None
    return json.loads(result.stdout) if result.stdout.strip() else {}


def gh_graphql(query: str, variables: dict, env: dict) -> dict | None:
    """Chama a GraphQL API do GitHub via gh CLI."""
    cmd = ["gh", "api", "graphql", "-f", f"query={query}"]
    for k, v in variables.items():
        cmd.extend(["-F", f"{k}={v}"])
    result = subprocess.run(
        cmd,
        text=True,
        capture_output=True,
        env=env,
        check=False,
    )
    if result.returncode != 0:
        print(f"    ✗ GraphQL error: {result.stderr.strip()}")
        return None
    data = json.loads(result.stdout) if result.stdout.strip() else {}
    if "errors" in data:
        for err in data["errors"]:
            print(f"    ✗ GraphQL: {err.get('message')}")
        return None
    return data


# ─── Fluxo de criação de um ticket ───────────────────────────────────────────

def create_ticket(title: str, body: str, env: dict) -> bool:
    """Cria a issue, adiciona ao Project e define status Backlog. Retorna True se OK."""

    # 1. Cria a issue no repositório
    issue = gh_api(
        f"repos/{REPO}/issues",
        "POST",
        {"title": title, "body": body, "assignees": [ASSIGNEE]},
        env,
    )
    if not issue or "node_id" not in issue:
        print("    ✗ Falha ao criar a issue.")
        return False

    node_id      = issue["node_id"]
    issue_number = issue["number"]

    # 2. Adiciona ao Project
    add_res = gh_graphql(
        """
        mutation($project: ID!, $issue: ID!) {
          addProjectV2ItemById(input: {projectId: $project, contentId: $issue}) {
            item { id }
          }
        }
        """,
        {"project": PROJECT_ID, "issue": node_id},
        env,
    )
    if not add_res or not add_res.get("data", {}).get("addProjectV2ItemById"):
        print(f"    ✗ Issue #{issue_number} criada mas não adicionada ao Project.")
        return False

    item_id = add_res["data"]["addProjectV2ItemById"]["item"]["id"]

    # 3. Define status = Backlog
    status_res = gh_graphql(
        """
        mutation($project: ID!, $item: ID!, $field: ID!, $value: String!) {
          updateProjectV2ItemFieldValue(input: {
            projectId: $project,
            itemId: $item,
            fieldId: $field,
            value: { singleSelectOptionId: $value }
          }) {
            projectV2Item { id }
          }
        }
        """,
        {
            "project": PROJECT_ID,
            "item":    item_id,
            "field":   STATUS_FIELD,
            "value":   BACKLOG_OPT,
        },
        env,
    )
    if not status_res:
        print(f"    ⚠ Issue #{issue_number} no Project, mas status não definido.")
        return False

    print(f"    ✓ #{issue_number} → Backlog")
    return True


# ─── Main ─────────────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Cria tickets de Geografia 2º Ano no Kanban Bibline."
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Executa a criação real dos tickets no GitHub (sem este flag = dry-run).",
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=SLEEP_BETWEEN,
        help=f"Pausa (segundos) entre criações. Padrão: {SLEEP_BETWEEN}",
    )
    args = parser.parse_args()

    # Carrega token
    token = load_token()
    env   = os.environ.copy()
    env["GITHUB_TOKEN"] = token
    print(f"🔑 Token carregado: {TOKEN_NAME[:6]}...{token[-4:]}")
    print(f"👤 Assignee: {ASSIGNEE}")
    print(f"📁 Repositório: {REPO}")
    print(f"📋 Arquivo de referência:\n   {REFERENCE_FILE}\n")

    # Lê tickets do arquivo de referência
    tickets = parse_tickets()
    print(f"📌 {len(tickets)} tickets encontrados no arquivo de referência.\n")

    for i, (title, _) in enumerate(tickets, 1):
        print(f"  [{i:03}/{len(tickets)}] {title}")

    print()

    if not args.apply:
        print("ℹ️  Modo dry-run — nenhum ticket criado.")
        print("   Execute com --apply para criar os tickets no GitHub.\n")
        return 0

    # Cria os tickets
    print("🚀 Iniciando criação dos tickets...\n")
    succeeded = 0
    failed: list[str] = []

    for i, (title, body) in enumerate(tickets, 1):
        print(f"[{i:03}/{len(tickets)}] {title}")
        ok = create_ticket(title, body, env)
        if ok:
            succeeded += 1
        else:
            failed.append(title)
        time.sleep(args.sleep)

    # Relatório final
    print(f"\n{'='*60}")
    print(f"✅ Criados com sucesso: {succeeded}/{len(tickets)}")
    if failed:
        print(f"❌ Falhas ({len(failed)}):")
        for t in failed:
            print(f"   - {t}")
    print("="*60)

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
