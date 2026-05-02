import httpx

class AuditBridge:
    def __init__(self, audit_engine_url="http://localhost:3001"):
        self.url = audit_engine_url

    async def trigger_audit(self, url, location="au_sydney"):
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"{self.url}/trigger-audit",
                json={"url": url, "location": location},
                timeout=120.0
            )
            return resp.json()
