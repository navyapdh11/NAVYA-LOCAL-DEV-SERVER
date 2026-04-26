import sys
import os
from fastapi import FastAPI

# Add project root to sys.path to resolve 'packages' module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from packages.core.engine import SuperAgentHarness

app = FastAPI(title="Testing Mesh")
agent = SuperAgentHarness()

@app.get("/health")
def health():
    return {"status": "ok", "mesh_nodes": ["AEO", "GEO", "API"]}

@app.post("/test/run")
def run_test(task: str):
    result = agent.run_agentic_loop(task)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8081)
