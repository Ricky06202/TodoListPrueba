import os
import sys

# 1. Agregamos el directorio actual al Path de Python
sys.path.insert(0, os.path.dirname(__file__))

# 2. Importamos el adaptador y tu app
from a2wsgi import ASGIMiddleware
from main import app  # Donde 'main' es main.py y 'app' es FastAPI()

# 3. El objeto que busca Passenger
application = ASGIMiddleware(app)
