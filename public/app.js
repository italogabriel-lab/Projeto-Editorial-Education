let yearChartInstance = null;
let subjectChartInstance = null;

const META_POR_DISCIPLINA = 168;
const NUM_DISCIPLINAS = 7;
const META_EQUIPE_ANO = META_POR_DISCIPLINA * NUM_DISCIPLINAS;
const META_TOTAL = META_EQUIPE_ANO * 5;

const GOALS_LIST = {
    2: { month: 2, label: "Março" },
    3: { month: 3, label: "Abril" },
    1: { month: 4, label: "Maio" },
    4: { month: 5, label: "Junho" },
    5: { month: 6, label: "Julho" }
};

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
    
    const currentDate = new Date();
    const currentMonth = currentDate.getMonth() + 1;
    const currentYear = currentDate.getFullYear();
    const dayOfMonth = currentDate.getDate();
    
    const yearStats = { 
        1: {total: 0, done: 0, backlog: 0, inProgress: 0, review: 0, video: 0}, 
        2: {total: 0, done: 0, backlog: 0, inProgress: 0, review: 0, video: 0}, 
        3: {total: 0, done: 0, backlog: 0, inProgress: 0, review: 0, video: 0}, 
        4: {total: 0, done: 0, backlog: 0, inProgress: 0, review: 0, video: 0}, 
        5: {total: 0, done: 0, backlog: 0, inProgress: 0, review: 0, video: 0}
    };
    
    const subjects = {};
    
    items.forEach(i => {
        const y = i.year;
        const status = i.status;
        const sub = i.subject || 'Outros';
        
        if (!subjects[sub]) subjects[sub] = 0;
        subjects[sub]++;
        
        if (yearStats[y]) {
            yearStats[y].total++;
            if (status === 'Done/Published') yearStats[y].done++;
            else if (status === 'Backlog') yearStats[y].backlog++;
            else if (status === 'In Progress') yearStats[y].inProgress++;
            else if (status === 'In Review') yearStats[y].review++;
            else if (status === 'Video') yearStats[y].video++;
        }
    });
    
    let metaHTML = '';
    const renderOrder = [2, 3, 1, 4, 5];
    
    renderOrder.forEach(y => {
        const stats = yearStats[y];
        if (stats.total === 0) return;
        
        const goal = GOALS_LIST[y];
        const pct = Math.round((stats.done / META_EQUIPE_ANO) * 100);
        const remaining = META_EQUIPE_ANO - stats.done;
        
        const targetMonth = goal.month;
        let monthsLeft = 0;
        let isOverdue = false;
        
        if (targetMonth < currentMonth) {
            monthsLeft = 0;
            isOverdue = true;
        } else {
            monthsLeft = targetMonth - currentMonth;
        }
        
        const daysInTargetMonth = new Date(currentYear, targetMonth, 0).getDate();
        const daysRemainingInMonth = daysInTargetMonth - dayOfMonth;
        
        let velocityNeeded = 0;
        if (monthsLeft === 0 && remaining > 0) {
            velocityNeeded = remaining;
        } else if (monthsLeft > 0 && remaining > 0) {
            velocityNeeded = Math.ceil(remaining / monthsLeft);
        }
        
        let statusClass = 'success';
        let statusIcon = '<i class="ph ph-check-circle"></i>';
        let statusMsg = '';
        
        if (pct >= 100) {
            statusClass = 'success';
            statusIcon = '<i class="ph ph-check-circle"></i>';
            statusMsg = '<span style="color: var(--color-success-light);">Concluído!</span>';
        } else if (isOverdue) {
            statusClass = 'danger';
            statusIcon = '<i class="ph ph-warning-circle"></i>';
            statusMsg = `<span style="color: var(--color-danger-light);">ATRASADO! Meta era ${goal.label}.</span>`;
        } else if (pct < 25 && monthsLeft <= 1) {
            statusClass = 'danger';
            statusIcon = '<i class="ph ph-warning"></i>';
            statusMsg = `<span style="color: var(--color-danger-light);">Risco Alto! Precisa acelerar.</span>`;
        } else if (pct < 50 && monthsLeft <= 2) {
            statusClass = 'warning';
            statusIcon = '<i class="ph ph-warning"></i>';
            statusMsg = `<span style="color: var(--color-warning-light);">Atenção! Ritmo precisa aumentar.</span>`;
        } else {
            statusClass = 'success';
            statusIcon = '<i class="ph ph-clock"></i>';
            statusMsg = `<span style="color: var(--color-success-light);">No prazo. Prazo: ${goal.label}.</span>`;
        }
        
        const progressBarPct = Math.min(pct, 100);
        
        metaHTML += `
            <div class="insight-item ${statusClass} animate-fade-in" style="margin-bottom: 12px;">
                <div class="insight-item-title" style="display: flex; justify-content: space-between; align-items: center;">
                    <span>${statusIcon} ${y}º Ano — ${goal.label}</span>
                    <span style="font-size: 1.1rem; font-weight: 700; color: ${pct >= 100 ? 'var(--color-success-light)' : (isOverdue ? 'var(--color-danger-light)' : 'inherit')};">${pct}%</span>
                </div>
                <div class="insight-item-desc">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 0.85rem;">
                        <span>Produzido: <strong style="color: var(--color-success-light);">${stats.done}</strong> / ${META_EQUIPE_ANO}</span>
                        <span>Faltando: <strong>${remaining}</strong></span>
                    </div>
                    <div style="width: 100%; height: 8px; background: rgba(255,255,255,0.1); border-radius: 4px; overflow: hidden; margin-bottom: 8px;">
                        <div style="width: ${progressBarPct}%; height: 100%; background: ${pct >= 100 ? 'var(--color-success)' : (isOverdue ? 'var(--color-danger)' : (pct < 50 ? 'var(--color-warning)' : 'var(--color-primary)'))}; transition: width 0.3s;"></div>
                    </div>
                    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; font-size: 0.75rem; margin-bottom: 8px;">
                        <div style="text-align: center; padding: 4px; background: rgba(0,0,0,0.2); border-radius: 4px;">
                            <div style="color: var(--color-warning-light); font-weight: 600;">${stats.backlog}</div>
                            <div style="color: var(--text-muted);">Backlog</div>
                        </div>
                        <div style="text-align: center; padding: 4px; background: rgba(0,0,0,0.2); border-radius: 4px;">
                            <div style="color: var(--color-primary-light); font-weight: 600;">${stats.inProgress + stats.review + stats.video}</div>
                            <div style="color: var(--text-muted);">Em Fluxo</div>
                        </div>
                        <div style="text-align: center; padding: 4px; background: rgba(0,0,0,0.2); border-radius: 4px;">
                            <div style="color: var(--color-success-light); font-weight: 600;">${stats.done}</div>
                            <div style="color: var(--text-muted);">Concluído</div>
                        </div>
                    </div>
                    <div style="font-size: 0.8rem; color: var(--text-muted); border-top: 1px solid var(--border-glass); padding-top: 8px; display: flex; justify-content: space-between;">
                        <span>${statusMsg}</span>
                        ${velocityNeeded > 0 ? `<span><i class="ph ph-lightning"></i> Precisa: <strong>${velocityNeeded}/mês</strong></span>` : ''}
                    </div>
                </div>
            </div>
        `;
    });
    
    document.getElementById('meta-container').innerHTML = metaHTML || '<div class="insight-item">Sem dados suficientes.</div>';
    
    // Render Year Chart
    const ctxYear = document.getElementById('yearChart');
    if (ctxYear) {
        const labels = renderOrder.map(y => `${y}º Ano`);
        const doneData = renderOrder.map(y => yearStats[y].done);
        const pendingData = renderOrder.map(y => Math.max(0, META_EQUIPE_ANO - yearStats[y].done));
        
        if (yearChartInstance) yearChartInstance.destroy();
        yearChartInstance = new Chart(ctxYear.getContext('2d'), {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [
                    {
                        label: 'Concluídas',
                        data: doneData,
                        backgroundColor: 'rgba(16, 185, 129, 0.8)'
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
