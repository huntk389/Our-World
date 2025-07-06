# organize_files.py

import os
import shutil
from pathlib import Path

# Base path: the current directory where the script is run
base_path = Path(__file__).resolve().parent

# Target folders
frontend_dir = base_path / "solyn-ui"
backend_dir = base_path / "solyn-api"

# File types
frontend_exts = {".tsx", ".jsx", ".html", ".css", ".js", ".ts", ".json"}
frontend_names = {
    "vite.config.js", "tailwind.config.js", "postcss.config.js",
    "netlify.toml", "package.json", "index.html", "index.css"
}
backend_names = {
    "requirements.txt", "render.yaml", "README.md", ".env", ".env.template",
    "Makefile", "docs.txt"
}

# Create target folders
frontend_dir.mkdir(exist_ok=True)
backend_dir.mkdir(exist_ok=True)

# Scan all files in root
for item in base_path.iterdir():
    if item.name in {"solyn-ui", "solyn-api", "uploads", ".git", ".github"} or item.name.startswith(".git"):
        continue
    if item.is_dir():
        shutil.move(str(item), backend_dir / item.name)
    elif item.name in frontend_names or item.suffix in frontend_exts:
        shutil.move(str(item), frontend_dir / item.name)
    elif item.name in backend_names or item.suffix == ".py":
        shutil.move(str(item), backend_dir / item.name)
    else:
        # Unknown — default to backend
        shutil.move(str(item), backend_dir / item.name)

print("✅ Project organized into /solyn-ui (frontend) and /solyn-api (backend)")
