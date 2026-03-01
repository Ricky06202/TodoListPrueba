def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b"Hello World! El servidor WSGI funciona correctamente."]
