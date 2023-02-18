"""
Курс: MIFIIB
Модуль.6.Python
Сквозная задача: (клиент)
Выполнил: Юрий Шамрай (yura.shamray@gmail.com)
"""

# Импортируем модули
import argparse
import requests
import json

# Настраиваем парсинг из терминала
parser = argparse.ArgumentParser(description="Network scanner")
parser.add_argument(
    "task", choices=["scan", "sendhttp"], help="Network scan or send HTTP request"
)
parser.add_argument("-i", "--ip", type=str, help="IP address")
parser.add_argument("-n", "--num_of_hosts", type=int, help="Number of hosts")


# Функция метода отправки http запроса
def sent_http_request(target, method, headers=None, payload=None, task="scan"):
    headers_dict = dict()
    payload_dict = dict()

    if headers is not None and method.lower() == "post":
        for header in headers:
            header_name = header.split(":", 1)[0]
            header_value = header.split(":", 1)[1]
            headers_dict[header_name] = header_value
    if payload is not None and method.lower() == "post":
        for pyl in payload:
            payload_name = pyl.split(":", 1)[0]
            payload_value = pyl.split(":", 1)[1]
            payload_dict[payload_name] = payload_value

    if method == "GET":
        target = target + "/" + task
        response = requests.get(
            target,
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload),
        )
    elif method == "POST":
        target = target + "/" + task
        print(type(headers_dict))
        response = requests.post(
            target, headers=headers_dict, data=json.dumps(payload_dict)
        )
    print(
        f"[#] Response status code: {response.status_code}\n"
        f"[#] Response headers: {json.dumps(dict(response.headers), indent=4, sort_keys=True)}\n"
        f"[#] Response content:\n {response.text}"
    )


args = vars(parser.parse_args())
task = args["task"]
ip = args["ip"]
num_of_hosts = args["num_of_hosts"]

# Запрашиваем адрес сервера где запущен REST API
target = str(input("Target (e.g. http://127.0.0.1:3000): "))
method = str(input("Method (GET|POST): "))  # Тип HTTP запроса

# Запрашиваем данные для HTTP запроса POST
if method == "POST":
    headers = list(input("Headers (name1:value1 name2:value2 ...) ").split())
    payload = list(input("Payload: (name1:value1 name2:value2 ...) ").split())
else:
    payload = {"target": ip, "count": num_of_hosts}

    headers = None

if payload == "":
    payload = None
sent_http_request(target, method, headers, payload, task)
