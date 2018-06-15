import requests
import base64


def general_basic():
    '''
    通用文字识别
    '''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    access_token = "24.46a179f08cc86620cd7bf4b09e5e57ac.2592000.1528250089.282335-11200882"
    with open('case1.jpeg', 'rb') as f:
        image = base64.b64encode(f.read())
    params = {"image": image, "probability": "true"}
    payload = {"access_token": access_token}
    response = requests.post(url=request_url, data=params, headers=headers, params=payload)
    print(response.json())


def accurate_basic():
    '''
    通用文字识别(高精度)
    '''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    access_token = "24.46a179f08cc86620cd7bf4b09e5e57ac.2592000.1528250089.282335-11200882"
    with open('case1.jpeg', 'rb') as f:
        image = base64.b64encode(f.read())
    params = {"image": image}
    payload = {"access_token": access_token}
    response = requests.post(url=request_url, data=params, headers=headers, params=payload)
    print(response.json())


def general():
    '''
    通用文字识别(含位置信息)
    '''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general"
    access_token = "24.46a179f08cc86620cd7bf4b09e5e57ac.2592000.1528250089.282335-11200882"
    with open('case1.jpeg', 'rb') as f:
        image = base64.b64encode(f.read())
    params = {"image": image}
    payload = {"access_token": access_token}
    response = requests.post(url=request_url, data=params, headers=headers, params=payload)
    print(response.json())


if __name__ == '__main__':
    general()
