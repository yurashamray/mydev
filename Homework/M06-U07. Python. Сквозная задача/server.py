from flask import Flask, request, jsonify
import requests
import os


app = Flask(__name__)

# this is ping_sweep method which will send ping call
def ping_sweep(network, count):

    active_hosts = []
    ip_parts = network.split(".")
    network_ip = ip_parts[0] + "." + ip_parts[1] + "." + ip_parts[2] + "."
    for i in range(1, count + 1):
        scanned_ip = network_ip + str(int(ip_parts[3]) + i)
        response = os.popen(f"ping -n 1 {scanned_ip}")
        res = response.readlines()
        print(f"[#] Result of scanning: {scanned_ip} [#]\n{res[2]}", end="\n\n")
    return active_hosts

# this is end point of our post request /sendhttp
@app.route("/sendhttp", methods=["POST"])
def send_http_request():
    request_data = request.get_json() #here it is getting data from our api call
    headers = request.headers   #getting header from our api call
    
    method = request_data["method"] #provide method in your api call from script.py
    target = request_data["target"] #you need to provide targer in your api call from script.py
    payload = request_data.get("payload", None)
    #this sending request to our targer
    response = requests.request(method, target, headers=headers, data=payload)
    return response.content, response.status_code

# this is get method for scan
@app.route("/scan", methods=["GET"])
def scan_network():
    target = request.args.get("target")
    count = int(request.args.get("count"))
    active_hosts = ping_sweep(target, count)
    return jsonify(active_hosts)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3012)
