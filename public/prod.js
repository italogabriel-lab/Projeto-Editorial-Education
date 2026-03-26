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
    
    items.forEach(i => {
        const user = i.assignee || 'Unassigned';
        const sub = normalizeSubject(i.subject);
        const year = i.year;
        const status = i.status;
        
        if (!userStats[user]) {
            userStats[user] = {
                subjects: {},
                years: { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0 },
                done: 0,
                pending: 0
            };
        }
        
        if (sub) {
            if (!userStats[user].subjects[sub]) userStats[user].subjects[sub] = 0;
            userStats[user].subjects[sub]++;
        }
        
        if (year) {
            userStats[user].years[year]++;
        }
        
        if (status === 'Done/Published') {
            userStats[user].done++;
        } else if (status === 'Backlog' || status === 'In Progress') {
            userStats[user].pending++;
        }
    });
    
    const userKeys = Object.keys(userStats).filter(u => u !== 'Unassigned');
    
    let rankingHTML = '';
    userKeys.forEach(u => {
        const o = userStats[u];
        
        const disciplinesCount = Object.keys(o.subjects).length;
        const metaTarget = META_POR_DISCIPLINA;
        const done = o.done;
        const pending = o.pending;
        const remaining = metaTarget - done;
        
        const now = new Date();
        const currentMonth = now.getMonth() + 1;
        const monthNames = ['', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'];
        
        let targetMonth = null;
        let targetMonthName = '';
        
        Object.keys(goalsList).forEach(yr => {
            const gm = goalsList[yr];
            if (gm.monthNum >= currentMonth) {
                if (!targetMonth || gm.monthNum < targetMonth) {
                    targetMonth = gm.monthNum;
                    targetMonthName = gm.monthName;
                }
            }
        });
        
        if (!targetMonth) {
            targetMonth = 12;
            targetMonthName = 'Dezembro';
        }
        
        const daysRemaining = getDaysRemainingInMonth(targetMonth);
        const velocityNeeded = daysRemaining > 0 ? Math.ceil(remaining / daysRemaining) : remaining;
        
        const pct = Math.round((done / metaTarget) * 100);
        
        let statusClass = 'warning';
        let statusMsg = 'Atenção';
        let velocityColor = '#f59e0b';
        
        if (pct >= 100) {
            statusClass = 'success';
            statusMsg = 'Meta Alcançada! 🎉';
            velocityColor = '#10b981';
        } else if (pct >= 50) {
            statusClass = 'warning';
            statusMsg = 'No caminho';
            velocityColor = '#3b82f6';
        } else if (pct < 20) {
            statusClass = 'danger';
            statusMsg = 'Precisa acelerar!';
            velocityColor = '#ef4444';
        }
        
        const progressBar = '█'.repeat(Math.min(pct, 100) / 5) + '░'.repeat(20 - Math.min(pct, 100) / 5);
        
        rankingHTML += `
            <div class="insight-item ${statusClass}" style="margin: 0;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                    <div class="insight-item-title" style="font-size: 1.1rem;">@${u}</div>
                    <div style="text-align: right;">
                        <strong style="font-size: 1.4rem; color: ${velocityColor};">${pct}%</strong>
                        <div style="font-size: 0.75rem; opacity: 0.7;">${statusMsg}</div>
                    </div>
                </div>
                
                <div style="background: rgba(255,255,255,0.05); padding: 12px; border-radius: 8px; margin-bottom: 12px;">
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; font-size: 0.9rem;">
                        <div>
                            <div style="color: #94a3b8; font-size: 0.75rem;">JÁ PRODUZIDO</div>
                            <div style="font-weight: 600; color: #10b981;">${done} aulas</div>
                        </div>
                        <div>
                            <div style="color: #94a3b8; font-size: 0.75rem;">META TOTAL</div>
                            <div style="font-weight: 600;">${metaTarget} aulas</div>
                        </div>
                    </div>
                </div>
                
                <div style="margin-bottom: 12px;">
                    <div style="display: flex; justify-content: space-between; font-size: 0.85rem; margin-bottom: 6px;">
                        <span style="color: #94a3b8;">Progresso</span>
                        <span>${progressBar}</span>
                    </div>
                    <div style="width: 100%; height: 10px; background: rgba(255,255,255,0.1); border-radius: 5px; overflow: hidden;">
                        <div style="width: ${Math.min(pct, 100)}%; height: 100%; background: ${velocityColor}; transition: width 0.3s;"></div>
                    </div>
                </div>
                
                <div style="background: rgba(0,0,0,0.2); padding: 12px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1);">
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; font-size: 0.9rem;">
                        <div>
                            <div style="color: #94a3b8; font-size: 0.75rem;">FALTAM</div>
                            <div style="font-weight: 600; color: #fb923c;">${remaining} aulas</div>
                        </div>
                        <div>
                            <div style="color: #94a3b8; font-size: 0.75rem;">DIAS ATÉ ${targetMonthName.toUpperCase()}</div>
                            <div style="font-weight: 600;">${daysRemaining} dias</div>
                        </div>
                    </div>
                    
                    <div style="margin-top: 12px; padding-top: 12px; border-top: 1px solid rgba(255,255,255,0.1); text-align: center;">
                        <div style="color: #94a3b8; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px;">VELOCIDADE NECESSÁRIA</div>
                        <div style="font-size: 1.8rem; font-weight: 700; color: ${velocityColor};">${velocityNeeded}</div>
                        <div style="font-size: 0.85rem; color: #94a3b8;">aulas/dia</div>
                    </div>
                </div>
            </div>
        `;
    });
    
    rankingHTML += `
        <div class="insight-item warning" style="margin: 0; opacity: 0.7;">
            <div class="insight-item-title">📊 Meta da Equipe</div>
            <div class="insight-item-desc">
                Cada colaborador precisa produzir <strong>${META_POR_DISCIPLINA} aulas</strong> por ano (168/disciplina × 1 disciplina).<br>
                Prazo: ${targetMonthName} ${now.getFullYear()}
            </div>
        </div>
    `;
    
    document.getElementById('ranking-container').innerHTML = rankingHTML;

    // --- 2. Bottlenecks (Gargalos) ---
    let bottleneckHTML = '';
    
    if (userStats['Unassigned'] && userStats['Unassigned'].pending > 0) {
        bottleneckHTML += `
            <div class="insight-item danger">
                <div class="insight-item-title">⚠️ Tarefas Órfãs</div>
                <div class="insight-item-desc">Há ${userStats['Unassigned'].pending} tarefas sem dono.</div>
            </div>
        `;
    }
    
    userKeys.forEach(u => {
        const o = userStats[u];
        const pct = Math.round((o.done / META_POR_DISCIPLINA) * 100) || 0;
        if (o.pending > 15 && pct < 40) {
            bottleneckHTML += `
                <div class="insight-item warning">
                    <div class="insight-item-title">Sobrecarga: @${u}</div>
                    <div class="insight-item-desc">Fila de ${o.pending} itens com baixa taxa de conclusão.</div>
                </div>
            `;
        }
    });
    
    if(!bottleneckHTML) bottleneckHTML = '<div class="insight-item success">Nenhum gargalo detectado.</div>';
    document.getElementById('bottleneck-list').innerHTML = bottleneckHTML;

    // --- 3. Balanceamento de Equipe (Chart) ---
    const ctx = document.getElementById('teamChart').getContext('2d');
    if(teamChartInstance) teamChartInstance.destroy();
    
    const doneData = userKeys.map(u => userStats[u].done);
    
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
