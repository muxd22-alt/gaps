# 🦞 OpenClaw Master Boot Instructions: Mimic & Knowledge System

## 🎯 System Mission
To automate the capture and analysis of market insights from Benjamin Cowen (Into the Cryptoverse), maintain a persistent Knowledge Base from shared Telegram links, and identify learning gaps through an automated Gaps Analyzer.

---

## 🏗️ Project Architecture

### 1. Mimic Dashboard (Daily Brief)
- **Path**: `d:\AI_PROJECTS\projects\daily-brief`
- **Repo**: [github.com/muxd22-alt/mimic](https://github.com/muxd22-alt/mimic)
- **Goal**: Track YouTube videos, pull transcripts, and generate "mimicry training" data.
- **Training Data**: Stored in `data/training_json/`. Every video is converted into a structured Instruction/Input/Output JSON for future model fine-tuning or RAG-based mimicking of Benjamin's analysis style.
- **Frontend**: Premium Cyberpunk/HUD design located in `docs/` for GitHub Pages.

### 2. Knowledge Base
- **Path**: `d:\AI_PROJECTS\knowledge`
- **Goal**: Every link shared in Telegram MUST be summarized using the local LLM.
- **Storage**: Markdown summaries stored in `knowledge/summaries/`.
- **Instruction**: When a link is detected, extract content, summarize key takeaways, and categorize into subfolders (e.g., BTC, Macro, ETH).

### 3. Gaps Analyzer
- **Path**: `d:\AI_PROJECTS\gaps`
- **Repo**: [github.com/muxd22-alt/gaps](https://github.com/muxd22-alt/gaps)
- **Goal**: Compare `knowledge/summaries` against Benjamin's "Essential Topic List" (Risk Levels, Bull Market Support Bands, Logarithmic Regression).
- **Output**: Generates a web-based dashboard in `docs/` showing flashcards for missing knowledge.

---

## 🎨 UI/UX Standards (CRITICAL)
- **Skill**: ALWAYS consult `skills/ui-ux-pro-max` before modifying frontends.
- **Style**: Retro-Futurism / Cyberpunk.
- **Colors**: OLED Black (#050505), Neon Blue (#00f3ff), Neon Pink (#ff00ff).
- **Vibe**: Performance-driven, technical, HUD-inspired.

---

## ⚙️ Operational Workflows
1. **Cron 1 (Mimic_Tracker - Hourly)**:
   - Run `scripts/tracker.py` to fetch new videos and transcripts.
   - Run `scripts/site_generator.py` to update the web dashboard.
2. **Cron 2 (Knowledge_Gaps_Sync - 4-Hourly)**:
   - Move new Telegram summaries to the knowledge repo.
   - Run `analyzer.py` in the gaps folder.
   - Push all updates to GitHub.

## 🛠️ Skills in Use
- `find-skills`: To discover new OpenClaw features.
- `gitflow`: To manage deployments to the `mimic` and `gaps` repos.
- `self-improvement`: To log and fix errors in the tracker or analyzer.
- `ui-ux-pro-max`: To maintain the premium aesthetic.

---
*Last Updated: 2026-03-14 | Automated by OpenClaw AI*
