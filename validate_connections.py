import httpx
import asyncio
from typing import Dict, List

BASE_URL = "http://localhost:8081"

async def test_provider(client: httpx.AsyncClient, provider: str):
    try:
        resp = await client.get("/api/test-connection", params={"provider": provider}, timeout=5.0)
        data = resp.json()
        return {
            "provider": provider,
            "status": data.get("status", "unknown").upper(),
            "details": "Connection Established" if data.get("status") == "active" else "Service Offline/Timeout"
        }
    except Exception as e:
        return {"provider": provider, "status": "ERROR", "details": str(e)}

async def run_connectivity_audit():
    print("--- 🌐 NAVYA MYTHOS: API CONNECTIVITY AUDIT ---")
    
    providers = ["local_mythos", "ollama", "lm_studio"]
    
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        # Check if mesh is up first
        try:
            await client.get("/health")
        except:
            print("❌ Error: Testing Mesh server is not running on localhost:8081")
            return

        tasks = [test_provider(client, p) for p in providers]
        results = await asyncio.gather(*tasks)

    print(f"{'Provider':<20} | {'Status':<10} | {'Diagnostics'}")
    print("-" * 60)
    
    active_count = 0
    for r in results:
        status_icon = "✅" if r["status"] == "ACTIVE" else "❌"
        if r["status"] == "ACTIVE": active_count += 1
        print(f"{r['provider']:<20} | {r['status']:<10} | {status_icon} {r['details']}")

    # 3rd Party Placeholder Validation
    print(f"{'third_party_gateway':<20} | {'READY':<10} | 🔒 Awaiting API Key in GUI")

    print("-" * 60)
    score = (active_count / len(providers)) * 100
    print(f"CONNECTIVITY STABILITY SCORE: {score:.0f}/100")
    
    if score == 100:
        print("RESULT: FULLY WIRED - All local neural engines online.")
    elif score > 0:
        print("RESULT: HYBRID - System operational but some engines are offline.")
    else:
        print("RESULT: ISOLATED - No local LLM engines detected.")

if __name__ == "__main__":
    asyncio.run(run_connectivity_audit())
