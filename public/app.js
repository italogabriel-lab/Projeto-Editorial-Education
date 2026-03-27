let yearChartInstance = null;
let subjectChartInstance = null;

async function performSync() {
    try {
        const response = await fetch('public/data.json?t=' + new Date().getTime());
        const data = await response.json();
        
        document.getElementById('last-sync-time').textContent = new Date(data.last_updated).toLocaleString();
        
        const items = data.items || [];
        
        runAnalyzer(items);
        runProgressEngine(items);
        runGargaloDetector(items);
        
    } catch (e) {
        console.error("Error loading data:", e);
        document.getElementById('kpi-total').textContent = "ERROR";
        document.getElementById('meta-container').innerHTML = `<div class="insight-item danger animate-fade-in"><div class="insight-item-title">⚠️ Erro de Dados</div><div class="insight-item-desc">Não foi possível carregar data.json. Verifique a conexão.</div></div>`;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    performSync();
    // Auto-refresh every 60 seconds
    setInterval(performSync, 60000);
});
function runAnalyzer(items) {
    const total = items.length;
    const doneItems = items.filter(i => i.status === 'Done/Published');
    const done = doneItems.length;
    const inReviewItems = items.filter(i => i.status && i.status.toLowerCase().includes('review'));
    const inReview = inReviewItems.length;
    const inProgressItems = items.filter(i => i.status && !['Done/Published', 'Backlog', 'No Status'].includes(i.status));
    const inProgress = inProgressItems.length;
    
    document.getElementById('kpi-total').textContent = total;
    document.getElementById('kpi-done').textContent = done;
    document.getElementById('kpi-in-progress').textContent = inProgress;
    document.getElementById('kpi-review').textContent = inReview;
}

function runProgressEngine(items) {
    // Group by Year
    const goalsList = {
        2: { month: 2, label: "Março" },
        3: { month: 3, label: "Abril" },
        1: { month: 4, label: "Maio" },
        4: { month: 5, label: "Junho" },
        5: { month: 6, label: "Julho" }
    };
    
    const yearStats = { 1: {total:0, done:0}, 2: {total:0, done:0}, 3: {total:0, done:0}, 4: {total:0, done:0}, 5: {total:0, done:0} };
    
    items.forEach(i => {
        const y = i.year;
        if (yearStats[y]) {
            yearStats[y].total++;
            if (i.status === 'Done/Published') yearStats[y].done++;
        }
    });
    
    const currentMonth = new Date().getMonth(); // 0 is Jan
    
    let metaHTML = '';
    const labels = [];
    const doneData = [];
    const pendingData = [];
    
    let riskCount = 0;
    
    Object.keys(yearStats).forEach(y => {
        const stats = yearStats[y];
        if (stats.total === 0) return;
        
        labels.push(`${y}º Ano`);
        doneData.push(stats.done);
        pendingData.push(stats.total - stats.done);
        
        const pct = Math.round((stats.done / stats.total) * 100);
        
        // Evaluate Risk
        const goal = goalsList[y];
        let riskClass = 'success';
        let riskMsg = 'Dentro da meta';
        
        if (goal) {
            const monthsLeft = goal.month - currentMonth;
            if (pct < 100 && monthsLeft < 0) {
                riskClass = 'danger';
                riskMsg = `Atrasado! Meta era ${goal.label}.`;
                riskCount++;
            } else if (pct < 50 && monthsLeft <= 1) {
                riskClass = 'warning';
                riskMsg = `Risco: Alto. Meta para ${goal.label} e só tem ${pct}% pronto.`;
                riskCount++;
            } else if (pct === 100) {
                riskClass = 'success';
                riskMsg = 'Concluído!';
            } else {
                riskClass = 'success';
                riskMsg = `Ritmo normal. Prazo: ${goal.label}.`;
            }
        }
        
        metaHTML += `
            <div class="insight-item ${riskClass} animate-fade-in">
                <div class="insight-item-title">🎓 ${y}º Ano Escolar</div>
                <div class="insight-item-desc">${pct}% Concluído (${stats.done}/${stats.total}). ${riskMsg}</div>
            </div>
        `;
    });
    
    document.getElementById('meta-container').innerHTML = metaHTML || '<div class="insight-item">Sem dados o suficiente.</div>';
    
    // Render Chart
    const ctx = document.getElementById('yearChart').getContext('2d');
    if (yearChartInstance) yearChartInstance.destroy();
    yearChartInstance = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Concluídas',
                    data: doneData,
                    backgroundColor: 'rgba(52, 211, 153, 0.8)' // Emerald
                },
                {
                    label: 'Pendentes / In Progress',
                    data: pendingData,
                    backgroundColor: 'rgba(148, 163, 184, 0.4)' // Slate
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: { stacked: true, grid: { color: 'rgba(255,255,255,0.05)' } },
                y: { stacked: true, grid: { color: 'rgba(255,255,255,0.05)' } }
            },
            plugins: {
                legend: { labels: { color: '#cbd5e1' } }
            }
        }
    });
}

const META_POR_ANO = 168;

function runGargaloDetector(items) {
    const subjects = {};
    const assignees = {};
    
    const ACTIVE_STATUSES = ['Backlog', 'In Progress'];
    const DONE_STATUS = 'Done/Published';
    const EXCLUDED_STATUSES = ['In Review', 'Video', 'Block', 'No Status'];
    
    items.forEach(i => {
        const sub = i.subject || null;
        if (sub) {
            if (!subjects[sub]) subjects[sub] = 0;
            subjects[sub]++;
        }
        
        const user = i.assignee || 'Unassigned';
        if (!assignees[user]) {
            assignees[user] = { 
                pending: 0, 
                done: 0, 
                years: { 1: {p:0, d:0}, 2: {p:0, d:0}, 3: {p:0, d:0}, 4: {p:0, d:0}, 5: {p:0, d:0} },
                subjects: {}
            };
        }
        
        const status = i.status;
        const year = i.year;
        
        if (ACTIVE_STATUSES.includes(status)) {
            assignees[user].pending++;
            if (year && assignees[user].years[year]) {
                assignees[user].years[year].p++;
            }
        } else if (status === DONE_STATUS) {
            assignees[user].done++;
            if (year && assignees[user].years[year]) {
                assignees[user].years[year].d++;
            }
        }
        
        if (sub && (ACTIVE_STATUSES.includes(status) || status === DONE_STATUS)) {
            if (!assignees[user].subjects[sub]) assignees[user].subjects[sub] = 0;
            assignees[user].subjects[sub]++;
        }
    });
    
    let gargaloHTML = '';
    
    if (assignees['Unassigned'] && assignees['Unassigned'].pending > 0) {
        gargaloHTML += `
            <div class="insight-item warning animate-fade-in">
                <div class="insight-item-title">⚠️ Tickets Órfãos</div>
                <div class="insight-item-desc">Existen ${assignees['Unassigned'].pending} tarefas pendentes sem nenhum usuário atribuído.</div>
            </div>
        `;
    }
    
    Object.keys(assignees).forEach(u => {
        if (u === 'Unassigned') return;
        const o = assignees[u];
        if (o.pending === 0 && o.done === 0) return;
        
        const totalAssigned = o.pending + o.done;
        const totalMeta = META_POR_ANO * 5;
        const pct = Math.round((o.done / totalMeta) * 100) || 0;
        
        let yearDetails = '';
        [1,2,3,4,5].forEach(yr => {
            const yrData = o.years[yr];
            if (yrData.p === 0 && yrData.d === 0) return;
            const yrPct = Math.round((yrData.d / META_POR_ANO) * 100) || 0;
            yearDetails += `<div style="margin-top:4px; font-size:0.8rem;"><span style="color:#94a3b8;">Ano ${yr}:</span> ${yrData.d}/${META_POR_ANO} (${yrPct}%)</div>`;
        });
        
        if (pct < 20) {
            gargaloHTML += `
                <div class="insight-item danger animate-fade-in">
                    <div class="insight-item-title">⚠️ @${u} — Baixa Performance</div>
                    <div class="insight-item-desc">
                        <strong>${pct}%</strong> da meta total (${o.done}/${totalMeta}).<br>
                        <span style="color:var(--color-warning-light);">Pendente: ${o.pending}</span> | Concluído: ${o.done}<br>
                        ${yearDetails}
                    </div>
                </div>
            `;
        } else if (pct >= 50) {
            gargaloHTML += `
                <div class="insight-item success animate-fade-in">
                    <div class="insight-item-title">✅ @${u} — Excelente Performance</div>
                    <div class="insight-item-desc">
                        <strong>${pct}%</strong> da meta total (${o.done}/${totalMeta}).<br>
                        ${yearDetails}
                    </div>
                </div>
            `;
        }
    });
    
    document.getElementById('gargalo-container').innerHTML = gargaloHTML || '<div class="insight-item">Nenhum gargalo de performance detectado no grupo ativo.</div>';
    
    const subLabels = Object.keys(subjects).slice(0, 5);
    const subData = subLabels.map(l => subjects[l]);
    
    const ctx = document.getElementById('subjectChart').getContext('2d');
    if (subjectChartInstance) subjectChartInstance.destroy();
    subjectChartInstance = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: subLabels,
            datasets: [{
                data: subData,
                backgroundColor: ['#3b82f6', '#8b5cf6', '#10b981', '#f59e0b', '#ef4444'],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'right', labels: { color: '#cbd5e1' } } }
        }
    });
}
