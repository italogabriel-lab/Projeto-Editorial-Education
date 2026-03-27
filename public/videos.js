let videosSubjectChartInstance = null;
let videosYearChartInstance = null;

async function loadVideosData() {
    try {
        const response = await fetch('public/data.json?t=' + new Date().getTime());
        const data = await response.json();
        
        document.getElementById('last-sync-time').textContent = new Date(data.last_updated).toLocaleString();
        
        const items = data.items || [];
        const videoItems = items.filter(i => i.status === 'Video');
        
        runVideoAnalyzer(videoItems);
        runVideoProgressEngine(videoItems);
        runVideoGargaloDetector(videoItems);
        
    } catch (e) {
        console.error("Error loading data:", e);
        document.getElementById('kpi-total').textContent = "ERROR";
    }
}

function runVideoAnalyzer(items) {
    const total = items.length;
    const review = items.filter(i => i.labels && i.labels.includes('In review')).length;
    const blocked = items.filter(i => i.labels && i.labels.includes('Block')).length;
    const producing = total - review - blocked;
    
    document.getElementById('kpi-total').textContent = total;
    document.getElementById('kpi-review').textContent = review;
    document.getElementById('kpi-producing').textContent = producing;
    document.getElementById('kpi-blocked').textContent = blocked;
    
    renderCharts(items);
    renderAssigneeCards(items);
}

function renderCharts(items) {
    const subjects = {};
    const years = {};
    
    items.forEach(i => {
        const sub = i.subject || 'Outros';
        if (!subjects[sub]) subjects[sub] = 0;
        subjects[sub]++;
        
        const y = i.year || 0;
        if (!years[y]) years[y] = 0;
        years[y]++;
    });
    
    // Year chart (bar)
    const yearLabels = Object.keys(years).filter(y => y > 0).map(y => y + 'º Ano').sort((a,b) => parseInt(a)-parseInt(b));
    const yearData = yearLabels.map(l => years[parseInt(l)]);
    
    const ctx1 = document.getElementById('videosYearChart').getContext('2d');
    if (videosYearChartInstance) videosYearChartInstance.destroy();
    videosYearChartInstance = new Chart(ctx1, {
        type: 'bar',
        data: {
            labels: yearLabels,
            datasets: [{
                label: 'Total Videos',
                data: yearData,
                backgroundColor: 'rgba(139, 92, 246, 0.8)'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: { grid: { color: 'rgba(255,255,255,0.05)' } },
                y: { grid: { color: 'rgba(255,255,255,0.05)' } }
            },
            plugins: { legend: { labels: { color: '#cbd5e1' } } }
        }
    });
    
    // Subject chart (doughnut)
    const subLabels = Object.keys(subjects);
    const subData = subLabels.map(l => subjects[l]);
    
    const ctx2 = document.getElementById('videosSubjectChart').getContext('2d');
    if (videosSubjectChartInstance) videosSubjectChartInstance.destroy();
    videosSubjectChartInstance = new Chart(ctx2, {
        type: 'doughnut',
        data: {
            labels: subLabels,
            datasets: [{
                data: subData,
                backgroundColor: ['#8b5cf6', '#3b82f6', '#10b981', '#f59e0b', '#ef4444', '#ec4899', '#06b6d4'],
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

function renderAssigneeCards(items) {
    const assignees = {};
    
    items.forEach(i => {
        const user = i.assignee || 'Unassigned';
        if (!assignees[user]) {
            assignees[user] = { total: 0, backlog: 0, block: 0, review: 0, producing: 0 };
        }
        assignees[user].total++;
        if (i.labels && i.labels.includes('Backlog')) assignees[user].backlog++;
        else if (i.labels && i.labels.includes('Block')) assignees[user].block++;
        else if (i.labels && i.labels.includes('In review')) assignees[user].review++;
        else assignees[user].producing++;
    });
    
    // Sort by total
    const sorted = Object.keys(assignees).sort((a,b) => assignees[b].total - assignees[a].total);
    
    const html = sorted.map(user => {
        if (user === 'Unassigned') return '';
        const a = assignees[user];
        return `
            <div class="assignee-card glass-panel">
                <div class="assignee-header">
                    <span class="assignee-avatar">${user.charAt(0).toUpperCase()}</span>
                    <div class="assignee-info">
                        <h4>@${user}</h4>
                        <span class="assignee-total">${a.total} videos</span>
                    </div>
                </div>
                <div class="assignee-phases">
                    <div class="phase-stat">
                        <span class="phase-count">${a.backlog}</span>
                        <span class="phase-label">Backlog</span>
                    </div>
                    <div class="phase-stat">
                        <span class="phase-count">${a.block}</span>
                        <span class="phase-label">Block</span>
                    </div>
                    <div class="phase-stat">
                        <span class="phase-count">${a.producing}</span>
                        <span class="phase-label">Produzindo</span>
                    </div>
                    <div class="phase-stat highlight">
                        <span class="phase-count">${a.review}</span>
                        <span class="phase-label">Revisão</span>
                    </div>
                </div>
            </div>
        `;
    }).join('');
    
    document.getElementById('assignee-grid').innerHTML = html || '<div class="empty-state">Nenhum responsável encontrado</div>';
}

function runVideoProgressEngine(items) {
    const goalsList = {
        1: { month: 4, label: "Abril" },
        2: { month: 3, label: "Março" },
        3: { month: 5, label: "Maio" }
    };
    
    const yearStats = { 1: {total:0, review:0}, 2: {total:0, review:0}, 3: {total:0, review:0} };
    
    items.forEach(i => {
        const y = i.year;
        if (yearStats[y]) {
            yearStats[y].total++;
            if (i.labels && i.labels.includes('In review')) yearStats[y].review++;
        }
    });
    
    const currentMonth = new Date().getMonth();
    let metaHTML = '';
    let riskCount = 0;
    
    Object.keys(yearStats).forEach(y => {
        const stats = yearStats[y];
        if (stats.total === 0) return;
        
        const pct = Math.round((stats.review / stats.total) * 100);
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
                riskMsg = `Risco: Alto. Meta para ${goal.label} e só tem ${pct}% em revisão.`;
                riskCount++;
            } else if (pct >= 80) {
                riskClass = 'success';
                riskMsg = `Excelente! ${pct}% em revisão.`;
            } else {
                riskClass = 'success';
                riskMsg = `Ritmo normal. Prazo: ${goal.label}.`;
            }
        }
        
        metaHTML += `
            <div class="insight-item ${riskClass} animate-fade-in">
                <div class="insight-item-title">🎬 ${y}º Ano Escolar</div>
                <div class="insight-item-desc">${pct}% Concluído (${stats.review}/${stats.total} em revisão). ${riskMsg}</div>
            </div>
        `;
    });
    
    document.getElementById('meta-container').innerHTML = metaHTML || '<div class="insight-item">Sem dados suficientes.</div>';
}

function runVideoGargaloDetector(items) {
    const assignees = {};
    const subjects = {};
    
    items.forEach(i => {
        const user = i.assignee || 'Unassigned';
        if (!assignees[user]) assignees[user] = { total: 0, review: 0, block: 0 };
        assignees[user].total++;
        if (i.labels && i.labels.includes('In review')) assignees[user].review++;
        if (i.labels && i.labels.includes('Block')) assignees[user].block++;
        
        const sub = i.subject || 'Outros';
        if (!subjects[sub]) subjects[sub] = 0;
        subjects[sub]++;
    });
    
    let gargaloHTML = '';
    
    // Check blocked items
    const blockedItems = items.filter(i => i.labels && i.labels.includes('Block'));
    if (blockedItems.length > 0) {
        const byAssignee = {};
        blockedItems.forEach(i => {
            const user = i.assignee || 'Unassigned';
            if (!byAssignee[user]) byAssignee[user] = 0;
            byAssignee[user]++;
        });
        Object.keys(byAssignee).forEach(u => {
            if (u === 'Unassigned') return;
            gargaloHTML += `
                <div class="insight-item danger animate-fade-in">
                    <div class="insight-item-title">⛔ Bloqueado: @${u}</div>
                    <div class="insight-item-desc">${byAssignee[u]} video(s) bloqueado(s) aguardando desbloqueio.</div>
                </div>
            `;
        });
    }
    
    // Check unassigned
    if (assignees['Unassigned']) {
        gargaloHTML += `
            <div class="insight-item warning animate-fade-in">
                <div class="insight-item-title">⚠️ Videos Órfãos</div>
                <div class="insight-item-desc">${assignees['Unassigned'].total} videos sem responsável atribuído.</div>
            </div>
        `;
    }
    
    // Check low performance
    Object.keys(assignees).forEach(u => {
        if (u === 'Unassigned') return;
        const a = assignees[u];
        const pct = Math.round((a.review / a.total) * 100) || 0;
        if (pct < 20 && a.total > 10) {
            gargaloHTML += `
                <div class="insight-item warning animate-fade-in">
                    <div class="insight-item-title">⚠️ Baixa Performance: @${u}</div>
                    <div class="insight-item-desc">Apenas ${pct}% em revisão (${a.review}/${a.total}). Ritmo abaixo do esperado.</div>
                </div>
            `;
        } else if (pct >= 80 && a.total > 5) {
            gargaloHTML += `
                <div class="insight-item success animate-fade-in">
                    <div class="insight-item-title">✅ Alta Performance: @${u}</div>
                    <div class="insight-item-desc">Excelente! ${pct}% dos videos em revisão.</div>
                </div>
            `;
        }
    });
    
    // Subject bottleneck
    Object.keys(subjects).forEach(s => {
        if (subjects[s] > 80) {
            gargaloHTML += `
                <div class="insight-item warning animate-fade-in">
                    <div class="insight-item-title">📚 Alto Volume: ${s}</div>
                    <div class="insight-item-desc">${subjects[s]} videos pendentes nesta disciplina. Considere redistribuir.</div>
                </div>
            `;
        }
    });
    
    document.getElementById('gargalo-container').innerHTML = gargaloHTML || '<div class="insight-item success animate-fade-in">✅ Nenhum gargalo detectado. Equipe operando normalmente.</div>';
}

document.addEventListener('DOMContentLoaded', () => {
    loadVideosData();
    setInterval(loadVideosData, 60000);
});