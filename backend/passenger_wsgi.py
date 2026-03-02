import os
import sys

# 1. Agregamos el directorio actual al Path de Python
sys.path.insert(0, os.path.dirname(__file__))

# 2. Importamos el adaptador y tu app
# Renombramos 'app' a 'fastapi_app' para evitar que Passenger lo encuentre por error
from a2wsgi import ASGIMiddleware
from main import app as fastapi_app

# 3. El objeto que busca Passenger (WSGI)
# Al no existir una variable llamada 'app', Passenger se ve obligado a usar 'application'
application = ASGIMiddleware(fastapi_app)
