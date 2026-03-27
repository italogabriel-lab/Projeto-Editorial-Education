let teamChartInstance = null;

const META_POR_DISCIPLINA = 168;
const NUM_DISCIPLINAS = 7;
const META_EQUIPE_ANO = META_POR_DISCIPLINA * NUM_DISCIPLINAS;
const NUM_ANOS = 5;
const META_TOTAL = META_EQUIPE_ANO * NUM_ANOS;

const goalsList = {
    1: { monthName: "Maio", monthNum: 4 },
    2: { monthName: "Março", monthNum: 2 },
    3: { monthName: "Abril", monthNum: 3 },
    4: { monthName: "Junho", monthNum: 5 },
    5: { monthName: "Julho", monthNum: 6 }
};

function getProgressColorHex(pct) {
    if (pct >= 100) return '#34d399';
    if (pct >= 50) return '#60a5fa';
    if (pct > 0) return '#fb923c';
    return '#94a3b8';
}

function renderProgressBar(pct, width = 20) {
    const filled = Math.round((pct / 100) * width);
    const empty = width - filled;
    return '█'.repeat(Math.max(0, filled)) + '░'.repeat(Math.max(0, empty));
}

function getDaysRemainingInMonth(targetMonth) {
    const now = new Date();
    const currentYear = now.getFullYear();
    const currentMonth = now.getMonth() + 1;
    
    let targetYear = currentYear;
    if (targetMonth < currentMonth) {
        targetYear = currentYear + 1;
    }
    
    const lastDayOfMonth = new Date(targetYear, targetMonth, 0).getDate();
    const remainingDays = lastDayOfMonth - now.getDate();
    
    return remainingDays > 0 ? remainingDays : 0;
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
        'matemática': 'Matemática',
        'portugues': 'Linguagem',
        'português': 'Linguagem'
    };
    return map[lower] || name;
}

async function performSync() {
    try {
        const response = await fetch('public/data.json?t=' + new Date().getTime());
        const data = await response.json();
        
        document.getElementById('last-sync-time').textContent = new Date(data.last_updated).toLocaleString();
        
        const items = data.items || [];
        renderProdutividade(items);
        
    } catch (e) {
        console.error("Error loading data:", e);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    performSync();
    setInterval(performSync, 60000);
});

function renderProdutividade(items) {
    const userStats = {};
    const META_POR_DISCIPLINA = 168;
    
    items.forEach(i => {
        const user = i.assignee || 'Unassigned';
        const sub = normalizeSubject(i.subject);
        const year = i.year;
        const status = i.status;
        
        if (!userStats[user]) {
            userStats[user] = {
                subjects: {},
                years: { 
                    1: {done: 0, pending: 0, inProgress: 0, review: 0, video: 0, backlog: 0}, 
                    2: {done: 0, pending: 0, inProgress: 0, review: 0, video: 0, backlog: 0},
                    3: {done: 0, pending: 0, inProgress: 0, review: 0, video: 0, backlog: 0},
                    4: {done: 0, pending: 0, inProgress: 0, review: 0, video: 0, backlog: 0},
                    5: {done: 0, pending: 0, inProgress: 0, review: 0, video: 0, backlog: 0}
                }
            };
        }
        
        if (sub) {
            if (!userStats[user].subjects[sub]) userStats[user].subjects[sub] = 0;
            userStats[user].subjects[sub]++;
        }
        
        if (year && userStats[user].years[year]) {
            if (status === 'Done/Published') {
                userStats[user].years[year].done++;
            } else if (status === 'Backlog') {
                userStats[user].years[year].backlog++;
                userStats[user].years[year].pending++;
            } else if (status === 'In Progress') {
                userStats[user].years[year].inProgress++;
                userStats[user].years[year].pending++;
            } else if (status === 'In Review') {
                userStats[user].years[year].review++;
            } else if (status === 'Video') {
                userStats[user].years[year].video++;
            }
        }
    });
    
    const userKeys = Object.keys(userStats).filter(u => u !== 'Unassigned');
    
    let rankingHTML = '';
    userKeys.forEach(u => {
        const o = userStats[u];
        const now = new Date();
        const currentMonth = now.getMonth() + 1;
        
        let totalDoneAllYears = 0;
        let totalPendingAllYears = 0;
        
        let yearsHTML = '';
        [1,2,3,4,5].forEach(yr => {
            const yrData = o.years[yr];
            const done = yrData.done;
            const inProgress = yrData.inProgress;
            const backlog = yrData.backlog;
            const review = yrData.review;
            const video = yrData.video;
            const pendingNow = inProgress + backlog;
            const remaining = META_POR_DISCIPLINA - done;
            
            totalDoneAllYears += done;
            totalPendingAllYears += pendingNow;
            
            const targetMonth = goalsList[yr].monthNum;
            const targetMonthName = goalsList[yr].monthName;
            
            let targetYear = now.getFullYear();
            if (targetMonth < currentMonth) {
                targetYear = now.getFullYear() + 1;
            }
            
            const lastDayOfMonth = new Date(targetYear, targetMonth, 0).getDate();
            const daysRemaining = lastDayOfMonth - now.getDate();
            const velocityNeeded = daysRemaining > 0 ? Math.ceil(remaining / daysRemaining) : remaining;
            
            const pct = Math.round((done / META_POR_DISCIPLINA) * 100);
            
            let yrStatusColor = '#94a3b8';
            if (pct >= 100) yrStatusColor = '#10b981';
            else if (pct >= 50) yrStatusColor = '#3b82f6';
            else if (pct > 0) yrStatusColor = '#fb923c';
            else yrStatusColor = '#ef4444';
            
            const progressBar = '█'.repeat(Math.min(pct, 100) / 5) + '░'.repeat(20 - Math.min(pct, 100) / 5);
            
            let statusBadge = '';
            if (inProgress > 0 || backlog > 0) {
                statusBadge = `<span style="background: #f59e0b; color: #000; padding: 2px 6px; border-radius: 4px; font-size: 0.65rem; margin-left: 8px;">${inProgress + backlog} pendentes</span>`;
            } else if (review > 0 || video > 0) {
                statusBadge = `<span style="background: #8b5cf6; color: #fff; padding: 2px 6px; border-radius: 4px; font-size: 0.65rem; margin-left: 8px;">${review + video} em fluxo</span>`;
            }
            
            yearsHTML += `
                <div style="background: rgba(255,255,255,0.03); padding: 10px; border-radius: 6px; margin-bottom: 8px; border-left: 3px solid ${yrStatusColor};">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-weight: 600; font-size: 0.9rem;"><i class="ph ph-book-open"></i> Ano ${yr} (${targetMonthName})</span>
                        <span style="font-weight: 700; color: ${yrStatusColor};">${pct}%</span>
                    </div>
                    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; font-size: 0.7rem; margin-bottom: 6px;">
                        <div style="text-align: center;"><div style="color: #10b981;"><i class="ph ph-check-circle"></i> ${done}</div><div style="color: #94a3b8;">Feito</div></div>
                        <div style="text-align: center;"><div style="color: #f59e0b;"><i class="ph ph-clock"></i> ${pendingNow}</div><div style="color: #94a3b8;">Pendente</div></div>
                        <div style="text-align: center;"><div style="color: #8b5cf6;"><i class="ph ph-arrows-clockwise"></i> ${review + video}</div><div style="color: #94a3b8;">Em fluxo</div></div>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; font-size: 0.7rem; margin-bottom: 4px;">
                        <span style="color: #94a3b8;">${progressBar}</span>
                        <span style="font-weight: 700; color: ${yrStatusColor};"><i class="ph ph-lightning"></i> ${velocityNeeded}/dia</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; font-size: 0.65rem; color: #94a3b8;">
                        <span>Faltam: ${remaining}</span>
                        <span>Dias: ${daysRemaining}</span>
                    </div>
                </div>
            `;
        });
        
        const totalMeta = META_POR_DISCIPLINA * 5;
        const totalPct = Math.round((totalDoneAllYears / totalMeta) * 100);
        
        let totalStatusColor = '#f59e0b';
        if (totalPct >= 100) totalStatusColor = '#10b981';
        else if (totalPct >= 50) totalStatusColor = '#3b82f6';
        else if (totalPct > 0) totalStatusColor = '#fb923c';
        else totalStatusColor = '#ef4444';
        
        const totalProgressBar = '█'.repeat(Math.min(totalPct, 100) / 5) + '░'.repeat(20 - Math.min(totalPct, 100) / 5);
        
        rankingHTML += `
            <div class="insight-item animate-fade-in" style="margin: 0; border-left: 3px solid ${totalStatusColor};">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                    <div class="insight-item-title" style="font-size: 1.1rem;"><i class="ph ph-user"></i> @${u}</div>
                    <div style="text-align: right;">
                        <strong style="font-size: 1.4rem; color: ${totalStatusColor};">${totalPct}%</strong>
                        <div style="font-size: 0.75rem; opacity: 0.7;">${totalDoneAllYears}/${totalMeta} aulas</div>
                    </div>
                </div>
                
                <div style="margin-bottom: 12px;">
                    <div style="display: flex; justify-content: space-between; font-size: 0.85rem; margin-bottom: 6px;">
                        <span style="color: var(--text-muted);">Progresso Total (5 anos)</span>
                        <span>${totalProgressBar}</span>
                    </div>
                </div>
                
                <div style="border-top: 1px solid var(--border-glass); padding-top: 12px;">
                    <div style="font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;"><i class="ph ph-chart-bar"></i> Detalhamento por Ano</div>
                    ${yearsHTML}
                </div>
            </div>
        `;
    });
    
    rankingHTML += `
        <div class="insight-item" style="margin: 0; opacity: 0.7; background: rgba(255,255,255,0.02);">
            <div class="insight-item-title"><i class="ph ph-info"></i> Legenda de Status</div>
            <div class="insight-item-desc" style="font-size: 0.85rem;">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                    <div><i class="ph ph-check-circle"></i> <strong>Feito</strong> - Concluído</div>
                    <div><i class="ph ph-clock"></i> <strong>Pendente</strong> - Backlog + In Progress</div>
                    <div><i class="ph ph-arrows-clockwise"></i> <strong>Em fluxo</strong> - In Review + Video</div>
                    <div><i class="ph ph-lightning"></i> <strong>/dia</strong> - Velocidade necessária</div>
                </div>
                <br>
                <strong>Meta por colaborador:</strong> 168 aulas/ano × 5 anos = 840 aulas<br>
                <strong>Meses de entrega:</strong> Ano 2→Março | Ano 3→Abril | Ano 1→Maio | Ano 4→Junho | Ano 5→Julho
            </div>
        </div>
    `;
    
    document.getElementById('ranking-container').innerHTML = rankingHTML;

    // --- 2. Bottlenecks (Gargalos) ---
    let bottleneckHTML = '';
    
    if (userStats['Unassigned']) {
        const totalPending = Object.values(userStats['Unassigned'].years).reduce((sum, yr) => sum + (yr.inProgress + yr.backlog), 0);
        if (totalPending > 0) {
            bottleneckHTML += `
                <div class="insight-item danger animate-fade-in">
                    <div class="insight-item-title"><i class="ph ph-warning"></i> Tarefas Órfãs</div>
                    <div class="insight-item-desc">Há ${totalPending} tarefas sem dono.</div>
                </div>
            `;
        }
    }
    
    userKeys.forEach(u => {
        const o = userStats[u];
        const totalDone = Object.values(o.years).reduce((sum, yr) => sum + yr.done, 0);
        const totalPending = Object.values(o.years).reduce((sum, yr) => sum + (yr.inProgress + yr.backlog), 0);
        const totalMeta = META_POR_DISCIPLINA * 5;
        const pct = Math.round((totalDone / totalMeta) * 100) || 0;
        
        if (totalPending > 15 && pct < 40) {
            bottleneckHTML += `
                <div class="insight-item warning animate-fade-in">
                    <div class="insight-item-title"><i class="ph ph-warning"></i> Sobrecarga: @${u}</div>
                    <div class="insight-item-desc">Fila de ${totalPending} itens com baixa taxa de conclusão (${pct}%).</div>
                </div>
            `;
        }
    });
    
    if(!bottleneckHTML) bottleneckHTML = '<div class="insight-item success animate-fade-in"><i class="ph ph-check-circle"></i> Nenhum gargalo detectado na equipe.</div>';
    document.getElementById('bottleneck-list').innerHTML = bottleneckHTML;

    // --- 3. Balanceamento de Equipe (Chart) ---
    const ctx = document.getElementById('teamChart').getContext('2d');
    if(teamChartInstance) teamChartInstance.destroy();
    
    const doneData = userKeys.map(u => {
        return Object.values(userStats[u].years).reduce((sum, yr) => sum + yr.done, 0);
    });
    
    teamChartInstance = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: userKeys.map(u => '@' + u),
            datasets: [{
                data: doneData,
                backgroundColor: ['#f43f5e', '#a855f7', '#3b82f6', '#10b981', '#f59e0b', '#06b6d4'],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true, maintainAspectRatio: false,
            plugins: { legend: { position: 'right', labels: { color: '#cbd5e1' } } }
        }
    });
}
