const fs = require('fs');
const path = require('path');

// Performance tracking
const startTime = Date.now();

// PAT_TOKEN tem prioridade pois o GITHUB_TOKEN padrão do Actions
// não tem permissão para acessar GitHub Projects (ProjectV2) via GraphQL
let GITHUB_TOKEN =
  process.env.TRIVIUMOS_GITHUB_TOKEN ||
  process.env.PAT_TOKEN ||
  process.env.GITHUB_TOKEN_CLASSIC ||
  process.env.GITHUB_TOKEN_FINE ||
  process.env.GITHUB_TOKEN;

function tryReadTokenFromEnvFile(envPath) {
  try {
    const envFile = fs.readFileSync(envPath, 'utf8');
    const tokenMatch =
      envFile.match(/TRIVIUMOS_GITHUB_TOKEN=(.*)/) ||
      envFile.match(/GITHUB_TOKEN=(.*)/);

    if (tokenMatch) {
      return tokenMatch[1].trim();
    }
  } catch (error) {
    return null;
  }

  return null;
}

if (!GITHUB_TOKEN) {
  const candidateEnvFiles = [
    path.resolve(__dirname, '../.env'),
    path.resolve(__dirname, '../Projeto Bibline Academy/.env')
  ];

  for (const envPath of candidateEnvFiles) {
    GITHUB_TOKEN = tryReadTokenFromEnvFile(envPath);
    if (GITHUB_TOKEN) {
      break;
    }
  }
}

console.log("🔑 GITHUB_TOKEN status:", GITHUB_TOKEN ? "SET" : "NOT SET");

if (!GITHUB_TOKEN) {
  console.error("❌ ERRO: GITHUB_TOKEN não encontrado.");
  process.exit(1);
}

const PROJECT_ID =
  process.env.TRIVIUMOS_PROJECT_ID ||
  process.env.GITHUB_PROJECT_ID ||
  "PVT_kwDODLv1ac4BH1XW";

console.log("🚀 Starting Vision Board Sync Process...");
console.log("📋 PROJECT_ID:", PROJECT_ID);
console.log("⏱️  Start time:", new Date().toISOString());

async function runGraphQL(query, variables = {}) {
  console.log("Executing GraphQL query...");
  try {
    const res = await fetch('https://api.github.com/graphql', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${GITHUB_TOKEN}`,
        'Content-Type': 'application/json',
        'Accept': 'application/vnd.github.v4.idl'
      },
      body: JSON.stringify({ query, variables })
    });

    if (!res.ok) {
      console.error(`GraphQL falhou: ${res.status} - ${res.statusText}`);
      if (res.status === 401) {
        console.error("Erro de autenticação: verifique o GITHUB_TOKEN e suas permissões");
      }
      if (res.status === 404) {
        console.error("Projeto não encontrado: verifique o PROJECT_ID");
      }
      return null;
    }
    return await res.json();
  } catch (error) {
    console.error("Erro na requisição GraphQL:", error.message);
    return null;
  }
}

const query = `
query($cursor: String) {
  node(id: "${PROJECT_ID}") {
    ... on ProjectV2 {
      items(first: 100, after: $cursor) {
        nodes {
          content {
            ... on Issue {
              id
              number
              title
              createdAt
              state
              closedAt
              assignees(first: 10) {
                nodes {
                  login
                }
              }
              labels(first: 10) {
                nodes {
                  name
                }
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
`;

async function sync() {
  console.log("Iniciando varredura do GitHub Projects...");
  let allItems = [];
  let cursor = null;
  let hasNextPage = true;

  // To speed up local testing, we might limit pages if it's too big,
  // but PRD requires full analysis.
  let pagesFetched = 0;
  console.log("Starting GraphQL query...");

  while (hasNextPage) {
    process.stdout.write(`Fetching page ${pagesFetched + 1}... `);
    const data = await runGraphQL(query, { cursor });

    if (!data || !data.data || !data.data.node) {
      console.error(JSON.stringify(data)); console.error("Falha ao ler o Projeto. Verifique token ou permissions.");
      break;
    }

    const items = data.data.node.items;
    if (!items || !items.nodes) {
      console.log("Sem nós encontrados no projeto");
      break;
    }

    console.log(`✓ ${items.nodes.length} registros processados nesta página`);

    for (const item of items.nodes) {
      if (!item || !item.content || !item.content.title) continue;

      let status = "No Status";
      if (item.fieldValues && item.fieldValues.nodes) {
        for (const fv of item.fieldValues.nodes) {
          if (fv && fv.field && fv.field.name === 'Status') {
            status = fv.name;
          }
        }
      }

      const content = item.content;

      // Extract Assignees
      let assignee = "Unassigned";
      if (content.assignees && content.assignees.nodes && content.assignees.nodes.length > 0) {
        assignee = content.assignees.nodes[0].login;
      }

      // Extract Labels
      let labels = [];
      if (content.labels && content.labels.nodes) {
        labels = content.labels.nodes.map(n => n.name);
      }

      // Parse Subject and Year from title: "[Ciência] - Ano 4 - 8.1..."
      let subject = "Outros";
      let year = 0;

      const titleMatch = content.title.match(/^\[(.*?)\]\s*-\s*Ano\s*(\d)/i);
      if (titleMatch) {
        subject = titleMatch[1].trim();
        year = parseInt(titleMatch[2], 10);
      } else if (content.title.includes("[Belas artes]")) {
        subject = "Belas Artes";
        const yrMatch = content.title.match(/Ano\s*(\d)/i);
        if (yrMatch) year = parseInt(yrMatch[1], 10);
      }

      let lead_time_days = null;
      if (content.closedAt) {
        const created = new Date(content.createdAt);
        const closed = new Date(content.closedAt);
        lead_time_days = (closed - created) / (1000 * 60 * 60 * 24);
      }

      allItems.push({
        id: content.id,
        number: content.number,
        title: content.title,
        status: status,
        state: content.state,
        assignee: assignee,
        subject: subject,
        year: year,
        created_at: content.createdAt,
        closed_at: content.closedAt,
        lead_time_days: lead_time_days,
        labels: labels
      });
    }

    console.log(`OK! Registros extraídos: ${items.nodes.length}`);
    hasNextPage = items.pageInfo.hasNextPage;
    cursor = items.pageInfo.endCursor;
    pagesFetched += 1;

    // DEBUG LIMIT: Only fetch 5 pages for early prototyping
    // if (pagesFetched >= 5) break; 
  }

  console.log(`Total de tarefas válidas extraídas: ${allItems.length}`);

  if (allItems.length === 0) {
    console.log("⚠️ Nenhum dado encontrado. Verifique o PROJECT_ID e permissões do token.");
    console.log("⚠️ data.json NÃO será sobrescrito para preservar dados existentes.");
    process.exit(1);
  }

  const output = {
    last_updated: new Date().toISOString(),
    total_items: allItems.length,
    items: allItems
  };

  const docsDir = path.resolve(__dirname, '../public');
  fs.writeFileSync(path.join(docsDir, 'data.json'), JSON.stringify(output, null, 2));

  const duration = ((Date.now() - startTime) / 1000).toFixed(2);

  console.log(`✅ Data gravada em ${docsDir}/data.json`);
  console.log(`✅ Total de items: ${output.total_items}`);
  console.log(`✅ Última atualização: ${new Date().toISOString()}`);
  console.log(`⏱️  Duration: ${duration}s`);
  console.log(`🎉 Sync completed successfully!`);
}

async function startDaemon() {
  if (process.env.CI) {
    console.log("Running in CI mode. Single execution.");
    await sync();
    process.exit(0);
  } else {
    console.log("Iniciando Daemon do Vision Board (Sync a cada 60s)...");
    await sync(); // run immediately
    setInterval(() => {
      sync().catch(e => console.error("Erro no sync em background:", e));
    }, 60000);
  }
}

startDaemon().catch(console.error);
