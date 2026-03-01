import os
import sys

# 1. Configurar la ruta para que encuentre main.py y las librerías
INTERP = os.path.expanduser("~/api-todolistblazor.rsanjur.com/venv/bin/python")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0, os.path.dirname(__file__))

# 2. Sistema de logging para cazar errores (si los hay)
def write_error(msg):
    with open(os.path.join(os.path.dirname(__file__), 'error_log.txt'), 'a') as f:
        import datetime
        f.write(f"[{datetime.datetime.now()}] {msg}\n")

try:
    from a2wsgi import ASGIMiddleware
    from main import app
    
    # 3. Punto de entrada para Passenger (WSGI)
    application = ASGIMiddleware(app)
    
except Exception:
    import traceback
    error_msg = traceback.format_exc()
    write_error(error_msg)
    
    def application(environ, start_response):
        start_response('500 Internal Error', [('Content-Type', 'text/plain')])
        return [f"Error detectado:\n\n{error_msg}".encode('utf-8')]
