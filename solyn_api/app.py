from fastapi import FastAPI, Request, UploadFile, File
from agent import get_solyn_response
from retriever import retriever
from tools import tools
import uvicorn

app = FastAPI()

@app.post("/query")
async def query_endpoint(req: Request):
    data = await req.json()
    question = data.get("question", "")
    dev_mode = data.get("dev_mode", False)
    answer = get_solyn_response(question, retriever, tools, dev_mode)
    return {"answer": answer}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    save_path = f"story/{file.filename}"
    with open(save_path, "wb") as f:
        f.write(contents)
    return {"status": "uploaded", "filename": file.filename}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
