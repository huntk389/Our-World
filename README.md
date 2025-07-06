
# Solyn API — Autonomous AI Agent

A fully featured AI backend with LLM + RAG + Tools.

## 🔥 Features
- GPT-4 `/ask` chat endpoint
- Tool agent `/tool` (file ops, code exec, web)
- FAISS/Chroma vector memory-ready
- Clean workspace folder
- Easy deploy via Render

## 🛠 Endpoints
- `POST /ask`: Ask Solyn a GPT-4 question
- `POST /tool`: Send tool tasks to LangChain agent

## ✅ Deploy
- GitHub → Render → Done.

---

## 🧠 Memory (RAG)

1. Add text files to the `story/` folder (e.g. `memory.txt`)
2. Run `python index_build.py` to generate FAISS index
3. Use `rag_utils.get_context(query)` in chat agents
