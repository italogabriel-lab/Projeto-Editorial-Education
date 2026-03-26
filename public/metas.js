let yearChartInstance = null;
let subjectChartInstance = null;

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
        // Ano
        if (i.year && yearStats[i.year]) {
            yearStats[i.year].t++;
            if (i.status === 'Done') yearStats[i.year].d++;
        }
        
        // Disciplina
        const sub = i.subject || 'Outros';
        if (!subjectStats[sub]) subjectStats[sub] = {t:0, d:0};
        subjectStats[sub].t++;
        if (i.status === 'Done') subjectStats[sub].d++;
    });

    // --- 1. Cards de Disciplina ---
    let discHTML = '';
    const sortedSubs = Object.keys(subjectStats).sort((a,b) => subjectStats[b].t - subjectStats[a].t);
    sortedSubs.forEach(sub => {
        const st = subjectStats[sub];
        if(st.t === 0) return;
        const pct = Math.round((st.d / st.t)*100);
        let color = pct === 100 ? 'green' : (pct > 50 ? 'blue' : 'purple');
        discHTML += `
            <div class="kpi-card glass-panel">
                <div class="kpi-icon ${color}">📚</div>
                <div class="kpi-data">
                    <h3>${sub}</h3>
                    <p>${pct}% (${st.d}/${st.t})</p>
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
