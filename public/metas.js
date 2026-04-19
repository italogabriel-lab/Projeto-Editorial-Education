let yearChartInstance = null;
let subjectChartInstance = null;

const META_POR_DISCIPLINA = 168;
const NUM_ANOS = 5;
const META_EQUIPE_ANO = META_POR_DISCIPLINA * NUM_ANOS;

// Tudo que passou de "In Progress" é considerado produzido pela equipe de desenvolvimento
const PRODUCED_STATUSES = ['In Review', 'Video', 'Done/Published'];
function isProduced(status) {
    return PRODUCED_STATUSES.includes(status);
}

function normalizeSubject(name) {
    if (!name) return null;
    const lower = name.toLowerCase().trim();
    if (lower === 'outros') return null;

    const map = {
        'historia': 'História',
        'história': 'História',
        'ciência': 'Ciências',
        'ciencias': 'Ciências',
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
    return map[lower] || name;
}

function getSubjectIcon(subject, sizeClass = '') {
    const icons = {
        'História': 'ph-book-bookmark',
        'Ciências': 'ph-flask',
        'Geografia': 'ph-globe-hemisphere-west',
        'Matemática': 'ph-function',
        'Português': 'ph-text-aa',
        'Belas Artes': 'ph-palette',
        'Bíblia': 'ph-book-open'
    };
    const iconClass = icons[subject] || 'ph-book-open';
    const style = sizeClass ? ` style="${sizeClass}"` : ' style="font-size: 1.2rem;"';
    return `<i class="ph ${iconClass}"${style}></i>`;
}

function getProgressColor(pct) {
    if (pct >= 100) return 'green';
    if (pct >= 50) return 'blue';
    if (pct > 0) return 'orange';
    return 'gray';
}

function getProgressColorHex(pct) {
    if (pct >= 100) return '#34d399';
    if (pct >= 50) return '#60a5fa';
    if (pct > 0) return '#fb923c';
    return '#94a3b8';
}

function renderProgressBar(pct, width = 20) {
    const filled = Math.min(Math.round((pct / 100) * width), width);
    const empty = width - filled;
    return '█'.repeat(filled) + '░'.repeat(empty);
}

async function performSync() {
    const syncEl = document.getElementById('last-sync-time');
    try {
        const response = await fetch('public/data.json?t=' + new Date().getTime());
        if (!response.ok) throw new Error('HTTP ' + response.status);
        const data = await response.json();

        syncEl.textContent = new Date(data.last_updated).toLocaleString();
        syncEl.style.color = '';

        const items = data.items || [];
        renderMetas(items);

    } catch (e) {
        console.error("Error loading data:", e);
        syncEl.textContent = 'Erro ao carregar dados';
        syncEl.style.color = 'var(--color-danger-light)';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    performSync();
    setInterval(performSync, 60000);
});

function renderMetas(items) {
    const yearStats = { 1: { t: 0, d: 0 }, 2: { t: 0, d: 0 }, 3: { t: 0, d: 0 }, 4: { t: 0, d: 0 }, 5: { t: 0, d: 0 } };
    const subjectStats = {};
    const META_POR_DISCIPLINA = 168;
    const NUM_DISCIPLINAS = 7;
    const META_EQUIPE_ANO = META_POR_DISCIPLINA * NUM_DISCIPLINAS;
    const META_TOTAL = META_EQUIPE_ANO * 5;

    items.forEach(i => {
        const sub = normalizeSubject(i.subject);
        if (!sub) return;
        const y = i.year;

        if (!subjectStats[sub]) subjectStats[sub] = { t: 0, d: 0, years: { 1: {}, 2: {}, 3: {}, 4: {}, 5: {} } };

        subjectStats[sub].t++;
        if (isProduced(i.status)) subjectStats[sub].d++;

        if (y && subjectStats[sub].years[y]) {
            if (!subjectStats[sub].years[y].t) subjectStats[sub].years[y] = { t: 0, d: 0 };
            subjectStats[sub].years[y].t++;
            if (isProduced(i.status)) subjectStats[sub].years[y].d++;
        }

        if (y && yearStats[y]) {
            yearStats[y].t++;
            if (isProduced(i.status)) yearStats[y].d++;
        }
    });

    // --- 1. Cards de Disciplina ---
    let discHTML = '';
    const sortedSubs = Object.keys(subjectStats).sort((a, b) => subjectStats[b].t - subjectStats[a].t);

    sortedSubs.forEach((sub, idx) => {
        const st = subjectStats[sub];
        if (st.t === 0) return;

        const totalMetaDisciplina = META_POR_DISCIPLINA * 5;
        const pct = Math.round((st.d / totalMetaDisciplina) * 100) || 0;
        const color = getProgressColor(pct);

        let yearRowsHTML = '';
        [1, 2, 3, 4, 5].forEach(ano => {
            const yr = st.years[ano] || { t: 0, d: 0 };
            const hasData = yr.t > 0;
            const yrPct = hasData ? Math.round((yr.d / META_POR_DISCIPLINA) * 100) : 0;
            const yrColorHex = hasData ? getProgressColorHex(yrPct) : '#94a3b8';
            const doneCount = hasData ? yr.d : 0;

            yearRowsHTML += `
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; padding: 8px 12px; background: rgba(255,255,255,0.03); border-radius: 6px;">
                    <span style="color: #cbd5e1; font-weight: 500;">Ano ${ano}:</span>
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <span style="font-size: 0.85rem; color: #94a3b8;">${renderProgressBar(yrPct, 10)}</span>
                        <strong style="color: ${yrColorHex}; font-size: 0.9rem;">
                            ${doneCount}/${META_POR_DISCIPLINA} (${yrPct}%)
                        </strong>
                    </div>
                </div>
            `;
        });

        const subjectIcons = {
            'História': '<i class="ph ph-book-bookmark"></i>',
            'Ciências': '<i class="ph ph-flask"></i>',
            'Geografia': '<i class="ph ph-globe-hemisphere-west"></i>',
            'Matemática': '<i class="ph ph-function"></i>',
            'Português': '<i class="ph ph-text-aa"></i>',
            'Belas Artes': '<i class="ph ph-palette"></i>',
            'Bíblia': '<i class="ph ph-book-open"></i>'
        };
        const icon = subjectIcons[sub] || '<i class="ph ph-book-open"></i>';

        discHTML += `
            <div class="kpi-card glass-panel card-entered" style="padding-bottom: 15px; transition-delay: ${idx * 0.05}s;">
                <div class="kpi-icon ${color}">${icon}</div>
                <div class="kpi-data" style="width: 100%;">
                    <h3>${sub}</h3>
                    <p style="margin-bottom: 12px; font-size: 1.3rem;">
                        <strong>${pct}%</strong> <span style="font-size: 1rem; opacity: 0.8">(${st.d}/${totalMetaDisciplina})</span>
                    </p>
                    <div style="width: 100%; height: 8px; background: rgba(255,255,255,0.1); border-radius: 4px; margin-bottom: 15px; overflow: hidden;">
                        <div style="width: ${pct}%; height: 100%; background: ${getProgressColorHex(pct)}; transition: width 0.3s;"></div>
                    </div>
                    <small style="opacity: 0.6; display:block; text-transform: uppercase; font-size: 0.7rem; letter-spacing: 1px; margin-bottom: 10px;">Meta: ${META_POR_DISCIPLINA} aulas/ano</small>
                    <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 10px;">
                        ${yearRowsHTML}
                    </div>
                </div>
            </div>
        `;
    });

    document.getElementById('disciplines-grid').innerHTML = discHTML;

    // --- 2. Chart: Cumprimento Ano a Ano ---
    const yearMonthMap = { 2: "Março", 3: "Abril", 1: "Maio", 4: "Junho", 5: "Julho" };

    const yLabels = [];
    const yDone = [];
    const yPend = [];
    [1, 2, 3, 4, 5].forEach(y => {
        yLabels.push(`${y}º Ano (${yearMonthMap[y]})`);
        yDone.push(yearStats[y].d);
        yPend.push(META_EQUIPE_ANO - yearStats[y].d);
    });

    const ctxY = document.getElementById('metasYearChart').getContext('2d');
    if (yearChartInstance) yearChartInstance.destroy();
    yearChartInstance = new Chart(ctxY, {
        type: 'bar',
        data: {
            labels: yLabels,
            datasets: [
                { label: 'Produzidas', data: yDone, backgroundColor: '#10b981' },
                { label: 'Pendentes', data: yPend, backgroundColor: '#94a3b8' }
            ]
        },
        options: {
            responsive: true, maintainAspectRatio: false,
            scales: { x: { stacked: true }, y: { stacked: true } },
            plugins: { legend: { labels: { color: '#cbd5e1' } } }
        }
    });

    // --- 3. Chart: Volume Disciplina ---
    const ctxS = document.getElementById('metasSubjectChart').getContext('2d');
    if (subjectChartInstance) subjectChartInstance.destroy();
    subjectChartInstance = new Chart(ctxS, {
        type: 'doughnut',
        data: {
            labels: sortedSubs.slice(0, 5),
            datasets: [{
                data: sortedSubs.slice(0, 5).map(s => subjectStats[s].t),
                backgroundColor: ['#3b82f6', '#8b5cf6', '#10b981', '#f59e0b', '#ef4444'],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true, maintainAspectRatio: false,
            plugins: { legend: { position: 'bottom', labels: { color: '#cbd5e1' } } }
        }
    });

    // --- 4. Saúde das Metas por Disciplina ---
    renderSubjectHealth(items);
}

function getMetaHealth(remaining, targetMonth) {
    const currentDate = new Date();
    const currentMonth = currentDate.getMonth() + 1;
    const currentYear = currentDate.getFullYear();
    const dayOfMonth = currentDate.getDate();

    let monthsLeft = 0;
    let isOverdue = false;

    if (targetMonth < currentMonth) {
        monthsLeft = 0;
        isOverdue = true;
    } else {
        monthsLeft = targetMonth - currentMonth;
    }

    const daysInTargetMonth = new Date(currentYear, targetMonth, 0).getDate();
    const daysRemaining = (monthsLeft - 1) * 30 + (daysInTargetMonth - dayOfMonth);

    let velocityNeeded = 0;
    if (remaining > 0) {
        if (monthsLeft === 0) {
            velocityNeeded = remaining;
        } else {
            velocityNeeded = Math.ceil(remaining / monthsLeft);
        }
    }

    let health = 'healthy';
    let healthIcon = '<i class="ph ph-heart"></i>';
    let healthMsg = 'No prazo';
    let healthColor = 'var(--color-success-light)';

    if (remaining === 0) {
        health = 'completed';
        healthIcon = '<i class="ph ph-seal-check"></i>';
        healthMsg = 'Meta atingida!';
        healthColor = 'var(--color-success-light)';
    } else if (isOverdue || (monthsLeft === 0 && remaining > 0)) {
        health = 'critical';
        healthIcon = '<i class="ph ph-warning-circle"></i>';
        healthMsg = 'ATRASADO';
        healthColor = 'var(--color-danger-light)';
    } else if (remaining > velocityNeeded * monthsLeft * 1.5) {
        health = 'warning';
        healthIcon = '<i class="ph ph-heartbeat"></i>';
        healthMsg = 'Atenção';
        healthColor = 'var(--color-warning-light)';
    }

    return { health, healthIcon, healthMsg, healthColor, monthsLeft, daysRemaining, velocityNeeded, isOverdue };
}

function renderSubjectHealth(items) {
    const META_POR_DISCIPLINA_ANO = 168;
    const NUM_ANOS = 5;
    const META_POR_DISCIPLINA_TOTAL = META_POR_DISCIPLINA_ANO * NUM_ANOS;

    const subjectStats = {};

    items.forEach(i => {
        const sub = normalizeSubject(i.subject);
        if (!sub) return;
        const status = i.status;
        const year = i.year;

        if (!subjectStats[sub]) {
            subjectStats[sub] = { done: 0, backlog: 0, inProgress: 0, review: 0, video: 0, years: {} };
        }

        if (status === 'Done/Published') subjectStats[sub].done++;
        else if (status === 'Backlog') subjectStats[sub].backlog++;
        else if (status === 'In Progress') subjectStats[sub].inProgress++;
        else if (status === 'In Review') subjectStats[sub].review++;
        else if (status === 'Video') subjectStats[sub].video++;

        if (year) {
            if (!subjectStats[sub].years[year]) subjectStats[sub].years[year] = { produced: 0 };
            if (isProduced(status)) subjectStats[sub].years[year].produced++;
        }
    });

    let html = '';
    const sorted = Object.keys(subjectStats).sort((a, b) => subjectStats[b].done - subjectStats[a].done);

    sorted.forEach(sub => {
        const stats = subjectStats[sub];
        const totalProduced = stats.review + stats.video + stats.done;
        const remaining = Math.max(0, META_POR_DISCIPLINA_TOTAL - totalProduced);
        const healthData = getMetaHealth(remaining, 6);
        const pct = Math.round((totalProduced / META_POR_DISCIPLINA_TOTAL) * 100);
        const inFlow = stats.inProgress + stats.review + stats.video;

        const cardStyle = healthData.health === 'critical' ? 'border-left: 4px solid var(--color-danger);' :
            healthData.health === 'warning' ? 'border-left: 4px solid var(--color-warning);' :
                healthData.health === 'completed' ? 'border-left: 4px solid var(--color-success);' : '';

        html += `
            <div class="insight-item animate-fade-in" style="${cardStyle} margin: 0;">
                <div class="insight-item-title" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                    <span style="display: flex; align-items: center; gap: 8px;">
                        ${getSubjectIcon(sub)}
                        <strong>${sub}</strong>
                    </span>
                    <span style="font-size: 1.2rem; font-weight: 700; color: ${healthData.healthColor};">${pct}%</span>
                </div>
                <div class="insight-item-desc">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 0.85rem;">
                        <span>Produzido: <strong style="color: var(--color-success-light);">${totalProduced}</strong> / ${META_POR_DISCIPLINA_TOTAL}</span>
                        <span>Faltando: <strong>${remaining}</strong></span>
                    </div>
                    <div style="width: 100%; height: 6px; background: rgba(255,255,255,0.1); border-radius: 3px; overflow: hidden; margin-bottom: 10px;">
                        <div style="width: ${Math.min(pct, 100)}%; height: 100%; background: ${healthData.health === 'completed' ? 'var(--color-success)' : (healthData.health === 'critical' ? 'var(--color-danger)' : (healthData.health === 'warning' ? 'var(--color-warning)' : 'var(--color-primary)'))}; transition: width 0.3s;"></div>
                    </div>
                    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; font-size: 0.7rem; margin-bottom: 10px;">
                        <div style="text-align: center; padding: 4px; background: rgba(0,0,0,0.2); border-radius: 4px;">
                            <div style="color: var(--color-warning-light); font-weight: 600;">${stats.backlog}</div>
                            <div style="color: var(--text-muted);">Backlog</div>
                        </div>
                        <div style="text-align: center; padding: 4px; background: rgba(0,0,0,0.2); border-radius: 4px;">
                            <div style="color: var(--color-primary-light); font-weight: 600;">${inFlow}</div>
                            <div style="color: var(--text-muted);">Em Fluxo</div>
                        </div>
                        <div style="text-align: center; padding: 4px; background: rgba(0,0,0,0.2); border-radius: 4px;">
                            <div style="color: var(--color-success-light); font-weight: 600;">${stats.done}</div>
                            <div style="color: var(--text-muted);">Feito</div>
                        </div>
                        <div style="text-align: center; padding: 4px; background: rgba(0,0,0,0.2); border-radius: 4px;">
                            <div style="color: ${healthData.healthColor}; font-weight: 600;">${Math.max(0, healthData.daysRemaining)}</div>
                            <div style="color: var(--text-muted);">Dias</div>
                        </div>
                    </div>
                    <div style="font-size: 0.75rem; color: var(--text-muted); border-top: 1px solid var(--border-glass); padding-top: 8px; display: flex; justify-content: space-between; align-items: center;">
                        <span style="color: ${healthData.healthColor};">${healthData.healthIcon} ${healthData.healthMsg}</span>
                        ${remaining > 0 ? `<span><i class="ph ph-lightning"></i> Precisa: <strong>${healthData.velocityNeeded}/mês</strong></span>` : ''}
                    </div>
                </div>
            </div>
        `;
    });

    const container = document.getElementById('subject-health-container');
    if (container) {
        container.innerHTML = html || '<div class="insight-item">Nenhum dado de disciplina encontrado.</div>';
    }
}
