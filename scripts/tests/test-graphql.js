const fs = require('fs');

let token = '';
try {
  const envFile = fs.readFileSync('Projeto Bibline Academy/.env', 'utf8');
  const match = envFile.match(/GITHUB_TOKEN=([^\n\r]+)/);
  if (match) token = match[1];
} catch (e) { console.log(e); }

async function run() {
  const query = `
  query {
    node(id: "PVT_kwDODLv1ac4BH1XW") {
      ... on ProjectV2 {
        items(first: 100) {
          nodes {
            content {
              ... on Issue {
                title
              }
            }
            fieldValues(first: 20) {
              nodes {
                __typename
                ... on ProjectV2ItemFieldSingleSelectValue {
                  name
                  field { ... on ProjectV2SingleSelectField { name } }
                }
                ... on ProjectV2ItemFieldTextValue {
                  text
                  field { ... on ProjectV2FieldCommon { name } }
                }
                ... on ProjectV2ItemFieldIterationValue {
                  title
                  field { ... on ProjectV2IterationField { name } }
                }
              }
            }
          }
        }
      }
    }
  }
  `;

  const res = await fetch('https://api.github.com/graphql', {
    method: 'POST',
    headers: {
      'Authorization': `bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ query })
  });
  
  const data = await res.json();
  fs.writeFileSync('graphql_out.json', JSON.stringify(data, null, 2));
  console.log('Saved to graphql_out.json');
}

run();
