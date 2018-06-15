import requests
import base64
from json.decoder import JSONDecodeError


def main():
    '''
    通用文字识别测试
    '''
    source = {"http://127.0.0.1:8000/ocr/general_basic/": "case1.jpeg",
              "http://127.0.0.1:8000/ocr/accurate_basic/": "case1.jpeg",
              "http://127.0.0.1:8000/ocr/general/": "case1.jpeg",
              "http://127.0.0.1:8000/ocr/accurate/": "case1.jpeg",
              "http://127.0.0.1:8000/ocr/general_enhanced/": "case1.jpeg",
              }
    for request_url, img_path in source.items():
        f = open(img_path, 'rb')
        image = base64.b64encode(f.read())
        params = {"image": image}
        response = requests.post(url=request_url, data=params)
        try:
            if response.json().get("result"):
                print(response.json()["result"])
            else:
                print(response.json())
        except JSONDecodeError:
            print(response.content)


if __name__ == '__main__':
    main()
