import os
import openai
from fastapi import FastAPI
from pydantic import BaseModel

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask_solyn(query: Query):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are Solyn, a helpful assistant with access to knowledge and memory."},
            {"role": "user", "content": query.question}
        ]
    )
    return {"answer": response['choices'][0]['message']['content']}