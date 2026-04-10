import os
import subprocess
import json

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

# GraphQL query to get project items and their status
query = """
query {
  node(id: "PVT_kwDODLv1ac4BH1XW") {
    ... on ProjectV2 {
      items(first: 100) {
        nodes {
          content {
            ... on Issue {
              number
              title
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

cmd = ["gh", "api", "graphql", "-f", f"query={query}"]
try:
    res = subprocess.check_output(cmd, env=os.environ).decode()
    data = json.loads(res)
    items = data['data']['node']['items']['nodes']
    
    backlog_items = []
    for item in items:
        if not item.get('content') or 'number' not in item['content']:
            continue
            
        status = None
        for fv in item['fieldValues']['nodes']:
            if not fv: continue
            if 'field' in fv and fv['field'] and fv['field'].get('name') == 'Status':
                status = fv.get('name')
                
        if status == 'Backlog':
            backlog_items.append({
                'number': item['content']['number'],
                'title': item['content']['title']
            })
            
    # Sort by number to see the sequence
    backlog_items.sort(key=lambda x: x['number'])
    print(f"Found {len(backlog_items)} Backlog items in the first 100 project items.")
    for b in backlog_items[:15]:
        print(f"#{b['number']}: {b['title']}")
except subprocess.CalledProcessError as e:
    print(f"Error: {e.output}")
