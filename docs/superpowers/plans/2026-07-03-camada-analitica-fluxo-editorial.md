# Camada Analítica do Fluxo Editorial Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Construir uma tela read-only de Fluxo Editorial que classifica os cards do Kanban atual em subestados analíticos e mostra gargalos de revisão, vídeo e entrega.

**Architecture:** A lógica de classificação e agregação ficará em um módulo puro testável, sem dependência de DOM. A tela `flow-editorial.html` carregará `public/data.json`, chamará o módulo analítico e renderizará KPIs, funis, filas críticas e recomendações. A navegação existente será atualizada para expor a nova página sem alterar o Kanban do GitHub Projects.

**Tech Stack:** Node test runner, JavaScript ES modules, HTML estático, CSS existente em `public/styles.css`, Chart.js já carregado nas páginas do dashboard.

---

## File Structure

- Create: `public/flow-analytics-core.mjs`
  - Responsável por normalizar labels, classificar subestados, calcular idade desde criação, agrupar métricas e gerar alertas.
- Create: `tests/flow-analytics.test.mjs`
  - Testa a classificação de subestados, agregações por status/subestado, envelhecimento e recomendações.
- Create: `src/flow-editorial.html`
  - Tela nova do dashboard com KPIs, funil analítico, listas de gargalos e tabela de cards críticos.
- Create: `public/flow-editorial.js`
  - Código de browser que carrega `public/data.json`, chama `buildFlowAnalytics`, renderiza a tela e inicializa gráficos.
- Modify: `public/styles.css`
  - Adiciona estilos reutilizáveis para cards compactos, tabela de fluxo, badges de subestado e cards de alerta.
- Modify: `src/index.html`
  - Adiciona link de navegação para `flow-editorial.html`.
- Modify: `src/metas.html`
  - Adiciona link de navegação para `flow-editorial.html`.
- Modify: `src/metas-disciplinas.html`
  - Adiciona link de navegação para `flow-editorial.html`.
- Modify: `src/videos.html`
  - Adiciona link de navegação para `flow-editorial.html`.
- Modify: `src/lib/install.mjs`
  - Inclui `flow-editorial.html` na instalação do scaffolder.
- Modify: `package.json`
  - Inclui `public/flow-analytics-core.mjs` e `public/flow-editorial.js` no pacote publicado.
- Verify: `npm test`, `npm run lint`, `npm run typecheck`.

---

### Task 1: Pure Analytics Module

**Files:**
- Create: `public/flow-analytics-core.mjs`
- Test: `tests/flow-analytics.test.mjs`

- [ ] **Step 1: Write failing tests for substate classification**

Create `tests/flow-analytics.test.mjs` with this content:

```js
import test from "node:test";
import assert from "node:assert/strict";
import {
  classifyFlowSubstate,
  buildFlowAnalytics,
  normalizeReviewLabel
} from "../public/flow-analytics-core.mjs";

const NOW = new Date("2026-07-03T03:00:00.000Z");

function item(overrides) {
  return {
    id: "I_test",
    number: 1,
    title: "[Matemática] - Ano 1 - 1.1 Números",
    status: "In Review",
    assignee: "revisor",
    subject: "Matemática",
    year: 1,
    lesson_code: "1.1",
    lesson_title: "Números",
    created_at: "2026-06-03T03:00:00.000Z",
    closed_at: null,
    labels: [],
    ...overrides
  };
}

test("normalizeReviewLabel accepts review labels case-insensitively", () => {
  assert.equal(normalizeReviewLabel("review:peer"), "review:peer");
  assert.equal(normalizeReviewLabel("Review:Final"), "review:final");
  assert.equal(normalizeReviewLabel(" review:video-ready "), "review:video-ready");
  assert.equal(normalizeReviewLabel("matemática"), null);
});

test("classifyFlowSubstate maps real statuses without changing Kanban columns", () => {
  assert.equal(classifyFlowSubstate(item({ status: "Backlog" })).substate, "Não iniciado");
  assert.equal(classifyFlowSubstate(item({ status: "In Progress" })).substate, "Em produção editorial");
  assert.equal(classifyFlowSubstate(item({ status: "Video" })).substate, "Em produção de vídeo");
  assert.equal(classifyFlowSubstate(item({ status: "Done/Published" })).substate, "Done");
});

test("classifyFlowSubstate maps In Review labels to analytical substates", () => {
  assert.equal(classifyFlowSubstate(item({ labels: ["review:peer"] })).substate, "Peer review");
  assert.equal(classifyFlowSubstate(item({ labels: ["review:ajustes-autor"] })).substate, "Ajustes do autor");
  assert.equal(classifyFlowSubstate(item({ labels: ["review:final"] })).substate, "Review final");
  assert.equal(classifyFlowSubstate(item({ labels: ["review:video-ready"] })).substate, "Pronto para vídeo");
});

test("classifyFlowSubstate keeps unqualified In Review explicit", () => {
  const result = classifyFlowSubstate(item({ labels: ["ano:1"] }));
  assert.equal(result.substate, "Review sem classificação");
  assert.equal(result.confidence, "low");
  assert.equal(result.source, "status");
});

test("buildFlowAnalytics aggregates status, substate, age and recommendations", () => {
  const result = buildFlowAnalytics([
    item({ number: 1, status: "In Review", labels: ["review:peer"], subject: "Matemática", year: 1 }),
    item({ number: 2, status: "In Review", labels: ["review:final"], subject: "Matemática", year: 1 }),
    item({ number: 3, status: "Video", labels: [], subject: "Português", year: 2 }),
    item({ number: 4, status: "Done/Published", labels: [], subject: "Português", year: 2, closed_at: "2026-07-01T03:00:00.000Z" })
  ], { now: NOW });

  assert.equal(result.total, 4);
  assert.equal(result.byStatus["In Review"].count, 2);
  assert.equal(result.bySubstate["Peer review"].count, 1);
  assert.equal(result.bySubstate["Review final"].count, 1);
  assert.equal(result.bySubstate["Em produção de vídeo"].count, 1);
  assert.equal(result.delivery.producedEditorially, 4);
  assert.equal(result.delivery.done, 1);
  assert.equal(result.delivery.doneLast30Days, 1);
  assert.ok(result.criticalItems[0].ageDays >= 30);
  assert.ok(result.recommendations.length >= 1);
});
```

- [ ] **Step 2: Run test to verify it fails**

Run:

```bash
npm test -- tests/flow-analytics.test.mjs
```

Expected: the command fails because `public/flow-analytics-core.mjs` does not exist.

- [ ] **Step 3: Create the analytics module**

Create `public/flow-analytics-core.mjs` with this content:

```js
export const REVIEW_LABELS = new Map([
  ["review:peer", "Peer review"],
  ["review:ajustes-autor", "Ajustes do autor"],
  ["review:final", "Review final"],
  ["review:video-ready", "Pronto para vídeo"]
]);

export const STATUS_SUBSTATES = new Map([
  ["Backlog", "Não iniciado"],
  ["In Progress", "Em produção editorial"],
  ["Video", "Em produção de vídeo"],
  ["Done/Published", "Done"],
  ["Block", "Bloqueado"],
  ["No Status", "Sem status"]
]);

export function normalizeReviewLabel(label) {
  if (typeof label !== "string") return null;
  const normalized = label.trim().toLowerCase();
  return REVIEW_LABELS.has(normalized) ? normalized : null;
}

export function classifyFlowSubstate(item) {
  const status = item?.status || "No Status";

  if (status === "In Review") {
    const labels = Array.isArray(item.labels) ? item.labels : [];
    const reviewLabel = labels.map(normalizeReviewLabel).find(Boolean);

    if (reviewLabel) {
      return {
        status,
        substate: REVIEW_LABELS.get(reviewLabel),
        confidence: "high",
        source: "label",
        label: reviewLabel
      };
    }

    return {
      status,
      substate: "Review sem classificação",
      confidence: "low",
      source: "status",
      label: null
    };
  }

  return {
    status,
    substate: STATUS_SUBSTATES.get(status) || "Sem status",
    confidence: "high",
    source: "status",
    label: null
  };
}

export function calculateAgeDays(item, now = new Date()) {
  if (!item?.created_at) return 0;
  const createdAt = new Date(item.created_at);
  if (Number.isNaN(createdAt.getTime())) return 0;
  return Math.max(0, (now.getTime() - createdAt.getTime()) / 86400000);
}

function emptyBucket(label) {
  return {
    label,
    count: 0,
    ageTotal: 0,
    avgAgeDays: 0,
    over7: 0,
    over14: 0,
    over30: 0,
    over60: 0
  };
}

function addToBucket(target, label, item) {
  if (!target[label]) target[label] = emptyBucket(label);
  const bucket = target[label];
  const ageDays = item.ageDays || 0;
  bucket.count += 1;
  bucket.ageTotal += ageDays;
  if (ageDays > 7) bucket.over7 += 1;
  if (ageDays > 14) bucket.over14 += 1;
  if (ageDays > 30) bucket.over30 += 1;
  if (ageDays > 60) bucket.over60 += 1;
}

function finalizeBuckets(target) {
  for (const bucket of Object.values(target)) {
    bucket.avgAgeDays = bucket.count > 0 ? Number((bucket.ageTotal / bucket.count).toFixed(1)) : 0;
    delete bucket.ageTotal;
  }
}

function sortObjectBuckets(target) {
  return Object.fromEntries(
    Object.entries(target).sort((a, b) => b[1].count - a[1].count || a[0].localeCompare(b[0]))
  );
}

function buildComboKey(item) {
  const subject = item.subject || "Outros";
  const year = item.year ? `${item.year}º ano` : "Ano não informado";
  return `${subject} | ${year} | ${item.substate}`;
}

function buildRecommendations(analytics) {
  const recommendations = [];
  const inReview = analytics.byStatus["In Review"]?.count || 0;
  const video = analytics.byStatus.Video?.count || 0;
  const unclassified = analytics.bySubstate["Review sem classificação"]?.count || 0;
  const total = analytics.total || 1;

  if (inReview / total >= 0.45) {
    recommendations.push({
      level: "danger",
      title: "Revisão concentra o fluxo",
      text: `In Review concentra ${Math.round((inReview / total) * 100)}% do Kanban. Priorize triagem de revisão antes de abrir novos lotes.`
    });
  }

  if (video > 100) {
    recommendations.push({
      level: "warning",
      title: "Fila de vídeo alta",
      text: `Há ${video} cards em Video. Revise capacidade de gravação, edição e publicação audiovisual.`
    });
  }

  if (unclassified > 0) {
    recommendations.push({
      level: "warning",
      title: "Review sem classificação",
      text: `${unclassified} cards em In Review ainda não têm label review:*. Aplicar labels leves melhora o diagnóstico.`
    });
  }

  const topCombo = analytics.topQueues[0];
  if (topCombo) {
    recommendations.push({
      level: "info",
      title: "Maior fila por disciplina e ano",
      text: `${topCombo.label} tem ${topCombo.count} cards. Use essa fila como candidata ao próximo mutirão.`
    });
  }

  return recommendations;
}

export function buildFlowAnalytics(items, options = {}) {
  const now = options.now || new Date();
  const enrichedItems = (Array.isArray(items) ? items : []).map((item) => {
    const classification = classifyFlowSubstate(item);
    const ageDays = Number(calculateAgeDays(item, now).toFixed(1));

    return {
      ...item,
      status: classification.status,
      substate: classification.substate,
      substateConfidence: classification.confidence,
      substateSource: classification.source,
      reviewLabel: classification.label,
      ageDays
    };
  });

  const analytics = {
    total: enrichedItems.length,
    generatedAt: now.toISOString(),
    byStatus: {},
    bySubstate: {},
    bySubject: {},
    byYear: {},
    byCombo: {},
    topQueues: [],
    criticalItems: [],
    delivery: {
      producedEditorially: 0,
      done: 0,
      readyForVideo: 0,
      doneLast7Days: 0,
      doneLast14Days: 0,
      doneLast30Days: 0,
      doneLast60Days: 0,
      producedToDoneGap: 0
    },
    recommendations: []
  };

  for (const item of enrichedItems) {
    addToBucket(analytics.byStatus, item.status || "No Status", item);
    addToBucket(analytics.bySubstate, item.substate || "Sem status", item);
    addToBucket(analytics.bySubject, item.subject || "Outros", item);
    addToBucket(analytics.byYear, item.year ? `${item.year}º ano` : "Ano não informado", item);
    addToBucket(analytics.byCombo, buildComboKey(item), item);

    if (["In Review", "Video", "Done/Published"].includes(item.status)) {
      analytics.delivery.producedEditorially += 1;
    }

    if (item.substate === "Pronto para vídeo") {
      analytics.delivery.readyForVideo += 1;
    }

    if (item.status === "Done/Published") {
      analytics.delivery.done += 1;
      if (item.closed_at) {
        const closedAt = new Date(item.closed_at);
        const ageClosedDays = (now.getTime() - closedAt.getTime()) / 86400000;
        if (ageClosedDays <= 7) analytics.delivery.doneLast7Days += 1;
        if (ageClosedDays <= 14) analytics.delivery.doneLast14Days += 1;
        if (ageClosedDays <= 30) analytics.delivery.doneLast30Days += 1;
        if (ageClosedDays <= 60) analytics.delivery.doneLast60Days += 1;
      }
    }
  }

  finalizeBuckets(analytics.byStatus);
  finalizeBuckets(analytics.bySubstate);
  finalizeBuckets(analytics.bySubject);
  finalizeBuckets(analytics.byYear);
  finalizeBuckets(analytics.byCombo);

  analytics.byStatus = sortObjectBuckets(analytics.byStatus);
  analytics.bySubstate = sortObjectBuckets(analytics.bySubstate);
  analytics.bySubject = sortObjectBuckets(analytics.bySubject);
  analytics.byYear = sortObjectBuckets(analytics.byYear);
  analytics.byCombo = sortObjectBuckets(analytics.byCombo);
  analytics.topQueues = Object.values(analytics.byCombo).slice(0, 12);
  analytics.criticalItems = enrichedItems
    .filter((item) => item.status !== "Done/Published")
    .sort((a, b) => b.ageDays - a.ageDays || (a.number || 0) - (b.number || 0))
    .slice(0, 25);
  analytics.delivery.producedToDoneGap = analytics.delivery.producedEditorially - analytics.delivery.done;
  analytics.recommendations = buildRecommendations(analytics);

  return analytics;
}
```

- [ ] **Step 4: Run analytics tests**

Run:

```bash
npm test -- tests/flow-analytics.test.mjs
```

Expected: all tests in `tests/flow-analytics.test.mjs` pass.

- [ ] **Step 5: Commit analytics core**

Run:

```bash
git add public/flow-analytics-core.mjs tests/flow-analytics.test.mjs
git commit -m "feat: add flow analytics core"
```

---

### Task 2: Browser Rendering for Flow Analytics

**Files:**
- Create: `public/flow-editorial.js`
- Test: `tests/flow-analytics.test.mjs`

- [ ] **Step 1: Extend tests for empty and invalid data**

Append this test to `tests/flow-analytics.test.mjs`:

```js
test("buildFlowAnalytics handles empty and non-array input", () => {
  assert.equal(buildFlowAnalytics([], { now: NOW }).total, 0);
  assert.equal(buildFlowAnalytics(null, { now: NOW }).total, 0);
});
```

- [ ] **Step 2: Run test**

Run:

```bash
npm test -- tests/flow-analytics.test.mjs
```

Expected: tests pass because `buildFlowAnalytics` already handles empty and non-array input.

- [ ] **Step 3: Create browser renderer**

Create `public/flow-editorial.js` with this content:

```js
import { buildFlowAnalytics } from "./flow-analytics-core.mjs";

let substateChartInstance = null;
let subjectChartInstance = null;

function formatNumber(value) {
  return new Intl.NumberFormat("pt-BR").format(value || 0);
}

function formatAge(value) {
  return `${Number(value || 0).toFixed(1)} dias`;
}

function escapeHtml(value) {
  const div = document.createElement("div");
  div.textContent = value == null ? "" : String(value);
  return div.innerHTML;
}

function setText(id, value) {
  const el = document.getElementById(id);
  if (el) el.textContent = value;
}

function bucketListToRows(buckets, limit = 8) {
  return Object.values(buckets).slice(0, limit);
}

function renderKpis(analytics) {
  setText("flow-total", formatNumber(analytics.total));
  setText("flow-review", formatNumber(analytics.byStatus["In Review"]?.count || 0));
  setText("flow-peer", formatNumber(analytics.bySubstate["Peer review"]?.count || 0));
  setText("flow-unclassified", formatNumber(analytics.bySubstate["Review sem classificação"]?.count || 0));
  setText("flow-video", formatNumber(analytics.byStatus.Video?.count || 0));
  setText("flow-done", formatNumber(analytics.delivery.done));
  setText("flow-gap", formatNumber(analytics.delivery.producedToDoneGap));
  setText("flow-ready-video", formatNumber(analytics.delivery.readyForVideo));
}

function renderRecommendations(analytics) {
  const container = document.getElementById("flow-recommendations");
  if (!container) return;

  container.innerHTML = analytics.recommendations.map((item) => `
    <article class="flow-alert flow-alert-${escapeHtml(item.level)}">
      <strong>${escapeHtml(item.title)}</strong>
      <p>${escapeHtml(item.text)}</p>
    </article>
  `).join("") || `
    <article class="flow-alert flow-alert-success">
      <strong>Sem alerta crítico</strong>
      <p>O snapshot atual não gerou recomendações de risco.</p>
    </article>
  `;
}

function renderBucketTable(id, buckets) {
  const body = document.getElementById(id);
  if (!body) return;

  body.innerHTML = bucketListToRows(buckets, 10).map((bucket) => `
    <tr>
      <td>${escapeHtml(bucket.label)}</td>
      <td>${formatNumber(bucket.count)}</td>
      <td>${formatAge(bucket.avgAgeDays)}</td>
      <td>${formatNumber(bucket.over30)}</td>
      <td>${formatNumber(bucket.over60)}</td>
    </tr>
  `).join("");
}

function renderCriticalItems(analytics) {
  const body = document.getElementById("flow-critical-items");
  if (!body) return;

  body.innerHTML = analytics.criticalItems.map((item) => `
    <tr>
      <td><a href="https://github.com/bibline/Projeto-Editorial-Education/issues/${encodeURIComponent(item.number)}" target="_blank" rel="noopener">#${escapeHtml(item.number)}</a></td>
      <td>${escapeHtml(item.title)}</td>
      <td><span class="flow-badge">${escapeHtml(item.substate)}</span></td>
      <td>${escapeHtml(item.subject || "Outros")}</td>
      <td>${item.year ? `${escapeHtml(item.year)}º` : "Sem ano"}</td>
      <td>${escapeHtml(item.assignee || "Unassigned")}</td>
      <td>${formatAge(item.ageDays)}</td>
    </tr>
  `).join("");
}

function renderCharts(analytics) {
  const substateCanvas = document.getElementById("flowSubstateChart");
  if (substateCanvas && window.Chart) {
    const labels = bucketListToRows(analytics.bySubstate, 8).map((bucket) => bucket.label);
    const data = bucketListToRows(analytics.bySubstate, 8).map((bucket) => bucket.count);
    if (substateChartInstance) substateChartInstance.destroy();
    substateChartInstance = new Chart(substateCanvas.getContext("2d"), {
      type: "bar",
      data: {
        labels,
        datasets: [{ label: "Cards", data, backgroundColor: "rgba(59, 130, 246, 0.78)" }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: { grid: { color: "rgba(148,163,184,0.18)" } },
          y: { grid: { color: "rgba(148,163,184,0.18)" } }
        },
        plugins: { legend: { labels: { color: "#334155" } } }
      }
    });
  }

  const subjectCanvas = document.getElementById("flowSubjectChart");
  if (subjectCanvas && window.Chart) {
    const labels = bucketListToRows(analytics.bySubject, 7).map((bucket) => bucket.label);
    const data = bucketListToRows(analytics.bySubject, 7).map((bucket) => bucket.count);
    if (subjectChartInstance) subjectChartInstance.destroy();
    subjectChartInstance = new Chart(subjectCanvas.getContext("2d"), {
      type: "doughnut",
      data: {
        labels,
        datasets: [{
          data,
          backgroundColor: ["#3b82f6", "#8b5cf6", "#10b981", "#f59e0b", "#ef4444", "#ec4899", "#06b6d4"],
          borderWidth: 0
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { position: "right", labels: { color: "#334155" } } }
      }
    });
  }
}

async function loadFlowData() {
  try {
    const response = await fetch("../public/data.json?t=" + Date.now());
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();
    const analytics = buildFlowAnalytics(data.items || []);

    const lastSync = document.getElementById("last-sync-time");
    if (lastSync) lastSync.textContent = new Date(data.last_updated).toLocaleString("pt-BR");

    renderKpis(analytics);
    renderRecommendations(analytics);
    renderBucketTable("flow-substate-table", analytics.bySubstate);
    renderBucketTable("flow-combo-table", analytics.byCombo);
    renderCriticalItems(analytics);
    renderCharts(analytics);
  } catch (error) {
    const container = document.getElementById("flow-recommendations");
    if (container) {
      container.innerHTML = `
        <article class="flow-alert flow-alert-danger">
          <strong>Erro ao carregar dados</strong>
          <p>${escapeHtml(error.message)}</p>
        </article>
      `;
    }
  }
}

document.addEventListener("DOMContentLoaded", () => {
  loadFlowData();
  setInterval(loadFlowData, 60000);
});
```

- [ ] **Step 4: Run tests**

Run:

```bash
npm test -- tests/flow-analytics.test.mjs
```

Expected: tests pass.

- [ ] **Step 5: Commit browser renderer**

Run:

```bash
git add public/flow-editorial.js tests/flow-analytics.test.mjs
git commit -m "feat: render flow analytics data"
```

---

### Task 3: Flow Editorial Page

**Files:**
- Create: `src/flow-editorial.html`
- Modify: `public/styles.css`

- [ ] **Step 1: Create the page**

Create `src/flow-editorial.html` with this content:

```html
<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">
    <meta name="description" content="Fluxo Editorial — camada analítica read-only do Kanban Bibline Academy.">
    <title>Fluxo Editorial | Bibline Academy</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;900&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="stylesheet" href="../public/styles.css?v=11">
</head>

<body>
    <div class="bg-orbs" aria-hidden="true">
        <div class="bg-orb bg-orb-1"></div>
        <div class="bg-orb bg-orb-2"></div>
        <div class="bg-orb bg-orb-3"></div>
        <div class="bg-orb bg-orb-4"></div>
    </div>
    <div class="bg-mesh" aria-hidden="true"></div>

    <div class="dashboard-container">
        <aside class="sidebar glass-panel">
            <div class="logo-area">
                <img src="assets/bibline-icon-512x512-red.png" alt="Bibline" class="logo-main">
                <h2>Vision Board</h2>
                <span class="badge">Live Sync</span>
            </div>

            <nav class="menu">
                <a href="index.html">
                    <i class="ph ph-chart-pie-slice icon"></i> Overview Geral
                </a>
                <a href="metas.html">
                    <i class="ph ph-target icon"></i> Metas (Currículo)
                </a>
                <a href="metas-disciplinas.html">
                    <i class="ph ph-book-open-text icon"></i> Metas (Disciplinas)
                </a>
                <a href="flow-editorial.html" class="active">
                    <i class="ph ph-git-branch icon"></i> Fluxo Editorial
                </a>
                <a href="videos.html">
                    <i class="ph ph-video-camera icon"></i> Videos Pipeline
                </a>
            </nav>

            <div class="sync-status">
                <p>Última Sincronização:</p>
                <div id="last-sync-time" class="time-badge">Aguardando...</div>
            </div>
        </aside>

        <main class="main-content">
            <section class="flow-header">
                <div>
                    <p class="flow-eyebrow">Camada read-only sobre o Kanban atual</p>
                    <h1>Fluxo Editorial</h1>
                    <p>Diagnóstico de peer review, review final, vídeo e entrega sem alterar as colunas do GitHub Projects.</p>
                </div>
            </section>

            <section class="kpi-grid flow-kpi-grid">
                <div class="kpi-card glass-panel">
                    <div class="kpi-icon blue"><i class="ph ph-folder-simple"></i></div>
                    <div class="kpi-data"><h3>Total</h3><p id="flow-total">0</p></div>
                </div>
                <div class="kpi-card glass-panel">
                    <div class="kpi-icon orange"><i class="ph ph-magnifying-glass"></i></div>
                    <div class="kpi-data"><h3>In Review</h3><p id="flow-review">0</p></div>
                </div>
                <div class="kpi-card glass-panel">
                    <div class="kpi-icon cyan"><i class="ph ph-users-three"></i></div>
                    <div class="kpi-data"><h3>Peer Review</h3><p id="flow-peer">0</p></div>
                </div>
                <div class="kpi-card glass-panel">
                    <div class="kpi-icon gray"><i class="ph ph-question"></i></div>
                    <div class="kpi-data"><h3>Review sem classe</h3><p id="flow-unclassified">0</p></div>
                </div>
            </section>

            <section class="kpi-grid flow-kpi-grid">
                <div class="kpi-card glass-panel">
                    <div class="kpi-icon pink"><i class="ph ph-video-camera"></i></div>
                    <div class="kpi-data"><h3>Video</h3><p id="flow-video">0</p></div>
                </div>
                <div class="kpi-card glass-panel">
                    <div class="kpi-icon green"><i class="ph ph-check-circle"></i></div>
                    <div class="kpi-data"><h3>Done</h3><p id="flow-done">0</p></div>
                </div>
                <div class="kpi-card glass-panel">
                    <div class="kpi-icon purple"><i class="ph ph-arrow-fat-lines-right"></i></div>
                    <div class="kpi-data"><h3>Gap produzido</h3><p id="flow-gap">0</p></div>
                </div>
                <div class="kpi-card glass-panel">
                    <div class="kpi-icon yellow"><i class="ph ph-seal-check"></i></div>
                    <div class="kpi-data"><h3>Pronto para vídeo</h3><p id="flow-ready-video">0</p></div>
                </div>
            </section>

            <section class="flow-grid-two">
                <div class="chart-container glass-panel">
                    <h3>Funil por subestado analítico</h3>
                    <div class="chart-wrapper">
                        <canvas id="flowSubstateChart"></canvas>
                    </div>
                </div>
                <div class="chart-container glass-panel">
                    <h3>Volume por disciplina</h3>
                    <div class="chart-wrapper">
                        <canvas id="flowSubjectChart"></canvas>
                    </div>
                </div>
            </section>

            <section class="flow-grid-two">
                <div class="glass-panel flow-panel">
                    <h3>Recomendações estratégicas</h3>
                    <div id="flow-recommendations" class="flow-alert-list"></div>
                </div>
                <div class="glass-panel flow-panel">
                    <h3>Subestados com maior fila</h3>
                    <table class="flow-table">
                        <thead><tr><th>Subestado</th><th>Cards</th><th>Idade média</th><th>>30d</th><th>>60d</th></tr></thead>
                        <tbody id="flow-substate-table"></tbody>
                    </table>
                </div>
            </section>

            <section class="glass-panel flow-panel">
                <h3>Filas por disciplina, ano e subestado</h3>
                <table class="flow-table">
                    <thead><tr><th>Fila</th><th>Cards</th><th>Idade média</th><th>>30d</th><th>>60d</th></tr></thead>
                    <tbody id="flow-combo-table"></tbody>
                </table>
            </section>

            <section class="glass-panel flow-panel">
                <h3>Cards críticos por idade desde criação</h3>
                <table class="flow-table flow-critical-table">
                    <thead>
                        <tr>
                            <th>Issue</th><th>Título</th><th>Subestado</th><th>Disciplina</th><th>Ano</th><th>Responsável</th><th>Idade</th>
                        </tr>
                    </thead>
                    <tbody id="flow-critical-items"></tbody>
                </table>
            </section>
        </main>
    </div>

    <script src="../public/sidebar.js?v=2"></script>
    <script type="module" src="../public/flow-editorial.js?v=1"></script>
</body>

</html>
```

- [ ] **Step 2: Add CSS for flow page**

Append this CSS to `public/styles.css`:

```css
.flow-header {
    margin-bottom: 1.5rem;
    padding: 1.5rem 0 0;
}

.flow-header h1 {
    margin: 0;
    font-size: clamp(2rem, 4vw, 3.25rem);
    line-height: 1;
    letter-spacing: 0;
    color: var(--text-primary);
}

.flow-header p {
    max-width: 760px;
    color: var(--text-secondary);
    line-height: 1.5;
}

.flow-eyebrow {
    margin: 0 0 0.5rem;
    color: var(--color-primary-light);
    font-size: 0.78rem;
    font-weight: 700;
    text-transform: uppercase;
}

.flow-kpi-grid {
    margin-top: 1rem;
}

.flow-grid-two {
    display: grid;
    grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
    gap: 1.25rem;
    margin-top: 1.5rem;
}

.flow-panel {
    padding: 1.25rem;
    margin-top: 1.5rem;
}

.flow-panel h3,
.chart-container h3 {
    margin-top: 0;
}

.flow-alert-list {
    display: grid;
    gap: 0.75rem;
}

.flow-alert {
    padding: 0.9rem 1rem;
    border-radius: 8px;
    border-left: 4px solid var(--color-primary);
    background: rgba(241, 245, 249, 0.86);
}

.flow-alert strong {
    display: block;
    color: var(--text-primary);
    margin-bottom: 0.35rem;
}

.flow-alert p {
    margin: 0;
    color: var(--text-secondary);
    line-height: 1.45;
}

.flow-alert-danger {
    border-left-color: var(--color-danger);
}

.flow-alert-warning {
    border-left-color: var(--color-warning);
}

.flow-alert-info {
    border-left-color: var(--color-primary);
}

.flow-alert-success {
    border-left-color: var(--color-success);
}

.flow-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.88rem;
}

.flow-table th,
.flow-table td {
    padding: 0.75rem 0.65rem;
    border-bottom: 1px solid rgba(148, 163, 184, 0.24);
    text-align: left;
    vertical-align: top;
}

.flow-table th {
    color: var(--text-muted);
    font-size: 0.74rem;
    text-transform: uppercase;
}

.flow-table td {
    color: var(--text-primary);
}

.flow-critical-table td:nth-child(2) {
    max-width: 460px;
}

.flow-badge {
    display: inline-flex;
    align-items: center;
    min-height: 1.5rem;
    padding: 0.15rem 0.5rem;
    border-radius: 999px;
    background: rgba(59, 130, 246, 0.12);
    color: var(--color-primary-dark);
    font-size: 0.75rem;
    font-weight: 700;
    white-space: nowrap;
}

@media (max-width: 980px) {
    .flow-grid-two {
        grid-template-columns: 1fr;
    }

    .flow-table {
        display: block;
        overflow-x: auto;
        white-space: nowrap;
    }
}
```

- [ ] **Step 3: Open page locally as static file check**

Run:

```bash
test -f src/flow-editorial.html
```

Expected: exit code 0.

- [ ] **Step 4: Commit page and styles**

Run:

```bash
git add src/flow-editorial.html public/styles.css
git commit -m "feat: add flow editorial dashboard page"
```

---

### Task 4: Navigation and Packaging

**Files:**
- Modify: `src/index.html`
- Modify: `src/metas.html`
- Modify: `src/metas-disciplinas.html`
- Modify: `src/videos.html`
- Modify: `src/lib/install.mjs`
- Modify: `package.json`

- [ ] **Step 1: Add navigation link to dashboard pages**

In each of these files, add the `Fluxo Editorial` link immediately before the `videos.html` link:

- `src/index.html`
- `src/metas.html`
- `src/metas-disciplinas.html`
- `src/videos.html`

Use this exact markup in pages where the link is not active:

```html
<a href="flow-editorial.html">
    <i class="ph ph-git-branch icon"></i> Fluxo Editorial
</a>
```

In `src/flow-editorial.html`, the active version is already present:

```html
<a href="flow-editorial.html" class="active">
    <i class="ph ph-git-branch icon"></i> Fluxo Editorial
</a>
```

- [ ] **Step 2: Include flow page in installer**

Modify the page copy list in `src/lib/install.mjs` so it includes:

```js
{ type: "file", source: "flow-editorial.html", target: "flow-editorial.html" },
```

Place it next to the existing `index.html`, `metas.html`, `metas-disciplinas.html`, and `videos.html` entries.

- [ ] **Step 3: Include new public assets in package files**

Modify `package.json` and add these entries inside the `"files"` array near the other `public/` files:

```json
"public/flow-analytics-core.mjs",
"public/flow-editorial.js",
```

- [ ] **Step 4: Run tests**

Run:

```bash
npm test
```

Expected: all Node tests pass.

- [ ] **Step 5: Commit navigation and packaging**

Run:

```bash
git add src/index.html src/metas.html src/metas-disciplinas.html src/videos.html src/lib/install.mjs package.json
git commit -m "feat: expose flow editorial dashboard"
```

---

### Task 5: Quality Verification

**Files:**
- Verify existing project files.

- [ ] **Step 1: Run focused analytics tests**

Run:

```bash
npm test -- tests/flow-analytics.test.mjs
```

Expected: `tests/flow-analytics.test.mjs` passes.

- [ ] **Step 2: Run full test suite**

Run:

```bash
npm test
```

Expected: all tests pass.

- [ ] **Step 3: Run lint**

Run:

```bash
npm run lint
```

Expected: lint exits with code 0.

- [ ] **Step 4: Run typecheck**

Run:

```bash
npm run typecheck
```

Expected: typecheck exits with code 0.

- [ ] **Step 5: Inspect git status**

Run:

```bash
git status --short
```

Expected: only intentional files remain modified. If `public/data.json` is still modified from the live Kanban sync, do not include it in the implementation commit unless the user explicitly asks to publish the refreshed snapshot.

---

### Task 6: Documentation Update

**Files:**
- Modify: `README.md`
- Modify: `docs-estratégicos-funcionamento-framework/vision-board/ROADMAP.md`

- [ ] **Step 1: Update README dashboard file list**

In `README.md`, update the dashboard file list so the `src/` section includes:

```text
index.html / metas.html / metas-disciplinas.html / flow-editorial.html / videos.html
```

Also add one sentence in the dashboard description:

```markdown
`flow-editorial.html` apresenta a camada analítica read-only do fluxo editorial, separando subestados como Peer review, Review final, Pronto para vídeo e Done sem alterar as colunas do Kanban.
```

- [ ] **Step 2: Update roadmap**

In `docs-estratégicos-funcionamento-framework/vision-board/ROADMAP.md`, under `Fase 2 — Escala e Ação`, add this completed item after the drill-down item:

```markdown
- [x] Camada analítica read-only para interpretar gargalos dentro de `In Review` sem alterar as colunas do Kanban.
```

- [ ] **Step 3: Run doc grep verification**

Run:

```bash
rg -n "flow-editorial|Fluxo Editorial|camada analítica" README.md docs-estratégicos-funcionamento-framework/vision-board/ROADMAP.md
```

Expected: output includes the README entry and the ROADMAP entry.

- [ ] **Step 4: Commit docs**

Run:

```bash
git add README.md docs-estratégicos-funcionamento-framework/vision-board/ROADMAP.md
git commit -m "docs: documenta camada analitica do fluxo editorial"
```

---

## Self-Review Checklist

- Spec coverage:
  - Subestados analíticos são implementados em Task 1.
  - Métricas de fila, envelhecimento e entrega são implementadas em Task 1.
  - Tela de Fluxo Editorial é implementada em Tasks 2 e 3.
  - Navegação e empacotamento são implementados em Task 4.
  - Verificação é coberta em Task 5.
  - Documentação é coberta em Task 6.
- Red flag scan:
  - O plano não usa marcadores de conteúdo indefinido.
  - Cada arquivo novo tem código concreto.
  - Cada comando tem resultado esperado.
- Type consistency:
  - `buildFlowAnalytics`, `classifyFlowSubstate` e `normalizeReviewLabel` são exportados no módulo e importados nos testes.
  - `flow-editorial.js` usa os ids definidos em `src/flow-editorial.html`.
  - Os nomes de subestado no teste são os mesmos usados no módulo e na tela.
