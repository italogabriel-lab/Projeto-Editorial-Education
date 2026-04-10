# Saúde das Metas — Visão Geral por Ano (Feature)

## 📋 Resumo da Implementação

Nova funcionalidade adicionada ao sistema de metas por disciplina que permite visualizar a saúde das metas para cada ano individualmente, com métricas de produção diária, alertas de status e mensagens motivacionais para a equipe.

---

## 🎯 Funcionalidades Implementadas

### 1. **Visualização Detalhada por Ano**
- Ao clicar em um card de ano na visão de disciplina, o sistema exibe uma análise completa da meta daquele ano específico
- Cada ano tem um mês-alvo definida no cronograma:
  - 1º Ano: Maio
  - 2º Ano: Março
  - 3º Ano: Abril
  - 4º Ano: Junho
  - 5º Ano: Julho

### 2. **Métricas de Produção**
O sistema calcula e exibe:
- **Aulas Produzidas**: Total de aulas já concluídas para aquele ano
- **Aulas Restantes**: Quantas aulas faltam para atingir a meta de 168
- **Dias Úteis Restantes**: Contagem de dias úteis (seg-sex) até o fim do mês-alvo
- **Meta Diária**: Quantas aulas por dia precisam ser produzidas para atingir a meta

### 3. **Sistema de Alertas e Status**
O sistema analisa automaticamente o ritmo de produção e classifica em 4 níveis:

#### ✅ **Completado** (Verde)
- Meta de 168 aulas atingida
- Mensagem: "Meta atingida!"
- Ícone: Seal Check

#### 🌟 **Saudável** (Verde)
- Produção dentro ou acima do esperado
- Mensagens: "Ritmo bom!", "Excelente ritmo!"
- Ícones: Trend Up, Rocket

#### ⚠️ **Atenção** (Amarelo)
- 10-20 aulas abaixo do esperado
- Mensagem: "Atenção - Ritmo lento"
- Ícone: Heartbeat

#### 🔴 **Crítico** (Vermelho)
- Mais de 20 aulas abaixo do esperado OU mês-alvo ultrapassado
- Mensagens: "ATRASADO", "MUITO ATRASADO"
- Ícone: Warning Circle

### 4. **Análise de Ritmo**
Comparação entre produção esperada vs. produção realizada:
- **Produção Esperada**: Calculada baseada na progressão do tempo até o mês-alvo
- **Produção Realizada**: Total atual de aulas produzidas
- **Diferença**: Gap entre esperado e realizado (positivo ou negativo)

### 5. **Plano de Ação**
Recomendações automáticas baseadas no status:
- Meta diária de produção necessária
- Foco nas aulas restantes
- Alertas de prioridade quando atrasado
- Incentivos quando no ritmo correto

### 6. **Mensagens Motivacionais**
Sistema rotativo de mensagens para motivar a equipe:
- **Crítico**: "⚠️ URGENTE: Precisamos acelerar! Cada dia conta!"
- **Atenção**: "⚡ Atenção: Podemos melhorar! Vamos manter o ritmo!"
- **Saudável**: "🌟 Excelente ritmo! Continuemos assim, equipe!"
- **Completado**: "🏆 META ATINGIDA! Parabéns equipe!"

---

## 🔧 Arquivos Modificados

### `metas-disciplinas.html`
- Adicionada seção `year-health-detail-section` para exibir detalhes do ano

### `public/metas-disciplinas.js`
Novas funções adicionadas:

1. **`calculateYearHealth(subject, year)`**
   - Calcula todas as métricas de saúde para um ano específico
   - Retorna objeto completo com dados de produção, dias restantes, status, etc.

2. **`showYearHealthDetail(subject, year)`**
   - Renderiza a interface de detalhes do ano
   - Exibe métricas, alertas, e plano de ação

3. **`backToDisciplineDetail()`**
   - Retorna para a visão de cards de ano

4. **Constantes adicionadas**:
   - `YEAR_TARGET_MONTHS`: Mapeamento de anos para meses-alvo
   - `MONTH_NAMES`: Nomes dos meses em português
   - `MOTIVATIONAL_MESSAGES`: Banco de mensagens motivacionais

---

## 📊 Como Funciona o Cálculo

### Dias Úteis Restantes
```javascript
// Conta apenas dias de segunda a sexta
// Do dia seguinte até o último dia do mês-alvo
let workingDays = 0;
for (let date = tomorrow; date <= endOfMonth; date++) {
    if (date.getDay() >= 1 && date.getDay() <= 5) {
        workingDays++;
    }
}
```

### Meta Diária
```javascript
dailyRateNeeded = Math.ceil(remaining / workingDaysRemaining);
// Se não há dias úteis: dailyRateNeeded = remaining (tudo agora)
```

### Produção Esperada
```javascript
timeProgress = daysElapsed / totalDaysInMonth;
expectedProduced = Math.round(168 * timeProgress);
productionGap = produced - expectedProduced;
```

### Classificação de Status
- **Crítico**: `productionGap < -20` OU mês-alvo ultrapassado
- **Atenção**: `-20 <= productionGap < -10`
- **Saudável**: `productionGap >= 0`
- **Completado**: `remaining === 0`

---

## 🎨 Interface do Usuário

### Elementos Visuais
- **Card interativo**: Ano clicável com hover effect
- **Header**: Disciplina + Ano + Meta do mês
- **Alert Banner**: Status colorido com ícone e mensagem
- **Metrics Grid**: 4 cards (Produzidas, Restantes, Dias Úteis, Meta Diária)
- **Progress Bar**: Barra de progresso com referência
- **Rhythm Analysis**: Grid comparativo esperado vs. realizado
- **Action Plan**: Lista de ações recomendadas

### Cores de Status
- ✅ Verde: `var(--color-success-light)` / `#34d399`
- ⚠️ Amarelo: `var(--color-warning-light)` / `#fb923c`
- 🔴 Vermelho: `var(--color-danger-light)` / `#ef4444`

---

## 🚀 Como Usar

1. Acesse `metas-disciplinas.html`
2. Clique em uma disciplina para ver os detalhes
3. Clique em um dos cards de ano (1º ao 5º)
4. Visualize a saúde completa da meta daquele ano
5. Use o botão "Voltar" para retornar aos cards de ano

---

## 📈 Benefícios

✅ **Visibilidade Clara**: Equipe sabe exatamente quantas aulas precisa produzir por dia
✅ **Alertas Proativos**: Sistema avisa quando está atrasado antes do deadline
✅ **Motivação**: Mensagens positivas incentivam a equipe
✅ **Planejamento**: Métricas de dias úteis ajudam no planejamento realista
✅ **Accountability**: Comparação esperado vs. realizado mostra gaps claramente
✅ **Foco**: Plano de ação específico para cada situação

---

## 🔄 Próximos Passos (Sugestões)

- [ ] Adicionar histórico de progresso ao longo do tempo (gráfico)
- [ ] Exportar relatório em PDF
- [ ] Notificações automáticas quando status mudar
- [ ] Metas personalizáveis por disciplina
- [ ] Integração com calendário para feriados
- [ ] Média de produção por membro da equipe

---

## 📝 Notas Técnicas

- Todos os cálculos são feitos client-side em JavaScript
- Status considerados "produzidos": `In Review`, `Video`, `Done/Published`
- Meta por disciplina por ano: **168 aulas**
- Sistema usa data atual do navegador para cálculos
- Dias úteis calculados dinamicamente (seg-sex)

---

**Implementado em**: Abril 2026  
**Versão**: 1.0  
**Status**: ✅ Produção Ready
