# 🚀 NAVYA MYTHOS: Complete Features & Developer Guide

Welcome to the **NAVYA LOCAL DEV SERVER**, the 2026 industry-standard ecosystem for high-performance AI application testing, optimization, and strategy. This guide covers everything from your first audit to managing autonomous agent extensions.

---

## 1. 🏰 The Command Center (`/`)
This is your main dashboard. It’s where you orchestrate your testing mesh.
- **Agentic Verification:** Click "Execute Full-Stack Audit" to trigger a **TestSprite Agent**. It will check your frontend for broken links (and self-heal them), fuzz your API backend for leaks, and verify database state.
- **Optimization Insights:** Trigger an **AEO/GEO scan** to see if your site is readable by modern Answer Engines like Perplexity or DeepSeek.

## 2. 🌐 The API Connectivity Hub (`/connectivity`)
Manage your "Neural Wirings."
- **Local Engines:** Connect and verify **Ollama** or **LM Studio** instances running on your machine.
- **Third-Party Gateways:** Securely input API keys for OpenAI, Anthropic, or DeepSeek-V4.
- **Health Checks:** Real-time status tags (Active/Offline) ensure your agents never hit a dead-end bridge.

## 3. 🧠 Strategy Intel Engine (`/intelligence`)
Your competitive advantage.
- **Semantic Scraping:** Enter any competitor's URL. Our engine performs a "Semantic Extract," stripping away the noise (ads/nav) and converting the site into clean Markdown for AI analysis.
- **Thrashing Moves:** The engine autonomously identifies "moves" to beat competitors, such as injecting ISO-2026-X schemas to out-rank them in AI search results.

## 4. 🔌 Agentic Extension Portal (`/portal`)
The power of scalability.
- **MCP Native:** Built on the **Model Context Protocol**.
- **Discover & Install:** Browse trending extensions like **CyberAudit X** (Security) or **Alibaba Page Agent** (Browser Automation).
- **Run Anywhere:** Once installed, you can execute these third-party agents directly from your portal to handle specialized tasks.

## 5. 🧬 Self-Evolving Core (The Brain)
The most advanced part of your server.
- **WikiLLM Librarian:** Every test result is recorded in a persistent knowledge base.
- **Nanochat Trainer:** The server "learns" from every audit. Every time a test passes, the **Muon Optimizer** simulates a fine-tuning step, increasing the "Knowledge Level" of your local node.
- **Self-Healing:** If a test fails, the server consults the Librarian for past successful fixes to help the agent self-repair.

---

## 🛠️ Developer Quick-Start

### 1. Installation
Ensure you have `uv` installed (the 2026 standard for Python).
```bash
uv sync
```

### 2. Launch the Server
```bash
uv run services/testing-mesh/main.py
```
Open **[http://localhost:8081](http://localhost:8081)** in your browser.

### 3. Run a System Validation
Want to make sure everything is 100/100?
```bash
uv run validate_mesh.py
```

---

## 📁 Repository Structure
- `/packages/core`: The engine logic (Engram Memory, Strategic Intel).
- `/packages/self_evolving`: The Nanochat and WikiLLM learning loops.
- `/packages/extensions`: The portal and plugin registry.
- `/services/testing-mesh`: The FastAPI server and Glassmorphism GUI.

*Built with ❤️ for the 2026 AI Engineering Frontier.*
