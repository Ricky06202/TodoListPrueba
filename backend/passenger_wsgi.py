import os
import sys
from a2wsgi import ASGIMiddleware

# Esto le dice a cPanel dónde está tu código
sys.path.insert(0, os.path.dirname(__file__))

# Importamos tu app de FastAPI (asumiendo que tu archivo es main.py)
from main import app

# Envolvemos la app para que sea compatible con Passenger (WSGI)
application = ASGIMiddleware(app)
