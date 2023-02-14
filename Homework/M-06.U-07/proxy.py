import json
import requests


def sent_http_request(target, method, headers=None, payload=None):
    headers_dict = dict()

    if headers:
        for header in headers:
            header_name = header.split(":")[0]
            header_value = header.split(":")[1:]
            headers_dict[header_name] = ":".join(header_value)

    if method == "GET":
        response = requests.get(target, headers=headers_dict)
    elif method == "POST":
        response = requests.post(target, headers=headers_dict, data=payload)
    print(
        f"[#] Response status code: {response.status_code}\n"
        f"[#] Response headers: {json.dumps(dict(response.headers), indent=4, sort_keys=True)}\n"
        f"[#] Response content:\n {response.text}"
    )


target = str(input("Target:"))
method = str(input("Method (GET|POST):"))
headers = list(input("Headers (name1:value1 name2:value2 ...)").split())
if method == "POST":
    payload = str(input("Payload:"))

sent_http_request(target, method, headers, payload)
