import httpx


class SmitheryAdapter:
    """
    Adapter for integrating MCP tools from Smithery.ai.
    """

    BASE_URL = "https://api.smithery.ai/v1"

    @staticmethod
    async def fetch_tools():
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{SmitheryAdapter.BASE_URL}/tools")
                try:
                    return response.json()
                except Exception as je:
                    return {"error": f"JSON Decode Error: {str(je)}", "raw": response.text[:500]}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    async def get_tool_manifest(tool_id: str):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{SmitheryAdapter.BASE_URL}/tools/{tool_id}/manifest")
                try:
                    return response.json()
                except Exception as je:
                    return {"error": f"JSON Decode Error: {str(je)}", "raw": response.text[:500]}
        except Exception as e:
            return {"error": str(e)}
