import httpx
import os

class InferenceOrchestrator:
    def __init__(self, vector_engine_url="http://localhost:3002", inference_gateway=None):
        self.vector_engine_url = vector_engine_url
        self.inference_gateway = inference_gateway

    async def retrieve_context(self, query: str):
        async with httpx.AsyncClient() as client:
            resp = await client.post(f"{self.vector_engine_url}/retrieve", params={"query": query})
            return resp.json().get("results", [])

    async def run_inference_loop(self, query: str):
        context = await self.retrieve_context(query)
        prompt = f"Context: {context}\n\nQuery: {query}\n\nPerform Chain-of-Thought reasoning."
        return await self.inference_gateway.generate(prompt)
