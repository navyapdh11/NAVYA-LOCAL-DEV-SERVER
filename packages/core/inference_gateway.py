import os
import httpx

class InferenceGateway:
    """Centralized DeepSeek V4 Inference Gateway (SGLang)."""
    def __init__(self, endpoint=os.getenv("DEEPSEEK_V4_ENDPOINT", "http://localhost:30000")):
        self.endpoint = endpoint

    async def generate(self, prompt: str, system: str = "You are a strategic AI agent."):
        async with httpx.AsyncClient() as client:
            try:
                resp = await client.post(f"{self.endpoint}/generate", json={
                    "text": f"<|system|>{system}<|user|>{prompt}<|assistant|>",
                    "sampling_params": {"max_new_tokens": 1024, "temperature": 0.7}
                }, timeout=30.0)
                return resp.json().get("text", "")
            except Exception as e:
                print(f"Inference Error: {e}")
                return ""
