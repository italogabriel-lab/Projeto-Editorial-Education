let yearChartInstance = null;
let subjectChartInstance = null;

const META_POR_ANO = 168;

function normalizeSubject(name) {
    if (!name) return null;
    const lower = name.toLowerCase().trim();
    const map = {
        'historia': 'História',
        'história': 'História',
        'hi stória': 'História',
        'ciência': 'Ciências',
        'ciencias': 'Ciências',
        'geogrfia': 'Geografia',
        'matemática': 'Matemática',
        'portugues': 'Português',
        'português': 'Português'
    };
    return map[lower] || name;
}

function getProgressColor(pct) {
    if (pct >= 100) return 'green';
    if (pct >= 50) return 'blue';
    if (pct > 0) return 'orange';
    return 'gray';
}

function getProgressColorHex(pct) {
    if (pct >= 100) return '#34d399';
    if (pct >= 50) return '#60a5fa';
    if (pct > 0) return '#fb923c';
    return '#94a3b8';
}

function renderProgressBar(pct, width = 20) {
    const filled = Math.round((pct / 100) * width);
    const empty = width - filled;
    return '█'.repeat(filled) + '░'.repeat(empty);
}

async function performSync() {
    try {
        const response = await fetch('public/data.json?t=' + new Date().getTime());
        const data = await response.json();
        
        document.getElementById('last-sync-time').textContent = new Date(data.last_updated).toLocaleString();
        
        const items = data.items || [];
        
        renderMetas(items);
        
    } catch (e) {
        console.error("Error loading data:", e);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    performSync();
    setInterval(performSync, 60000);
});

function renderMetas(items) {
    const goalsList = {
        2: { monthName: "Março" },
        3: { monthName: "Abril" },
        1: { monthName: "Maio" },
        4: { monthName: "Junho" },
        5: { monthName: "Julho" }
    };
    
    const yearStats = { 1: {t:0, d:0}, 2: {t:0, d:0}, 3: {t:0, d:0}, 4: {t:0, d:0}, 5: {t:0, d:0} };
    const subjectStats = {};
    
    items.forEach(i => {
        const sub = normalizeSubject(i.subject);
        if (!sub) return;
        const y = i.year;
        
        if (!subjectStats[sub]) subjectStats[sub] = {t:0, d:0, years: {1:{}, 2:{}, 3:{}, 4:{}, 5:{}}};
        
        subjectStats[sub].t++;
        if (i.status === 'Done/Published') subjectStats[sub].d++;
        
        if (y && subjectStats[sub].years[y]) {
            if (!subjectStats[sub].years[y].t) subjectStats[sub].years[y] = {t:0, d:0};
            subjectStats[sub].years[y].t++;
            if (i.status === 'Done/Published') subjectStats[sub].years[y].d++;
        }
        
        if (y && yearStats[y]) {
            yearStats[y].t++;
            if (i.status === 'Done/Published') yearStats[y].d++;
        }
    });

    // --- 1. Cards de Disciplina ---
    let discHTML = '';
    const sortedSubs = Object.keys(subjectStats).sort((a,b) => subjectStats[b].t - subjectStats[a].t);
    
    sortedSubs.forEach(sub => {
        const st = subjectStats[sub];
        if(st.t === 0) return;
        
        const totalMeta = META_POR_ANO * 5;
        const pct = Math.round((st.d / totalMeta) * 100) || 0;
        const color = getProgressColor(pct);
        
        let yearRowsHTML = '';
        [1,2,3,4,5].forEach(ano => {
            const yr = st.years[ano] || {t:0, d:0};
            const hasData = yr.t > 0;
            const yrPct = hasData ? Math.round((yr.d / META_POR_ANO) * 100) : 0;
            const yrColorHex = hasData ? getProgressColorHex(yrPct) : '#94a3b8';
            
            yearRowsHTML += `
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; padding: 8px 12px; background: rgba(255,255,255,0.03); border-radius: 6px;">
                    <span style="color: #cbd5e1; font-weight: 500;">Ano ${ano}:</span>
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <span style="font-size: 0.85rem; color: #94a3b8;">${renderProgressBar(yrPct, 10)}</span>
                        <strong style="color: ${yrColorHex}; font-size: 0.9rem;">
                            ${hasData ? yr.d + '/' + META_POR_ANO + ' (' + yrPct + '%)' : '-/-'}
                        </strong>
                    </div>
                </div>
            `;
        });
        
        discHTML += `
            <div class="kpi-card glass-panel" style="padding-bottom: 15px;">
                <div class="kpi-icon ${color}">📚</div>
                <div class="kpi-data" style="width: 100%;">
                    <h3>${sub}</h3>
                    <p style="margin-bottom: 12px; font-size: 1.3rem;">
                        <strong>${pct}%</strong> <span style="font-size: 1rem; opacity: 0.8">(${st.d}/${totalMeta})</span>
                    </p>
                    <div style="width: 100%; height: 8px; background: rgba(255,255,255,0.1); border-radius: 4px; margin-bottom: 15px; overflow: hidden;">
                        <div style="width: ${pct}%; height: 100%; background: ${getProgressColorHex(pct)}; transition: width 0.3s;"></div>
                    </div>
                    <small style="opacity: 0.6; display:block; text-transform: uppercase; font-size: 0.7rem; letter-spacing: 1px; margin-bottom: 10px;">Meta: ${META_POR_ANO} aulas/ano</small>
                    <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 10px;">
                        ${yearRowsHTML}
                    </div>
                </div>
            </div>
        `;
    });
    document.getElementById('disciplines-grid').innerHTML = discHTML;

    // --- 2. Chart: Cumprimento Ano a Ano ---
    const yLabels = [];
    const yDone = [];
    const yPend = [];
    [1,2,3,4,5].forEach(y => {
        if(yearStats[y].t > 0) {
            yLabels.push(`${y}º Ano (${goalsList[y].monthName})`);
            yDone.push(yearStats[y].d);
            yPend.push(yearStats[y].t - yearStats[y].d);
        }
    });

    const ctxY = document.getElementById('metasYearChart').getContext('2d');
    if (yearChartInstance) yearChartInstance.destroy();
    yearChartInstance = new Chart(ctxY, {
        type: 'bar',
        data: {
            labels: yLabels,
            datasets: [
                { label: 'Concluídas', data: yDone, backgroundColor: '#10b981' },
                { label: 'Pendentes', data: yPend, backgroundColor: '#94a3b8' }
            ]
        },
        options: {
            responsive: true, maintainAspectRatio: false,
            scales: { x: { stacked: true }, y: { stacked: true } },
            plugins: { legend: { labels: { color: '#cbd5e1' } } }
        }
    });

    // --- 3. Chart: Volume Disciplina ---
    const ctxS = document.getElementById('metasSubjectChart').getContext('2d');
    if (subjectChartInstance) subjectChartInstance.destroy();
    subjectChartInstance = new Chart(ctxS, {
        type: 'doughnut',
        data: {
            labels: sortedSubs.slice(0,5),
            datasets: [{
                data: sortedSubs.slice(0,5).map(s => subjectStats[s].t),
                backgroundColor: ['#3b82f6', '#8b5cf6', '#10b981', '#f59e0b', '#ef4444'],
                borderWidth:0
            }]
        },
        options: {
            responsive: true, maintainAspectRatio: false,
            plugins: { legend: { position: 'bottom', labels: { color: '#cbd5e1' } } }
        }
    });

    // --- 4. Timeline do Currículo ---
    let timelineHTML = '';
    // Sorted by deliverable month order (Mar, Apr, May, Jun, Jul => 2,3,1,4,5)
    const renderOrder = [2, 3, 1, 4, 5]; 
    renderOrder.forEach(y => {
        const st = yearStats[y];
        if(st.t === 0) return;
        const pct = Math.round((st.d / st.t)*100);
        let icon = pct === 100 ? '✅' : '⏳';
        timelineHTML += `
            <div class="insight-item">
                <div class="insight-item-title">${icon} Entrega de ${goalsList[y].monthName}: Currículo do ${y}º Ano</div>
                <div class="insight-item-desc">
                    <strong>${pct}%</strong> pronto. Falta produzir ${st.t - st.d} aulas oficiais do total de ${st.t}.
                </div>
            </div>
        `;
    });
    document.getElementById('timeline-container').innerHTML = timelineHTML;
}
