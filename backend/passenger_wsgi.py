def application(environ, start_response):
    status = '200 OK'
    text = '¡Hola Mundo! El Python 3.9 en cPanel esta VIVO.'
    output = text.encode('utf-8')
    response_headers = [('Content-Type', 'text/plain; charset=utf-8'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]
