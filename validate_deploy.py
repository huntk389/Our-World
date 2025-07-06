# validate_deploy.py
import os
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("validate_deploy.log"),
        logging.StreamHandler()
    ]
)

ROOT_LOCKED = {
    ".github",
    "solyn-api",
    "solyn-ui",
    ".env.template",
    "Makefile",
    "README.md",
    "docs.txt",
    "index_build.py",
    "organize_files.py",
    "render.yaml",
    "solyn_ui.py",
    "main.py",
    "validate_deploy.py",
    "netlify.toml",
}

def validate_root_files(autofix=False):
    root = Path(".")
    current_files = {p.name for p in root.iterdir()}

    missing_files = ROOT_LOCKED - current_files
    unexpected_files = current_files - ROOT_LOCKED

    if missing_files:
        logging.warning("Missing required files/directories:")
        for f in missing_files:
            logging.warning(f"  - {f}")
        if autofix:
            for f in missing_files:
                with open(f, "w") as file:
                    file.write(f"# placeholder for missing file: {f}\n")
                logging.info(f"Restored missing file: {f}")

    if unexpected_files:
        logging.warning("Unexpected files/directories in root:")
        for f in unexpected_files:
            logging.warning(f"  - {f}")
        if autofix:
            for f in unexpected_files:
                path = root / f
                try:
                    if path.is_dir():
                        os.rmdir(path)
                    else:
                        os.remove(path)
                    logging.info(f"Removed unexpected file/directory: {f}")
                except Exception as e:
                    logging.error(f"Failed to remove {f}: {e}")

    if not missing_files and not unexpected_files:
        logging.info("Root directory is valid ✅")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Validate or fix root layout before deploy.")
    parser.add_argument("--autofix", action="store_true", help="Automatically fix layout issues.")
    args = parser.parse_args()

    validate_root_files(autofix=args.autofix)
