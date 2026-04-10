import os
import re
import subprocess
import json
import time

PROJECT_ID = "PVT_kwDODLv1ac4BH1XW"
STATUS_FIELD_ID = "PVTSSF_lADODLv1ac4BH1XWzg4eN1w"
BACKLOG_OPTION_ID = "f75ad846"
ASSIGNEE = "Italo-bibline"
REPO = "bibline/curriculum"

env_token = ""
env_path = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto Bibline Academy/.env"
try:
    with open(env_path) as f:
        for line in f:
            if line.startswith("GITHUB_TOKEN="):
                env_token = line.split("=", 1)[1].strip()
except Exception as e:
    print(f"Did not find token at {env_path}")
    
if env_token:
    os.environ["GITHUB_TOKEN"] = env_token

titles = {}
macro_path = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto Bibline Academy/Belas Artes - Fase da Gramática/1 Fase - Gramática/3º Ano - ARTE CRISTÃ ORIENTAL ATÉ O RENASCIMENTO DO NORTE/Estrutura Curricular - 3º ANO/1 - Curriculo Macro - Arte Cristã Oriental até o Renascimento do Norte - 3º ANO.md"

with open(macro_path) as f:
    current_week = 0
    for line in f:
        w_match = re.match(r"^## Semana (\d+)", line)
        if w_match:
            current_week = int(w_match.group(1))
        
        d_match = re.search(r"- Dia (\d):\s+(.*)", line)
        if d_match and current_week >= 11:
            dia = int(d_match.group(1))
            raw_title = d_match.group(2).replace('✅', '').strip()
            raw_title = raw_title.replace('"', '').strip()
            titles[f"{current_week}.{dia}"] = raw_title

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
        res = subprocess.check_output(cmd, env=os.environ).decode()
        return json.loads(res) if res else {}
    except subprocess.CalledProcessError as e:
        print(f"Error calling API {path}: {e.output}")
        return None

def run_graphql(query, variables=None):
    cmd = ["gh", "api", "graphql", "-f", f"query={query}"]
    if variables:
        for k, v in variables.items():
             cmd.extend(["-F", f"{k}={v}"])
    try:
        res = subprocess.check_output(cmd, env=os.environ).decode()
        return json.loads(res) if res else {}
    except subprocess.CalledProcessError as e:
        print(f"Error calling GraphQL: {e.output}")
        return None

items_processed = 0
for week_day, title in titles.items():
    items_processed += 1
    issue_title = f"[Belas artes] - Ano 3 - {week_day} {title}"
    print(f"[{items_processed}/{len(titles)}] Creating issue: {issue_title}")
    
    issue_data = run_gh_api(f"repos/{REPO}/issues", method="POST", fields={
        "title": issue_title,
        "assignees": [ASSIGNEE]
    })
    
    if not issue_data or "node_id" not in issue_data:
        print(f"Failed to create issue {week_day}")
        continue
    
    issue_node_id = issue_data["node_id"]
    issue_number = issue_data["number"]
    
    query_add = """
    mutation($project: ID!, $issue: ID!) {
      addProjectV2ItemById(input: {projectId: $project, contentId: $issue}) {
        item { id }
      }
    }
    """
    add_res = run_graphql(query_add, variables={"project": PROJECT_ID, "issue": issue_node_id})
    if not add_res or "data" not in add_res or "errors" in add_res:
        print(f"Failed to add item to project for issue {issue_number}")
        continue
    
    item_node_id = add_res["data"]["addProjectV2ItemById"]["item"]["id"]
    
    query_status = """
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
    """
    status_res = run_graphql(query_status, variables={
        "project": PROJECT_ID, "item": item_node_id, "field": STATUS_FIELD_ID, "value": BACKLOG_OPTION_ID
    })
    
    print(f"Successfully configured: {issue_title}")
    time.sleep(1.5)

print("Finished processing all issues.")
