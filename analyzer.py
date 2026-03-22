#!/usr/bin/env python3
"""
Gaps Knowledge Analyzer - Final Version (V5)
Tests your understanding of daily briefs, market analysis, and sumzy data.
Automatically reads from sibling project directories at D:\AI_PROJECTS\projects.
Saves flashcards into docs/data.json and updates knowledge_gaps_dashboard.md.
Now includes git_push to ensure GitHub Pages updates automatically.
"""

import json
import os
import subprocess
from datetime import datetime
from pathlib import Path
import re

class GapsAnalyzer:
    """Analyzes knowledge gaps based on daily-brief content."""
    
    def __init__(self, projects_root: str = r"D:\AI_PROJECTS\projects"):
        self.projects_root = Path(projects_root)
        self.gaps_dir = self.projects_root / "gaps"
        self.daily_brief_data = self.projects_root / "daily-brief" / "docs" / "data.json"
        self.sumzy_data = self.projects_root / "sumzy" / "docs" / "data.json"
        self.docs = self.gaps_dir / "docs"
        self.data_json = self.docs / "data.json"
        
        # Knowledge domains to test
        self.domains = {
            "market_analysis": {"weight": 0.35, "topics": ["cryptocurrency", "trading", "technical analysis"]},
            "youtube_briefs": {"weight": 0.25, "topics": ["content tracking", "daily brief format"]},
            "sumzy_data": {"weight": 0.30, "topics": ["dashboards", "data visualization"]},
            "general_knowledge": {"weight": 0.10, "topics": ["knowledge gaps", "flashcards"]}
        }
    
    def git_push(self):
        """Stage, commit, and push if there are changes."""
        try:
            subprocess.run(["git", "add", "-A"], cwd=self.gaps_dir, capture_output=True)
            diff = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=self.gaps_dir)
            
            if diff.returncode != 0:
                msg = f"auto: gaps dashboard update {datetime.now().strftime('%Y-%m-%d %H:%M')}"
                subprocess.run(["git", "commit", "-m", msg], cwd=self.gaps_dir, capture_output=True)
                print("🚀 Committing changes...")
                
                push_res = subprocess.run(["git", "push", "origin", "HEAD"], cwd=self.gaps_dir, capture_output=True, text=True)
                if push_res.returncode == 0:
                    print("📤 Pushed to GitHub.")
                    return True
                else:
                    print(f"⚠️ Push failed: {push_res.stderr}")
                    return False
            else:
                print("✅ No changes to push.")
                return False
        except Exception as e:
            print(f"⚠️ Git push error: {e}")
            return False

    def normalize_json(self, data):
        """Standardize to a list of entries, whether source was [..] or { 'data': [..] }."""
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            if "data" in data:
                return data["data"]
            if "briefs" in data:
                return data["briefs"]
            # Fallback to dictionary values if it's some other non-standard wrapper
            return list(data.values())[0] if len(data) == 1 else []
        return []

    def load_content(self) -> dict:
        """Load and parse content from daily-brief and sumzy."""
        content = {
            "timestamp": datetime.now().isoformat(),
            "daily_brief_count": 0,
            "sumzy_count": 0,
            "raw_data": []
        }
        
        # Load Daily Brief data
        if self.daily_brief_data.exists():
            try:
                with open(self.daily_brief_data, "r", encoding="utf-8") as f:
                    content_str = f.read().strip()
                    if content_str:
                        db_data = self.normalize_json(json.loads(content_str))
                        content["daily_brief_count"] = len(db_data)
                        # Process latest 20 items
                        for item in db_data[:20]:
                            content["raw_data"].append({
                                "source": "daily-brief",
                                "title": item.get("title", ""),
                                "preview": item.get("analysis", {}).get("summary", "")[:300]
                            })
            except Exception as e:
                print(f"Error loading daily-brief data: {e}")
        
        # Load Sumzy data
        if self.sumzy_data.exists():
            try:
                with open(self.sumzy_data, "r", encoding="utf-8") as f:
                    content_str = f.read().strip()
                    if content_str:
                        s_data = self.normalize_json(json.loads(content_str))
                        content["sumzy_count"] = len(s_data)
                        for item in s_data[:20]:
                            content["raw_data"].append({
                                "source": "sumzy",
                                "title": item.get("title", ""),
                                "preview": item.get("summary", "")[:300]
                            })
            except Exception as e:
                print(f"Error loading sumzy data: {e}")
        
        return content
    
    def generate_flashcards(self, raw_content: dict) -> list:
        """Generate flashcards for the JS dashboard."""
        flashcards = []
        
        # Base questions
        flashcards.append({
            "question": "What is the primary function of the OpenViking Market Analyzer?",
            "answer": "To provide structured technical and macro analysis of daily market movements.",
            "category": "SYSTEM"
        })
        
        # Dynamic questions from content
        for item in raw_content["raw_data"]:
            title = item.get("title", "")
            if title and len(title) > 8:
                source_label = "brief" if item["source"] == "daily-brief" else "Telegram Link"
                flashcards.append({
                    "question": f"Key takeaway from the {source_label}: '{title}'?",
                    "answer": f"{item.get('preview', 'Refer to original document for full analysis.')}...",
                    "category": "DAILY_BRIEF" if item["source"] == "daily-brief" else "SUMZY"
                })
        
        return flashcards
    
    def update_files(self, flashcards: list, results: dict):
        """Update both data.json and the dashboard markdown file."""
        os.makedirs(self.docs, exist_ok=True)
        
        # Save flashcards as FLAT LIST for script.js
        with open(self.data_json, "w", encoding="utf-8") as f:
            json.dump(flashcards, f, indent=4, ensure_ascii=True)
            
        # Update Markdown Dashboard
        time_str = datetime.now().strftime('%Y-%m-%d %H:%M')
        content = f"""# Gaps Knowledge Dashboard
Updated: `{time_str}`

## Source Health
- 📺 **Daily Brief Source**: `{"ACTIVE (" + str(results.get('daily_brief_count', 0)) + ")" if self.daily_brief_data.exists() else "MISSING"}`
- 📡 **Sumzy Source**: `{"ACTIVE (" + str(results.get('sumzy_count', 0)) + ")" if self.sumzy_data.exists() else "MISSING"}`

## Knowledge Coverage
- **Total Flashcards**: `{len(flashcards)}`
- **Domains Covered**: {', '.join(set(fc['category'] for fc in flashcards))}

---

## Targeted Improvement Tasks
"""
        for cat in set(fc['category'] for fc in flashcards):
            content += f"- 🟡 **{cat}**: Review concepts to ensure consistency.\n"

        content += "\n\n*Dashboard synchronized by OpenViking Gaps Analyzer*"
        
        dashboard_path = self.docs / "knowledge_gaps_dashboard.md"
        with open(dashboard_path, "w", encoding="utf-8") as f:
            f.write(content)
        return dashboard_path

    def run_analysis(self):
        """Execute full pipeline."""
        print(f"🚀 Gaps Knowledge Synchronizer Started")
        raw = self.load_content()
        print(f"  + Scanned Daily Brief: {raw['daily_brief_count']} sources")
        print(f"  + Scanned Sumzy: {raw['sumzy_count']} sources")
        
        flashcards = self.generate_flashcards(raw)
        print(f"  + Generated {len(flashcards)} knowledge cards")
        
        path = self.update_files(flashcards, raw)
        print(f"✅ Synced flashcards to {self.data_json}")
        print(f"✅ Dashboard updated: {path}")
        
        # PUSH TO GITHUB
        self.git_push()
        
        return flashcards

if __name__ == "__main__":
    analyzer = GapsAnalyzer()
    analyzer.run_analysis()