from http.server import BaseHTTPRequestHandler, HTTPServer

# --- DATA ---
itemlines = [
    "101 18V Cordless Drill 2 89.99",
    "102 6-inch Wood Clamp 4 12.50",
    "103 Carpenter's Hammer 1 19.99"
]

#
# -------------------------
# Legacy HTTPServer Handler
# -------------------------
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/itemlines":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            for t in itemlines:
                self.wfile.write(f"<custom>{t}</custom>\n".encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

#
def run_http_server(host="0.0.0.0", port=8443): 
    server_address = (host, port)
    httpd = HTTPServer(server_address, Handler)
    print(f"[A] Legacy server at http://{host}:{port}/itemlines")
    httpd.serve_forever()

if __name__ == "__main__":
    run_http_server(host="0.0.0.0", port=8003)
