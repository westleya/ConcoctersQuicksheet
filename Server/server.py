# python -m http.server 8000 --directory ./my_dir

from http.server import HTTPServer as BaseHTTPServer, SimpleHTTPRequestHandler
import os
import json



class HTTPHandler(SimpleHTTPRequestHandler):
    """This handler uses server.base_path instead of always using os.getcwd()"""

    def translate_path(self, path):
        path = SimpleHTTPRequestHandler.translate_path(self, path)
        relpath = os.path.relpath(path, os.getcwd())
        fullpath = os.path.join(self.server.base_path, relpath)
        return fullpath
    def do_GET(self):
        if self.path == '/':
            self.path = '/display.html'
        return SimpleHTTPRequestHandler.do_GET(self)
    def do_POST(self):
        length = int(self.headers['Content-length'])
        print("here")
        print(self.path)
        print(self.rfile.read(length))
        self.send_response(200, "OK")
        self.end_headers()
        self.wfile.write("serverdata")


class HTTPServer(BaseHTTPServer):
    """The main server, you pass in base_path which is the path you want to serve requests from"""

    def __init__(self, base_path, server_address, RequestHandlerClass=HTTPHandler):
        self.base_path = base_path
        BaseHTTPServer.__init__(self, server_address, RequestHandlerClass)


web_dir = os.path.join(os.path.dirname(__file__))
print(__file__)
httpd = HTTPServer(web_dir, ("", 8000))
httpd.serve_forever()

# accept json object and confirm it got it