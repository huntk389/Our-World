# main.py (in root)
# main.py at root — safe patch for folder named solyn-api

import sys
import os

# Add the solyn-api folder to PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), "solyn-api"))

# Now import the app from solyn-api/main.py
from main import app
