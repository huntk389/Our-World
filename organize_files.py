import os
import shutil
from pathlib import Path

base_path = Path(__file__).resolve().parent
frontend_dir = base_path / "solyn-ui"
backend_dir = base_path / "solyn-api"

frontend_exts = {".tsx", ".jsx", ".html", ".css", ".js", ".ts", ".json"}
frontend_names = {
    "vite.config.js", "tailwind.config.js", "postcss.config.js",
    "netlify.toml", "package.json", "index.html", "index.css"
}

backend_names = {
    "main.py", "app.py", "agent.py", "tool_agent.py", "tools.py",
    "query_api.py", "retriever.py", "web_tool.py", "python_tool.py",
    "file_tool.py", "vector_store.py", "rag_utils.py", "hash_refresh.py",
    "requirements.txt", "memory.txt"
}

stay_in_root = {
    "README.md", "render.yaml", "Makefile", "docs.txt",
    ".env", ".env.template", "organize_files.py", "organize_files_solyn.py",
    "solyn_ui.py", "index_build.py"
}

frontend_dir.mkdir(exist_ok=True)
backend_dir.mkdir(exist_ok=True)

for item in base_path.iterdir():
    if item.name in {"solyn-ui", "solyn-api", "uploads", ".git", ".github"} or item.name.startswith(".git"):
        continue
    if item.is_dir():
        shutil.move(str(item), backend_dir / item.name)
    elif item.name in stay_in_root:
        continue
    elif item.name in frontend_names or item.suffix in frontend_exts:
        shutil.move(str(item), frontend_dir / item.name)
    elif item.name in backend_names or item.suffix == ".py":
        shutil.move(str(item), backend_dir / item.name)
    else:
        continue

print("✅ Final structure set. index_build.py and orchestrators stay in root.")