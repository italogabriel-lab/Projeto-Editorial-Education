import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

// ES module equivalent of __dirname
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Performance tracking
const startTime = Date.now();

// PAT_TOKEN tem prioridade pois o GITHUB_TOKEN padrão do Actions
// não tem permissão para acessar GitHub Projects (ProjectV2) via GraphQL
let GITHUB_TOKEN =
  process.env['TRIVIUM-METHOD-EDITORIAL_GITHUB_TOKEN'] ||
  process.env.PAT_TOKEN ||
  process.env.GITHUB_TOKEN_CLASSIC ||
  process.env.GITHUB_TOKEN_FINE ||
  process.env.GITHUB_TOKEN;

function tryReadTokenFromEnvFile(envPath) {
  try {
    const envFile = fs.readFileSync(envPath, 'utf8');
    const tokenMatch =
      envFile.match(/TRIVIUM-METHOD-EDITORIAL_GITHUB_TOKEN=(.*)/) ||
      envFile.match(/GITHUB_TOKEN=(.*)/) ||
      envFile.match(/PAT_TOKEN=(.*)/);

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
  process.env['TRIVIUM-METHOD-EDITORIAL_PROJECT_ID'] ||
  process.env.GITHUB_PROJECT_ID ||
  "PVT_kwDODLv1ac4BH1XW";

const STATUS_PRIORITY = {
  'Done/Published': 5,
  'Video': 4,
  'In Review': 3,
  'In Progress': 2,
  'Backlog': 1,
  'Block': 0,
  'No Status': -1
};

function normalizeSubjectName(name) {
  if (!name) return 'Outros';

  const lower = name.toLowerCase().trim();
  const map = {
    'historia': 'História',
    'história': 'História',
    'ciência': 'Ciências',
    'ciencia': 'Ciências',
    'ciencias': 'Ciências',
    'ciências': 'Ciências',
    'geogrfia': 'Geografia',
    'geografia': 'Geografia',
    'matemática': 'Matemática',
    'matematica': 'Matemática',
    'portugues': 'Português',
    'português': 'Português',
    'linguagem': 'Português',
    'belas artes': 'Belas Artes',
    'belasartes': 'Belas Artes',
    'bíblia': 'Bíblia',
    'biblia': 'Bíblia'
  };

  return map[lower] || name.trim();
}

function normalizeLessonCode(rawCode, rawTitle) {
  if (!rawCode) return null;

  const code = rawCode.trim().replace(/\s+/g, '');
  if (/^\d{1,2}\.\d$/.test(code)) {
    return code;
  }

  // Legado do Kanban.
  // Alguns tickets de revisão e prova foram criados como "9 Revisão" e "10 Prova"
  // em vez de "8.4 Revisão" e "8.5 Prova". Mantemos o número legado para
  // contabilizar o item no Vision Board, sem descartá-lo.
  if (/^\d{1,2}$/.test(code) && /\b(revis[aã]o|prova|provas)\b/i.test(rawTitle || '')) {
    return code;
  }

  return null;
}

function parseCanonicalLessonTitle(title) {
  if (!title) return null;

  const compactTitle = title.replace(/\s+/g, ' ').trim();
  const match = compactTitle.match(
    /^\[\s*(?<subject>[^\]]+?)\s*\]\s*-\s*ano\s*(?<year>[1-5])\s*-\s*(?<lesson>\d{1,2}(?:\s*\.\s*\d)?)\s*-?\s*(?<lessonTitle>.+?)\s*$/i
  );
  if (!match || !match.groups) return null;

  const lessonTitle = match.groups.lessonTitle.trim();

  // Metadados editoriais fora do padrão não entram na contabilidade.
  if (!lessonTitle) return null;
  if (/\bupdate\b/i.test(lessonTitle)) return null;
  if (/^\s*[-–—]/.test(lessonTitle)) return null;

  const subject = normalizeSubjectName(match.groups.subject);
  const year = parseInt(match.groups.year, 10);
  const lessonCode = normalizeLessonCode(match.groups.lesson, lessonTitle);
  if (!lessonCode) return null;
  const canonicalTitle = `[${subject}] - Ano ${year} - ${lessonCode} ${lessonTitle}`;
  const canonicalKey = `${subject.toLowerCase()}|${year}|${lessonCode}|${lessonTitle.toLowerCase()}`;

  return {
    subject,
    year,
    lesson_code: lessonCode,
    lesson_title: lessonTitle,
    canonical_title: canonicalTitle,
    canonical_key: canonicalKey
  };
}

function choosePreferredDuplicate(current, candidate) {
  const currentPriority = STATUS_PRIORITY[current.status] ?? -1;
  const candidatePriority = STATUS_PRIORITY[candidate.status] ?? -1;

  if (candidatePriority !== currentPriority) {
    return candidatePriority > currentPriority ? candidate : current;
  }

  return (candidate.number ?? 0) > (current.number ?? 0) ? candidate : current;
}

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
  const validItemsByKey = new Map();
  const ignoredItems = [];
  const duplicateItems = [];
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

      const parsedTitle = parseCanonicalLessonTitle(content.title);
      if (!parsedTitle) {
        ignoredItems.push({
          id: content.id,
          number: content.number,
          title: content.title,
          reason: 'title_out_of_pattern'
        });
        continue;
      }

      let lead_time_days = null;
      if (content.closedAt) {
        const created = new Date(content.createdAt);
        const closed = new Date(content.closedAt);
        lead_time_days = (closed - created) / (1000 * 60 * 60 * 24);
      }

      const normalizedItem = {
        id: content.id,
        number: content.number,
        title: parsedTitle.canonical_title,
        status: status,
        state: content.state,
        assignee: assignee,
        subject: parsedTitle.subject,
        year: parsedTitle.year,
        lesson_code: parsedTitle.lesson_code,
        lesson_title: parsedTitle.lesson_title,
        canonical_key: parsedTitle.canonical_key,
        created_at: content.createdAt,
        closed_at: content.closedAt,
        lead_time_days: lead_time_days,
        labels: labels
      };

      const existingItem = validItemsByKey.get(parsedTitle.canonical_key);
      if (existingItem) {
        const preferredItem = choosePreferredDuplicate(existingItem, normalizedItem);
        const discardedItem = preferredItem === existingItem ? normalizedItem : existingItem;

        duplicateItems.push({
          kept_number: preferredItem.number,
          discarded_number: discardedItem.number,
          canonical_key: parsedTitle.canonical_key,
          title: preferredItem.title
        });

        validItemsByKey.set(parsedTitle.canonical_key, preferredItem);
      } else {
        validItemsByKey.set(parsedTitle.canonical_key, normalizedItem);
      }
    }

    console.log(`OK! Registros extraídos: ${items.nodes.length}`);
    hasNextPage = items.pageInfo.hasNextPage;
    cursor = items.pageInfo.endCursor;
    pagesFetched += 1;

    // DEBUG LIMIT: Only fetch 5 pages for early prototyping
    // if (pagesFetched >= 5) break; 
  }

  const allItems = Array.from(validItemsByKey.values()).sort((a, b) => (a.number ?? 0) - (b.number ?? 0));

  console.log(`Total de tarefas válidas extraídas: ${allItems.length}`);
  console.log(`Total de tarefas ignoradas por título fora do padrão: ${ignoredItems.length}`);
  console.log(`Total de duplicatas descartadas: ${duplicateItems.length}`);

  if (allItems.length === 0) {
    console.log("⚠️ Nenhum dado encontrado. Verifique o PROJECT_ID e permissões do token.");
    console.log("⚠️ data.json NÃO será sobrescrito para preservar dados existentes.");
    process.exit(1);
  }

  const output = {
    last_updated: new Date().toISOString(),
    total_items: allItems.length,
    ignored_items_count: ignoredItems.length,
    duplicate_items_count: duplicateItems.length,
    ignored_items: ignoredItems,
    duplicate_items: duplicateItems,
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
