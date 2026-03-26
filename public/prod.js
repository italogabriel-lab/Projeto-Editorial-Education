let teamChartInstance = null;

const META_POR_DISCIPLINA = 168;
const goalsList = {
    1: { monthName: "Maio", monthNum: 4 },
    2: { monthName: "Março", monthNum: 2 },
    3: { monthName: "Abril", monthNum: 3 },
    4: { monthName: "Junho", monthNum: 5 },
    5: { monthName: "Julho", monthNum: 6 }
};

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
                years: { 1: {done: 0, pending: 0}, 2: {done: 0, pending: 0}, 3: {done: 0, pending: 0}, 4: {done: 0, pending: 0}, 5: {done: 0, pending: 0} }
            };
        }
        
        if (sub) {
            if (!userStats[user].subjects[sub]) userStats[user].subjects[sub] = 0;
            userStats[user].subjects[sub]++;
        }
        
        if (year && userStats[user].years[year]) {
            if (status === 'Done/Published') {
                userStats[user].years[year].done++;
            } else if (status === 'Backlog' || status === 'In Progress') {
                userStats[user].years[year].pending++;
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
            const pending = yrData.pending;
            const remaining = META_POR_DISCIPLINA - done;
            
            totalDoneAllYears += done;
            totalPendingAllYears += pending;
            
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
            
            yearsHTML += `
                <div style="background: rgba(255,255,255,0.03); padding: 10px; border-radius: 6px; margin-bottom: 8px; border-left: 3px solid ${yrStatusColor};">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-weight: 600; font-size: 0.9rem;">Ano ${yr} (${targetMonthName})</span>
                        <span style="font-weight: 700; color: ${yrStatusColor};">${pct}%</span>
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; font-size: 0.75rem; margin-bottom: 6px;">
                        <div><span style="color: #94a3b8;">Feito:</span> <span style="color: #10b981; font-weight: 600;">${done}</span></div>
                        <div><span style="color: #94a3b8;">Faltam:</span> <span style="color: #fb923c; font-weight: 600;">${remaining}</span></div>
                        <div><span style="color: #94a3b8;">Dias:</span> <span style="font-weight: 600;">${daysRemaining}</span></div>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; font-size: 0.7rem; margin-bottom: 4px;">
                        <span style="color: #94a3b8;">${progressBar}</span>
                        <span style="font-weight: 700; color: ${yrStatusColor};">⚡ ${velocityNeeded}/dia</span>
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
            <div class="insight-item" style="margin: 0; border-left: 3px solid ${totalStatusColor};">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                    <div class="insight-item-title" style="font-size: 1.1rem;">@${u}</div>
                    <div style="text-align: right;">
                        <strong style="font-size: 1.4rem; color: ${totalStatusColor};">${totalPct}%</strong>
                        <div style="font-size: 0.75rem; opacity: 0.7;">${totalDoneAllYears}/${totalMeta} aulas</div>
                    </div>
                </div>
                
                <div style="margin-bottom: 12px;">
                    <div style="display: flex; justify-content: space-between; font-size: 0.85rem; margin-bottom: 6px;">
                        <span style="color: #94a3b8;">Progresso Total (5 anos)</span>
                        <span>${totalProgressBar}</span>
                    </div>
                </div>
                
                <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 12px;">
                    <div style="font-size: 0.75rem; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">Detalhamento por Ano</div>
                    ${yearsHTML}
                </div>
            </div>
        `;
    });
    
    rankingHTML += `
        <div class="insight-item" style="margin: 0; opacity: 0.7; background: rgba(255,255,255,0.02);">
            <div class="insight-item-title">📊 Meta por Colaborador</div>
            <div class="insight-item-desc">
                Cada colaborador: <strong>${META_POR_DISCIPLINA} aulas/ano</strong> × 5 anos = <strong>840 aulas</strong> no total.<br>
                <br>
                <strong>Mês de entrega por ano:</strong><br>
                • Ano 2 → Março | Ano 3 → Abril | Ano 1 → Maio<br>
                • Ano 4 → Junho | Ano 5 → Julho
            </div>
        </div>
    `;
    
    document.getElementById('ranking-container').innerHTML = rankingHTML;

    // --- 2. Bottlenecks (Gargalos) ---
    let bottleneckHTML = '';
    
    if (userStats['Unassigned']) {
        const totalPending = Object.values(userStats['Unassigned'].years).reduce((sum, yr) => sum + yr.pending, 0);
        if (totalPending > 0) {
            bottleneckHTML += `
                <div class="insight-item danger">
                    <div class="insight-item-title">⚠️ Tarefas Órfãs</div>
                    <div class="insight-item-desc">Há ${totalPending} tarefas sem dono.</div>
                </div>
            `;
        }
    }
    
    userKeys.forEach(u => {
        const o = userStats[u];
        const totalDone = Object.values(o.years).reduce((sum, yr) => sum + yr.done, 0);
        const totalPending = Object.values(o.years).reduce((sum, yr) => sum + yr.pending, 0);
        const totalMeta = META_POR_DISCIPLINA * 5;
        const pct = Math.round((totalDone / totalMeta) * 100) || 0;
        
        if (totalPending > 15 && pct < 40) {
            bottleneckHTML += `
                <div class="insight-item warning">
                    <div class="insight-item-title">Sobrecarga: @${u}</div>
                    <div class="insight-item-desc">Fila de ${totalPending} itens com baixa taxa de conclusão (${pct}%).</div>
                </div>
            `;
        }
    });
    
    if(!bottleneckHTML) bottleneckHTML = '<div class="insight-item success">Nenhum gargalo detectado.</div>';
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
