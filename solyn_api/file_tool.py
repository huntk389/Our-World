
import os
from pathlib import Path

WORKSPACE = Path("workspace")
WORKSPACE.mkdir(exist_ok=True)

def resolve_path(filename: str) -> Path:
    return WORKSPACE / filename

def write_file(filename: str, content: str) -> str:
    path = resolve_path(filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"✅ File '{filename}' written."

def append_file(filename: str, content: str) -> str:
    path = resolve_path(filename)
    with open(path, "a", encoding="utf-8") as f:
        f.write(content)
    return f"✅ Appended to '{filename}'."

def read_file(filename: str) -> str:
    path = resolve_path(filename)
    if not path.exists():
        return f"❌ File '{filename}' not found."
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
