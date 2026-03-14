import os
import json

KNOWLEDGE_DIR = "d:/AI_PROJECTS/knowledge/summaries"
GAPS_DATA_FILE = "d:/AI_PROJECTS/gaps/docs/data.json"
FLASHCARDS_MD = "d:/AI_PROJECTS/gaps/flashcards.md"

REQUIRED_TOPICS = [
    "Bull Market Support Band",
    "Logarithmic Regression",
    "Bitcoin Risk Levels",
    "ETH/BTC Ratio",
    "Dollar Cost Averaging (DCA) Strategy",
    "Macro Backdrop"
]

def analyze_gaps():
    shared_summaries = []
    shared_text_blob = ""
    
    if os.path.exists(KNOWLEDGE_DIR):
        for filename in os.listdir(KNOWLEDGE_DIR):
            if filename.endswith(".md"):
                with open(os.path.join(KNOWLEDGE_DIR, filename), 'r') as f:
                    content = f.read()
                    shared_text_blob += content.lower()
                    shared_summaries.append({
                        "title": filename.replace(".md", ""),
                        "preview": content[:150] + "...",
                        "type": "Summary"
                    })

    gaps = []
    for topic in REQUIRED_TOPICS:
        if topic.lower() not in shared_text_blob:
            gaps.append({
                "title": f"Gap: {topic}",
                "preview": f"You haven't shared enough data regarding {topic}. We need to study this more.",
                "type": "Flashcard",
                "tag": "Missing"
            })

    # Save to JSON for dashboard
    output = {
        "gaps": gaps,
        "knowledge": shared_summaries
    }
    
    docs_dir = os.path.dirname(GAPS_DATA_FILE)
    if not os.path.exists(docs_dir):
        os.makedirs(docs_dir)

    with open(GAPS_DATA_FILE, 'w') as f:
        json.dump(output, f, indent=4)
    
    # Also keep the markdown version for manual reading
    with open(FLASHCARDS_MD, 'w') as f:
        f.write("# Knowledge Gaps & Flashcards\n\n")
        for g in gaps:
            f.write(f"## 🃏 {g['title']}\n{g['preview']}\n\n")
    
    print(f"Analysis complete. Found {len(gaps)} gaps and {len(shared_summaries)} summaries.")

if __name__ == "__main__":
    analyze_gaps()
