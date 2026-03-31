let videosSubjectChartInstance = null;
let videosYearChartInstance = null;

// ============================================
// CONFIGURAÇÕES DA EQUIPE DE VÍDEO
// ============================================

// Responsáveis pela equipe de vídeo
const VIDEO_TEAM = ['ViniciusOsvaldo', 'Gabrielrdr', 'alissonvtz', 'RickMitre'];

// Metas por ano (mês alvo)
const VIDEO_GOALS = {
    1: { month: 6, label: "Junho" },
    2: { month: 4, label: "Abril" },
    3: { month: 5, label: "Maio" },
    4: { month: 7, label: "Julho" },
    5: { month: 8, label: "Agosto" }
};

// Status que contam como "produzido" para equipe de vídeo
const VIDEO_PRODUCED_STATUSES = ['Video', 'Done/Published'];

function isVideoProduced(status) {
    return VIDEO_PRODUCED_STATUSES.includes(status);
}

// Meta de aulas por ano para equipe de vídeo (ajuste conforme necessário)
const VIDEO_META_POR_ANO = {
    1: 100,  // 1º Ano
    2: 100,  // 2º Ano
    3: 100,  // 3º Ano
    4: 100,  // 4º Ano
    5: 100   // 5º Ano
};

// ============================================
// FUNÇÕES PRINCIPAIS
// ============================================

async function loadVideosData() {
    try {
        const response = await fetch('public/data.json?t=' + new Date().getTime());
        const data = await response.json();

        document.getElementById('last-sync-time').textContent = new Date(data.last_updated).toLocaleString();

        const allItems = data.items || [];
        
        // Filtrar apenas itens da equipe de vídeo
        const videoTeamItems = allItems.filter(i => 
            i.assignee && VIDEO_TEAM.includes(i.assignee)
        );

        console.log(`Videos Pipeline: ${videoTeamItems.length} itens da equipe de vídeo (de ${allItems.length} total)`);

        runVideoAnalyzer(videoTeamItems);
        runVideoProgressEngine(videoTeamItems);
        runVideoGargaloDetector(videoTeamItems);

    } catch (e) {
        console.error("Error loading data:", e);
        document.getElementById('kpi-total').textContent = "ERROR";
    }
}

function runVideoAnalyzer(items) {
    // KPIs
    const total = items.length;
    const review = items.filter(i => i.status === 'In Review').length;
    const blocked = items.filter(i => i.status === 'Block').length;
    
    // Em produção = Backlog + In Progress
    const producing = items.filter(i => 
        i.status === 'Backlog' || i.status === 'In Progress'
    ).length;

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

        const y = i.year;
        if (y && y >= 1 && y <= 5) {
            if (!years[y]) years[y] = 0;
            years[y]++;
        }
    });

    // Year chart (bar) - 5 anos
    const yearLabels = ['1º Ano', '2º Ano', '3º Ano', '4º Ano', '5º Ano'];
    const yearData = [1, 2, 3, 4, 5].map(y => years[y] || 0);

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
    const subLabels = Object.keys(subjects).sort((a, b) => subjects[b] - subjects[a]);
    const subData = subLabels.map(l => subjects[l]);
    const subColors = ['#8b5cf6', '#3b82f6', '#10b981', '#f59e0b', '#ef4444', '#ec4899', '#06b6d4'];

    const ctx2 = document.getElementById('videosSubjectChart').getContext('2d');
    if (videosSubjectChartInstance) videosSubjectChartInstance.destroy();
    videosSubjectChartInstance = new Chart(ctx2, {
        type: 'doughnut',
        data: {
            labels: subLabels,
            datasets: [{
                data: subData,
                backgroundColor: subColors.slice(0, subLabels.length),
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

    // Inicializar todos os membros da equipe de vídeo
    VIDEO_TEAM.forEach(user => {
        assignees[user] = { total: 0, backlog: 0, block: 0, review: 0, producing: 0, video: 0, done: 0 };
    });

    items.forEach(i => {
        const user = i.assignee;
        if (!user || !assignees[user]) return;

        assignees[user].total++;
        
        if (i.status === 'Backlog') assignees[user].backlog++;
        else if (i.status === 'Block') assignees[user].block++;
        else if (i.status === 'In Progress') assignees[user].producing++;
        else if (i.status === 'In Review') assignees[user].review++;
        else if (i.status === 'Video') assignees[user].video++;
        else if (i.status === 'Done/Published') assignees[user].done++;
    });

    // Ordenar por total (equipe fixa)
    const sorted = VIDEO_TEAM.filter(u => assignees[u].total > 0);

    const html = sorted.map(user => {
        const a = assignees[user];
        const produced = a.video + a.done;
        return `
            <div class="assignee-card glass-panel">
                <div class="assignee-header">
                    <span class="assignee-avatar">${user.charAt(0).toUpperCase()}</span>
                    <div class="assignee-info">
                        <h4>@${user}</h4>
                        <span class="assignee-total">${a.total} videos</span>
                    </div>
                </div>
                <div class="assignee-progress" style="margin: 12px 0; padding: 10px; background: rgba(16,185,129,0.1); border-radius: 6px;">
                    <div style="font-size: 0.75rem; color: var(--text-muted); margin-bottom: 4px;">Produzidos (Video + Done)</div>
                    <div style="font-size: 1.1rem; font-weight: 700; color: var(--color-success-light);">${produced} / ${a.total}</div>
                </div>
                <div class="assignee-phases">
                    <div class="phase-stat">
                        <span class="phase-count">${a.backlog}</span>
                        <span class="phase-label">Backlog</span>
                    </div>
                    <div class="phase-stat">
                        <span class="phase-count">${a.producing}</span>
                        <span class="phase-label">Em Progresso</span>
                    </div>
                    <div class="phase-stat">
                        <span class="phase-count">${a.block}</span>
                        <span class="phase-label">Block</span>
                    </div>
                    <div class="phase-stat highlight">
                        <span class="phase-count">${a.review}</span>
                        <span class="phase-label">Em Revisão</span>
                    </div>
                    <div class="phase-stat" style="border-left: 2px solid var(--color-success);">
                        <span class="phase-count" style="color: var(--color-success-light);">${a.video}</span>
                        <span class="phase-label">Em Vídeo</span>
                    </div>
                    <div class="phase-stat" style="border-left: 2px solid var(--color-success);">
                        <span class="phase-count" style="color: var(--color-success-light);">${a.done}</span>
                        <span class="phase-label">Done</span>
                    </div>
                </div>
            </div>
        `;
    }).join('');

    document.getElementById('assignee-grid').innerHTML = html || '<div class="empty-state">Nenhum responsável encontrado</div>';
}

function runVideoProgressEngine(items) {
    const yearStats = { 
        1: { total: 0, video: 0, done: 0, review: 0, backlog: 0, inProgress: 0, block: 0 }, 
        2: { total: 0, video: 0, done: 0, review: 0, backlog: 0, inProgress: 0, block: 0 },
        3: { total: 0, video: 0, done: 0, review: 0, backlog: 0, inProgress: 0, block: 0 },
        4: { total: 0, video: 0, done: 0, review: 0, backlog: 0, inProgress: 0, block: 0 },
        5: { total: 0, video: 0, done: 0, review: 0, backlog: 0, inProgress: 0, block: 0 }
    };

    items.forEach(i => {
        const y = i.year;
        if (y && yearStats[y]) {
            yearStats[y].total++;
            
            if (i.status === 'Backlog') yearStats[y].backlog++;
            else if (i.status === 'In Progress') yearStats[y].inProgress++;
            else if (i.status === 'In Review') yearStats[y].review++;
            else if (i.status === 'Video') yearStats[y].video++;
            else if (i.status === 'Done/Published') yearStats[y].done++;
            else if (i.status === 'Block') yearStats[y].block++;
        }
    });

    const currentDate = new Date();
    const currentMonth = currentDate.getMonth() + 1;
    const currentYear = currentDate.getFullYear();
    const dayOfMonth = currentDate.getDate();

    let metaHTML = '';

    [1, 2, 3, 4, 5].forEach(y => {
        const stats = yearStats[y];
        const goal = VIDEO_GOALS[y];
        const metaAno = VIDEO_META_POR_ANO[y];

        // Produzido = Video + Done
        const produced = stats.video + stats.done;
        const remaining = Math.max(0, metaAno - produced);
        const pct = metaAno > 0 ? Math.round((produced / metaAno) * 100) : 0;

        // Calcular meses restantes e status
        let monthsLeft = 0;
        let isOverdue = false;

        if (goal.month < currentMonth) {
            monthsLeft = 0;
            isOverdue = true;
        } else {
            monthsLeft = goal.month - currentMonth;
        }

        const daysInTargetMonth = new Date(currentYear, goal.month, 0).getDate();
        const daysRemaining = (monthsLeft - 1) * 30 + (daysInTargetMonth - dayOfMonth);

        // Calcular velocidade necessária
        let velocityNeeded = 0;
        if (remaining > 0) {
            if (monthsLeft === 0) {
                velocityNeeded = remaining;
            } else {
                velocityNeeded = Math.ceil(remaining / monthsLeft);
            }
        }

        // Determinar status/risco
        let riskClass = 'success';
        let riskIcon = '<i class="ph ph-check-circle"></i>';
        let riskMsg = '';

        if (produced === 0 && stats.total === 0) {
            riskClass = 'warning';
            riskIcon = '<i class="ph ph-calendar-blank"></i>';
            riskMsg = `<span style="color: var(--color-warning-light);">Sem atividades. Prazo: ${goal.label}.</span>`;
        } else if (pct >= 100) {
            riskClass = 'success';
            riskIcon = '<i class="ph ph-seal-check"></i>';
            riskMsg = '<span style="color: var(--color-success-light);">Meta atingida!</span>';
        } else if (isOverdue) {
            riskClass = 'danger';
            riskIcon = '<i class="ph ph-warning-circle"></i>';
            riskMsg = `<span style="color: var(--color-danger-light);">ATRASADO! Meta era ${goal.label}.</span>`;
        } else if (pct < 25 && monthsLeft <= 1) {
            riskClass = 'danger';
            riskIcon = '<i class="ph ph-warning"></i>';
            riskMsg = `<span style="color: var(--color-danger-light);">Risco Alto! Precisa acelerar.</span>`;
        } else if (pct < 50 && monthsLeft <= 2) {
            riskClass = 'warning';
            riskIcon = '<i class="ph ph-heartbeat"></i>';
            riskMsg = `<span style="color: var(--color-warning-light);">Atenção! Ritmo precisa aumentar.</span>`;
        } else {
            riskClass = 'success';
            riskIcon = '<i class="ph ph-clock"></i>';
            riskMsg = `<span style="color: var(--color-success-light);">No prazo. Prazo: ${goal.label}.</span>`;
        }

        const borderColor = riskClass === 'danger' ? 'var(--color-danger)' : 
                           (riskClass === 'warning' ? 'var(--color-warning)' : 
                           (pct >= 100 ? 'var(--color-success)' : 'var(--color-primary)'));

        metaHTML += `
            <div class="insight-item ${riskClass} animate-fade-in" style="border-left: 4px solid ${borderColor}; margin: 0;">
                <div class="insight-item-title" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                    <span style="display: flex; align-items: center; gap: 8px;">
                        ${riskIcon}
                        <strong>${y}º Ano — ${goal.label}</strong>
                    </span>
                    <span style="font-size: 1.2rem; font-weight: 700; color: ${pct >= 100 ? 'var(--color-success-light)' : (isOverdue ? 'var(--color-danger-light)' : 'inherit')};">${pct}%</span>
                </div>
                <div class="insight-item-desc">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 0.9rem;">
                        <span>Produzido (Video + Done): <strong style="color: var(--color-success-light);">${produced}</strong> / ${metaAno}</span>
                        <span>Faltando: <strong>${remaining}</strong></span>
                    </div>
                    <div style="width: 100%; height: 8px; background: rgba(255,255,255,0.1); border-radius: 4px; overflow: hidden; margin-bottom: 12px;">
                        <div style="width: ${Math.min(pct, 100)}%; height: 100%; background: ${pct >= 100 ? 'var(--color-success)' : (isOverdue ? 'var(--color-danger)' : 'var(--color-primary)')}; transition: width 0.3s;"></div>
                    </div>
                    
                    <div style="display: grid; grid-template-columns: repeat(6, 1fr); gap: 6px; font-size: 0.7rem; margin-bottom: 10px;">
                        <div style="text-align: center; padding: 6px 4px; background: rgba(0,0,0,0.2); border-radius: 4px;">
                            <div style="color: var(--color-warning-light); font-weight: 700; font-size: 0.9rem;">${stats.backlog}</div>
                            <div style="color: var(--text-muted); margin-top: 2px;">Backlog</div>
                        </div>
                        <div style="text-align: center; padding: 6px 4px; background: rgba(0,0,0,0.2); border-radius: 4px;">
                            <div style="color: var(--color-primary-light); font-weight: 700; font-size: 0.9rem;">${stats.inProgress}</div>
                            <div style="color: var(--text-muted); margin-top: 2px;">Em Progresso</div>
                        </div>
                        <div style="text-align: center; padding: 6px 4px; background: rgba(59,130,246,0.15); border-radius: 4px;">
                            <div style="color: #93c5fd; font-weight: 700; font-size: 0.9rem;">${stats.review}</div>
                            <div style="color: var(--text-muted); margin-top: 2px;">Em Revisão</div>
                        </div>
                        <div style="text-align: center; padding: 6px 4px; background: rgba(139,92,246,0.15); border-radius: 4px;">
                            <div style="color: #c4b5fd; font-weight: 700; font-size: 0.9rem;">${stats.video}</div>
                            <div style="color: var(--text-muted); margin-top: 2px;">Em Vídeo</div>
                        </div>
                        <div style="text-align: center; padding: 6px 4px; background: rgba(16,185,129,0.15); border-radius: 4px;">
                            <div style="color: var(--color-success-light); font-weight: 700; font-size: 0.9rem;">${stats.done}</div>
                            <div style="color: var(--text-muted); margin-top: 2px;">Done</div>
                        </div>
                        <div style="text-align: center; padding: 6px 4px; background: rgba(239,68,68,0.15); border-radius: 4px;">
                            <div style="color: var(--color-danger-light); font-weight: 700; font-size: 0.9rem;">${stats.block}</div>
                            <div style="color: var(--text-muted); margin-top: 2px;">Bloqueado</div>
                        </div>
                    </div>

                    <div style="background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.2); border-radius: 6px; padding: 10px 14px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center; font-size: 0.85rem;">
                        <span style="color: var(--color-success-light);"><i class="ph ph-check-square"></i> Produzido pela equipe de vídeo</span>
                        <strong style="color: var(--color-success-light); font-size: 1rem;">${produced} videos</strong>
                    </div>

                    <div style="font-size: 0.85rem; color: var(--text-muted); border-top: 1px solid var(--border-glass); padding-top: 10px; display: flex; justify-content: space-between; align-items: center;">
                        <span>${riskMsg}</span>
                        ${velocityNeeded > 0 ? `<span><i class="ph ph-lightning"></i> Precisa: <strong>${velocityNeeded}/mês</strong></span>` : ''}
                    </div>
                </div>
            </div>
        `;
    });

    document.getElementById('meta-container').innerHTML = metaHTML || '<div class="insight-item">Sem dados suficientes.</div>';
}

function runVideoGargaloDetector(items) {
    const assignees = {};
    const subjects = {};

    // Inicializar assignees
    VIDEO_TEAM.forEach(user => {
        assignees[user] = { total: 0, review: 0, block: 0, video: 0, done: 0, backlog: 0, inProgress: 0 };
    });

    items.forEach(i => {
        const user = i.assignee;
        if (!user || !assignees[user]) return;

        assignees[user].total++;
        
        if (i.status === 'Backlog') assignees[user].backlog++;
        else if (i.status === 'In Progress') assignees[user].inProgress++;
        else if (i.status === 'In Review') assignees[user].review++;
        else if (i.status === 'Video') assignees[user].video++;
        else if (i.status === 'Done/Published') assignees[user].done++;
        else if (i.status === 'Block') assignees[user].block++;

        const sub = i.subject || 'Outros';
        if (!subjects[sub]) subjects[sub] = 0;
        subjects[sub]++;
    });

    let gargaloHTML = '';

    // Check blocked items by assignee
    const blockedByAssignee = {};
    items.filter(i => i.status === 'Block').forEach(i => {
        const user = i.assignee;
        if (user && assignees[user]) {
            if (!blockedByAssignee[user]) blockedByAssignee[user] = 0;
            blockedByAssignee[user]++;
        }
    });

    Object.keys(blockedByAssignee).forEach(u => {
        gargaloHTML += `
            <div class="insight-item danger animate-fade-in">
                <div class="insight-item-title"><i class="ph ph-prohibit"></i> Bloqueado: @${u}</div>
                <div class="insight-item-desc">${blockedByAssignee[u]} video(s) bloqueado(s) aguardando desbloqueio.</div>
            </div>
        `;
    });

    // Check performance
    VIDEO_TEAM.forEach(u => {
        const a = assignees[u];
        if (a.total === 0) return;

        const produced = a.video + a.done;
        const producedPct = Math.round((produced / a.total) * 100) || 0;
        const inProgress = a.backlog + a.inProgress;

        if (a.block > 0 && a.block > a.total * 0.3) {
            gargaloHTML += `
                <div class="insight-item danger animate-fade-in">
                    <div class="insight-item-title"><i class="ph ph-warning-circle"></i> Muitos Bloqueios: @${u}</div>
                    <div class="insight-item-desc">${a.block} de ${a.total} videos bloqueados (${Math.round((a.block / a.total) * 100)}%).</div>
                </div>
            `;
        } else if (producedPct < 20 && a.total > 5) {
            gargaloHTML += `
                <div class="insight-item warning animate-fade-in">
                    <div class="insight-item-title"><i class="ph ph-warning"></i> Baixa Produção: @${u}</div>
                    <div class="insight-item-desc">Apenas ${producedPct}% produzidos (${produced}/${a.total}). ${inProgress} em andamento.</div>
                </div>
            `;
        } else if (producedPct >= 70 && a.total > 3) {
            gargaloHTML += `
                <div class="insight-item success animate-fade-in">
                    <div class="insight-item-title"><i class="ph ph-trophy"></i> Alta Performance: @${u}</div>
                    <div class="insight-item-desc">Excelente! ${producedPct}% produzidos (${produced} videos).</div>
                </div>
            `;
        }
    });

    // Subject bottleneck
    Object.keys(subjects).forEach(s => {
        if (subjects[s] > 50) {
            gargaloHTML += `
                <div class="insight-item warning animate-fade-in">
                    <div class="insight-item-title"><i class="ph ph-book-open"></i> Alto Volume: ${s}</div>
                    <div class="insight-item-desc">${subjects[s]} videos nesta disciplina. Considere redistribuir.</div>
                </div>
            `;
        }
    });

    document.getElementById('gargalo-container').innerHTML = gargaloHTML || 
        '<div class="insight-item success animate-fade-in"><i class="ph ph-check-circle"></i> Nenhum gargalo detectado. Equipe operando normalmente.</div>';
}

document.addEventListener('DOMContentLoaded', () => {
    loadVideosData();
    setInterval(loadVideosData, 60000);
});
