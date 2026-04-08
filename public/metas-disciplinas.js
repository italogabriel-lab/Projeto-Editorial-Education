let yearChartInstance = null;
let subjectChartInstance = null;

const META_POR_DISCIPLINA_ANO = 168;
const NUM_ANOS = 5;
const META_POR_DISCIPLINA_TOTAL = META_POR_DISCIPLINA_ANO * NUM_ANOS;

// Tudo que passou de "In Progress" é considerado produzido pela equipe de desenvolvimento
const PRODUCED_STATUSES = ['In Review', 'Video', 'Done/Published'];
function isProduced(status) {
    return PRODUCED_STATUSES.includes(status);
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
        'geografia': 'Geografia',
        'matemática': 'Matemática',
        'matematica': 'Matemática',
        'portugues': 'Português',
        'português': 'Português',
        'linguagem': 'Português',
        'belas artes': 'Belas Artes',
        'belasartes': 'Belas Artes',
        'bíblia': 'Bíblia',
        'biblia': 'Bíblia'
    };
    return map[lower] || name;
}

function getSubjectIcon(subject, sizeClass = '') {
    const icons = {
        'História': 'ph-book-bookmark',
        'Ciências': 'ph-flask',
        'Geografia': 'ph-globe-hemisphere-west',
        'Matemática': 'ph-function',
        'Português': 'ph-text-aa',
        'Belas Artes': 'ph-palette',
        'Bíblia': 'ph-book-open'
    };
    const iconClass = icons[subject] || 'ph-book-open';
    const style = sizeClass ? ` style="${sizeClass}"` : ' style="font-size: 1.2rem;"';
    return `<i class="ph ${iconClass}"${style}></i>`;
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
    const filled = Math.min(Math.round((pct / 100) * width), width);
    const empty = width - filled;
    return '█'.repeat(filled) + '░'.repeat(empty);
}

async function performSync() {
    try {
        const response = await fetch('public/data.json?t=' + new Date().getTime());
        const data = await response.json();

        document.getElementById('last-sync-time').textContent = new Date(data.last_updated).toLocaleString();

        const items = data.items || [];

        renderDisciplineCards(items);
        renderSubjectHealth(items);

    } catch (e) {
        console.error("Error loading data:", e);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    performSync();
    setInterval(performSync, 60000);

    // Year filter buttons
    document.querySelectorAll('.year-filter-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.year-filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const year = btn.dataset.year;
            filterByYear(year);
        });
    });

    // Back to cards button
    document.getElementById('back-to-cards-btn').addEventListener('click', () => {
        showDisciplineCards();
    });
});

let currentItems = [];
let currentYearFilter = 'all';

function filterByYear(year) {
    currentYearFilter = year;
    renderDisciplineCards(currentItems);
}

function renderDisciplineCards(items) {
    currentItems = items;
    const yearStats = { 1: { t: 0, d: 0 }, 2: { t: 0, d: 0 }, 3: { t: 0, d: 0 }, 4: { t: 0, d: 0 }, 5: { t: 0, d: 0 } };
    const subjectStats = {};

    items.forEach(i => {
        const sub = normalizeSubject(i.subject);
        if (!sub) return;
        const y = i.year;

        if (!subjectStats[sub]) subjectStats[sub] = { t: 0, d: 0, years: { 1: {}, 2: {}, 3: {}, 4: {}, 5: {} } };

        subjectStats[sub].t++;
        if (isProduced(i.status)) subjectStats[sub].d++;

        if (y && subjectStats[sub].years[y]) {
            if (!subjectStats[sub].years[y].t) subjectStats[sub].years[y] = { t: 0, d: 0 };
            subjectStats[sub].years[y].t++;
            if (isProduced(i.status)) subjectStats[sub].years[y].d++;
        }

        if (y && yearStats[y]) {
            yearStats[y].t++;
            if (isProduced(i.status)) yearStats[y].d++;
        }
    });

    const container = document.getElementById('discipline-cards-container');
    const sortedSubs = Object.keys(subjectStats).sort((a, b) => subjectStats[b].d - subjectStats[a].d);

    let html = '';
    sortedSubs.forEach(sub => {
        const st = subjectStats[sub];
        if (st.t === 0) return;

        const totalMetaDisciplina = META_POR_DISCIPLINA_TOTAL;
        const pct = Math.round((st.d / totalMetaDisciplina) * 100) || 0;
        const color = getProgressColor(pct);
        const colorHex = getProgressColorHex(pct);

        const subjectIcons = {
            'História': '<i class="ph ph-book-bookmark"></i>',
            'Ciências': '<i class="ph ph-flask"></i>',
            'Geografia': '<i class="ph ph-globe-hemisphere-west"></i>',
            'Matemática': '<i class="ph ph-function"></i>',
            'Português': '<i class="ph ph-text-aa"></i>',
            'Belas Artes': '<i class="ph ph-palette"></i>',
            'Bíblia': '<i class="ph ph-book-open"></i>'
        };
        const icon = subjectIcons[sub] || '<i class="ph ph-book-open"></i>';

        html += `
            <div class="discipline-card glass-panel" data-subject="${sub}" style="cursor: pointer; padding: 1.5rem; transition: all 0.3s; border-left: 4px solid ${colorHex};" onclick="showDisciplineDetail('${sub}')">
                <div style="display: flex; align-items: flex-start; gap: 16px; margin-bottom: 1rem;">
                    <div style="width: 52px; height: 52px; background: linear-gradient(135deg, ${colorHex}22, ${colorHex}11); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.6rem; color: ${colorHex}; flex-shrink: 0;">
                        ${icon}
                    </div>
                    <div style="flex: 1;">
                        <h3 style="font-size: 1.15rem; font-weight: 700; color: var(--text-primary); margin: 0 0 4px 0;">${sub}</h3>
                        <p style="font-size: 0.8rem; color: var(--text-muted); margin: 0;">Clique para ver detalhes por ano</p>
                    </div>
                </div>
                <div style="margin-bottom: 1rem;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <span style="font-size: 0.85rem; color: var(--text-secondary);">Progresso Total</span>
                        <span style="font-size: 1.1rem; font-weight: 700; color: ${colorHex};">${pct}%</span>
                    </div>
                    <div style="width: 100%; height: 8px; background: rgba(255,255,255,0.08); border-radius: 4px; overflow: hidden;">
                        <div style="width: ${pct}%; height: 100%; background: ${colorHex}; transition: width 0.3s;"></div>
                    </div>
                    <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 6px; text-align: right;">
                        ${st.d} / ${totalMetaDisciplina} aulas
                    </div>
                </div>
                <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 8px; padding-top: 1rem; border-top: 1px solid var(--border-glass);">
        `;

        [1, 2, 3, 4, 5].forEach(ano => {
            const yr = st.years[ano] || { t: 0, d: 0 };
            const yrPct = yr.t > 0 ? Math.round((yr.d / META_POR_DISCIPLINA_ANO) * 100) : 0;
            const yrColor = getProgressColorHex(yrPct);
            html += `
                <div style="text-align: center;">
                    <div style="font-size: 0.7rem; color: var(--text-muted); margin-bottom: 4px;">${ano}º Ano</div>
                    <div style="font-size: 0.85rem; font-weight: 600; color: ${yrColor};">${yrPct}%</div>
                </div>
            `;
        });

        html += `
                </div>
            </div>
        `;
    });

    container.innerHTML = html || '<div class="glass-panel" style="padding: 2rem; text-align: center; color: var(--text-muted);">Nenhuma disciplina encontrada.</div>';
}

function showDisciplineDetail(subject) {
    const items = currentItems;
    const subjectStats = { t: 0, d: 0, years: { 1: {}, 2: {}, 3: {}, 4: {}, 5: {} }, done: 0, backlog: 0, inProgress: 0, review: 0, video: 0 };

    items.forEach(i => {
        const sub = normalizeSubject(i.subject);
        if (sub !== subject) return;
        const status = i.status;
        const year = i.year;

        subjectStats.t++;
        if (isProduced(status)) subjectStats.d++;

        if (status === 'Done/Published') subjectStats.done++;
        else if (status === 'Backlog') subjectStats.backlog++;
        else if (status === 'In Progress') subjectStats.inProgress++;
        else if (status === 'In Review') subjectStats.review++;
        else if (status === 'Video') subjectStats.video++;

        if (year && subjectStats.years[year]) {
            if (!subjectStats.years[year].t) subjectStats.years[year] = { t: 0, d: 0 };
            subjectStats.years[year].t++;
            if (isProduced(status)) subjectStats.years[year].d++;
        }
    });

    const totalProduced = subjectStats.review + subjectStats.video + subjectStats.done;
    const remaining = Math.max(0, META_POR_DISCIPLINA_TOTAL - totalProduced);
    const pct = Math.round((totalProduced / META_POR_DISCIPLINA_TOTAL) * 100);
    const colorHex = getProgressColorHex(pct);

    const subjectIcons = {
        'História': '<i class="ph ph-book-bookmark"></i>',
        'Ciências': '<i class="ph ph-flask"></i>',
        'Geografia': '<i class="ph ph-globe-hemisphere-west"></i>',
        'Matemática': '<i class="ph ph-function"></i>',
        'Português': '<i class="ph ph-text-aa"></i>',
        'Belas Artes': '<i class="ph ph-palette"></i>',
        'Bíblia': '<i class="ph ph-book-open"></i>'
    };
    const icon = subjectIcons[subject] || '<i class="ph ph-book-open"></i>';

    // Update header
    document.getElementById('discipline-detail-icon').innerHTML = icon;
    document.getElementById('discipline-detail-icon').style.background = `linear-gradient(135deg, ${colorHex}22, ${colorHex}11)`;
    document.getElementById('discipline-detail-icon').style.color = colorHex;
    document.getElementById('discipline-detail-name').textContent = subject;
    document.getElementById('discipline-detail-subtitle').textContent = `Meta: ${META_POR_DISCIPLINA_ANO} aulas/ano × ${NUM_ANOS} anos = ${META_POR_DISCIPLINA_TOTAL} aulas`;
    document.getElementById('discipline-detail-pct').textContent = `${pct}%`;
    document.getElementById('discipline-detail-pct').style.color = colorHex;
    document.getElementById('discipline-detail-count').textContent = `${totalProduced} / ${META_POR_DISCIPLINA_TOTAL} aulas produzidas`;
    document.getElementById('discipline-detail-bar-label').textContent = `${totalProduced} produzidas | ${remaining} restantes`;
    document.getElementById('discipline-detail-bar').style.width = `${Math.min(pct, 100)}%`;
    document.getElementById('discipline-detail-bar').style.background = colorHex;

    // Year cards
    const yearCardsContainer = document.getElementById('discipline-year-cards');
    let yearCardsHTML = '';

    [1, 2, 3, 4, 5].forEach(ano => {
        const yr = subjectStats.years[ano] || { t: 0, d: 0 };
        const yrPct = yr.t > 0 ? Math.round((yr.d / META_POR_DISCIPLINA_ANO) * 100) : 0;
        const yrColor = getProgressColorHex(yrPct);
        const yrRemaining = Math.max(0, META_POR_DISCIPLINA_ANO - yr.d);

        yearCardsHTML += `
            <div class="year-detail-card glass-panel" style="padding: 1.25rem; border-top: 3px solid ${yrColor}; cursor: pointer; transition: all 0.3s;" onclick="showYearHealthDetail('${subject}', ${ano})" onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 8px 16px rgba(0,0,0,0.3)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                    <h4 style="font-size: 1rem; font-weight: 700; color: var(--text-primary); margin: 0;">
                        <i class="ph ph-graduation-cap" style="color: ${yrColor}; margin-right: 8px;"></i>
                        ${ano}º Ano
                    </h4>
                    <span style="font-size: 1.3rem; font-weight: 700; color: ${yrColor};">${yrPct}%</span>
                </div>
                <div style="margin-bottom: 1rem;">
                    <div style="width: 100%; height: 8px; background: rgba(255,255,255,0.08); border-radius: 4px; overflow: hidden;">
                        <div style="width: ${yrPct}%; height: 100%; background: ${yrColor}; transition: width 0.3s;"></div>
                    </div>
                    <div style="display: flex; justify-content: space-between; margin-top: 6px; font-size: 0.75rem; color: var(--text-muted);">
                        <span>${yr.d} produzidas</span>
                        <span>${yrRemaining} restantes</span>
                    </div>
                </div>
                <div style="display: flex; align-items: center; justify-content: center; gap: 6px; padding-top: 1rem; border-top: 1px solid var(--border-glass); font-size: 0.75rem; color: var(--color-primary-light);">
                    <i class="ph ph-heartbeat"></i>
                    <span>Clique para ver saúde da meta</span>
                </div>
            </div>
        `;
    });

    yearCardsContainer.innerHTML = yearCardsHTML;

    // Metrics
    const metricsContainer = document.getElementById('discipline-metrics');
    const inFlow = subjectStats.inProgress + subjectStats.review + subjectStats.video;
    metricsContainer.innerHTML = `
        <div style="text-align: center; padding: 1rem; background: rgba(0,0,0,0.2); border-radius: 8px;">
            <div style="font-size: 1.5rem; font-weight: 700; color: var(--color-warning-light);">${subjectStats.backlog}</div>
            <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 4px;">Backlog</div>
        </div>
        <div style="text-align: center; padding: 1rem; background: rgba(0,0,0,0.2); border-radius: 8px;">
            <div style="font-size: 1.5rem; font-weight: 700; color: var(--color-primary-light);">${inFlow}</div>
            <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 4px;">Em Fluxo</div>
        </div>
        <div style="text-align: center; padding: 1rem; background: rgba(0,0,0,0.2); border-radius: 8px;">
            <div style="font-size: 1.5rem; font-weight: 700; color: var(--color-success-light);">${subjectStats.done}</div>
            <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 4px;">Publicadas</div>
        </div>
        <div style="text-align: center; padding: 1rem; background: rgba(0,0,0,0.2); border-radius: 8px;">
            <div style="font-size: 1.5rem; font-weight: 700; color: var(--color-primary);">${subjectStats.review}</div>
            <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 4px;">Em Review</div>
        </div>
        <div style="text-align: center; padding: 1rem; background: rgba(0,0,0,0.2); border-radius: 8px;">
            <div style="font-size: 1.5rem; font-weight: 700; color: var(--color-secondary-light);">${subjectStats.video}</div>
            <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 4px;">Em Vídeo</div>
        </div>
        <div style="text-align: center; padding: 1rem; background: rgba(0,0,0,0.2); border-radius: 8px;">
            <div style="font-size: 1.5rem; font-weight: 700; color: ${colorHex};">${remaining}</div>
            <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 4px;">Restantes</div>
        </div>
    `;

    // Show detail section, hide cards and health overview
    document.getElementById('discipline-cards-container').style.display = 'none';
    document.getElementById('discipline-detail-section').style.display = 'block';
    document.getElementById('year-health-detail-section').style.display = 'none';
    document.getElementById('health-overview-section').style.display = 'none';
    document.querySelector('.year-filter-section').style.display = 'none';

    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function showDisciplineCards() {
    document.getElementById('discipline-cards-container').style.display = 'grid';
    document.getElementById('discipline-detail-section').style.display = 'none';
    document.getElementById('year-health-detail-section').style.display = 'none';
    document.getElementById('health-overview-section').style.display = 'block';
    document.querySelector('.year-filter-section').style.display = 'block';
}

// Month target mapping for each year (based on curriculum planning)
const YEAR_TARGET_MONTHS = {
    1: 5,  // Maio
    2: 3,  // Março
    3: 4,  // Abril
    4: 6,  // Junho
    5: 7   // Julho
};

const MONTH_NAMES = [
    'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
    'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
];

const MOTIVATIONAL_MESSAGES = {
    critical: [
        "⚠️ URGENTE: Precisamos acelerar! Cada dia conta!",
        "🔥 ALERTA VERMELHO: Vamos nos organizar e recuperar o tempo perdido!",
        "💪 FOCO TOTAL: Hora de dar um gás e atingir a meta!"
    ],
    warning: [
        "⚡ Atenção: Podemos melhorar! Vamos manter o ritmo e acelerar um pouco!",
        "🎯 Quase lá! Mais um pouco de esforço vamos conseguir!",
        "📈 Bom ritmo, mas podemos acelerar mais para garantir a meta!"
    ],
    healthy: [
        "🌟 Excelente ritmo! Continuemos assim, equipe!",
        "✅ Ótimo progresso! Estamos no caminho certo!",
        "🚀 Mandando bem! Vamos manter essa velocidade!"
    ],
    completed: [
        "🏆 META ATINGIDA! Parabéns equipe! Vocês são incríveis!",
        "🎉 CONCLUÍDO! Trabalho excepcional, orgulho de vocês!",
        "⭐ MISSÃO CUMPRIDA! Vocês arrasaram, continue assim!"
    ]
};

function calculateYearHealth(subject, year) {
    const items = currentItems;
    const META_ANO = META_POR_DISCIPLINA_ANO;

    // Calculate produced lessons for this year
    let produced = 0;
    items.forEach(i => {
        const sub = normalizeSubject(i.subject);
        if (sub === subject && i.year === year && isProduced(i.status)) {
            produced++;
        }
    });

    const remaining = Math.max(0, META_ANO - produced);
    const pct = Math.round((produced / META_ANO) * 100);

    // Get current date
    const currentDate = new Date();
    const currentYear = currentDate.getFullYear();
    const currentMonth = currentDate.getMonth() + 1; // 1-12
    const currentDay = currentDate.getDate();

    // Get target month for this year
    const targetMonth = YEAR_TARGET_MONTHS[year];
    const targetMonthName = MONTH_NAMES[targetMonth - 1];

    // Calculate complete working days remaining in target month
    // Count only weekdays (Monday to Friday) from current day to end of target month
    let workingDaysRemaining = 0;
    let isOverdue = false;

    if (currentMonth > targetMonth || (currentMonth === targetMonth && currentDay > 25)) {
        // Past the target month or very late in the month
        isOverdue = true;
        workingDaysRemaining = 0;
    } else {
        // Calculate working days from tomorrow to end of target month
        const endDate = new Date(currentYear, targetMonth, 0); // Last day of target month
        const startDate = new Date(currentYear, currentMonth - 1, currentDay + 1); // Tomorrow

        if (startDate > endDate) {
            isOverdue = true;
            workingDaysRemaining = 0;
        } else {
            let checkDate = new Date(startDate);
            while (checkDate <= endDate) {
                const dayOfWeek = checkDate.getDay();
                // Count Monday (1) through Friday (5)
                if (dayOfWeek >= 1 && dayOfWeek <= 5) {
                    workingDaysRemaining++;
                }
                checkDate.setDate(checkDate.getDate() + 1);
            }
        }
    }

    // Calculate daily production rate needed
    let dailyRateNeeded = 0;
    if (remaining > 0 && workingDaysRemaining > 0) {
        dailyRateNeeded = Math.ceil(remaining / workingDaysRemaining);
    } else if (remaining > 0 && workingDaysRemaining === 0) {
        dailyRateNeeded = remaining; // All remaining must be done now
    }

    // Calculate ideal production rate based on time elapsed
    const totalDaysInMonth = new Date(currentYear, targetMonth, 0).getDate();
    const daysElapsed = (currentMonth === targetMonth) ? currentDay : totalDaysInMonth;
    const daysInMonth = totalDaysInMonth;
    const timeProgress = daysElapsed / daysInMonth;
    const expectedProduced = Math.round(META_ANO * timeProgress);
    const productionGap = produced - expectedProduced;

    // Determine health status
    let health = 'healthy';
    let healthIcon = '<i class="ph ph-heart"></i>';
    let healthMsg = 'No prazo';
    let healthColor = 'var(--color-success-light)';
    let healthBg = 'rgba(16, 185, 129, 0.1)';

    if (remaining === 0) {
        health = 'completed';
        healthIcon = '<i class="ph ph-seal-check"></i>';
        healthMsg = 'Meta atingida!';
        healthColor = 'var(--color-success-light)';
        healthBg = 'rgba(16, 185, 129, 0.15)';
    } else if (isOverdue || (workingDaysRemaining === 0 && remaining > 0)) {
        health = 'critical';
        healthIcon = '<i class="ph ph-warning-circle"></i>';
        healthMsg = 'ATRASADO';
        healthColor = 'var(--color-danger-light)';
        healthBg = 'rgba(239, 68, 68, 0.15)';
    } else if (productionGap < -20) {
        // More than 20 lessons behind schedule
        health = 'critical';
        healthIcon = '<i class="ph ph-warning-circle"></i>';
        healthMsg = 'MUITO ATRASADO';
        healthColor = 'var(--color-danger-light)';
        healthBg = 'rgba(239, 68, 68, 0.15)';
    } else if (productionGap < -10) {
        // 10-20 lessons behind schedule
        health = 'warning';
        healthIcon = '<i class="ph ph-heartbeat"></i>';
        healthMsg = 'Atenção - Ritmo lento';
        healthColor = 'var(--color-warning-light)';
        healthBg = 'rgba(245, 158, 11, 0.15)';
    } else if (productionGap >= 0 && productionGap < 15) {
        health = 'healthy';
        healthIcon = '<i class="ph ph-trend-up"></i>';
        healthMsg = 'Ritmo bom!';
        healthColor = 'var(--color-success-light)';
        healthBg = 'rgba(16, 185, 129, 0.1)';
    } else if (productionGap >= 15) {
        health = 'healthy';
        healthIcon = '<i class="ph ph-rocket"></i>';
        healthMsg = 'Excelente ritmo!';
        healthColor = 'var(--color-success-light)';
        healthBg = 'rgba(16, 185, 129, 0.15)';
    }

    // Get motivational message
    const messages = MOTIVATIONAL_MESSAGES[health];
    const motivationalMsg = messages[Math.floor(Math.random() * messages.length)];

    return {
        health,
        healthIcon,
        healthMsg,
        healthColor,
        healthBg,
        produced,
        remaining,
        pct,
        workingDaysRemaining,
        dailyRateNeeded,
        targetMonthName,
        isOverdue,
        productionGap,
        expectedProduced,
        motivationalMsg
    };
}

function showYearHealthDetail(subject, year) {
    const healthData = calculateYearHealth(subject, year);
    const yearNames = ['', '1º Ano', '2º Ano', '3º Ano', '4º Ano', '5º Ano'];
    const yearColor = getProgressColorHex(healthData.pct);

    // Build the year health detail section
    const container = document.getElementById('year-health-detail-section');

    let html = `
        <div class="glass-panel" style="padding: 1.5rem; border-left: 4px solid ${healthData.healthColor};">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; padding-bottom: 1rem; border-bottom: 1px solid var(--border-glass);">
                <div style="display: flex; align-items: center; gap: 16px;">
                    <button id="back-to-discipline-detail-btn" style="background: rgba(255,255,255,0.05); border: 1px solid var(--border-glass); border-radius: 8px; padding: 8px 12px; cursor: pointer; color: var(--text-primary); display: flex; align-items: center; gap: 6px; transition: all 0.2s;" onclick="backToDisciplineDetail()">
                        <i class="ph ph-arrow-left"></i> Voltar
                    </button>
                    <div style="width: 56px; height: 56px; background: ${healthData.healthBg}; border-radius: 14px; display: flex; align-items: center; justify-content: center; font-size: 1.8rem; color: ${healthData.healthColor};">
                        ${getSubjectIcon(subject)}
                    </div>
                    <div>
                        <h2 style="font-size: 1.5rem; font-weight: 700; color: var(--text-primary); margin: 0 0 4px 0;">
                            ${subject} — ${yearNames[year]}
                        </h2>
                        <p style="font-size: 0.85rem; color: var(--text-muted); margin: 0;">
                            Meta: ${META_POR_DISCIPLINA_ANO} aulas até ${healthData.targetMonthName}
                        </p>
                    </div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 2.2rem; font-weight: 700; color: ${healthData.healthColor};">${healthData.pct}%</div>
                    <div style="font-size: 0.75rem; color: var(--text-muted);">${healthData.produced} / ${META_POR_DISCIPLINA_ANO} aulas</div>
                </div>
            </div>

            <!-- Status Alert -->
            <div style="padding: 1rem; background: ${healthData.healthBg}; border-radius: 10px; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 12px;">
                <div style="font-size: 2rem; color: ${healthData.healthColor};">
                    ${healthData.healthIcon}
                </div>
                <div style="flex: 1;">
                    <div style="font-size: 1rem; font-weight: 700; color: ${healthData.healthColor}; margin-bottom: 4px;">
                        ${healthData.healthMsg}
                    </div>
                    <div style="font-size: 0.85rem; color: var(--text-secondary);">
                        ${healthData.motivationalMsg}
                    </div>
                </div>
            </div>

            <!-- Production Metrics Grid -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 1.5rem;">
                <div style="padding: 1.25rem; background: rgba(0,0,0,0.2); border-radius: 10px; text-align: center;">
                    <div style="font-size: 0.75rem; color: var(--text-muted); margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">
                        <i class="ph ph-check-circle"></i> Produzidas
                    </div>
                    <div style="font-size: 2rem; font-weight: 700; color: var(--color-success-light);">
                        ${healthData.produced}
                    </div>
                    <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 4px;">
                        aulas concluídas
                    </div>
                </div>

                <div style="padding: 1.25rem; background: rgba(0,0,0,0.2); border-radius: 10px; text-align: center;">
                    <div style="font-size: 0.75rem; color: var(--text-muted); margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">
                        <i class="ph ph-hourglass-simple"></i> Restantes
                    </div>
                    <div style="font-size: 2rem; font-weight: 700; color: ${healthData.healthColor};">
                        ${healthData.remaining}
                    </div>
                    <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 4px;">
                        aulas faltando
                    </div>
                </div>

                <div style="padding: 1.25rem; background: rgba(0,0,0,0.2); border-radius: 10px; text-align: center;">
                    <div style="font-size: 0.75rem; color: var(--text-muted); margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">
                        <i class="ph ph-calendar"></i> Dias Úteis
                    </div>
                    <div style="font-size: 2rem; font-weight: 700; color: var(--color-primary-light);">
                        ${healthData.workingDaysRemaining}
                    </div>
                    <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 4px;">
                        até ${healthData.targetMonthName}
                    </div>
                </div>

                <div style="padding: 1.25rem; background: rgba(0,0,0,0.2); border-radius: 10px; text-align: center; border: 2px solid ${healthData.healthColor};">
                    <div style="font-size: 0.75rem; color: var(--text-muted); margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">
                        <i class="ph ph-lightning"></i> Meta Diária
                    </div>
                    <div style="font-size: 2.5rem; font-weight: 700; color: ${healthData.healthColor};">
                        ${healthData.dailyRateNeeded}
                    </div>
                    <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 4px;">
                        aulas/dia necessárias
                    </div>
                </div>
            </div>

            <!-- Progress Bar -->
            <div style="margin-bottom: 1.5rem;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 0.85rem;">
                    <span style="color: var(--text-secondary);">Progresso até ${healthData.targetMonthName}</span>
                    <span style="color: ${healthData.healthColor}; font-weight: 600;">${healthData.produced}/${META_POR_DISCIPLINA_ANO}</span>
                </div>
                <div style="width: 100%; height: 12px; background: rgba(255,255,255,0.08); border-radius: 6px; overflow: hidden;">
                    <div style="width: ${Math.min(healthData.pct, 100)}%; height: 100%; background: ${healthData.healthColor}; transition: width 0.4s ease;"></div>
                </div>
                <div style="display: flex; justify-content: space-between; margin-top: 6px; font-size: 0.75rem;">
                    <span style="color: var(--text-muted);">0</span>
                    <span style="color: var(--text-muted);">Esperado: ${healthData.expectedProduced} aulas</span>
                    <span style="color: var(--text-muted);">${META_POR_DISCIPLINA_ANO}</span>
                </div>
            </div>

            <!-- Production Gap Analysis -->
            <div style="padding: 1rem; background: rgba(0,0,0,0.15); border-radius: 8px; margin-bottom: 1.5rem;">
                <h4 style="font-size: 0.9rem; font-weight: 600; color: var(--text-primary); margin: 0 0 12px 0; display: flex; align-items: center; gap: 8px;">
                    <i class="ph ph-chart-line-up" style="color: var(--color-primary-light);"></i>
                    Análise de Ritmo
                </h4>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px;">
                    <div>
                        <div style="font-size: 0.75rem; color: var(--text-muted); margin-bottom: 4px;">Produção Esperada</div>
                        <div style="font-size: 1.3rem; font-weight: 600; color: var(--text-primary);">${healthData.expectedProduced} aulas</div>
                    </div>
                    <div>
                        <div style="font-size: 0.75rem; color: var(--text-muted); margin-bottom: 4px;">Produção Realizada</div>
                        <div style="font-size: 1.3rem; font-weight: 600; color: ${healthData.productionGap >= 0 ? 'var(--color-success-light)' : 'var(--color-danger-light)'};">
                            ${healthData.produced} aulas
                        </div>
                    </div>
                    <div>
                        <div style="font-size: 0.75rem; color: var(--text-muted); margin-bottom: 4px;">Diferença</div>
                        <div style="font-size: 1.3rem; font-weight: 600; color: ${healthData.productionGap >= 0 ? 'var(--color-success-light)' : 'var(--color-danger-light)'};">
                            ${healthData.productionGap >= 0 ? '+' : ''}${healthData.productionGap} aulas
                        </div>
                    </div>
                </div>
            </div>

            <!-- Action Items -->
            <div style="padding: 1rem; background: ${healthData.healthBg}; border-radius: 8px; border-left: 3px solid ${healthData.healthColor};">
                <h4 style="font-size: 0.9rem; font-weight: 600; color: var(--text-primary); margin: 0 0 12px 0; display: flex; align-items: center; gap: 8px;">
                    <i class="ph ph-target" style="color: ${healthData.healthColor};"></i>
                    Plano de Ação
                </h4>
                <ul style="margin: 0; padding-left: 20px; color: var(--text-secondary); font-size: 0.85rem; line-height: 1.8;">
                    <li>Produzir <strong style="color: ${healthData.healthColor};">${healthData.dailyRateNeeded} aulas/dia</strong> até ${healthData.targetMonthName}</li>
                    <li>Focar em ${healthData.remaining} aulas restantes com qualidade</li>
                    <li>Manter ritmo constante e revisar pendências</li>
                    ${healthData.isOverdue ? '<li style="color: var(--color-danger-light); font-weight: 600;">⚠️ Prioridade máxima: recuperar atraso!</li>' : ''}
                    ${healthData.productionGap < -10 ? '<li style="color: var(--color-warning-light); font-weight: 600;">⚡ Acelerar produção para alcançar meta esperada</li>' : ''}
                    ${healthData.productionGap >= 0 ? '<li style="color: var(--color-success-light); font-weight: 600;">✅ Excelente! Continuar nesse ritmo</li>' : ''}
                </ul>
            </div>
        </div>
    `;

    container.innerHTML = html;

    // Show year health detail, hide year cards
    document.getElementById('discipline-year-cards').style.display = 'none';
    document.getElementById('year-health-detail-section').style.display = 'block';

    // Scroll to the detail section
    container.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function backToDisciplineDetail() {
    document.getElementById('discipline-year-cards').style.display = 'grid';
    document.getElementById('year-health-detail-section').style.display = 'none';
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
        healthIcon = '<i class="ph ph-seal-check"></i>';
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

    return { health, healthIcon, healthMsg, healthColor, monthsLeft, daysRemaining, velocityNeeded, isOverdue };
}

function renderSubjectHealth(items) {
    const subjectStats = {};

    items.forEach(i => {
        const sub = normalizeSubject(i.subject);
        if (!sub) return;
        const status = i.status;
        const year = i.year;

        if (!subjectStats[sub]) {
            subjectStats[sub] = { done: 0, backlog: 0, inProgress: 0, review: 0, video: 0, years: {} };
        }

        if (status === 'Done/Published') subjectStats[sub].done++;
        else if (status === 'Backlog') subjectStats[sub].backlog++;
        else if (status === 'In Progress') subjectStats[sub].inProgress++;
        else if (status === 'In Review') subjectStats[sub].review++;
        else if (status === 'Video') subjectStats[sub].video++;

        if (year) {
            if (!subjectStats[sub].years[year]) subjectStats[sub].years[year] = { produced: 0 };
            if (isProduced(status)) subjectStats[sub].years[year].produced++;
        }
    });

    let html = '';
    const sorted = Object.keys(subjectStats).sort((a, b) => subjectStats[b].done - subjectStats[a].done);

    sorted.forEach(sub => {
        const stats = subjectStats[sub];
        const totalProduced = stats.review + stats.video + stats.done;
        const remaining = Math.max(0, META_POR_DISCIPLINA_TOTAL - totalProduced);
        const healthData = getMetaHealth(remaining, 6);
        const pct = Math.round((totalProduced / META_POR_DISCIPLINA_TOTAL) * 100);
        const inFlow = stats.inProgress + stats.review + stats.video;

        const cardStyle = healthData.health === 'critical' ? 'border-left: 4px solid var(--color-danger);' :
            healthData.health === 'warning' ? 'border-left: 4px solid var(--color-warning);' :
                healthData.health === 'completed' ? 'border-left: 4px solid var(--color-success);' : '';

        html += `
            <div class="insight-item animate-fade-in" style="${cardStyle} margin: 0;">
                <div class="insight-item-title" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                    <span style="display: flex; align-items: center; gap: 8px;">
                        ${getSubjectIcon(sub)}
                        <strong>${sub}</strong>
                    </span>
                    <span style="font-size: 1.2rem; font-weight: 700; color: ${healthData.healthColor};">${pct}%</span>
                </div>
                <div class="insight-item-desc">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 0.85rem;">
                        <span>Produzido: <strong style="color: var(--color-success-light);">${totalProduced}</strong> / ${META_POR_DISCIPLINA_TOTAL}</span>
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
                            <div style="color: ${healthData.healthColor}; font-weight: 600;">${Math.max(0, healthData.daysRemaining)}</div>
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
        container.innerHTML = html || '<div class="insight-item">Nenhum dado de disciplina encontrado.</div>';
    }
}
