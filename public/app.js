let yearChartInstance = null;
let subjectChartInstance = null;

const META_POR_DISCIPLINA = 168;
const NUM_DISCIPLINAS = 7;
const META_EQUIPE_ANO = META_POR_DISCIPLINA * NUM_DISCIPLINAS;
const META_TOTAL = META_EQUIPE_ANO * 5;

// Tudo que passou de "In Progress" é considerado produzido pela equipe de desenvolvimento
const PRODUCED_STATUSES = ['In Review', 'Video', 'Done/Published'];
function isProduced(status) {
    return PRODUCED_STATUSES.includes(status);
}

function normalizeSubject(name) {
    if (!name) return 'Outros';
    const lower = name.toLowerCase().trim();
    const map = {
        'historia': 'História', 'história': 'História', 'história': 'História',
        'ciência': 'Ciências', 'ciencias': 'Ciências', 'ciências': 'Ciências',
        'geogrfia': 'Geografia', 'geografia': 'Geografia',
        'matemática': 'Matemática', 'matematica': 'Matemática',
        'portugues': 'Linguagem', 'português': 'Linguagem', 'linguagem': 'Linguagem',
        'belas artes': 'Belas Artes', 'bíblia': 'Bíblia', 'outros': 'Outros'
    };
    return map[lower] || name;
}

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
        const sub = normalizeSubject(i.subject);

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
        // Produzido = tudo que passou de In Progress (In Review + Video + Done)
        const produced = stats.review + stats.video + stats.done;
        const pct = Math.round((produced / META_EQUIPE_ANO) * 100);
        const remaining = Math.max(0, META_EQUIPE_ANO - produced);

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
            statusMsg = '<span style="color: var(--color-success-light);">Meta atingida!</span>';
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
        const progressColor = pct >= 100 ? 'var(--color-success)' : (isOverdue ? 'var(--color-danger)' : (pct < 50 ? 'var(--color-warning)' : 'var(--color-primary)'));

        metaHTML += `
            <div class="insight-item ${statusClass} animate-fade-in" style="margin-bottom: 16px; padding: 20px;">
                <div class="insight-item-title" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                    <span style="font-size: 1.05rem;">${statusIcon} ${y}º Ano — ${goal.label}</span>
                    <span style="font-size: 1.3rem; font-weight: 700; color: ${pct >= 100 ? 'var(--color-success-light)' : (isOverdue ? 'var(--color-danger-light)' : 'inherit')};">${pct}%</span>
                </div>
                <div class="insight-item-desc">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 0.9rem;">
                        <span>Produzido: <strong style="color: var(--color-success-light);">${produced}</strong> / ${META_EQUIPE_ANO}</span>
                        <span>Faltando: <strong>${remaining}</strong></span>
                    </div>
                    <div style="width: 100%; height: 10px; background: rgba(255,255,255,0.1); border-radius: 5px; overflow: hidden; margin-bottom: 16px;">
                        <div style="width: ${progressBarPct}%; height: 100%; background: ${progressColor}; transition: width 0.3s;"></div>
                    </div>

                    <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 8px; font-size: 0.75rem; margin-bottom: 14px;">
                        <div style="text-align: center; padding: 8px 4px; background: rgba(0,0,0,0.2); border-radius: 6px;">
                            <div style="color: var(--color-warning-light); font-weight: 700; font-size: 0.95rem;">${stats.backlog}</div>
                            <div style="color: var(--text-muted); margin-top: 2px;">Backlog</div>
                        </div>
                        <div style="text-align: center; padding: 8px 4px; background: rgba(0,0,0,0.2); border-radius: 6px;">
                            <div style="color: var(--color-primary-light); font-weight: 700; font-size: 0.95rem;">${stats.inProgress}</div>
                            <div style="color: var(--text-muted); margin-top: 2px;">Em Progresso</div>
                        </div>
                        <div style="text-align: center; padding: 8px 4px; background: rgba(59,130,246,0.15); border-radius: 6px; border: 1px solid rgba(59,130,246,0.3);">
                            <div style="color: #93c5fd; font-weight: 700; font-size: 0.95rem;">${stats.review}</div>
                            <div style="color: var(--text-muted); margin-top: 2px;">Em Revisão</div>
                        </div>
                        <div style="text-align: center; padding: 8px 4px; background: rgba(139,92,246,0.15); border-radius: 6px; border: 1px solid rgba(139,92,246,0.3);">
                            <div style="color: #c4b5fd; font-weight: 700; font-size: 0.95rem;">${stats.video}</div>
                            <div style="color: var(--text-muted); margin-top: 2px;">Em Vídeo</div>
                        </div>
                        <div style="text-align: center; padding: 8px 4px; background: rgba(16,185,129,0.15); border-radius: 6px; border: 1px solid rgba(16,185,129,0.3);">
                            <div style="color: var(--color-success-light); font-weight: 700; font-size: 0.95rem;">${stats.done}</div>
                            <div style="color: var(--text-muted); margin-top: 2px;">Publicado</div>
                        </div>
                    </div>

                    <div style="background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.2); border-radius: 6px; padding: 10px 14px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center; font-size: 0.85rem;">
                        <span style="color: var(--color-success-light);"><i class="ph ph-check-square"></i> Produzido pela equipe de desenvolvimento</span>
                        <strong style="color: var(--color-success-light); font-size: 1rem;">${produced} aulas</strong>
                    </div>

                    <div style="font-size: 0.85rem; color: var(--text-muted); border-top: 1px solid var(--border-glass); padding-top: 10px; display: flex; justify-content: space-between; align-items: center;">
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
        const doneData = renderOrder.map(y => yearStats[y].review + yearStats[y].video + yearStats[y].done);
        const pendingData = renderOrder.map(y => Math.max(0, META_EQUIPE_ANO - (yearStats[y].review + yearStats[y].video + yearStats[y].done)));
        
        if (yearChartInstance) yearChartInstance.destroy();
        yearChartInstance = new Chart(ctxYear.getContext('2d'), {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [
                    {
                        label: 'Produzidas',
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
    
    // Render Subject Chart (Distribution) — todas as disciplinas (sem "Outros")
    const subLabels = Object.keys(subjects).filter(s => s !== 'Outros').sort((a, b) => subjects[b] - subjects[a]);
    const subData = subLabels.map(l => subjects[l]);
    const subColors = ['#3b82f6', '#8b5cf6', '#10b981', '#f59e0b', '#ef4444', '#ec4899', '#06b6d4'];

    const ctxSub = document.getElementById('subjectChart');
    if (ctxSub) {
        if (subjectChartInstance) subjectChartInstance.destroy();
        subjectChartInstance = new Chart(ctxSub.getContext('2d'), {
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
    
    console.log('Progress engine completed');
    
    // Render User Health
    renderUserHealth(items);
    // Render Subject Health
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
        healthIcon = '<i class="ph ph-heart-break"></i>';
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
    
    return {
        health,
        healthIcon,
        healthMsg,
        healthColor,
        monthsLeft,
        daysRemaining,
        velocityNeeded,
        isOverdue
    };
}

function renderUserHealth(items) {
    console.log('Rendering user health...');
    
    const userStats = {};
    const META_POR_USER = META_EQUIPE_ANO;
    
    items.forEach(i => {
        const user = i.assignee || 'Unassigned';
        const status = i.status;
        const year = i.year;
        
        if (!userStats[user]) {
            userStats[user] = {
                done: 0,
                backlog: 0,
                inProgress: 0,
                review: 0,
                video: 0,
                years: {}
            };
        }
        
        if (status === 'Done/Published') userStats[user].done++;
        else if (status === 'Backlog') userStats[user].backlog++;
        else if (status === 'In Progress') userStats[user].inProgress++;
        else if (status === 'In Review') userStats[user].review++;
        else if (status === 'Video') userStats[user].video++;

        if (year) {
            if (!userStats[user].years[year]) {
                userStats[user].years[year] = { produced: 0 };
            }
            if (isProduced(status)) {
                userStats[user].years[year].produced++;
            }
        }
    });
    
    let userHealthHTML = '';
    const sortedUsers = Object.keys(userStats)
        .filter(u => u !== 'Unassigned')
        .sort((a, b) => userStats[b].done - userStats[a].done);
    
    if (userStats['Unassigned'] && userStats['Unassigned'].backlog > 0) {
        const orphan = userStats['Unassigned'];
        const remaining = META_POR_USER;
        const healthData = getMetaHealth(remaining, 6);
        
        userHealthHTML += `
            <div class="insight-item warning animate-fade-in">
                <div class="insight-item-title" style="display: flex; justify-content: space-between; align-items: center;">
                    <span><i class="ph ph-user"></i> Tarefas Órfãs</span>
                    <span style="color: var(--color-warning-light);">⚠️ ${orphan.backlog} pendentes</span>
                </div>
                <div class="insight-item-desc">
                    <div style="font-size: 0.8rem; color: var(--text-muted);">Atenção: tarefas sem responsável atribuído</div>
                </div>
            </div>
        `;
    }
    
    sortedUsers.forEach(user => {
        const stats = userStats[user];
        const totalProduced = stats.review + stats.video + stats.done;
        const totalDone = totalProduced;
        const remaining = Math.max(0, META_POR_USER - totalProduced);
        const healthData = getMetaHealth(remaining, 6);
        
        const pct = Math.round((totalDone / META_POR_USER) * 100);
        const inFlow = stats.inProgress + stats.review + stats.video;
        
        const cardStyle = healthData.health === 'critical' ? 'border-left: 4px solid var(--color-danger);' :
                         healthData.health === 'warning' ? 'border-left: 4px solid var(--color-warning);' :
                         healthData.health === 'completed' ? 'border-left: 4px solid var(--color-success);' : '';
        
        userHealthHTML += `
            <div class="insight-item animate-fade-in" style="${cardStyle} margin: 0;">
                <div class="insight-item-title" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                    <span style="display: flex; align-items: center; gap: 8px;">
                        <i class="ph ph-user-circle" style="font-size: 1.2rem;"></i>
                        <strong>${user}</strong>
                    </span>
                    <span style="font-size: 1.2rem; font-weight: 700; color: ${healthData.healthColor};">${pct}%</span>
                </div>
                <div class="insight-item-desc">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 0.85rem;">
                        <span>Produzido: <strong style="color: var(--color-success-light);">${totalDone}</strong> / ${META_POR_USER}</span>
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
                            <div style="color: ${healthData.healthColor}; font-weight: 600;">${healthData.daysRemaining}</div>
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
    
    const container = document.getElementById('user-health-container');
    if (container) {
        container.innerHTML = userHealthHTML || '<div class="insight-item">Nenhum dado de usuário encontrado.</div>';
    }
}

function renderSubjectHealth(items) {
    console.log('Rendering subject health...');
    
    const subjectStats = {};
    const META_POR_DISCIPLINA_ANO = 168;
    const NUM_ANOS = 5;
    const META_POR_DISCIPLINA_TOTAL = META_POR_DISCIPLINA_ANO * NUM_ANOS;
    
    items.forEach(i => {
        const sub = normalizeSubject(i.subject);
        const status = i.status;
        const year = i.year;

        if (!subjectStats[sub]) {
            subjectStats[sub] = {
                done: 0,
                backlog: 0,
                inProgress: 0,
                review: 0,
                video: 0,
                years: {}
            };
        }
        
        if (status === 'Done/Published') subjectStats[sub].done++;
        else if (status === 'Backlog') subjectStats[sub].backlog++;
        else if (status === 'In Progress') subjectStats[sub].inProgress++;
        else if (status === 'In Review') subjectStats[sub].review++;
        else if (status === 'Video') subjectStats[sub].video++;

        if (year) {
            if (!subjectStats[sub].years[year]) {
                subjectStats[sub].years[year] = { produced: 0 };
            }
            if (isProduced(status)) {
                subjectStats[sub].years[year].produced++;
            }
        }
    });
    
    let subjectHealthHTML = '';
    const sortedSubjects = Object.keys(subjectStats)
        .sort((a, b) => subjectStats[b].done - subjectStats[a].done);
    
    sortedSubjects.forEach(sub => {
        const stats = subjectStats[sub];
        const totalProduced = stats.review + stats.video + stats.done;
        const totalDone = totalProduced;
        const remaining = Math.max(0, META_POR_DISCIPLINA_TOTAL - totalProduced);

        const avgYearProgress = Object.keys(stats.years).reduce((sum, yr) => {
            const yrProduced = stats.years[yr].produced || 0;
            return sum + (yrProduced / META_POR_DISCIPLINA_ANO) * 100;
        }, 0) / NUM_ANOS;
        
        const targetMonth = 6;
        const healthData = getMetaHealth(remaining, targetMonth);
        
        const pct = Math.round((totalDone / META_POR_DISCIPLINA_TOTAL) * 100);
        const inFlow = stats.inProgress + stats.review + stats.video;
        
        const cardStyle = healthData.health === 'critical' ? 'border-left: 4px solid var(--color-danger);' :
                         healthData.health === 'warning' ? 'border-left: 4px solid var(--color-warning);' :
                         healthData.health === 'completed' ? 'border-left: 4px solid var(--color-success);' : '';
        
        subjectHealthHTML += `
            <div class="insight-item animate-fade-in" style="${cardStyle} margin: 0;">
                <div class="insight-item-title" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                    <span style="display: flex; align-items: center; gap: 8px;">
                        <i class="ph ph-book-open" style="font-size: 1.2rem;"></i>
                        <strong>${sub}</strong>
                    </span>
                    <span style="font-size: 1.2rem; font-weight: 700; color: ${healthData.healthColor};">${pct}%</span>
                </div>
                <div class="insight-item-desc">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 0.85rem;">
                        <span>Produzido: <strong style="color: var(--color-success-light);">${totalDone}</strong> / ${META_POR_DISCIPLINA_TOTAL}</span>
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
                            <div style="color: ${healthData.healthColor}; font-weight: 600;">${healthData.daysRemaining}</div>
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
        container.innerHTML = subjectHealthHTML || '<div class="insight-item">Nenhum dado de disciplina encontrado.</div>';
    }
}
