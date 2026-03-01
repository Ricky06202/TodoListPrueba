import os
import sys

# 1. Aseguramos que la carpeta actual esté en el PATH
sys.path.insert(0, os.path.dirname(__file__))

# 2. Sistema de logging básico
def write_error(msg):
    log_path = os.path.join(os.path.dirname(__file__), 'error_log.txt')
    with open(log_path, 'a') as f:
        import datetime
        f.write(f"[{datetime.datetime.now()}] {msg}\n")

# 3. Importación y arranque
try:
    from a2wsgi import ASGIMiddleware
    from main import app
    
    # Este es el objeto que busca Passenger
    application = ASGIMiddleware(app)
    
except Exception:
    import traceback
    error_msg = traceback.format_exc()
    write_error(error_msg)
    
    def application(environ, start_response):
        start_response('500 Error', [('Content-Type', 'text/plain')])
        return [f"ERROR DE ARRANQUE:\n\n{error_msg}".encode('utf-8')]
