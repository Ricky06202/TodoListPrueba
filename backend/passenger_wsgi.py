import os
import sys
import traceback

# 1. PATH: Aseguramos que Python encuentre main.py
sys.path.insert(0, os.path.dirname(__file__))

def application(environ, start_response):
    try:
        # Intentamos cargar las librerías
        from a2wsgi import ASGIMiddleware
        from main import app
        
        # Si llegamos aquí, creamos el adaptador
        _app = ASGIMiddleware(app)
        return _app(environ, start_response)
        
    except Exception as e:
        # SI ALGO FALLA, LO MOSTRAMOS EN PANTALLA (HTML)
        error_info = traceback.format_exc()
        status = '500 Internal Server Error'
        response_headers = [('Content-Type', 'text/html; charset=utf-8')]
        start_response(status, response_headers)
        
        html = f"""
        <html>
        <head><title>Error de Backend</title></head>
        <body style="font-family: sans-serif; padding: 20px; background: #fff0f0;">
            <h1 style="color: #c00;">❌ Error detectado en el servidor</h1>
            <p>El backend no pudo arrancar. Aquí tienes el detalle técnico:</p>
            <pre style="background: #eee; padding: 15px; border-radius: 5px; border: 1px solid #ccc; overflow: auto;">
{error_info}
            </pre>
            <p><b>Sugerencia:</b> Revisa si 'fastapi' y 'a2wsgi' están instalados en 'Setup Python App'.</p>
        </body>
        </html>
        """
        return [html.encode('utf-8')]
