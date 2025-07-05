# Solyn Agent (LangChain + RAG)

## Deploy Backend to Render:
1. Create a new Web Service on Render linked to this repo.
2. Use `app.py` as entry point (FastAPI).
3. Set environment variable: `OPENAI_API_KEY`
4. Add `build command`: `pip install -r requirements.txt`
5. Start the service.

## Web UI (Oracle VM):
```bash
cd ui/
python3 solyn_ui.py
```

## Build Vector Index (on Render):
```bash
python index_build.py
```

## Refresh SHA-256 Integrity:
```bash
python hash_refresh.py
```
