let teamChartInstance = null;

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
    const assignees = {};
    
    items.forEach(i => {
        const user = i.assignee || 'Unassigned';
        if (!assignees[user]) assignees[user] = { t: 0, d: 0, wip: 0, leadTimeSum: 0, leadTimeCount: 0 };
        
        assignees[user].t++;
        if (i.status === 'Done') {
            assignees[user].d++;
            if (i.lead_time_days !== null && i.lead_time_days > 0) {
                assignees[user].leadTimeSum += i.lead_time_days;
                assignees[user].leadTimeCount++;
            }
        } else {
            assignees[user].wip++;
        }
    });

    const userKeys = Object.keys(assignees).filter(u => u !== 'Unassigned').sort((a,b) => assignees[b].d - assignees[a].d);
    
    // --- 1. Ranking Individual View ---
    let rankingHTML = '';
    userKeys.forEach(u => {
        const o = assignees[u];
        const pct = Math.round((o.d / o.t)*100) || 0;
        const avgLT = o.leadTimeCount > 0 ? (o.leadTimeSum / o.leadTimeCount).toFixed(1) : 0;
        const statusClass = pct > 80 ? 'success' : (pct < 30 ? 'danger' : 'warning');
        
        rankingHTML += `
            <div class="insight-item ${statusClass}" style="margin: 0;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div class="insight-item-title">@${u}</div>
                    <strong style="font-size: 1.2rem;">${pct}%</strong>
                </div>
                <div class="insight-item-desc" style="margin-top: 10px;">
                    <div>✓ Concluídas: <b>${o.d}</b> / ${o.t}</div>
                    <div>⚡ Em Fila/Produção: <b>${o.wip}</b></div>
                    <div>⏱️ Lead Time Médio: <b>${avgLT} dias</b></div>
                </div>
            </div>
        `;
    });
    document.getElementById('ranking-container').innerHTML = rankingHTML;

    // --- 2. Bottlenecks (Gargalos) ---
    let bottleneckHTML = '';
    
    if (assignees['Unassigned'] && assignees['Unassigned'].wip > 0) {
        bottleneckHTML += `
            <div class="insight-item danger">
                <div class="insight-item-title">Orphan Tasks Alert</div>
                <div class="insight-item-desc">Há ${assignees['Unassigned'].wip} tarefas sem dono travando a fila de produção.</div>
            </div>
        `;
    }
    
    // Pessoas com fila muito grande e conclusão pequena
    userKeys.forEach(u => {
        const o = assignees[u];
        const pct = Math.round((o.d / o.t)*100) || 0;
        if (o.wip > 15 && pct < 40) {
            bottleneckHTML += `
                <div class="insight-item warning">
                    <div class="insight-item-title">Sobrecarga: @${u}</div>
                    <div class="insight-item-desc">Fila de WIP altíssima (${o.wip} itens) com baixa taxa de vasão. Risco de gargalo.</div>
                </div>
            `;
        }
    });
    
    if(!bottleneckHTML) bottleneckHTML = '<div class="insight-item success">Nenhum gargalo agudo detectado no momento.</div>';
    document.getElementById('bottleneck-list').innerHTML = bottleneckHTML;

    // --- 3. Balanceamento de Equipe (Chart) ---
    const ctx = document.getElementById('teamChart').getContext('2d');
    if(teamChartInstance) teamChartInstance.destroy();
    
    const wipData = userKeys.map(u => assignees[u].wip);
    
    teamChartInstance = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: userKeys.map(u => '@' + u),
            datasets: [{
                data: wipData,
                backgroundColor: ['#f43f5e', '#a855f7', '#3b82f6', '#10b981', '#f59e0b', '#06b6d4'],
                borderWidth:0
            }]
        },
        options: {
            responsive: true, maintainAspectRatio: false,
            plugins: { legend: { position: 'right', labels: { color: '#cbd5e1' } } }
        }
    });
}
