let yearChartInstance = null;
let subjectChartInstance = null;

async function performSync() {
    try {
        console.log('Fetching data.json...');
        const response = await fetch('public/data.json?t=' + new Date().getTime());
        
        if (!response.ok) {
            throw new Error('Network response was not ok: ' + response.status);
        }
        
        const data = await response.json();
        console.log('Data loaded:', data.total_items, 'items');
        
        document.getElementById('last-sync-time').textContent = new Date(data.last_updated).toLocaleString();
        
        const items = data.items || [];
        console.log('Processing', items.length, 'items');
        
        runAnalyzer(items);
        runProgressEngine(items);
        
    } catch (e) {
        console.error("Error loading data:", e);
        document.getElementById('kpi-total').textContent = "ERROR";
        document.getElementById('meta-container').innerHTML = `<div class="insight-item danger animate-fade-in"><div class="insight-item-title"><i class="ph ph-warning-circle"></i> Erro de Dados</div><div class="insight-item-desc">Não foi possível carregar data.json. Verifique a conexão.</div></div>`;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM loaded, starting sync...');
    performSync();
    setInterval(performSync, 60000);
});

function runAnalyzer(items) {
    console.log('Running analyzer...');
    const total = items.length;
    
    const doneItems = items.filter(i => i.status === 'Done/Published');
    const done = doneItems.length;
    
    const backlogItems = items.filter(i => i.status === 'Backlog');
    const backlog = backlogItems.length;
    
    const inProgressItems = items.filter(i => i.status === 'In Progress');
    const inProgress = inProgressItems.length;
    
    const reviewItems = items.filter(i => i.status === 'In Review');
    const review = reviewItems.length;
    
    const videoItems = items.filter(i => i.status === 'Video');
    const video = videoItems.length;
    
    const blockItems = items.filter(i => i.status === 'Block');
    const block = blockItems.length;
    
    const noStatusItems = items.filter(i => i.status === 'No Status' || !i.status);
    const noStatus = noStatusItems.length;
    
    console.log('KPIs:', { total, done, backlog, inProgress, review, video, block, noStatus });
    
    document.getElementById('kpi-total').textContent = total;
    document.getElementById('kpi-done').textContent = done;
    document.getElementById('kpi-backlog').textContent = backlog;
    document.getElementById('kpi-in-progress').textContent = inProgress;
    document.getElementById('kpi-review').textContent = review;
    document.getElementById('kpi-video').textContent = video;
    document.getElementById('kpi-block').textContent = block;
    document.getElementById('kpi-no-status').textContent = noStatus;
}

function runProgressEngine(items) {
    console.log('Running progress engine...');
    
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
    
    const currentMonth = new Date().getMonth();
    
    let metaHTML = '';
    const labels = [];
    const doneData = [];
    const pendingData = [];
    
    Object.keys(yearStats).forEach(y => {
        const stats = yearStats[y];
        if (stats.total === 0) return;
        
        labels.push(`${y}º Ano`);
        doneData.push(stats.done);
        pendingData.push(stats.total - stats.done);
        
        const pct = Math.round((stats.done / stats.total) * 100);
        
        const goal = goalsList[y];
        let riskClass = 'success';
        let riskMsg = 'Dentro da meta';
        
        if (goal) {
            const monthsLeft = goal.month - currentMonth;
            if (pct < 100 && monthsLeft < 0) {
                riskClass = 'danger';
                riskMsg = `Atrasado! Meta era ${goal.label}.`;
            } else if (pct < 50 && monthsLeft <= 1) {
                riskClass = 'warning';
                riskMsg = `Risco: Alto. Meta para ${goal.label} e só tem ${pct}% pronto.`;
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
                <div class="insight-item-title"><i class="ph ph-graduation-cap"></i> ${y}º Ano Escolar</div>
                <div class="insight-item-desc">${pct}% Concluído (${stats.done}/${stats.total}). ${riskMsg}</div>
            </div>
        `;
    });
    
    document.getElementById('meta-container').innerHTML = metaHTML || '<div class="insight-item">Sem dados suficientes.</div>';
    
    // Render Year Chart
    const ctxYear = document.getElementById('yearChart');
    if (ctxYear) {
        if (yearChartInstance) yearChartInstance.destroy();
        yearChartInstance = new Chart(ctxYear.getContext('2d'), {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [
                    {
                        label: 'Concluídas',
                        data: doneData,
                        backgroundColor: 'rgba(52, 211, 153, 0.8)'
                    },
                    {
                        label: 'Pendentes',
                        data: pendingData,
                        backgroundColor: 'rgba(148, 163, 184, 0.4)'
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
    
    // Render Subject Chart (Distribution)
    const subjects = {};
    items.forEach(i => {
        const sub = i.subject || 'Outros';
        if (!subjects[sub]) subjects[sub] = 0;
        subjects[sub]++;
    });
    
    const subLabels = Object.keys(subjects).slice(0, 5);
    const subData = subLabels.map(l => subjects[l]);
    
    const ctxSub = document.getElementById('subjectChart');
    if (ctxSub) {
        if (subjectChartInstance) subjectChartInstance.destroy();
        subjectChartInstance = new Chart(ctxSub.getContext('2d'), {
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
    
    console.log('Progress engine completed');
}
