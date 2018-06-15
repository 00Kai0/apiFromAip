# encoding:utf-8
import base64
import requests


def object_detect(access_token, img=None, img_path=None, with_face=1):
    '''
    图像主体检测
    '''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/object_detect"

    # 二进制方式打开图片文件
    if img_path:
        f = open(img_path, 'rb')
        img = base64.b64encode(f.read())

    params = {"image": img, "with_face": with_face}

    payload = {'access_token': access_token}
    response = requests.post(url=request_url, data=params, headers=headers, params=payload)
    content = response.json()
    return content


def car(access_token, img=None, img_path=None, top_num=5):
    '''
    车型识别
    '''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/car"

    # 二进制方式打开图片文件
    if img_path:
        f = open(img_path, 'rb')
        img = base64.b64encode(f.read())

    params = {"image": img, "top_num": top_num}

    payload = {'access_token': access_token}
    response = requests.post(url=request_url, data=params, headers=headers, params=payload)
    content = response.json()
    return content


def dish(access_token, img=None, img_path=None, top_num=5, filter_threshold=0.95):
    '''
    菜品识别
    '''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/dish"

    # 二进制方式打开图片文件
    if img_path:
        f = open(img_path, 'rb')
        img = base64.b64encode(f.read())

    params = {"image": img, "top_num": top_num, "filter_threshold": filter_threshold}

    payload = {'access_token': access_token}
    response = requests.post(url=request_url, data=params, headers=headers, params=payload)
    content = response.json()
    return content


def logo(access_token, img=None, img_path=None, custom_lib=False):
    '''
    logo商标识别
    '''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/logo"

    # 二进制方式打开图片文件
    if img_path:
        f = open(img_path, 'rb')
        img = base64.b64encode(f.read())

    params = {"custom_lib": custom_lib, "image": img}

    payload = {'access_token': access_token}
    response = requests.post(url=request_url, data=params, headers=headers, params=payload)
    content = response.json()
    return content


def animal(access_token, img=None, img_path=None, top_num=6):
    '''
    动物识别
    '''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal"

    # 二进制方式打开图片文件
    if img_path:
        f = open(img_path, 'rb')
        img = base64.b64encode(f.read())

    params = {"image": img, "top_num": top_num}

    payload = {'access_token': access_token}
    response = requests.post(url=request_url, data=params, headers=headers, params=payload)
    content = response.json()
    return content


def plant(access_token, img=None, img_path=None):
    '''
    植物识别
    '''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/plant"

    # 二进制方式打开图片文件
    if img_path:
        f = open(img_path, 'rb')
        img = base64.b64encode(f.read())

    params = {"image": img}

    payload = {'access_token': access_token}
    response = requests.post(url=request_url, data=params, headers=headers, params=payload)
    content = response.json()
    return content


def advanced_general(access_token, img=None, img_path=None):
    '''
    通用物体和场景识别
    '''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"

    # 二进制方式打开图片文件
    if img_path:
        f = open(img_path, 'rb')
        img = base64.b64encode(f.read())

    params = {"image": img}

    payload = {'access_token': access_token}
    response = requests.post(url=request_url, data=params, headers=headers, params=payload)
    content = response.json()
    return content


def customized_image(request_url, access_token, img=None, img_path=None, top_num=5):
    '''
    定制图像分类
    '''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    # 二进制方式打开图片文件
    if img_path:
        f = open(img_path, 'rb')
        img = base64.b64encode(f.read())

    params = {"image": img, "top_num": top_num}

    payload = {'access_token': access_token}
    response = requests.post(url=request_url, data=params, headers=headers, params=payload)
    content = response.json()
    return content


def customized_object(request_url, access_token, img=None, img_path=None):
    '''
    定制图像分类
    '''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    # 二进制方式打开图片文件
    if img_path:
        f = open(img_path, 'rb')
        img = base64.b64encode(f.read())

    params = {"image": img}

    payload = {'access_token': access_token}
    response = requests.post(url=request_url, data=params, headers=headers, params=payload)
    content = response.json()
    return content


def get_access_token(client_id, client_secret):
    '''
    获取access_token
    '''
    request_url = "https://aip.baidubce.com/oauth/2.0/token"

    payload = {"grant_type": "client_credentials", "client_id": client_id, "client_secret": client_secret}

    response = requests.post(url=request_url, params=payload)
    content = response.json()
    return content['access_token']


'''
if __name__ == '__main__':
    access_token = get_access_token()
    # content = object_detect(img_path='test.jpg',access_token=access_token)
    content = car(img_path='test.jpg', access_token=access_token)
    # content = dish(img_path='dish.jpeg', access_token=access_token)
    # content = plant(img_path='dish.jpeg', access_token=access_token)
    if content:
        print(content)
'''
