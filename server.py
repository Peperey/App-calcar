import http.server, socketserver
PORT = 8080
class H(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
print(f'Servidor listo en http://localhost:{PORT}')
socketserver.TCPServer(('', PORT), H).serve_forever()
