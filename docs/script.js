document.addEventListener('DOMContentLoaded', async () => {
    let cards = [];
    let currentIndex = 0;
    
    const container = document.getElementById('flashcard-container');
    const controls = document.getElementById('controls');
    
    try {
        const res = await fetch('data.json');
        if (!res.ok) throw new Error("No data found");
        cards = await res.json();
    } catch {
        cards = [
            { category: "SYSTEM", question: "Looks like there are no active flashcards right now.", answer: "The Gaps analyzer creates these from your Mimic and Sumzy data." }
        ];
    }
    
    function renderCard(index) {
        container.innerHTML = '';
        if (index >= cards.length) {
            container.innerHTML = `
                <div class="flashcard">
                    <div class="front">
                        <h2>All done for today! 🎉</h2>
                        <p style="color:var(--text-sec); margin-top:10px;">Check back later after new videos or links are analyzed.</p>
                    </div>
                </div>
            `;
            controls.style.display = 'none';
            controls.classList.remove('visible');
            return;
        }
        
        const c = cards[index];
        const cardEl = document.createElement('div');
        cardEl.className = 'flashcard';
        cardEl.innerHTML = `
            <div class="front">
                <span class="category">${c.category || 'KNOWLEDGE'}</span>
                <h2>${c.question}</h2>
                <span style="position:absolute; bottom:20px; color:var(--text-sec); font-size: 0.8rem;">Tap to reveal</span>
            </div>
            <div class="back">
                <span class="category">${c.category || 'KNOWLEDGE'}</span>
                <p>${c.answer}</p>
            </div>
        `;
        
        cardEl.addEventListener('click', () => {
            cardEl.classList.toggle('flipped');
            if (cardEl.classList.contains('flipped')) {
                controls.style.display = 'flex';
                // Trigger reflow for animation
                setTimeout(() => controls.classList.add('visible'), 50);
            } else {
                controls.classList.remove('visible');
            }
        });
        
        container.appendChild(cardEl);
        controls.style.display = 'none';
        controls.classList.remove('visible');
    }
    
    document.getElementById('btn-pass').addEventListener('click', () => { currentIndex++; renderCard(currentIndex); });
    document.getElementById('btn-fail').addEventListener('click', () => {
        // In a real SRS this would reset the timing algorithm
        currentIndex++; renderCard(currentIndex); 
    });
    
    renderCard(0);
});
