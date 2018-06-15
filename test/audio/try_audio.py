import base64
import requests
import os
import json

headers = {
    "Content-Type": "application/json",
}

requests_url = "https://vop.baidu.com/server_api"

format = "wav"
rate = 16000
dev_pid = 1536
channel = 1
token = "24.46a179f08cc86620cd7bf4b09e5e57ac.2592000.1528250089.282335-11200882"
cuid = "00:0c:29:53:5f:2f"
len = os.path.getsize('16k.wav')
f = open('16k.wav', 'rb')
speech = base64.b64encode(f.read()).decode("utf-8")

payloads = {"format": format,
            "rate": rate,
            "dev_pid": dev_pid,
            "channel": channel,
            "token": token,
            "cuid": cuid,
            "len": len,
            "speech": speech, }
response = requests.post(url=requests_url, data=json.dumps(payloads), headers=headers)
print(response.json())
