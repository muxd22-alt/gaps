async function loadDashboard() {
    const gapsContainer = document.getElementById('gaps-container');
    const knowledgeContainer = document.getElementById('knowledge-container');

    try {
        const response = await fetch('data.json');
        const data = await response.json();

        if (data.gaps.length === 0) {
            gapsContainer.innerHTML = '<p>No gaps identified! You are fully caught up.</p>';
        } else {
            gapsContainer.innerHTML = data.gaps.map(gap => `
                <div class="card">
                    <div class="card-type">${gap.type}</div>
                    <div class="card-title">${gap.title}</div>
                    <div class="card-body">${gap.preview}</div>
                    <span class="tag">${gap.tag}</span>
                </div>
            `).join('');
        }

        if (data.knowledge.length === 0) {
            knowledgeContainer.innerHTML = '<p>Knowledge base is empty. Start sharing links in Telegram!</p>';
        } else {
            knowledgeContainer.innerHTML = data.knowledge.map(item => `
                <div class="card" style="border-color: var(--accent-secondary)">
                    <div class="card-type" style="color: var(--accent-secondary)">${item.type}</div>
                    <div class="card-title">${item.title}</div>
                    <div class="card-body">${item.preview}</div>
                </div>
            `).join('');
        }

    } catch (e) {
        console.error("Dashboard error:", e);
        gapsContainer.innerHTML = '<p>Run analyzer.py to generate dashboard data.</p>';
    }
}

document.addEventListener('DOMContentLoaded', loadDashboard);
