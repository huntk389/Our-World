import sys
import os

# Ensure solyn-api is on the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "solyn-api"))

# Import the FastAPI app from the real backend
from main import app
