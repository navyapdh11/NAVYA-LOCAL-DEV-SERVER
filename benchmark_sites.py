import httpx
import asyncio
import time
import pandas as pd
import json
import os
import datetime
from typing import List, Dict

BASE_URL = "http://localhost:8081"
TARGET_SITES = [
    "https://www.allianz.com",
    "https://www.axa.com",
    "https://www.prudential.com",
    "https://www.chubb.com",
    "https://www.metlife.com"
]

def update_persistent_memory(results: List[Dict]):
    history_path = "knowledge_base/audit_history.json"
    if not os.path.exists(history_path):
        history = []
    else:
        with open(history_path, "r") as f:
            try:
                history = json.load(f)
            except:
                history = []
    
    for r in results:
        if r["status"] == "SUCCESS":
            entry = {
                "timestamp": datetime.datetime.now().isoformat(),
                "layer": "strategic_intel",
                "status": "SUCCESS",
                "data": {
                    "url": r["url"],
                    "latency_ms": r["latency_ms"],
                    "signals": r["signals"],
                    "moves": r["moves"],
                    "enterprise": r["enterprise"],
                    "pricing": r["pricing"]
                }
            }
            history.append(entry)
    
    with open(history_path, "w") as f:
        json.dump(history, f, indent=2)
    print(f"\n💾 Persistent memory updated: {len([r for r in results if r['status'] == 'SUCCESS'])} new records added.")

async def analyze_site(client: httpx.AsyncClient, url: str) -> Dict:
    start = time.time()
    try:
        resp = await client.get("/intel", params={"url": url}, timeout=30.0)
        latency = (time.time() - start) * 1000
        data = resp.json()
        
        if resp.status_code == 200 and "scrape" in data:
            return {
                "url": url,
                "status": "SUCCESS",
                "latency_ms": latency,
                "content_len": data["scrape"]["content_length"],
                "signals": len(data["strategy"]["signals"]) + len(data["strategy"]["signals"].get("aeo_keywords", [])),
                "moves": len(data["strategy"]["recommended_thrashing_moves"]),
                "enterprise": 1 if data["strategy"]["signals"].get("enterprise_focus") else 0,
                "pricing": 1 if data["strategy"]["signals"].get("pricing_detected") else 0
            }
        return {"url": url, "status": f"FAILED ({data.get('status', 'unknown')})", "latency_ms": latency}
    except Exception as e:
        return {"url": url, "status": f"ERROR: {str(e)[:20]}", "latency_ms": 0}

async def run_benchmark():
    print(f"--- 🚀 NAVYA MYTHOS: MULTI-SITE STRATEGY BENCHMARK ({len(TARGET_SITES)} SITES) ---")
    print("Initiating autonomous semantic extraction loops...")
    
    results = []
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        tasks = [analyze_site(client, url) for url in TARGET_SITES]
        results = await asyncio.gather(*tasks)

    # Statistical Report
    df = pd.DataFrame([r for r in results if r["status"] == "SUCCESS"])
    
    print("\n" + "="*85)
    print(f"{'Target URL':<30} | {'Status':<10} | {'Lat (ms)':<10} | {'Signals':<8} | {'Moves'}")
    print("-" * 85)
    
    for r in results:
        lat_str = f"{r['latency_ms']:>7.1f}" if r['latency_ms'] > 0 else "N/A"
        sig_str = str(r.get('signals', 'N/A'))
        mov_str = str(r.get('moves', 'N/A'))
        print(f"{r['url']:<30} | {r['status']:<10} | {lat_str} | {sig_str:<8} | {mov_str}")

    print("="*85)
    
    if not df.empty:
        print("\n📈 AGGREGATE STRATEGY METRICS")
        print(f"- Avg Latency: {df['latency_ms'].mean():.2f}ms")
        print(f"- Enterprise Penetration: {df['enterprise'].mean()*100:.0f}%")
        print(f"- Pricing Transparency: {df['pricing'].mean()*100:.0f}%")
        print(f"- Avg Strategy Signals detected: {df['signals'].mean():.1f}")
        print(f"- Total Thrashing Moves Generated: {df['moves'].sum()}")
        
        # 1-100 Performance Score
        # (Status success % * 0.4) + (Avg Signals * 10) + (Low Latency bonus)
        success_rate = len(df) / len(TARGET_SITES)
        score = (success_rate * 40) + (df['signals'].mean() * 15)
        print(f"\nFINAL STRATEGIC READINESS SCORE: {min(100, score):.0f}/100")
        
        # Update persistent knowledge base
        update_persistent_memory(results)
    else:
        print("\n❌ Benchmark failed: No successful extractions.")

if __name__ == "__main__":
    asyncio.run(run_benchmark())
