import requests

request_url = "https://tsn.baidu.com/text2audio"

tok = "24.46a179f08cc86620cd7bf4b09e5e57ac.2592000.1528250089.282335-11200882"

tex = "寥落古行宫 宫花寂寞红 白头宫女在 闲坐说玄宗 ".encode("utf-8")

cuid = "00:0c:29:53:5f:2f"

ctp = 1

lan = 'zh'

payloads = {'tex': tex, 'tok': tok, 'cuid': cuid, 'ctp': ctp, 'lan': lan}

response = requests.get(url=request_url, params=payloads)

if response.headers['Content-Type'] == 'audio/mp3':
    print('audio/mp3')
    content_size = int(response.headers['content-length'])
    print("content_size:" + str(content_size))
    with open('test.mp3', 'wb') as f:
        f.write(response.content)
        f.flush()
else:
    print('failed')
