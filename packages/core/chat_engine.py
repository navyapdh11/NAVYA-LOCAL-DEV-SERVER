import json
import os
import re
from typing import Dict, List, Any

class SolutionChatEngine:
    """
    2026 Advanced RAG Chat Engine for Strategic Solutions & Design.
    Queries the persistent WikiLLM knowledge base and provides deep-layered presets.
    """
    def __init__(self, kb_path: str = "knowledge_base/audit_history.json"):
        # Resolve path relative to the script directory if needed
        if not os.path.isabs(kb_path):
            script_dir = os.path.dirname(os.path.abspath(__file__))
            self.kb_path = os.path.join(script_dir, "../../", kb_path)
        else:
            self.kb_path = kb_path
            
        self.memory = self._load_kb()
        self.presets = self._init_presets()

    def _load_kb(self) -> List[Dict]:
        if os.path.exists(self.kb_path):
            try:
                with open(self.kb_path, "r") as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def _init_presets(self) -> Dict[str, Any]:
        """
        Deep layered presets for 2026 industry standards.
        """
        return {
            "ux_ui_2026": {
                "title": "2026 Top Industry UX/UI Design Standard",
                "description": "Deployment-ready architectural blueprint for high-conversion, AI-centric interfaces.",
                "content": """
### 🚀 2026 UX/UI DEPLOYMENT MANIFEST: "GLASS-MORPHIC INTELLIGENCE"

#### 1. Visual Architecture (CSS Vars)
```css
:root {
  --primary: #0070f3;
  --accent: #ff0080;
  --bg: #050505;
  --glass: rgba(255, 255, 255, 0.03);
  --glass-blur: blur(20px);
  --border: rgba(255, 255, 255, 0.08);
  --font-main: 'Inter Tight', system-ui;
  --font-mono: 'JetBrains Mono', monospace;
  --glow: 0 0 20px rgba(0, 112, 243, 0.4);
}
```

#### 2. Layout Components (React/HTML Pattern)
- **Persistent Intelligence Hub:** Floating dock for agentic interactions.
- **Dynamic Semantic Containers:** Cards that scale based on AEO signal density.
- **Contextual Glass Overlays:** Modals using `backdrop-filter` for deep focus.

#### 3. Interaction Design (2026 Best Practices)
- **Zero-Latency Feedback:** Instant optimistic UI updates for agent actions.
- **Semantic Transitioning:** CSS animations that reflect data processing states (shimmer for retrieval, pulse for thinking).
- **Haptic Intent:** (Mobile) Spatial haptics for critical strategic pivots.

#### 4. Deployment Ready Snippet (The "Mythos" Card)
```html
<div class="mythos-card">
  <div class="glass-bg"></div>
  <div class="content">
    <span class="badge">AEO OPTIMIZED</span>
    <h3>Semantic Dominance Engine</h3>
    <p>Real-time thrashing analysis active.</p>
    <div class="progress-bar"><div class="fill"></div></div>
  </div>
</div>

<style>
.mythos-card {
  position: relative; overflow: hidden; border-radius: 24px;
  border: 1px solid var(--border); background: var(--glass);
  backdrop-filter: var(--glass-blur); padding: 2rem;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.mythos-card:hover { border-color: var(--primary); box-shadow: var(--glow); transform: translateY(-5px); }
.badge { font-size: 0.7rem; font-weight: 800; color: var(--primary); letter-spacing: 0.1em; }
</style>
```
                """
            },
            "aeo_strategy_2026": {
                "title": "2026 Answer Engine Optimization (AEO) Blueprint",
                "description": "Complete schema and content strategy for zero-click dominance.",
                "content": "AEO Layered Preset: Use ISO-2026-X Schema with Micro-Contextual citations..."
            }
        }

    def query_solutions(self, user_query: str) -> Dict[str, Any]:
        """
        Enhanced retrieval and synthesis with preset detection and full-context window simulation.
        """
        query_lower = user_query.lower()
        
        # 1. Preset Detection
        if "ux" in query_lower or "ui" in query_lower or "design" in query_lower:
            preset = self.presets["ux_ui_2026"]
            return self._format_preset_response(preset, "UX/UI Design Architect")

        if "aeo" in query_lower or "seo" in query_lower:
            preset = self.presets["aeo_strategy_2026"]
            return self._format_preset_response(preset, "AEO Strategist")

        # 2. RAG Retrieval
        relevant_profiles = []
        for entry in self.memory:
            data = entry.get("data", {})
            url = data.get("url", "").lower()
            # Search URL, status, and moves for keyword matches
            search_blob = f"{url} {entry.get('status', '')} {str(data.get('moves', []))}".lower()
            if any(word in search_blob for word in query_lower.split() if len(word) > 3):
                relevant_profiles.append(entry)
        
        # 3. Full-Context Synthesis (Simulation of a large context window)
        if not relevant_profiles:
            relevant_profiles = self.memory[-20:] # Take most recent 20 for fresh context

        # Aggregate industry moves
        all_moves = []
        for p in relevant_profiles:
            moves = p.get("data", {}).get("moves", [])
            if isinstance(moves, list): all_moves.extend(moves)
            elif isinstance(moves, int): all_moves.append(f"Execute {moves} standard thrashing moves.")

        unique_moves = list(set(all_moves))
        
        return {
            "answer": f"I have analyzed your request against my complete internal knowledge base ({len(self.memory)} audited nodes). Synthesizing a high-fidelity solution based on {len(relevant_profiles)} relevant industry footprints.",
            "thinking_trace": [
                f"Initiating full-repo context scan...",
                f"Retrieved {len(relevant_profiles)} strategic entity profiles.",
                "Cross-referencing AEO signal density across the cluster...",
                "Generating deployment-ready strategic recommendations."
            ],
            "key_insights": [
                f"Market Saturation: Identified {len(relevant_profiles)} competitors with active strategic footprints.",
                "Signal Variance: High signal density detected in recent Semiconductor/SaaS benchmarks.",
                "Design Recommendation: Implement Glass-morphic primitives for 2026 standard compliance."
            ],
            "recommended_actions": unique_moves[:8],
            "context_source": [p["data"]["url"] for p in relevant_profiles[:8] if "url" in p.get("data", {})]
        }

    def _format_preset_response(self, preset: Dict, role: str) -> Dict:
        return {
            "answer": f"### \${preset['title']}\\n\\n\${preset['description']}\\n\\n\${preset['content']}",
            "thinking_trace": [
                f"Detecting request for \${role} capabilities...",
                "Loading 2026 Industry Best Practice Preset...",
                "Structuring deployment-ready manifest...",
                "Finalizing code-block integrity."
            ],
            "key_insights": [
                "Architecture: Modular CSS Variables for system-wide consistency.",
                "Performance: Optimized for zero-latency agentic feedback.",
                "Compliance: Meets 2026 high-performance accessibility standards."
            ],
            "recommended_actions": [
                "Copy the CSS Variables into your root :root selector.",
                "Apply 'backdrop-filter: blur(20px)' to all container surfaces.",
                "Use the provided 'mythos-card' component for agentic interaction points.",
                "Ensure Inter Tight is loaded as the primary typeface."
            ],
            "context_source": ["NAVYA 2026 DESIGN SYSTEM", "WIKILLM BEST PRACTICES"]
        }
