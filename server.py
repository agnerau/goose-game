import http.server
import socketserver
import os
import gzip

PORT = 8080


class GzipHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith(".gz"):
            self.send_response(200)
            self.send_header("Content-Encoding", "gzip")
            self.end_headers()

            with open(os.getcwd() + self.path, "rb") as f:
                self.wfile.write(f.read())
        else:
            return http.server.SimpleHTTPRequestHandler.do_GET(self)


with socketserver.TCPServer(("", PORT), GzipHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
