import os
import re
import subprocess
import json
import time

env_token = ""
env_path = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto Bibline Academy/.env"
try:
    with open(env_path) as f:
        for line in f:
            if line.startswith("GITHUB_TOKEN="):
                env_token = line.split("=", 1)[1].strip()
except Exception:
    pass

if env_token:
    os.environ["GITHUB_TOKEN"] = env_token

def run_graphql(query, variables=None):
    cmd = ["gh", "api", "graphql"]
    if variables:
        cmd.extend(["-f", f"query={query}", "-F", f"variables={json.dumps(variables)}"])
    else:
        cmd.extend(["-f", f"query={query}"])
        
    for attempt in range(3):
        try:
            res = subprocess.check_output(cmd, env=os.environ, stderr=subprocess.STDOUT).decode()
            return json.loads(res) if res else {}
        except subprocess.CalledProcessError as e:
            print(f"GraphQL Error on attempt {attempt+1}: {e.output.decode()}")
            time.sleep(2)
    return {}

def run_gh_api(path, method="GET", fields=None):
    cmd = ["gh", "api", path, "-X", method]
    if fields:
        for k, v in fields.items():
            if isinstance(v, list):
                for item in v:
                    cmd.extend(["-f", f"{k}[]={item}"])
            else:
                cmd.extend(["-f", f"{k}={v}"])
    
    for attempt in range(3):
        try:
            res = subprocess.check_output(cmd, env=os.environ, stderr=subprocess.STDOUT).decode()
            return json.loads(res) if res else {}
        except subprocess.CalledProcessError as e:
            print(f"REST API Error {path} on attempt {attempt+1}: {e.output.decode()}")
            time.sleep(2)
    return None

query = """
query($cursor: String) {
  node(id: "PVT_kwDODLv1ac4BH1XW") {
    ... on ProjectV2 {
      items(first: 100, after: $cursor) {
        nodes {
          content {
            ... on Issue {
              id
              number
              title
              repository {
                nameWithOwner
              }
            }
          }
          fieldValues(first: 20) {
            nodes {
              ... on ProjectV2ItemFieldSingleSelectValue {
                name
                field {
                  ... on ProjectV2SingleSelectField {
                    name
                  }
                }
              }
            }
          }
        }
        pageInfo {
          hasNextPage
          endCursor
        }
      }
    }
  }
}
"""

all_backlog_issues = []
cursor = None
print("Fetching project items from GitHub...")
while True:
    data = run_graphql(query, {"cursor": cursor} if cursor else None)
    project = data.get('data', {}).get('node', {})
    if not project:
        print("Failed to get project node data. Exiting pagination.")
        break
    items_conn = project.get('items', {})
    nodes = items_conn.get('nodes', [])
    
    for item in nodes:
        if not item or not item.get('content') or 'number' not in item['content']:
            continue
            
        issue_node = item['content']
        status = None
        for fv in item.get('fieldValues', {}).get('nodes', []):
            if not fv: continue
            if 'field' in fv and fv['field'] and fv['field'].get('name') == 'Status':
                status = fv.get('name')
                
        if status == 'Backlog':
            t = issue_node.get('title', '')
            # Match titles explicitly
            if t.startswith("[Belas artes] - Ano 1 "):
                all_backlog_issues.append({
                    'id': issue_node['id'],
                    'number': issue_node['number'],
                    'title': t,
                    'repo': issue_node['repository']['nameWithOwner']
                })
                
    page_info = items_conn.get('pageInfo', {})
    if page_info.get('hasNextPage'):
        cursor = page_info.get('endCursor')
        print(f"Fetched page, fetching next with cursor {cursor}...")
    else:
        break

print(f"\nTotal Ano 1 Backlog issues found: {len(all_backlog_issues)}")
all_backlog_issues.sort(key=lambda x: x['number'])

tickets_file = "/home/italo.gabriel/Documents/Developer/Projeto-Editorial-Education/Projeto Bibline Academy/Belas Artes - Fase da Gramática/1 Fase - Gramática/1º Ano/Estrutura Curricular - 1º ANO/6 - Descrições para tickets - 1º ANO.md"
with open(tickets_file, 'r', encoding='utf-8') as f:
    content = f.read()

blocks = re.split(r'\[Belas artes\] - Ano 1 - ', content)
target_tickets = []
for block in blocks[1:]:
    lines = block.strip().split('\n')
    title = "[Belas artes] - Ano 1 - " + lines[0].strip()
    
    desc = []
    for line in lines[1:]:
        if line.strip() == "---":
            break
        desc.append(line)
        
    description = "\n".join(desc).strip()
    if description.startswith("# Description"):
        description = description[len("# Description"):].strip()
        
    target_tickets.append({"title": title, "body": description})

print(f"Total target tickets parsed: {len(target_tickets)}")

# The user wants to start from issue #1957 which should map to the very first target ticket
start_idx = -1
for i, issue in enumerate(all_backlog_issues):
    if issue['number'] == 1957:
        start_idx = i
        break

if start_idx == -1:
    print("WARNING: Could not find issue #1957 in the Backlog!")
    print("Found issues:")
    for isr in all_backlog_issues[:5]:
        print(isr)
    print("Will try to find any issue that ends with 'Revisão do 1º Bimestre'...")
    for i, issue in enumerate(all_backlog_issues):
        if "Revisão do 1º Bimestre" in issue['title']:
            start_idx = i
            print(f"Found issue #{issue['number']} matching 'Revisão do 1º Bimestre'. Starting from there.")
            break

if start_idx == -1:
    print("Still could not find the starting issue. Using the very first Backlog Ano 1 issue found.")
    start_idx = 0

issues_to_update = all_backlog_issues[start_idx:]
num_updates = min(len(issues_to_update), len(target_tickets))

print(f"Will update {num_updates} issues starting from #{issues_to_update[0]['number']}.")
print("Preview of first 3 updates:")
for i in range(min(3, num_updates)):
    ex = issues_to_update[i]
    tg = target_tickets[i]
    print(f"#{ex['number']} ('{ex['title']}') -> '{tg['title']}'")

print("\nExecuting updates now...")
for i in range(num_updates):
    existing = issues_to_update[i]
    target = target_tickets[i]
    
    run_gh_api(f"repos/{existing['repo']}/issues/{existing['number']}", method="PATCH", fields={
        "title": target['title'],
        "body": target['body']
    })
    print(f"Updated #{existing['number']} to: {target['title']}")
    time.sleep(1.5)

print("All updates applied successfully.")
