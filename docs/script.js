document.addEventListener('DOMContentLoaded', async () => {
    let cards = [];
    let currentIndex = 0;
    
    const container = document.getElementById('flashcard-container');
    const controls = document.getElementById('controls');
    const btnNext = document.getElementById('btn-next');
    
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
                        <p style="color:var(--text-sec); margin-top:20px;">Check back later after new videos or links are analyzed.</p>
                    </div>
                </div>
            `;
            controls.style.display = 'none';
            return;
        }
        
        const c = cards[index];
        const cardEl = document.createElement('div');
        cardEl.className = 'flashcard';
        cardEl.innerHTML = `
            <div class="front">
                <span class="category">${c.category || 'KNOWLEDGE'}</span>
                <h2>${c.question}</h2>
                <span class="tap-hint">Tap to reveal</span>
            </div>
            <div class="back">
                <span class="category">${c.category || 'KNOWLEDGE'}</span>
                <p>${c.answer}</p>
            </div>
        `;
        
        cardEl.addEventListener('click', () => {
            cardEl.classList.toggle('flipped');
            if (cardEl.classList.contains('flipped')) {
                controls.classList.add('visible');
            } else {
                controls.classList.remove('visible');
            }
        });
        
        container.appendChild(cardEl);
        // Controls only show after flipping
        controls.classList.remove('visible');
        controls.style.display = 'flex';
    }
    
    btnNext.addEventListener('click', (e) => {
        e.stopPropagation();
        currentIndex++; 
        renderCard(currentIndex); 
    });
    
    renderCard(0);
});
