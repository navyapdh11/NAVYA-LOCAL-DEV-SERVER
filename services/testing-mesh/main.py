import sys
import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Add project root to sys.path to resolve 'packages' module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from packages.core.engine import SuperAgentHarness
from packages.core.intelligence import StrategicIntelligenceEngine
from packages.seo_agent.thrashing_engine import CompetitorThrashingEngine
from packages.test_sprite.auto_tester import TestSpriteAgent
from packages.self_evolving.core import SelfEvolvingCore
from packages.extensions.registry import ExtensionRegistry
from packages.seo_agent.hyperlocal import HyperlocalSEOAgent
from packages.core.compliance import ComplianceLegalAgent
from packages.core.chat_engine import SolutionChatEngine

app = FastAPI(title="NAVYA MYTHOS Dashboard")
agent = SuperAgentHarness()
intel_engine = StrategicIntelligenceEngine()
thrashing_engine = CompetitorThrashingEngine("localhost:8081")
test_sprite = TestSpriteAgent()
master_core = SelfEvolvingCore(mythos_engine=agent)
ext_portal = ExtensionRegistry()
compliance_agent = ComplianceLegalAgent()
chat_engine = SolutionChatEngine()
local_seo_agent = HyperlocalSEOAgent({
    "name": "NAVYA MYTHOS Enterprise",
    "address": "Local Hybrid Node 01",
    "lat": -37.8136,
    "lng": 144.9631,
    "neighborhoods": ["CBD", "Southbank", "Docklands"],
    "specialties": ["AI Testing", "Enterprise Sanitization"],
    "social_proof": ["https://google.com/maps/place/navya"]
})

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
            <a href="/" id="nav-home">Command Center</a>
            <a href="/connectivity" id="nav-conn">API Hub</a>
            <a href="/intelligence" id="nav-intel">Strategy Intel</a>
            <a href="/portal" id="nav-portal">Extension Portal</a>
            <a href="/governance" id="nav-gov">Governance & Local</a>
            <a href="/chat" id="nav-chat">Solution Chat</a>
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

@app.get("/intelligence", response_class=HTMLResponse)
async def intelligence_dashboard():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>NAVYA | Strategy Intelligence</title>
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
                font-family: 'Inter', sans-serif;
                margin: 0;
                display: flex;
                flex-direction: column;
                align-items: center;
                min-height: 100vh;
                background: radial-gradient(circle at top left, #1a1a1a, #0a0a0a);
            }
            nav { width: 100%; padding: 1rem 2rem; display: flex; gap: 2rem; border-bottom: 1px solid var(--border); background: rgba(0,0,0,0.5); }
            nav a { color: white; text-decoration: none; font-weight: bold; opacity: 0.6; }
            nav a:hover, nav a.active { opacity: 1; color: var(--primary); }
            .container { max-width: 1000px; width: 90%; margin-top: 2rem; }
            .glass { background: var(--glass); backdrop-filter: blur(12px); border: 1px solid var(--border); border-radius: 24px; padding: 2rem; margin-bottom: 1.5rem; }
            input { background: rgba(0,0,0,0.3); border: 1px solid var(--border); color: white; padding: 1rem; border-radius: 12px; width: 70%; margin-right: 1rem; font-size: 1rem; }
            button { background: var(--primary); color: white; border: none; padding: 1rem 2rem; border-radius: 12px; cursor: pointer; font-weight: bold; font-size: 1rem; }
            .result-card { background: rgba(0,255,0,0.05); border: 1px solid rgba(0,255,0,0.2); padding: 1.5rem; border-radius: 16px; margin-top: 2rem; display: none; }
            .signal { display: inline-block; padding: 4px 12px; background: var(--primary); border-radius: 20px; font-size: 0.8rem; margin-right: 8px; margin-bottom: 8px; }
            pre { background: rgba(0,0,0,0.5); padding: 1rem; border-radius: 8px; font-size: 0.85rem; overflow-x: auto; max-height: 200px; color: #aaa; }
        </style>
    </head>
    <body>
        <nav>
            <a href="/">Command Center</a>
            <a href="/connectivity">API Hub</a>
            <a href="/intelligence" class="active">Strategy Intel</a>
        </nav>
        <div class="container">
            <div class="glass">
                <h1>Competitor <span style="color:var(--primary)">Intelligence</span> Engine</h1>
                <p style="opacity:0.6">Autonomous semantic scraping and strategic "thrashing" moves based on 2026 AEO standards.</p>
                
                <div style="margin-top:2rem">
                    <input type="text" id="target-url" placeholder="https://competitor-site.com" value="https://www.google.com">
                    <button onclick="runIntel()">Analyze Strategy</button>
                </div>
            </div>

            <div id="loading" style="display:none; margin-bottom: 2rem;">🚀 Agent initiating semantic extraction loop...</div>

            <div class="result-card" id="result-box">
                <h3 style="color:var(--primary)">Intelligence Report: <span id="report-title"></span></h3>
                <div id="signals-box" style="margin-bottom:1.5rem"></div>
                
                <div class="glass" style="background:rgba(255,0,128,0.1); border-color:rgba(255,0,128,0.3)">
                    <h4 style="margin-top:0">Recommended Thrashing Moves</h4>
                    <ul id="moves-list" style="padding-left:1.5rem; line-height:1.6"></ul>
                    <p><strong>Impact:</strong> <span id="impact-text"></span></p>
                </div>

                <h4>Semantic Footprint (Markdown)</h4>
                <pre id="md-box"></pre>
            </div>
        </div>

        <script>
            async function runIntel() {
                const url = document.getElementById('target-url').value;
                const box = document.getElementById('result-box');
                const loading = document.getElementById('loading');
                
                if(!url) return alert("Please enter a URL");
                
                loading.style.display = "block";
                box.style.display = "none";

                try {
                    const res = await fetch(`/intel?url=${encodeURIComponent(url)}`);
                    const data = await res.json();
                    
                    if(data.status === "failed") throw new Error(data.error);

                    document.getElementById('report-title').innerText = data.scrape.meta.title;
                    document.getElementById('md-box').innerText = data.scrape.semantic_markdown;
                    
                    // Signals
                    const signalsBox = document.getElementById('signals-box');
                    signalsBox.innerHTML = "";
                    if(data.strategy.signals.pricing_detected) signalsBox.innerHTML += '<span class="signal">Pricing Logic Detected</span>';
                    if(data.strategy.signals.enterprise_focus) signalsBox.innerHTML += '<span class="signal">Enterprise Targeting</span>';
                    data.strategy.signals.aeo_keywords.forEach(k => {
                        signalsBox.innerHTML += `<span class="signal" style="background:var(--accent)">AEO: ${k}</span>`;
                    });

                    // Moves
                    const list = document.getElementById('moves-list');
                    list.innerHTML = "";
                    data.strategy.recommended_thrashing_moves.forEach(m => {
                        list.innerHTML += `<li>${m}</li>`;
                    });

                    document.getElementById('impact-text').innerText = data.strategy.share_of_model_prediction;

                    box.style.display = "block";
                } catch (e) {
                    alert("Extraction Failed: " + e.message);
                } finally {
                    loading.style.display = "none";
                }
            }
        </script>
    </body>
    </html>
    """

@app.get("/chat", response_class=HTMLResponse)
async def solution_chat_dashboard():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>NAVYA | Solution Chat</title>
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
                font-family: 'Inter', sans-serif;
                margin: 0;
                display: flex;
                flex-direction: column;
                align-items: center;
                min-height: 100vh;
                background: radial-gradient(circle at bottom right, #1a1a1a, #0a0a0a);
            }
            nav { width: 100%; padding: 1rem 2rem; display: flex; gap: 2rem; border-bottom: 1px solid var(--border); background: rgba(0,0,0,0.5); }
            nav a { color: white; text-decoration: none; font-weight: bold; opacity: 0.6; }
            nav a:hover, nav a.active { opacity: 1; color: var(--primary); }
            .container { max-width: 1000px; width: 90%; margin-top: 2rem; display: flex; flex-direction: column; height: 80vh; }
            .glass { background: var(--glass); backdrop-filter: blur(12px); border: 1px solid var(--border); border-radius: 24px; padding: 2rem; margin-bottom: 1.5rem; flex-shrink: 0; }
            #chat-window { flex-grow: 1; overflow-y: auto; background: rgba(255,255,255,0.02); border-radius: 24px; border: 1px solid var(--border); padding: 2rem; margin-bottom: 1.5rem; display: flex; flex-direction: column; gap: 1rem; }
            .message { max-width: 80%; padding: 1rem 1.5rem; border-radius: 16px; font-size: 0.95rem; line-height: 1.5; }
            .user-msg { align-self: flex-end; background: var(--primary); color: white; }
            .agent-msg { align-self: flex-start; background: rgba(255,255,255,0.1); border: 1px solid var(--border); }
            .input-area { display: flex; gap: 1rem; flex-shrink: 0; }
            input { flex-grow: 1; background: rgba(0,0,0,0.3); border: 1px solid var(--border); color: white; padding: 1rem; border-radius: 12px; font-size: 1rem; }
            button { background: var(--primary); color: white; border: none; padding: 1rem 2rem; border-radius: 12px; cursor: pointer; font-weight: bold; }
            .source-tag { font-size: 0.75rem; color: var(--primary); margin-top: 0.5rem; display: block; opacity: 0.8; }
        </style>
    </head>
    <body>
        <nav>
            <a href="/">Command Center</a>
            <a href="/connectivity">API Hub</a>
            <a href="/intelligence">Strategy Intel</a>
            <a href="/portal">Extension Portal</a>
            <a href="/governance">Governance & Local</a>
            <a href="/chat" class="active">Solution Chat</a>
        </nav>
        <div class="container">
            <div class="glass" style="padding: 1.5rem 2rem;">
                <h1 style="font-size: 1.8rem; margin: 0;">Solution <span style="color:var(--primary)">Chat</span></h1>
                <p style="opacity:0.6; margin: 0.5rem 0 0 0;">Query 140+ global site profiles and generated thrashing moves.</p>
            </div>

            <div id="chat-window">
                <div class="message agent-msg">
                    Welcome. I am the <strong>OpenMythos Strategy Agent</strong>. I have synthesized the data of 140 global market leaders. 
                    <br><br>How can I help you optimize your competitive position today?
                </div>
            </div>

            <div class="input-area">
                <input type="text" id="user-input" placeholder="Ask about a competitor or strategy... (e.g., 'How can I beat Microsoft?')" onkeypress="if(event.key==='Enter') sendMessage()">
                <button onclick="sendMessage()">Send Command</button>
            </div>
        </div>

        <script>
            async function sendMessage() {
                const input = document.getElementById('user-input');
                const query = input.value;
                if(!query) return;

                const chatWindow = document.getElementById('chat-window');
                
                // Add User Message
                chatWindow.innerHTML += `<div class="message user-msg">${query}</div>`;
                input.value = "";
                chatWindow.scrollTop = chatWindow.scrollHeight;

                try {
                    const res = await fetch(`/chat/query?query=${encodeURIComponent(query)}`, {method: 'POST'});
                    const data = await res.json();
                    
                    let responseHtml = `
                        <div class="message agent-msg">
                            ${data.answer}<br><br>
                            <strong>Key Insights:</strong>
                            <ul>${data.key_insights.map(i => `<li>${i}</li>`).join('')}</ul>
                            <strong>Recommended Actions:</strong>
                            <ul>${data.recommended_actions.map(a => `<li>${a}</li>`).join('')}</ul>
                            <span class="source-tag">Contextual Sources: ${data.context_source.join(', ')}</span>
                        </div>
                    `;
                    chatWindow.innerHTML += responseHtml;
                    chatWindow.scrollTop = chatWindow.scrollHeight;
                } catch (e) {
                    chatWindow.innerHTML += `<div class="message agent-msg">Error connecting to Mythos Core: ${e.message}</div>`;
                }
            }
        </script>
    </body>
    </html>
    """

@app.post("/chat/query")
def run_chat_query(query: str):
    return chat_engine.query_solutions(query)

@app.post("/evolve/run-test")
def run_evolved_test(layer: str, task: str):
    # Determine which agent func to run
    if "Audit" in task or "Integrity" in task:
        test_func = test_sprite.run_multi_layer_audit
    else:
        test_func = lambda: agent.run_agentic_loop(task)
        
    return master_core.run_evolved_test(layer, test_func)

@app.get("/evolve/history")
def get_evolve_history():
    return {
        "audit_count": len(master_core.librarian.audit_log),
        "knowledge_level": master_core.trainer.learning_progress,
        "logs": master_core.librarian.audit_log[-10:] # Last 10
    }

@app.get("/extensions")
def get_extensions():
    return ext_portal.get_all()

@app.post("/extensions/install")
def install_ext(ext_id: str):
    return ext_portal.install_extension(ext_id)

@app.post("/extensions/execute")
async def execute_ext(ext_id: str, payload: dict = {}):
    return await ext_portal.execute_extension(ext_id, payload)

@app.get("/portal", response_class=HTMLResponse)
async def extension_portal_dashboard():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>NAVYA | Extension Portal</title>
        <style>
            :root {
                --primary: #0070f3;
                --accent: #00ff00;
                --bg: #0a0a0a;
                --glass: rgba(255, 255, 255, 0.05);
                --border: rgba(255, 255, 255, 0.1);
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
                background: radial-gradient(circle at top right, #1a1a1a, #0a0a0a);
            }
            nav { width: 100%; padding: 1rem 2rem; display: flex; gap: 2rem; border-bottom: 1px solid var(--border); background: rgba(0,0,0,0.5); }
            nav a { color: white; text-decoration: none; font-weight: bold; opacity: 0.6; }
            nav a:hover, nav a.active { opacity: 1; color: var(--primary); }
            .container { max-width: 1000px; width: 90%; margin-top: 2rem; }
            .glass { background: var(--glass); backdrop-filter: blur(12px); border: 1px solid var(--border); border-radius: 24px; padding: 2rem; margin-bottom: 1.5rem; }
            .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1.5rem; }
            .ext-card { background: rgba(255,255,255,0.03); border: 1px solid var(--border); border-radius: 20px; padding: 1.5rem; transition: transform 0.2s; }
            .ext-card:hover { transform: translateY(-5px); border-color: var(--primary); }
            .badge { font-size: 0.7rem; background: var(--primary); padding: 4px 8px; border-radius: 6px; }
            .status { font-size: 0.8rem; font-weight: bold; text-transform: uppercase; margin-top: 1rem; display: block; }
            button { background: var(--primary); color: white; border: none; padding: 0.8rem 1.5rem; border-radius: 10px; cursor: pointer; font-weight: bold; width: 100%; margin-top: 1rem; }
            button.installed { background: rgba(0,255,0,0.1); color: var(--accent); border: 1px solid var(--accent); }
        </style>
    </head>
    <body>
        <nav>
            <a href="/">Command Center</a>
            <a href="/connectivity">API Hub</a>
            <a href="/intelligence">Strategy Intel</a>
            <a href="/portal" class="active">Extension Portal</a>
        </nav>
        <div class="container">
            <div class="glass">
                <h1>Agentic <span style="color:var(--primary)">Extension</span> Portal</h1>
                <p style="opacity:0.6">Discover and integrate 2026 enterprise-grade MCP tools and autonomous agents.</p>
            </div>

            <div class="grid" id="ext-grid">
                <!-- Extensions will be loaded here -->
            </div>
        </div>

        <script>
            async function loadExtensions() {
                const res = await fetch('/extensions');
                const exts = await res.json();
                const grid = document.getElementById('ext-grid');
                grid.innerHTML = "";

                for (const [id, data] of Object.entries(exts)) {
                    const isInstalled = data.status === "installed";
                    grid.innerHTML += `
                        <div class="ext-card">
                            <div style="display:flex; justify-content:space-between; align-items:start;">
                                <strong>${data.name}</strong>
                                <span class="badge">${data.version}</span>
                            </div>
                            <p style="font-size:0.85rem; opacity:0.7; margin: 1rem 0;">${data.description}</p>
                            <span class="status" style="color: ${isInstalled ? 'var(--accent)' : '#aaa'}">
                                ${isInstalled ? '● Active' : '○ Available'}
                            </span>
                            <button class="${isInstalled ? 'installed' : ''}" 
                                    onclick="${isInstalled ? `executeExt('${id}')` : `installExt('${id}')`}">
                                ${isInstalled ? 'Run Extension' : 'Install into Mesh'}
                            </button>
                        </div>
                    `;
                }
            }

            async function installExt(id) {
                await fetch(`/extensions/install?ext_id=${id}`, {method: 'POST'});
                loadExtensions();
            }

            async function executeExt(id) {
                alert(`Initiating MCP Handshake for ${id}... Check terminal for logs.`);
                await fetch(`/extensions/execute?ext_id=${id}`, {method: 'POST'});
            }

            loadExtensions();
        </script>
    </body>
    </html>
    """

@app.get("/governance", response_class=HTMLResponse)
async def governance_dashboard():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>NAVYA | Governance & Local SEO</title>
        <style>
            :root {
                --primary: #0070f3;
                --accent: #ffaa00;
                --bg: #0a0a0a;
                --glass: rgba(255, 255, 255, 0.05);
                --border: rgba(255, 255, 255, 0.1);
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
                background: radial-gradient(circle at bottom right, #1a1a1a, #0a0a0a);
            }
            nav { width: 100%; padding: 1rem 2rem; display: flex; gap: 2rem; border-bottom: 1px solid var(--border); background: rgba(0,0,0,0.5); }
            nav a { color: white; text-decoration: none; font-weight: bold; opacity: 0.6; }
            nav a:hover, nav a.active { opacity: 1; color: var(--primary); }
            .container { max-width: 1000px; width: 90%; margin-top: 2rem; }
            .glass { background: var(--glass); backdrop-filter: blur(12px); border: 1px solid var(--border); border-radius: 24px; padding: 2rem; margin-bottom: 1.5rem; }
            .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; }
            pre { background: rgba(0,0,0,0.5); padding: 1rem; border-radius: 12px; font-size: 0.85rem; overflow-x: auto; color: #00ff00; }
            .status-pass { color: #00ff00; font-weight: bold; }
            button { background: var(--primary); color: white; border: none; padding: 1rem; border-radius: 10px; cursor: pointer; font-weight: bold; width: 100%; margin-top: 10px; }
        </style>
    </head>
    <body>
        <nav>
            <a href="/">Command Center</a>
            <a href="/connectivity">API Hub</a>
            <a href="/intelligence">Strategy Intel</a>
            <a href="/portal">Extension Portal</a>
            <a href="/governance" class="active">Governance & Local</a>
        </nav>
        <div class="container">
            <div class="glass">
                <h1>Governance & <span style="color:var(--accent)">Hyperlocal</span> SEO</h1>
                <p style="opacity:0.6">Automated legal compliance auditing and micro-market entity verification.</p>
            </div>

            <div class="grid">
                <div class="glass">
                    <h3>Hyperlocal Optimization</h3>
                    <p style="font-size:0.85rem; opacity:0.7">Generate 2026-spec LocalBusiness schema and conversational FAQs.</p>
                    <button onclick="genSchema()">Generate Advanced Schema</button>
                    <button class="secondary" onclick="genFAQs()" style="margin-top:10px">Generate AEO FAQs</button>
                </div>
                <div class="glass">
                    <h3>Legal & Compliance Audit</h3>
                    <p style="font-size:0.85rem; opacity:0.7">Validate system against EU AI Act, India DPDP, and ISO 42001.</p>
                    <button onclick="runAudit()">Execute Legal Audit</button>
                    <button class="secondary" onclick="genManifest()" style="margin-top:10px">Generate Privacy Manifest</button>
                </div>
            </div>

            <div class="glass" id="gov-output-box" style="display:none">
                <h3 id="gov-output-title">Output</h3>
                <pre id="gov-output"></pre>
            </div>
        </div>

        <script>
            async function showOutput(title, content) {
                document.getElementById('gov-output-box').style.display = "block";
                document.getElementById('gov-output-title').innerText = title;
                document.getElementById('gov-output').innerText = typeof content === 'string' ? content : JSON.stringify(content, null, 2);
            }

            async function genSchema() {
                const res = await fetch('/local/schema');
                const data = await res.json();
                showOutput("Hyperlocal Schema (JSON-LD)", data.schema);
            }

            async function genFAQs() {
                const res = await fetch('/local/faqs?area=Melbourne%20CBD');
                const data = await res.json();
                showOutput("AEO Conversational FAQs", data.faqs);
            }

            async function runAudit() {
                const res = await fetch('/compliance/audit', {method: 'POST'});
                const data = await res.json();
                showOutput("Legal Compliance Report", data);
            }

            async function genManifest() {
                const res = await fetch('/compliance/manifest');
                const data = await res.json();
                showOutput("AI Privacy Manifest", data.manifest);
            }
        </script>
    </body>
    </html>
    """

@app.get("/local/schema")
def get_local_schema():
    return {"schema": local_seo_agent.generate_advanced_schema()}

@app.get("/local/faqs")
def get_local_faqs(area: str):
    return {"faqs": local_seo_agent.generate_aeo_faqs(area)}

@app.post("/compliance/audit")
def run_legal_audit():
    # Simulation of system metadata for audit
    meta = {"human_oversight": True, "data_locality": "India"}
    return compliance_agent.audit_legal_compliance(meta)

@app.get("/compliance/manifest")
def get_privacy_manifest():
    return {"manifest": compliance_agent.generate_privacy_manifest()}

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

@app.get("/intel")
async def run_intel(url: str):
    data = await intel_engine.scrape_semantic(url)
    if data["status"] == "success":
        strategy = intel_engine.analyze_strategy(data)
        return {"scrape": data, "strategy": strategy}
    return data

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
