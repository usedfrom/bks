from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        update = json.loads(post_data)

        print("Lava webhook:", update)

        if update.get("status") == "success":
            order_id = update.get("order_id")
            amount = update.get("amount")
            user_id = int(order_id.split("_")[1])
            print(f"Оплата успешна! User {user_id}, {amount} ₽")
            # Здесь вызови функцию активации подписки

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"status": "ok"}).encode())