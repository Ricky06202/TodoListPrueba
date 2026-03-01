import os
import sys

# Configurar el entorno
sys.path.insert(0, os.path.dirname(__file__))

def write_error(msg):
    with open(os.path.join(os.path.dirname(__file__), 'error_log.txt'), 'a') as f:
        import datetime
        f.write(f"[{datetime.datetime.now()}] {msg}\n")

try:
    from a2wsgi import ASGIMiddleware
    from main import app
    
    # Envolvemos la app para que sea compatible con Passenger (WSGI)
    application = ASGIMiddleware(app)
    
except Exception as e:
    import traceback
    error_msg = traceback.format_exc()
    write_error(error_msg)
    
    # Proveer una aplicación WSGI mínima que muestre el error si Passenger lo permite
    def application(environ, start_response):
        start_response('500 Internal Server Error', [('Content-Type', 'text/plain')])
        return [f"Error de arranque en el Backend:\n\n{error_msg}".encode('utf-8')]
