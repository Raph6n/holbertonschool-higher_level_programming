#!/usr/bin/python3
import http.server
import json

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    A simple HTTP request handler that serves basic responses and JSON data.
    """

    def do_GET(self):
        """
        Handle GET requests.
        Responds with different data based on the requested path.
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"404 Not Found")

if __name__ == '__main__':
    """
    Start the HTTP server on port 8000.
    """
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('Serving HTTP on port 8000...')
    httpd.serve_forever()
