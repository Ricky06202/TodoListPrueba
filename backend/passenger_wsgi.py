import os
import sys

# Aseguramos que Python encuentre main.py
sys.path.insert(0, os.path.dirname(__file__))

# Importaciones a nivel de módulo (Passenger las carga UNA vez al arrancar)
from a2wsgi import ASGIMiddleware
from main import app

# Objeto que busca Passenger - se crea una sola vez
application = ASGIMiddleware(app)
