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
        document.getElementById('meta-container').innerHTML = `<div class="insight-item danger"><div class="insight-item-title">Data Error</div><div class="insight-item-desc">Não foi possível carregar data.json.</div></div>`;
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
    
    // Average Lead Time
    let totalLeadTime = 0;
    let countLeadTime = 0;
    doneItems.forEach(i => {
        if (i.lead_time_days !== null) {
            totalLeadTime += i.lead_time_days;
            countLeadTime++;
        }
    });
    
    const avgLeadTime = countLeadTime > 0 ? (totalLeadTime / countLeadTime).toFixed(1) : 0;
    
    document.getElementById('kpi-total').textContent = total;
    document.getElementById('kpi-done').textContent = done;
    document.getElementById('kpi-leadtime').textContent = `${avgLeadTime} dias`;
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
            <div class="insight-item ${riskClass}">
                <div class="insight-item-title">${y}º Ano Escolar</div>
                <div class="insight-item-desc">${pct}% Concluído (${stats.done}/${stats.total}). ${riskMsg}</div>
            </div>
        `;
    });
    
    document.getElementById('meta-container').innerHTML = metaHTML || '<div class="insight-item">Sem dados o suficiente.</div>';
    document.getElementById('kpi-risk').textContent = riskCount;
    
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

function runGargaloDetector(items) {
    const assignees = {};
    const subjects = {};
    
    items.forEach(i => {
        // Subjects mapping
        const sub = i.subject || 'Outros';
        if (!subjects[sub]) subjects[sub] = 0;
        subjects[sub]++;
        
        // Assignees mapping
        const user = i.assignee || 'Unassigned';
        if (!assignees[user]) assignees[user] = { total: 0, done: 0 };
        assignees[user].total++;
        if (i.status === 'Done/Published') assignees[user].done++;
    });
    
    let gargaloHTML = '';
    
    // Find unassigned tasks
    if (assignees['Unassigned']) {
        gargaloHTML += `
            <div class="insight-item warning">
                <div class="insight-item-title">Tickets Órfãos</div>
                <div class="insight-item-desc">Existem ${assignees['Unassigned'].total} tarefas sem nenhum usuário atribuído. Elas podem ser esquecidas na fila.</div>
            </div>
        `;
    }
    
    Object.keys(assignees).forEach(u => {
        if (u === 'Unassigned') return;
        const o = assignees[u];
        const pct = Math.round((o.done / o.total) * 100) || 0;
        if (pct < 10 && o.total > 5) {
            gargaloHTML += `
                <div class="insight-item danger">
                    <div class="insight-item-title">Alerta Usuário: @${u}</div>
                    <div class="insight-item-desc">Baixa produtividade ou alta carga de trabalho: apenas ${pct}% de conclusão (${o.done}/${o.total}). Risco de gargalo operacional localizado.</div>
                </div>
            `;
        } else if (pct > 90) {
            gargaloHTML += `
                <div class="insight-item success">
                    <div class="insight-item-title">Alta Perfomance: @${u}</div>
                    <div class="insight-item-desc">Ritmo excelente com ${pct}% de conclusão na sua fila.</div>
                </div>
            `;
        }
    });
    
    document.getElementById('gargalo-container').innerHTML = gargaloHTML || '<div class="insight-item">Nenhum gargalo de performance detectado no grupo ativo.</div>';
    
    // Draw subject chart
    const subLabels = Object.keys(subjects).slice(0, 5); // top 5
    const subData = subLabels.map(l => subjects[l]);
    
    const ctx = document.getElementById('subjectChart').getContext('2d');
    if (subjectChartInstance) subjectChartInstance.destroy();
    subjectChartInstance = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: subLabels,
            datasets: [{
                data: subData,
                backgroundColor: [
                    '#3b82f6', '#8b5cf6', '#10b981', '#f59e0b', '#ef4444'
                ],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { position: 'right', labels: { color: '#cbd5e1' } }
            }
        }
    });

}
