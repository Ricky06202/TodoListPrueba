import sys, os
import traceback

# 1. Asegurar que el directorio del backend esté en el PATH
sys.path.insert(0, os.path.dirname(__file__))

def application(environ, start_response):
    try:
        # Intentamos importar y ejecutar el bridge de FastAPI
        from a2wsgi import ASGIMiddleware
        from main import app as fastapi_app
        
        # Creamos el puente
        app_bridge = ASGIMiddleware(fastapi_app)
        
        # Ejecutamos la app
        return app_bridge(environ, start_response)
        
    except Exception:
        # SI ALGO FALLA, capturamos el error y lo mostramos en el navegador
        # Esto evitará el "Request Timeout" genérico y nos dará el error real
        error_info = traceback.format_exc()
        start_response('500 Internal Server Error', [('Content-Type', 'text/plain; charset=utf-8')])
        return [error_info.encode('utf-8')]
