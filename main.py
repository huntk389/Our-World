from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/ask")
def ask_solyn(request: QuestionRequest):
    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": request.question}]
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))