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
        fields(first: 50) {
          nodes {
            __typename
            ... on ProjectV2FieldCommon { name }
            ... on ProjectV2SingleSelectField {
              name
              options { name }
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
  fs.writeFileSync('graphql_fields.json', JSON.stringify(data, null, 2));
  console.log('Saved to graphql_fields.json');
}

run();
