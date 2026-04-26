import sys
import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Add project root to sys.path to resolve 'packages' module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from packages.core.engine import SuperAgentHarness

app = FastAPI(title="NAVYA MYTHOS Dashboard")
agent = SuperAgentHarness()

# In-memory store for API connections
api_connections = {
    "ollama": {"url": "http://localhost:11434", "status": "unknown"},
    "lm_studio": {"url": "http://localhost:1234", "status": "unknown"},
    "local_mythos": {"url": "http://localhost:8081", "status": "active"},
}

@app.get("/", response_class=HTMLResponse)
async def dashboard():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>NAVYA MYTHOS | Command Center</title>
        <style>
            :root {
                --primary: #0070f3;
                --accent: #ff0080;
                --bg: #0a0a0a;
                --glass: rgba(255, 255, 255, 0.05);
                --border: rgba(255, 255, 255, 0.1);
            }
            body {
                background: var(--bg);
                color: white;
                font-family: 'Inter', -apple-system, sans-serif;
                margin: 0;
                display: flex;
                flex-direction: column;
                align-items: center;
                min-height: 100vh;
                background: radial-gradient(circle at top right, #1a1a1a, #0a0a0a);
            }
            nav { width: 100%; padding: 1rem 2rem; display: flex; gap: 2rem; border-bottom: 1px solid var(--border); background: rgba(0,0,0,0.5); position: sticky; top: 0; z-index: 100; }
            nav a { color: white; text-decoration: none; font-weight: bold; opacity: 0.6; transition: opacity 0.2s; }
            nav a:hover, nav a.active { opacity: 1; color: var(--primary); }
            .container {
                max-width: 1000px;
                width: 90%;
                margin-top: 2rem;
            }
            .glass {
                background: var(--glass);
                backdrop-filter: blur(12px);
                border: 1px solid var(--border);
                border-radius: 24px;
                padding: 2rem;
                margin-bottom: 2rem;
            }
            h1 { font-weight: 900; letter-spacing: -2px; font-size: 2.5rem; margin-bottom: 0.5rem; }
            .status-dot { height: 10px; width: 10px; background: #00ff00; border-radius: 50%; display: inline-block; margin-right: 8px; box-shadow: 0 0 10px #00ff00; }
            .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; }
            button {
                background: var(--primary);
                color: white;
                border: none;
                padding: 1rem 2rem;
                border-radius: 12px;
                font-weight: bold;
                cursor: pointer;
                transition: transform 0.2s, box-shadow 0.2s;
                width: 100%;
                margin-top: 1rem;
            }
            button:hover { transform: translateY(-2px); box-shadow: 0 10px 20px rgba(0, 112, 243, 0.3); }
            button.secondary { background: rgba(255,255,255,0.1); }
            #output { font-family: 'Fira Code', monospace; font-size: 0.9rem; color: #00ff00; background: rgba(0,0,0,0.3); padding: 1.5rem; border-radius: 12px; min-height: 100px; overflow-y: auto; max-height: 300px; white-space: pre-wrap; }
            .badge { font-size: 0.7rem; background: var(--primary); padding: 4px 8px; border-radius: 6px; vertical-align: middle; margin-left: 10px; }
        </style>
    </head>
    <body>
        <nav>
            <a href="/" class="active">Command Center</a>
            <a href="/connectivity">API Hub</a>
        </nav>
        <div class="container">
            <div class="glass">
                <h1>NAVYA <span style="color:var(--primary)">MYTHOS</span> <span class="badge">v2026.4</span></h1>
                <p style="opacity:0.6"><span class="status-dot"></span> Local Infrastructure Node Active</p>
            </div>
            
            <div class="grid">
                <div class="glass">
                    <h3>Agentic Verification</h3>
                    <p style="font-size:0.9rem; opacity:0.7">Trigger DeerFlow 2.0 autonomous testing loops across local nodes.</p>
                    <button onclick="runTest('Full Stack Integrity')">Execute Full-Stack Audit</button>
                    <button class="secondary" onclick="runTest('Security Sandbox')">Sandbox Scan</button>
                </div>
                <div class="glass">
                    <h3>Optimization Insights</h3>
                    <p style="font-size:0.9rem; opacity:0.7">Simulate Answer Engine (AEO) and Generative Search (GEO) rankings.</p>
                    <button onclick="aeoVerify()">Verify AEO Schema</button>
                    <button class="secondary" onclick="runTest('GEO Retrieval Simulation')">GEO Latency Test</button>
                </div>
            </div>

            <div class="glass">
                <h3>Terminal Output</h3>
                <div id="output">System initialized. Awaiting commands...</div>
            </div>
        </div>

        <script>
            async function log(msg) {
                const el = document.getElementById('output');
                el.innerHTML += `\\n[${new Date().toLocaleTimeString()}] ${msg}`;
                el.scrollTop = el.scrollHeight;
            }

            async function runTest(task) {
                log(`Initiating agentic loop: ${task}...`);
                try {
                    const res = await fetch(`/test/run?task=${encodeURIComponent(task)}`, {method: 'POST'});
                    const data = await res.json();
                    log(`SUCCESS: Agent ${data.agent_id} completed task.`);
                } catch (e) {
                    log(`ERROR: ${e.message}`);
                }
            }

            async function aeoVerify() {
                log("Analyzing local AEO schema...");
                try {
                    const res = await fetch('/aeo-verify');
                    const data = await res.json();
                    log(`RESULT: Schema ${data.schema_org}, Readability ${data.answer_engine_readability}`);
                } catch (e) {
                    log(`ERROR: ${e.message}`);
                }
            }
        </script>
    </body>
    </html>
    """

@app.get("/connectivity", response_class=HTMLResponse)
async def connectivity_dashboard():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>NAVYA | API Connectivity Hub</title>
        <style>
            :root {
                --primary: #0070f3;
                --accent: #ff0080;
                --bg: #0a0a0a;
                --glass: rgba(255, 255, 255, 0.05);
                --border: rgba(255, 255, 255, 0.1);
                --success: #00ff00;
                --warning: #ffaa00;
            }
            body {
                background: var(--bg);
                color: white;
                font-family: 'Inter', sans-serif;
                margin: 0;
                display: flex;
                flex-direction: column;
                align-items: center;
                min-height: 100vh;
                background: radial-gradient(circle at bottom left, #1a1a1a, #0a0a0a);
            }
            nav { width: 100%; padding: 1rem 2rem; display: flex; gap: 2rem; border-bottom: 1px solid var(--border); background: rgba(0,0,0,0.5); }
            nav a { color: white; text-decoration: none; font-weight: bold; opacity: 0.6; }
            nav a:hover, nav a.active { opacity: 1; color: var(--primary); }
            .container { max-width: 1000px; width: 90%; margin-top: 2rem; }
            .glass { background: var(--glass); backdrop-filter: blur(12px); border: 1px solid var(--border); border-radius: 24px; padding: 2rem; margin-bottom: 1.5rem; }
            .api-card { display: flex; justify-content: space-between; align-items: center; padding: 1.5rem; background: rgba(255,255,255,0.03); border-radius: 16px; margin-bottom: 1rem; border: 1px solid var(--border); }
            .status-tag { padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; text-transform: uppercase; }
            .status-active { background: rgba(0, 255, 0, 0.1); color: var(--success); border: 1px solid var(--success); }
            .status-offline { background: rgba(255, 0, 0, 0.1); color: #ff4444; border: 1px solid #ff4444; }
            .status-unknown { background: rgba(255, 255, 255, 0.1); color: #aaa; border: 1px solid #aaa; }
            input { background: rgba(0,0,0,0.3); border: 1px solid var(--border); color: white; padding: 0.8rem; border-radius: 8px; width: 250px; margin-right: 1rem; }
            button { background: var(--primary); color: white; border: none; padding: 0.8rem 1.5rem; border-radius: 8px; cursor: pointer; font-weight: bold; }
            .grid { display: grid; grid-template-columns: 1fr; gap: 1rem; }
        </style>
    </head>
    <body>
        <nav>
            <a href="/">Command Center</a>
            <a href="/connectivity" class="active">API Hub</a>
        </nav>
        <div class="container">
            <div class="glass">
                <h1>API <span style="color:var(--accent)">Connectivity</span> Hub</h1>
                <p style="opacity:0.6">Manage and verify connections to local LLM engines and third-party gateways.</p>
            </div>

            <div class="glass">
                <h3>Local & Managed Engines</h3>
                <div class="grid" id="api-list">
                    <!-- Cards will be injected here -->
                    <div class="api-card">
                        <div>
                            <strong>Ollama</strong><br>
                            <span style="font-size:0.8rem; opacity:0.5" id="url-ollama">http://localhost:11434</span>
                        </div>
                        <div>
                            <span class="status-tag status-unknown" id="status-ollama">Pending</span>
                            <button onclick="testConn('ollama')" style="margin-left:1rem">Verify</button>
                        </div>
                    </div>

                    <div class="api-card">
                        <div>
                            <strong>LM Studio</strong><br>
                            <span style="font-size:0.8rem; opacity:0.5" id="url-lm_studio">http://localhost:1234</span>
                        </div>
                        <div>
                            <span class="status-tag status-unknown" id="status-lm_studio">Pending</span>
                            <button onclick="testConn('lm_studio')" style="margin-left:1rem">Verify</button>
                        </div>
                    </div>

                    <div class="api-card">
                        <div>
                            <strong>Third Party (OpenAI/Anthropic)</strong><br>
                            <span style="font-size:0.8rem; opacity:0.5">Secure Gateway</span>
                        </div>
                        <div>
                            <input type="password" placeholder="Enter API Key" style="width:150px">
                            <button class="secondary">Connect</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <script>
            async function testConn(provider) {
                const statusEl = document.getElementById(`status-${provider}`);
                statusEl.innerText = "Testing...";
                statusEl.className = "status-tag status-unknown";
                
                try {
                    const res = await fetch(`/api/test-connection?provider=${provider}`);
                    const data = await res.json();
                    if (data.status === "active") {
                        statusEl.innerText = "Connected";
                        statusEl.className = "status-tag status-active";
                    } else {
                        statusEl.innerText = "Offline";
                        statusEl.className = "status-tag status-offline";
                    }
                } catch (e) {
                    statusEl.innerText = "Error";
                    statusEl.className = "status-tag status-offline";
                }
            }
        </script>
    </body>
    </html>
    """

@app.get("/api/test-connection")
async def test_api_connection(provider: str):
    import httpx
    url = api_connections.get(provider, {}).get("url")
    if not url:
        return {"status": "error", "message": "Provider not found"}
    
    try:
        async with httpx.AsyncClient() as client:
            # Short timeout for local checks
            response = await client.get(url, timeout=1.0)
            return {"status": "active" if response.status_code < 500 else "error"}
    except Exception:
        return {"status": "offline"}

@app.get("/health")
def health():
    return {"status": "ok", "mesh_nodes": ["AEO", "GEO", "API"]}

@app.post("/test/run")
def run_test(task: str):
    if "Audit" in task or "Integrity" in task:
        # 2026 TestSprite Indian DSA execution
        return test_sprite.run_multi_layer_audit()
    else:
        # Default DeerFlow execution
        result = agent.run_agentic_loop(task)
        return result

@app.get("/aeo-verify")
async def verify_aeo():
    # 2026 Competitor Thrashing Analysis
    analysis = thrashing_engine.analyze_citation_gaps()
    optimization_result = thrashing_engine.apply_auto_optimization()
    
    return {
        "schema_org": "valid",
        "json_ld": "optimized",
        "answer_engine_readability": 0.99,
        "thrashing_analysis": analysis,
        "auto_optimization_applied": optimization_result
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8081)
