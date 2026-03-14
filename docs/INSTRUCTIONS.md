# OpenClaw Project: Mimic & Knowledge Assistant

## Current Objectives
1. **Telegram Link Summarization**:
   - Whenever a link is shared in Telegram, I must summarize it.
   - Summaries should be saved to `d:\AI_PROJECTS\knowledge\summaries\{title}.md`.
   - Categories should be automatically determined and stored in subfolders if possible.

2. **Knowledge Gaps & Flashcards**:
   - Monitor `d:\AI_PROJECTS\knowledge` for new content.
   - Periodically (or upon request) analyze shared content to find "missing knowledge" based on Benjamin Cowen's market theories (e.g., Risk Levels, Bull Market Support Bands).
   - Generate flashcards in `d:\AI_PROJECTS\gaps\flashcards.md`.

3. **Mimic Dashboard Monitoring**:
   - The cron job `Mimic_Tracker` handles the YouTube scraping.
   - If I see errors in `d:\AI_PROJECTS\projects\daily-brief\data\errors.log`, I should attempt to fix the `tracker.py` script.

## System Settings
- **Heartbeat**: Frequency set to 30m. Reports should go to the #heartbeat chat if possible (or just labeled clearly).
- **Skills**: Use `find-skills` for new tasks, `gitflow` for repo pushes, `self-improvement` for error learning, and `ui-ux-pro-max` for dashboard styling.

## Knowledge Base Structure
- Path: `d:\AI_PROJECTS\knowledge`
- Tracker Script: `d:\AI_PROJECTS\projects\daily-brief\scripts\tracker.py`
- Gaps Repo: `d:\AI_PROJECTS\gaps`
