async function loadDashboard() {
    const gapsContainer = document.getElementById('gaps-container');
    const knowledgeContainer = document.getElementById('knowledge-container');

    try {
        const response = await fetch('data.json');
        const data = await response.json();

        // Render Gaps (Flashcards with Answers)
        if (data.gaps.length === 0) {
            gapsContainer.innerHTML = '<p>No active gaps! System synchronized.</p>';
        } else {
            gapsContainer.innerHTML = data.gaps.map((gap, index) => `
                <div class="card srs-card" onclick="this.classList.toggle('flipped')">
                    <div class="card-inner">
                        <div class="card-front">
                            <div class="card-type">${gap.status}</div>
                            <div class="card-title">${gap.title}</div>
                            <div class="card-body">${gap.question}</div>
                            <div class="hint">Click to flip for answer</div>
                        </div>
                        <div class="card-back">
                            <div class="card-title">Analysis</div>
                            <div class="card-body">${gap.answer}</div>
                        </div>
                    </div>
                </div>
            `).join('');
        }

        // Render Knowledge (With Value Flags & Categories)
        if (data.knowledge.length === 0) {
            knowledgeContainer.innerHTML = '<p>No analysis found. Run tracker.py.</p>';
        } else {
            knowledgeContainer.innerHTML = data.knowledge.map(item => `
                <div class="card" style="border-left: 4px solid var(--accent-secondary)">
                    <div class="card-header-flex">
                        <div class="card-type">${item.type}</div>
                        ${item.value_flag === 'HIGH' ? '<span class="value-flag">🔥 High Value</span>' : ''}
                    </div>
                    <div class="card-title">${item.title}</div>
                    <div class="card-body">${item.preview}</div>
                    <div class="category-tags">
                        ${(item.categories || []).map(cat => `<span class="cat-badge">${cat}</span>`).join('')}
                    </div>
                </div>
            `).join('');
        }

    } catch (e) {
        console.error("Dashboard error:", e);
    }
}

document.addEventListener('DOMContentLoaded', loadDashboard);
