import os
import json
from datetime import datetime, timedelta

KNOWLEDGE_DIR = "d:/AI_PROJECTS/knowledge/summaries"
GAPS_DATA_FILE = "d:/AI_PROJECTS/gaps/docs/data.json"
HISTORY_FILE = "d:/AI_PROJECTS/gaps/flashcard_history.json"

REQUIRED_TOPICS = {
    "Bull Market Support Band": "The combination of the 20-week SMA and 21-week EMA that historically acts as support in bull markets.",
    "Logarithmic Regression": "A mathematical model used to determine the fair value of Bitcoin over time based on diminishing returns.",
    "Bitcoin Risk Levels": "A metric from 0 to 1 based on logarithmic regression that indicates market heat (0-0.3 is accumulation, 0.7-1.0 is peak).",
    "ETH/BTC Ratio": "The valuation of Ethereum in terms of Bitcoin, often used to signal alt-season or flight to safety.",
    "Macro Backdrop": "The overall economic environment, including FED interest rates and SP500 performance, impacting all risk assets."
}

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_history(history):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=4)

def analyze_gaps():
    history = load_history()
    shared_summaries = []
    shared_text_blob = ""
    
    if os.path.exists(KNOWLEDGE_DIR):
        for filename in sorted(os.listdir(KNOWLEDGE_DIR), reverse=True):
            if filename.endswith(".md"):
                with open(os.path.join(KNOWLEDGE_DIR, filename), 'r') as f:
                    content = f.read()
                    shared_text_blob += content.lower()
                    shared_summaries.append({
                        "title": filename.replace(".md", ""),
                        "preview": content[:200] + "...",
                        "type": "Summary",
                        "timestamp": datetime.now().isoformat()
                    })

    now = datetime.now()
    gaps = []
    
    for topic, answer in REQUIRED_TOPICS.items():
        is_missing = topic.lower() not in shared_text_blob
        
        # Spaced Repetition Logic initialization
        if topic not in history:
            history[topic] = {
                "next_review": now.isoformat(),
                "interval": 1, 
                "status": "New"
            }
        
        next_review = datetime.fromisoformat(history[topic]["next_review"])
        
        if is_missing or next_review <= now:
            gaps.append({
                "title": topic,
                "question": f"What is the significance of the {topic} in the current market cycle?",
                "answer": answer,
                "type": "Flashcard",
                "status": "Missing" if is_missing else "Review Due",
                "next_review": history[topic]["next_review"]
            })

    output = {
        "gaps": gaps,
        "knowledge": shared_summaries,
        "categories": ["ECONOMICS", "CRYPTO", "MATHEMATICS", "FED", "SP500"]
    }
    
    with open(GAPS_DATA_FILE, 'w') as f:
        json.dump(output, f, indent=4)
    
    save_history(history)
    print(f"Analysis complete. {len(gaps)} cards ready for review.")

if __name__ == "__main__":
    analyze_gaps()
