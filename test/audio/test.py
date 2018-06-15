import requests


def main():
    '''
    语音识别测试
    '''
    tex = "寥落古行宫 宫花寂寞红 白头宫女在 闲坐说玄宗 ".encode("utf-8")
    cuid = "00:0c:29:53:5f:2f"
    payloads = {'tex': tex, 'cuid': cuid}
    request_url = "http://localhost:8000/text2audio/"

    response = requests.post(url=request_url, data=payloads)
    if response.headers['Content-Type'] == 'audio/mp3':
        with open("123.mp3", 'wb') as f:
            f.write(response.content)
            f.flush()
        print('download:' + '123.mp3')
    else:
        print(response.json())


if __name__ == '__main__':
    main()
