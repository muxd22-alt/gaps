#!/usr/bin/env python3
"""Interactive test with debug output"""
import sys
sys.path.insert(0, "D:/AI_PROJECTS/projects")

# Import and run the analyzer class directly
from analyzer import GapsAnalyzer

print("[1] Creating GapsAnalyzer instance...")
a = GapsAnalyzer()

print(f"[2] Project directory: {a.project_dir}")
print(f"   Daily brief path: {a.daily_brief}")
print(f"   Sumzy data path: {a.sumzy_data}")

print("\n[3] Loading content...")
raw_content = a.load_content()
print(f"    Files processed: {raw_content['files_processed']}")
print(f"    Raw data items: {len(raw_content.get('raw_data', []))}")
if raw_content['raw_data']:
    print("    Sample raw data preview:")
    for item in raw_content['raw_data'][:2]:
        if 'preview' in item and isinstance(item['preview'], list):
            print(f"      - {item.get('file', 'N/A')}: {len(item['preview'])} lines")

print("\n[4] Generating flashcards...")
flashcards = a.generate_flashcards(raw_content)
print(f"    Flashcards generated: {len(flashcards)}")

print("\n[5] Testing knowledge...")
test_results = a.test_knowledge(flashcards)
if 'error' in test_results:
    print(f"    ERROR: {test_results['error']}")
else:
    print(f"    Total flashcards: {test_results.get('total_flashcards', 0)}")
    print(f"    Categories covered: {test_results.get('categories_covered', [])}")

print("\n[6] Updating dashboard...")
if 'error' not in test_results:
    dashboard_path = a.update_dashboard(test_results)
    print(f"    Dashboard updated at: {dashboard_path}")
else:
    print("    Skipping dashboard update due to error")

print("\n[7] Complete results:")
print(f"    Files Processed: {raw_content.get('files_processed', 0)}")
print(f"    Flashcards Generated: {len(flashcards)}")
print(f"    Categories Analyzed: {len(set(fc['category'] for fc in flashcards))}")