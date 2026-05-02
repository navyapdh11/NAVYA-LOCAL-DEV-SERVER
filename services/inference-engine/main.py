from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

app = FastAPI(title="Inference Engine")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
index = faiss.IndexFlatL2(384)
documents = []

class Document(BaseModel):
    text: str
    metadata: dict

@app.post("/index")
async def index_document(doc: Document):
    embedding = model.encode([doc.text])
    index.add(np.array(embedding).astype('float32'))
    documents.append(doc)
    return {"status": "indexed", "id": len(documents) - 1}

@app.post("/retrieve")
async def retrieve(query: str, top_k: int = 5):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding).astype('float32'), top_k)
    results = [documents[i] for i in indices[0] if i != -1]
    return {"results": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3002)
