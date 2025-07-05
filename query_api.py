from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Solyn API is running"}

@app.post("/query")
def query_endpoint(query: str):
    return {"response": f"Echo: {query}"}
