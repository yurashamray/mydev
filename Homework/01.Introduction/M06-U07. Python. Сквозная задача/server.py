"""
Курс: MIFIIB
Модуль.6.Python
Сквозная задача: (сервер)
Выполнил: Юрий Шамрай (yura.shamray@gmail.com)
"""

# Импортируем модули
from flask import Flask, request, jsonify
import requests
import click
import os
import sys

# Используем фреймворк Flask
app = Flask(__name__)
cli = sys.modules['flask.cli']

# Баннер-приветствие Flask App сервера
cli.show_server_banner = lambda *x: click.echo("Hello, Flask App Server is Online")


# Функция для использования техники ping_sweep - отправки эхо-запросов диапазону IP адресов
def ping_sweep(network, count):
    active_hosts = {}
    ip_parts = network.split(".")
    network_ip = ip_parts[0] + "." + ip_parts[1] + "." + ip_parts[2] + "."
    for i in range(0, count + 1):
        scanned_ip = network_ip + str(int(ip_parts[3]) + i)
        response = os.popen(f"ping -n 1 {scanned_ip}")  # Для Linux параметры команды ping: ping -c 5
        res = response.readlines()
        active_hosts[scanned_ip] = res[2]
        print(f"[#] Result of scanning: {scanned_ip} [#]\n{res[2]}", end="\n")
    return active_hosts


# Декоратор для функции send_http_request
@app.route("/sendhttp", methods=["POST"])
def send_http_request():
    request_data = request.get_json()  # Получаем данные от нашего API
    headers = request.headers  # Получение заголовков от нашего API
    method = request_data["method"]  # Метод в нашем API из script.py
    target = request_data["target"]  # Таргет в нашем API из script.py
    payload = request_data.get("payload", None)
    # Отправка запроса нашему таргету
    response = requests.request(method, target, headers=headers, data=payload)
    return response.content, response.status_code


# Декоратор для функции scan
@app.route("/scan", methods=["GET"])
def scan_network():
    request_data = request.get_json()
    target = request_data["target"]
    count = int(request_data["count"])
    active_hosts = ping_sweep(target, count)
    return jsonify(active_hosts)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000) # Адрес и порт нашего Flask App сервера
