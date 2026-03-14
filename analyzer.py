import os
import json

KNOWLEDGE_DIR = "d:/AI_PROJECTS/knowledge/summaries"
GAPS_FILE = "d:/AI_PROJECTS/gaps/flashcards.md"

REQUIRED_TOPICS = [
    "Bull Market Support Band",
    "Logarithmic Regression",
    "Bitcoin Risk Levels",
    "ETH/BTC Ratio",
    "Dollar Cost Averaging (DCA) Strategy",
    "Macro Backdrop"
]

def analyze_gaps():
    if not os.path.exists(KNOWLEDGE_DIR):
        print("Knowledge base is empty.")
        return

    shared_content = ""
    for filename in os.listdir(KNOWLEDGE_DIR):
        if filename.endswith(".md"):
            with open(os.path.join(KNOWLEDGE_DIR, filename), 'r') as f:
                shared_content += f.read().lower()

    gaps = []
    for topic in REQUIRED_TOPICS:
        if topic.lower() not in shared_content:
            gaps.append(topic)

    with open(GAPS_FILE, 'w') as f:
        f.write("# Knowledge Gaps & Flashcards\n\n")
        f.write("Based on Benjamin Cowen's core market indicators, here are the areas you haven't shared links about yet:\n\n")
        for gap in gaps:
            f.write(f"## 🃏 Flashcard: {gap}\n")
            f.write(f"**Question:** What is the significance of the {gap} in the current market cycle?\n")
            f.write(f"**Answer:** (LLM will fill this based on historical Benjamin Cowen data in next iteration)\n\n")
    
    print(f"Analyzed knowledge. Found {len(gaps)} gaps.")

if __name__ == "__main__":
    analyze_gaps()
