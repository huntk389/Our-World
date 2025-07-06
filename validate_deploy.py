# validate_deploy.py
import os
import sys
import shutil
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

ROOT_LOCKED = {
    ".github",
    "solyn_ui.py",
    "solyn-api",  # will be renamed
    "solyn-ui",
    "Makefile",
    "README.md",
    "docs.txt",
    "index_build.py",
    "main.py",
    "organize_files.py",
    "render.yaml",
    ".env.template",
    "validate_deploy.py",
    "netlify.toml",
}

RENAME_MAP = {
    "solyn-api": "solyn_api",
}


def validate_structure(root_path=".", autofix=False):
    existing = set(os.listdir(root_path))

    # Rename folders if needed
    for bad, good in RENAME_MAP.items():
        bad_path = os.path.join(root_path, bad)
        good_path = os.path.join
