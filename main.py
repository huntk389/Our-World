import index_build

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os

from tool_agent import run_tool_agent

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class QuestionRequest(BaseModel):
    question: str

class TaskRequest(BaseModel):
    task: str

@app.post("/ask")
def ask_solyn(request: QuestionRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": request.question}]
        )
        return {"answer": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/tool")
def run_tool(request: TaskRequest):
    try:
        result = run_tool_agent(request.task)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
