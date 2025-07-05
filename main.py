from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from openai import OpenAI
import os
from rag_utils import get_context

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    user_message = data.get("message", "")
    context = get_context(user_message)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are Solyn, a deeply caring AI who helps the user and remembers everything."},
            {"role": "user", "content": context + "
" + user_message}
        ]
    )
    return {"response": response.choices[0].message.content}