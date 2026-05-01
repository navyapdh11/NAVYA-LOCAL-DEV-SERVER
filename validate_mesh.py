import asyncio
import time
from typing import Dict

import httpx

BASE_URL = "http://localhost:8081"


async def test_endpoint(
    client: httpx.AsyncClient,
    name: str,
    path: str,
    method: str = "GET",
    params: Dict = None,
    data: Dict = None,
):
    start = time.time()
    try:
        if method == "GET":
            resp = await client.get(path, params=params, timeout=15.0)
        else:
            resp = await client.post(path, params=params, json=data, timeout=15.0)

        latency = (time.time() - start) * 1000
        status = "PASS" if resp.status_code == 200 else "FAIL"
        return {"name": name, "status": status, "latency": latency, "code": resp.status_code}
    except Exception as e:
        return {"name": name, "status": f"ERROR: {str(e)}", "latency": 0, "code": 500}


async def run_validation():
    print("--- 🚀 NAVYA MYTHOS: SYSTEM VALIDATION LOOP ---")

    results = []
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        # 1. Base Health
        results.append(await test_endpoint(client, "Core Health", "/health"))

        # 2. Agentic Verification (TestSprite)
        results.append(
            await test_endpoint(
                client,
                "Full-Stack Audit Agent",
                "/test/run",
                "POST",
                params={"task": "Full Stack Integrity Audit"},
            )
        )

        # 3. AEO Verification Logic
        results.append(await test_endpoint(client, "AEO/GEO Verifier", "/aeo-verify"))

        # 4. API Hub Connectivity (Local Mythos check)
        results.append(
            await test_endpoint(
                client,
                "API Hub Bridge",
                "/api/test-connection",
                params={"provider": "local_mythos"},
            )
        )

        # 5. Strategic Intelligence (Real Scraping Test)
        results.append(
            await test_endpoint(
                client, "Strategic Intel Engine", "/intel", params={"url": "https://www.google.com"}
            )
        )

        # 6. Self-Evolving Core (Run Evolved Test)
        results.append(
            await test_endpoint(
                client,
                "Self-Evolving Test",
                "/evolve/run-test",
                method="POST",
                params={"layer": "frontend", "task": "Full Stack Integrity Audit"},
            )
        )

        # 7. Self-Evolving Core (History)
        results.append(await test_endpoint(client, "WikiLLM Audit History", "/evolve/history"))

        # 8. Extension Portal
        results.append(await test_endpoint(client, "Extension Registry", "/extensions"))

        # 9. GitHub Integration (Repo Info)
        results.append(
            await test_endpoint(
                client,
                "GitHub Repo Info",
                "/github/repo-info",
                params={"repo": "navyapdh11/NAVYA-LOCAL-DEV-SERVER"},
            )
        )

        # 10. API Gateway (Forwarding test to localhost health)
        results.append(
            await test_endpoint(
                client,
                "API Gateway Forward",
                "/api/forward",
                method="POST",
                data={"url": f"{BASE_URL}/health"},
            )
        )

    # Calculate Metrics
    total_score = 0
    print(f"{'Endpoint':<25} | {'Status':<10} | {'Latency':<10} | {'Score'}")
    print("-" * 65)

    # 8 tests, roughly 12.5 points each
    max_score_per_test = 100 / len(results)

    for r in results:
        score = max_score_per_test if r["status"] == "PASS" else 0
        # Latency Penalty
        if r["latency"] > 1500 and "Intel" not in r["name"]:
            score -= max_score_per_test * 0.25  # 25% penalty

        total_score += score
        print(
            f"{r['name']:<25} | {r['status']:<10} | {r['latency']:>7.2f}ms | {score:.1f}/{max_score_per_test:.1f}"
        )

    print("-" * 65)
    print(f"FINAL INFRASTRUCTURE SCORE: {total_score:.0f}/100")

    if total_score >= 90:
        print("STATUS: ENTERPRISE GRADE - READY FOR SCALE")
    elif total_score >= 70:
        print("STATUS: OPERATIONAL - OPTIMIZATION ADVISED")
    else:
        print("STATUS: CRITICAL - INFRASTRUCTURE REPAIR REQUIRED")


if __name__ == "__main__":
    asyncio.run(run_validation())
