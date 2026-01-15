from http.server import BaseHTTPRequestHandler
import json

YOUR_SECRET_KEY = "my_super_secret_key_2026_bks_vpn_!@#$%^&*"  # ← вставь сюда ТОТ САМЫЙ ключ, который ты указал в Lava

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Проверяем ключ из заголовка
        received_key = self.headers.get('X-Api-Key')
        if received_key != YOUR_SECRET_KEY:
            print(f"Неверный ключ: {received_key}")
            self.send_response(403)
            self.end_headers()
            return

        # Читаем тело запроса
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        update = json.loads(post_data)

        print("Lava webhook получен:", update)

        if update.get("status") == "success":
            order_id = update.get("order_id")  # например "pay_123456"
            amount = update.get("amount")
            user_id = int(order_id.split("_")[1])

            print(f"Оплата успешна! User {user_id}, сумма {amount} ₽")
            # Здесь можно добавить логику активации подписки
            # Например: вызвать функцию из бота (но пока просто лог)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"status": "ok"}).encode())
