from http.server import BaseHTTPRequestHandler
import json

YOUR_WEBHOOK_KEY = "aQgmkn70sDSrBtIlaa0jTfPjpkmQ61rNlbSdUraX50pKVHZV4NzpfE58pYX5Tbo5"  # ← ключ из поля Lava

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Webhook endpoint. Use POST from Lava.")

    def do_POST(self):
        print("POST request received!")  # ← отладка
        received_key = self.headers.get('X-Api-Key')
        print(f"Received X-Api-Key: {received_key}")
        
        if received_key != YOUR_WEBHOOK_KEY:
            print("Invalid key")
            self.send_response(403)
            self.end_headers()
            return

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        update = json.loads(post_data)
        print("Lava payload:", update)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"status": "ok"}).encode())
