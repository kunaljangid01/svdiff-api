from fastapi import FastAPI, HTTPException
from httpx import AsyncClient

app = FastAPI()

SVDIFF_PYTORCH_API = "https://api.bark.pharmaron.com/run"

@app.get("/")
async def read_root():
    return {"message": "Welcome to the SVDiff API!"}

@app.get("/svdiff")
async def get_svdiff_result(prompt: str):
    async with AsyncClient() as client:
        payload = {
            "model_id": "svdiff",
            "prompt": prompt
        }
        response = await client.post(SVDIFF_PYTORCH_API, json=payload)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error processing prompt")
        result = response.json()
        return result
