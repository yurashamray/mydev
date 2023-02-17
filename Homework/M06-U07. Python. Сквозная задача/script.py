import os
import json
import argparse
import requests


parser = argparse.ArgumentParser(description="Network scanner")
parser.add_argument(
    "task", choices=["scan", "sendhttp"], help="Network scan or send HTTP request"
)
parser.add_argument("-i", "--ip", type=str, help="IP address")
parser.add_argument("-n", "--num_of_hosts", type=int, help="Number of hosts")

args = parser.parse_args()

# method to send http request
def sent_http_request(target, method, headers=None, payload=None):
    headers_dict = dict()

    if headers:
        for header in headers:
            header_name = header.split(":")[0]
            header_value = header.split(":")[1:]
            headers_dict[header_name] = ":".join(header_value)

    if method == "GET":
        target = target + "/scan"
        response = requests.get(target, headers=headers_dict)
    elif method == "POST":
        target = target + "/sendhttp"
        response = requests.post(target, headers=headers_dict, data=payload)
    print(
        f"[#] Response status code: {response.status_code}\n"
        f"[#] Response headers: {json.dumps(dict(response.headers), indent=4, sort_keys=True)}\n"
        f"[#] Response content:\n {response.text}"
    )


# target will your url you will get from server.py
target = str(input("Target:"))  # enter server ip and port like http://127.0.0.1:3010
method = str(input("Method (GET|POST):"))  # type of request
headers = list(input("Headers (name1:value1 name2:value2 ...)").split())
if method == "POST":
    payload = str(input("Payload: "))

sent_http_request(target, method, headers, payload)
