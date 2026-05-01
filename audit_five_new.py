import asyncio
import datetime
import json
import os
import time
from typing import Dict, List
import httpx
import pandas as pd

BASE_URL = "http://localhost:8081"
# Target different sites to ensure fresh data
TARGET_SITES = [
    "https://www.uber.com",
    "https://www.airbnb.com",
    "https://www.spotify.com",
    "https://www.zoom.us",
    "https://www.slack.com",
]

def update_persistent_memory(results: List[Dict]):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    history_path = os.path.join(script_dir, "knowledge_base/audit_history.json")
    if not os.path.exists(history_path):
        history = []
    else:
        with open(history_path, "r") as f:
            try:
                history = json.load(f)
            except:
                history = []

    new_entries = 0
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
                    "pricing": r["pricing"],
                },
                "id": f"audit-new-{int(time.time())}-{new_entries}"
            }
            history.append(entry)
            new_entries += 1

    with open(history_path, "w") as f:
        json.dump(history, f, indent=2)
    print(f"\n💾 Persistent memory updated: {new_entries} new records added.")

async def analyze_site(client: httpx.AsyncClient, url: str) -> Dict:
    start = time.time()
    try:
        resp = await client.get("/intel", params={"url": url}, timeout=30.0)
        latency = (time.time() - start) * 1000
        data = resp.json()

        if resp.status_code == 200 and "scrape" in data:
            # Handle list vs dict signals structure
            signals_data = data["strategy"]["signals"]
            aeo_keywords = signals_data.get("aeo_keywords", [])
            sig_count = len(signals_data) + (len(aeo_keywords) if isinstance(aeo_keywords, list) else 0)
            
            return {
                "url": url,
                "status": "SUCCESS",
                "latency_ms": latency,
                "content_len": data["scrape"]["content_length"],
                "signals": sig_count,
                "moves": len(data["strategy"]["recommended_thrashing_moves"]),
                "enterprise": 1 if signals_data.get("enterprise_focus") else 0,
                "pricing": 1 if signals_data.get("pricing_detected") else 0,
            }
        error_msg = data.get("error", data.get("status", f"HTTP {resp.status_code}"))
        return {"url": url, "status": f"FAILED ({error_msg})", "latency_ms": latency}
    except Exception as e:
        return {"url": url, "status": f"ERROR: {str(e)[:40]}", "latency_ms": 0}

async def run_benchmark():
    print(f"--- 🚀 NAVYA MYTHOS: CUSTOM STRATEGY AUDIT ({len(TARGET_SITES)} SITES) ---")
    
    results = []
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        # Check if mesh is up
        try:
            await client.get("/health")
        except:
            print("❌ Error: Testing Mesh server is not running on localhost:8081")
            return

        tasks = [analyze_site(client, url) for url in TARGET_SITES]
        results = await asyncio.gather(*tasks)

    # Statistical Report
    success_results = [r for r in results if r["status"] == "SUCCESS"]
    df = pd.DataFrame(success_results)

    print("\n" + "=" * 85)
    print(f"{'Target URL':<30} | {'Status':<10} | {'Lat (ms)':<10} | {'Signals':<8} | {'Moves'}")
    print("-" * 85)

    for r in results:
        lat_str = f"{r['latency_ms']:>7.1f}" if r["latency_ms"] > 0 else "N/A"
        sig_str = str(r.get("signals", "N/A"))
        mov_str = str(r.get("moves", "N/A"))
        print(f"{r['url']:<30} | {r['status']:<10} | {lat_str} | {sig_str:<8} | {mov_str}")

    if not df.empty:
        print("\n📈 AGGREGATE STRATEGY METRICS")
        print(f"- Avg Latency: {df['latency_ms'].mean():.2f}ms")
        print(f"- Max Latency: {df['latency_ms'].max():.2f}ms")
        print(f"- Enterprise Penetration: {df['enterprise'].mean()*100:.0f}%")
        print(f"- Pricing Transparency: {df['pricing'].mean()*100:.0f}%")
        print(f"- Avg Strategy Signals: {df['signals'].mean():.1f}")
        print(f"- Total Moves Generated: {df['moves'].sum()}")
        
        update_persistent_memory(results)
    else:
        print("\n❌ No successful audits to record.")

if __name__ == "__main__":
    asyncio.run(run_benchmark())
