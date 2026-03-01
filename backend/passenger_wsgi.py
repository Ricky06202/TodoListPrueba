import os
import sys

# Esto le dice a cPanel dónde está tu código
sys.path.insert(0, os.path.dirname(__file__))

# Importamos tu app de FastAPI (asumiendo que tu archivo es main.py)
from main import app as application