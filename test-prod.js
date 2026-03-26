const fs = require('fs');
const data = JSON.parse(fs.readFileSync('public/data.json', 'utf8'));

const items = data.items;

const assignees = {};
items.forEach(i => {
    const user = i.assignee || 'Unassigned';
    if (!assignees[user]) assignees[user] = { t: 0, d: 0, wip: 0 };
    
    assignees[user].t++;
    if (i.status === 'Done/Published') {
        assignees[user].d++;
    } else {
        assignees[user].wip++;
    }
});

console.log(assignees['Fabiomorais87']);
