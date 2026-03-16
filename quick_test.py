#!/usr/bin/env python3
"""Quick test for Gaps Analyzer - Knowledge Test Summary"""
import sys
sys.path.insert(0, "D:/AI_PROJECTS/projects")
from analyzer import GapsAnalyzer

# Run analysis
a = GapsAnalyzer()
results = a.run_analysis()

print("\n" + "="*50)
print("KNOWLEDGE TEST SUMMARY")
print("="*50)
print(f"Files Processed: {results.get('files_processed', 0)}")
print(f"Total Flashcards Generated: {results.get('total_flashcards', 0)}")
print(f"Categories Analyzed: {len(results.get('categories_covered', []))}")

print("\n--- RECOMMENDED REVIEW ---")
for rec in results.get('recommended_review', []):
    priority = rec['priority'].capitalize()
    category = rec['category']
    reason = rec['reason']
    print(f"{priority}: **{category}** - {reason}")