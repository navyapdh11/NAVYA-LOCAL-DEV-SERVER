import json
import os
from typing import Dict, List, Any

class SolutionChatEngine:
    """
    2026 RAG-lite Chat Engine for Strategic Solutions.
    Queries the persistent WikiLLM knowledge base to provide agentic advice.
    """
    def __init__(self, kb_path: str = "knowledge_base/audit_history.json"):
        self.kb_path = kb_path
        self.memory = self._load_kb()

    def _load_kb(self) -> List[Dict]:
        if os.path.exists(self.kb_path):
            with open(self.kb_path, "r") as f:
                return json.load(f)
        return []

    def query_solutions(self, user_query: str) -> Dict[str, Any]:
        """
        Scans memory for relevant site profiles and synthesizes a solution.
        """
        query_lower = user_query.lower()
        relevant_profiles = []
        
        # 1. Retrieval (Keyword-based semantic filter)
        for entry in self.memory:
            url = entry.get("data", {}).get("url", "").lower()
            if any(word in url or word in query_lower for word in query_lower.split()):
                relevant_profiles.append(entry)
        
        # 2. Synthesis (Agentic Reasoning simulation)
        if not relevant_profiles:
            # Fallback to general cross-industry wisdom
            relevant_profiles = self.memory[:5] 

        # Extract common thrashing moves from relevant profiles
        suggested_moves = []
        for p in relevant_profiles:
            moves = p.get("data", {}).get("moves", [])
            if isinstance(moves, list):
                suggested_moves.extend(moves)
            elif isinstance(moves, int): # Round 1-24 used ints for moves count in data
                 suggested_moves.append(f"Execute {moves} standard thrashing moves identified for {p['data']['url']}")

        # 3. Formulate Solution
        response = {
            "answer": f"Based on the strategic footprints of {len(relevant_profiles)} global leaders in my memory, here is your path to dominance:",
            "key_insights": [
                "Target detected AEO gaps in institutional markup.",
                "Leverage high-latency competitive vulnerabilities found in recent benchmarks."
            ],
            "recommended_actions": list(set(suggested_moves))[:4],
            "context_source": [p["data"]["url"] for p in relevant_profiles[:3]]
        }

        return response
