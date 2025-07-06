# main.py (root-level)
import sys
import os

# Ensure we're importing from solyn-api, not self
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "solyn-api")))

from main import app  # this is solyn-api/main.py's `app`, not root
