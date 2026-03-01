import os
import sys

# 1. PATH: Aseguramos que Python encuentre main.py
sys.path.insert(0, os.path.dirname(__file__))

# 2. LOGGING: Para ver qué falla exactamente
def write_error(msg):
    log_path = os.path.join(os.path.dirname(__file__), 'error_log.txt')
    with open(log_path, 'a') as f:
        import datetime
        f.write(f"[{datetime.datetime.now()}] {msg}\n")

# 3. ARRANQUE: Intentar cargar FastAPI envuelto en WSGI
try:
    from a2wsgi import ASGIMiddleware
    from main import app
    
    # Objeto que busca Passenger
    application = ASGIMiddleware(app)
    
except Exception:
    import traceback
    error_msg = traceback.format_exc()
    write_error(error_msg)
    
    def application(environ, start_response):
        start_response('500 Internal Error', [('Content-Type', 'text/plain')])
        return [f"ERROR DE PYTHON EN EL SERVER:\n\n{error_msg}".encode('utf-8')]
