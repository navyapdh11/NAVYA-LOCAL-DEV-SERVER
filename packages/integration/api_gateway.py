import httpx
from typing import Dict, Any

class APIGateway:
    @staticmethod
    async def forward_request(url: str, method: str = "GET", payload: Dict[str, Any] = None, headers: Dict[str, str] = None):
        async with httpx.AsyncClient() as client:
            try:
                request_headers = headers or {}
                response = await client.request(method, url, json=payload, headers=request_headers)
                return {
                    "status": "success", 
                    "status_code": response.status_code,
                    "data": response.json() if response.text else None
                }
            except Exception as e:
                return {"status": "error", "message": str(e)}
