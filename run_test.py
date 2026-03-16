#!/usr/bin/env python3
"""Run test for Gaps Analyzer"""
import sys
sys.path.insert(0, "D:/AI_PROJECTS/projects")
os.chdir("D:/AI_PROJECTS/projects/gaps")

# Import the analyzer module and inspect it
from importlib.util import spec_from_file_location, module_from_spec
spec = spec_from_file_location('analyzer', 'D:/AI_PROJECTS/projects/gaps/analyzer.py')
analyzer_module = module_from_spec(spec)
spec.loader.exec_module(analyzer_module)

print('[1] Module loaded successfully')
print(f'[2] GapsAnalyzer class exists: {hasattr(analyzer_module, "GapsAnalyzer")}')

# Create instance and run
a = analyzer_module.GapsAnalyzer()
print(f'[3] Instance created at: {a.project_dir}')

# Run the analysis with error handling
try:
    print('[4] Starting load_content()...')
    raw_content = a.load_content()
    print(f'   Files processed: {raw_content["files_processed"]}')
except Exception as e:
    import traceback
    print(f'   ERROR in load_content(): {e}')
    traceback.print_exc()

print('\nScript completed.')