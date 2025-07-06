# organize_files.py

import os
import shutil
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="🔧 %(levelname)s: %(message)s")

# Files/folders that must remain in root
ROOT_LOCKED = {
    ".github",                 # GitHub workflows
    ".netlify",                # Netlify deploy config
    "solyn-api",               # Backend
    "solyn-ui",                # Frontend
    ".env.template",           # Env template
    "Makefile",                # Build automation
    "README.md",               # Project docs
    "docs.txt",                # Additional docs
    "index_build.py",          # Indexer
    "organize_files.py",       # This script
    "render.yaml",             # Render deploy config
    "solyn_ui.py",             # Frontend helper
}

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
UNORGANIZED_DIR = os.path.join(PROJECT_ROOT, "unorganized")

def should_preserve(path: str) -> bool:
    return os.path.basename(path) in ROOT_LOCKED

def ensure_unorganized_dir():
    if not os.path.exists(UNORGANIZED_DIR):
        os.makedirs(UNORGANIZED_DIR)
        logging.info(f"Created fallback folder: {UNORGANIZED_DIR}")

def move_unlocked_items():
    ensure_unorganized_dir()

    for item in os.listdir(PROJECT_ROOT):
        item_path = os.path.join(PROJECT_ROOT, item)

        if item in ROOT_LOCKED or item.startswith(".venv") or item == "__pycache__":
            continue

        # Move any unexpected files/folders to unorganized/
        target_path = os.path.join(UNORGANIZED_DIR, item)
        try:
            shutil.move(item_path, target_path)
            logging.info(f"Moved 🔀 '{item}' → 'unorganized/'")
        except Exception as e:
            logging.error(f"Failed to move '{item}': {e}")

def main():
    logging.info("🔍 Organizing root files...")
    move_unlocked_items()
    logging.info("✅ Root organization complete.")

if __name__ == "__main__":
    main()
