
# Solyn Agent (LangChain + RAG)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/YOUR_USERNAME/YOUR_REPO)

## 🚀 Overview

- FastAPI + LangChain agent
- GPT-4 with file tools, memory & dev mode
- RAG memory from .txt files in `story/`
- Web UI runs on Oracle (Gradio)

---

## 🌐 Deploy to Render

1. Click the button above ☝️
2. Set environment variable:
   - `OPENAI_API_KEY=your-openai-key`
3. Render will install and run Solyn automatically

---

## 🛠 Run Locally

```bash
python index_build.py
python hash_refresh.py
```

## 📁 Web UI (Oracle)

```bash
cd ui/
python3 solyn_ui.py
```
Then open: http://<your_oracle_ip>:8501

---

## 🧠 Memory

Combines:
- 🔁 ConversationBufferMemory
- 📚 Chroma vector search (RAG)

---

## 🧰 Tools

- Create/edit files from user input
- Developer mode (`dev_mode=true`) for transparency

---
