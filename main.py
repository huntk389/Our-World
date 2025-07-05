from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from openai import OpenAI
from rag_utils import get_context

app = FastAPI()
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
def ask_solyn(req: QuestionRequest):
    context = get_context(req.question)
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"Use this context: {context}"},
                {"role": "user", "content": req.question}
            ]
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))