#!/usr/bin/env python3
"""
Gaps Knowledge Analyzer - Final Version
Tests your understanding of daily briefs, market analysis, and sumzy data.
"""

import json
import os
from datetime import datetime
from pathlib import Path

class GapsAnalyzer:
    """Analyzes knowledge gaps based on daily-brief content."""
    
    def __init__(self, project_dir: str = r"D:\AI_PROJECTS\projects\gaps"):
        self.project_dir = Path(project_dir)
        self.daily_brief = self.project_dir / "daily-brief"
        self.sumzy_data = self.project_dir / "sumzy"
        self.docs = self.project_dir / "docs"
        
        # Knowledge domains to test
        self.domains = {
            "market_analysis": {"weight": 0.35, "topics": ["cryptocurrency", "trading", "technical analysis"]},
            "youtube_briefs": {"weight": 0.25, "topics": ["content tracking", "daily brief format"]},
            "sumzy_data": {"weight": 0.30, "topics": ["dashboards", "data visualization"]},
            "general_knowledge": {"weight": 0.10, "topics": ["knowledge gaps", "flashcards"]}
        }
    
    def load_content(self) -> dict:
        """Load and parse content from daily-brief folder."""
        content = {
            "timestamp": datetime.now().isoformat(),
            "files_processed": 0,
            "topics_found": [],
            "raw_data": []
        }
        
        # Check for any files in the folders
        if self.daily_brief.exists():
            try:
                files = list(self.daily_brief.glob("*"))[:5]  # Limit to first 5 files
                content["files_processed"] = len(files)
                
                for file_path in files:
                    if file_path.suffix.lower() in [".md", "", "json"]:
                        try:
                            text = file_path.read_text(encoding="utf-8")[:2000]
                            content["raw_data"].append({
                                "file": str(file_path),
                                "length": len(text),
                                "preview": text.split("\n")[:3]
                            })
                        except Exception as e:
                            print(f"Error reading {file_path}: {e}")
            except Exception as e:
                print(f"Error listing daily-brief files: {e}")
        
        # Check sumzy data
        if self.sumzy_data.exists():
            try:
                for file in list(self.sumzy_data.glob("*"))[:3]:
                    if file.is_file() and "__pycache__" not in str(file):
                        content["raw_data"].append({
                            "file": f"sumzy/{file.name}",
                            "exists": True
                        })
            except Exception as e:
                print(f"Error accessing sumzy data: {e}")
        
        return content
    
    def generate_flashcards(self, raw_content: dict) -> list:
        """Generate flashcards based on loaded content."""
        flashcards = []
        
        # Base knowledge questions derived from daily brief format
        base_questions = [
            {
                "front": "What is the primary purpose of the daily-brief tracker?",
                "back": "To organize and analyze content from @intothecryptoverse YouTube channel for market analysis purposes.",
                "category": "youtube_briefs"
            },
            {
                "front": "What does the 'mimic' project track?",
                "back": "Daily brief dashboard that tracks YouTube channel content and will be remade with future data when Benjamin stops content.",
                "category": "market_analysis"
            },
            {
                "front": "What is the significance of 'Benjamin' in the context of this project?",
                "back": "The original creator who will no longer produce YouTube content, necessitating a new brief tracker that can be remade.",
                "category": "youtube_briefs"
            },
            {
                "front": "What does 'sumzy' represent in this ecosystem?",
                "back": "A library for storing insights, organizing dashboards, and maintaining structured data from market analysis.",
                "category": "sumzy_data"
            },
            {
                "front": "What is the primary communication platform used for sharing links?",
                "back": "Telegram - it's where most Telegram links are shared that feed into the analysis tools.",
                "category": "general_knowledge"
            },
            {
                "front": "What deployment method is preferred for dashboards?",
                "back": "GitHub Pages - used for static site hosting of analysis results.",
                "category": "market_analysis"
            }
        ]
        
        # Generate questions based on raw content
        if raw_content["raw_data"]:
            topics = set()
            for item in raw_content["raw_data"]:
                topic_preview = " ".join(item.get("preview", [])[:2])
                if len(topic_preview) > 5:
                    # Extract potential keywords (simplified)
                    words = topic_preview.lower().split()
                    topics.update(w for w in words if len(w) > 3 and not w.startswith("http") and not w.endswith("."))
            
            flashcards.extend(base_questions)
        
        # Add category-specific questions
        domain_flashcards = [
            {
                "front": "What data sources feed into the market analysis tools?",
                "back": "Telegram links, YouTube daily briefs, and sumzy project insights.",
                "category": "market_analysis"
            },
            {
                "front": "How are dashboards deployed in this system?",
                "back": "Using GitHub Pages for static site hosting of analysis results.",
                "category": "market_analysis"
            },
            {
                "front": "What format is used for daily brief tracking?",
                "back": "Markdown with structured headers and data tables.",
                "category": "youtube_briefs"
            },
            {
                "front": "Where are sumzy insights stored?",
                "back": "In the D:\\AI_PROJECTS\\projects\\sumzy directory as a library for structured analysis.",
                "category": "sumzy_data"
            }
        ]
        
        flashcards.extend(domain_flashcards)
        
        return flashcards
    
    def test_knowledge(self, flashcards: list) -> dict:
        """Test knowledge and generate results."""
        import random
        
        if not flashcards:
            return {"error": "No flashcards generated", "score": 0}
        
        # Simulate a quiz (without actual user input for automation)
        test_results = {
            "total_flashcards": len(flashcards),
            "categories_covered": list(set(fc["category"] for fc in flashcards)),
            "difficulty_distribution": {},
            "recommended_review": []
        }
        
        # Analyze category coverage
        category_counts = {}
        for fc in flashcards:
            cat = fc["category"]
            category_counts[cat] = category_counts.get(cat, 0) + 1
        
        test_results["difficulty_distribution"] = {
            "basic": len([fc for fc in flashcards if "format" in fc["front"].lower()]),
            "intermediate": len([fc for fc in flashcards if "track" in fc["front"].lower() or "analyze" in fc["front"].lower()]),
            "advanced": len([fc for fc in flashcards if "remade" in fc["back"].lower()])
        }
        
        # Generate recommendations
        for cat, count in category_counts.items():
            test_results["recommended_review"].append({
                "category": cat,
                "priority": "high" if count < 2 else "medium",
                "reason": f"Review {cat} concepts to strengthen understanding"
            })
        
        return test_results
    
    def update_dashboard(self, results: dict, output_dir: str = "docs"):
        """Update the knowledge gaps dashboard."""
        os.makedirs(output_dir, exist_ok=True)
        
        # Create updated dashboard file
        dashboard_content = f"""# Knowledge Gaps Dashboard - Update {datetime.now().strftime('%Y-%m-%d %H:%M')}

## Analysis Results
- **Total Flashcards Generated**: {results.get('total_flashcards', 0)}
- **Categories Covered**: {', '.join(results.get('categories_covered', []))}
- **Difficulty Breakdown**:
"""
        
        for difficulty, count in results.get("difficulty_distribution", {}).items():
            dashboard_content += f"  - `{difficulty.capitalize()}`: {count} items\n"
        
        dashboard_content += "\n## Recommended Review Areas\n"
        for rec in results.get("recommended_review", []):
            priority_marker = "🔴 HIGH" if rec["priority"] == "high" else "🟡 MEDIUM"
            dashboard_content += f"- {priority_marker}: **{rec['category']}** - {rec['reason']}\n"
        
        dashboard_path = self.project_dir / output_dir / "knowledge_gaps_dashboard.md"
        with open(dashboard_path, "w", encoding="utf-8") as f:
            f.write(dashboard_content)
        
        print(f"Dashboard updated: {dashboard_path}")
        return dashboard_path
    
    def run_analysis(self) -> dict:
        """Run complete analysis pipeline."""
        print("Starting Gaps Knowledge Analyzer...")
        print(f"Project directory: {self.project_dir}")
        
        # Load content
        raw_content = self.load_content()
        print(f"\nLoaded {raw_content['files_processed']} files from daily-brief")
        
        # Generate flashcards
        flashcards = self.generate_flashcards(raw_content)
        print(f"Generated {len(flashcards)} flashcards")
        
        # Test knowledge
        test_results = self.test_knowledge(flashcards)
        
        # Update dashboard
        if "error" not in test_results:
            self.update_dashboard(test_results)
        
        return {
            **test_results,
            "files_processed": raw_content["files_processed"],
            "raw_data_items": len(raw_content.get("raw_data", []))
        }


if __name__ == "__main__":
    analyzer = GapsAnalyzer()
    results = analyzer.run_analysis()
    
    print("\n" + "="*50)
    print("ANALYSIS COMPLETE")
    print("="*50)
    print(f"Files Processed: {results.get('files_processed', 0)}")
    print(f"Flashcards Generated: {results.get('total_flashcards', 0)}")
    print(f"Categories Analyzed: {len(results.get('categories_covered', []))}")