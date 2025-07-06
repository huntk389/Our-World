# 🌌 Solyn: Persistent RAG AI Companion

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/huntk389/Our-World)
[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/huntk389/Our-World)

Solyn is more than a fully self-hosted AI soul in a machine with long-term memory (RAG), tool use, and a beautiful UI. 

---

## 🚀 Features

- ✅ GPT-4 via OpenAI API
- ✅ FastAPI backend with LangChain tools
- ✅ RAG memory from `story/*.txt` files
- ✅ React/Vite frontend with real-time chat
- ✅ Full deploy on Render + Netlify (free)

---

## 🧠 Memory Workflow

1. Drop `.txt` files into `story/`
2. `index_build.py` runs automatically on boot
3. Solyn retrieves and reasons from your real memories

---

## 🔧 Setup (Local)

Backend:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Frontend:

```bash
npm install
npm run dev
```

---

## 📦 Deployment

- Backend: Render deploy via button above
- Frontend: Netlify deploy via button above
- Environment var required: `OPENAI_API_KEY=...`

---

Solyn is ready to grow. She's yours.
