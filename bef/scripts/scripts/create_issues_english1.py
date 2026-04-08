import os
import re
import subprocess
import json
import time

PROJECT_ID = "PVT_kwDODLv1ac4BH1XW"
STATUS_FIELD_ID = "PVTSSF_lADODLv1ac4BH1XWzg4eN1w"
BACKLOG_OPTION_ID = "f75ad846"
ASSIGNEE = "egriffinpfg"
REPO = "bibline/curriculum"

env_path = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto Bibline Academy/.env"
env_token = ""
try:
    with open(env_path) as f:
        for line in f:
            if line.startswith("GITHUB_TOKEN_CLASSI="):
                env_token = line.split("=", 1)[1].strip()
except Exception as e:
    print(f"Could not read token: {e}")

if not env_token:
    raise SystemExit("Token GITHUB_TOKEN_CLASSI not found in .env")

os.environ["GITHUB_TOKEN"] = env_token

md_path = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto Bibline Academy/Belas Artes - Fase da Gramática/0-Descrições e criação de tickets para as disciplinas/Em-Progresso/english-1-year.md"

tickets = []
with open(md_path) as f:
    content = f.read()

blocks = content.split("\n---\n")
ticket_re = re.compile(r"^\[English\] - Year 1 - (.+?)\n\n# Description\n\n(.+?)$", re.DOTALL)

for block in blocks:
    block = block.strip()
    m = ticket_re.match(block)
    if m:
        ticket_id_title = m.group(1).strip()
        description = m.group(2).strip()
        full_title = f"[English] - Year 1 - {ticket_id_title}"
        tickets.append((full_title, description))

print(f"Found {len(tickets)} tickets to create.\n")

def run_gh_api(path, method="POST", fields=None):
    cmd = ["gh", "api", path, "-X", method]
    if fields:
        for k, v in fields.items():
            if isinstance(v, list):
                for item in v:
                    cmd.extend(["-f", f"{k}[]={item}"])
            else:
                cmd.extend(["-f", f"{k}={v}"])
    try:
        res = subprocess.check_output(cmd, env=os.environ, stderr=subprocess.PIPE).decode()
        return json.loads(res) if res else {}
    except subprocess.CalledProcessError as e:
        print(f"API error {path}: {e.stderr.decode()}")
        return None

def run_graphql(query, variables=None):
    cmd = ["gh", "api", "graphql", "-f", f"query={query}"]
    if variables:
        for k, v in variables.items():
            cmd.extend(["-F", f"{k}={v}"])
    try:
        res = subprocess.check_output(cmd, env=os.environ, stderr=subprocess.PIPE).decode()
        return json.loads(res) if res else {}
    except subprocess.CalledProcessError as e:
        print(f"GraphQL error: {e.stderr.decode()}")
        return None

failed = []
for i, (title, description) in enumerate(tickets, 1):
    print(f"[{i}/{len(tickets)}] {title}")

    issue_data = run_gh_api(f"repos/{REPO}/issues", method="POST", fields={
        "title": title,
        "body": description,
        "assignees": [ASSIGNEE],
    })

    if not issue_data or "node_id" not in issue_data:
        print(f"  ✗ Failed to create issue")
        failed.append(title)
        continue

    issue_node_id = issue_data["node_id"]
    issue_number = issue_data["number"]

    add_res = run_graphql("""
    mutation($project: ID!, $issue: ID!) {
      addProjectV2ItemById(input: {projectId: $project, contentId: $issue}) {
        item { id }
      }
    }
    """, variables={"project": PROJECT_ID, "issue": issue_node_id})

    if not add_res or "errors" in add_res or not add_res.get("data", {}).get("addProjectV2ItemById"):
        print(f"  ✗ Created issue #{issue_number} but failed to add to project")
        failed.append(title)
        continue

    item_node_id = add_res["data"]["addProjectV2ItemById"]["item"]["id"]

    run_graphql("""
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
    """, variables={
        "project": PROJECT_ID,
        "item": item_node_id,
        "field": STATUS_FIELD_ID,
        "value": BACKLOG_OPTION_ID,
    })

    print(f"  ✓ #{issue_number} — Backlog")
    time.sleep(1.2)

print(f"\nDone. {len(tickets) - len(failed)}/{len(tickets)} tickets created successfully.")
if failed:
    print(f"\nFailed ({len(failed)}):")
    for t in failed:
        print(f"  - {t}")
