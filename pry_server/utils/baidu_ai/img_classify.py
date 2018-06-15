import requests
from . import config

'''
百度图像识别相关api
参数设置参考百度文档
返回值均为百度ai返回的原始json数据
'''


def object_detect(access_token, img=None, with_face=1):
    '''
    图像主体检测
    '''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    request_url = config.object_detect_url

    params = {"image": img, "with_face": with_face}

    payload = {'access_token': access_token}
    response = requests.post(url=request_url, data=params, headers=headers, params=payload)
    content = response.json()
    return content


def car(access_token, img=None, top_num=5):
    '''
    车型识别
    '''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    request_url = config.car_url

    params = {"image": img, "top_num": top_num}

    payload = {'access_token': access_token}
    response = requests.post(url=request_url, data=params, headers=headers, params=payload)
    content = response.json()
    return content


def dish(access_token, img=None, top_num=5, filter_threshold=0.95):
    '''
    菜品识别
    '''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    request_url = config.dish_url

    params = {"image": img, "top_num": top_num, "filter_threshold": filter_threshold}

    payload = {'access_token': access_token}
    response = requests.post(url=request_url, data=params, headers=headers, params=payload)
    content = response.json()
    return content


def logo(access_token, img=None, custom_lib=False):
    '''
    logo商标识别
    '''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    request_url = config.logo_url

    params = {"custom_lib": custom_lib, "image": img}

    payload = {'access_token': access_token}
    response = requests.post(url=request_url, data=params, headers=headers, params=payload)
    content = response.json()
    return content


def animal(access_token, img=None, top_num=6):
    '''
    动物识别
    '''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    request_url = config.animal_url

    params = {"image": img, "top_num": top_num}

    payload = {'access_token': access_token}
    response = requests.post(url=request_url, data=params, headers=headers, params=payload)
    content = response.json()
    return content


def plant(access_token, img=None):
    '''
    植物识别
    '''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    request_url = config.plant_url

    params = {"image": img}

    payload = {'access_token': access_token}
    response = requests.post(url=request_url, data=params, headers=headers, params=payload)
    content = response.json()
    return content


def advanced_general(access_token, img=None):
    '''
    通用物体和场景识别
    '''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    request_url = config.advanced_general_url

    params = {"image": img}

    payload = {'access_token': access_token}
    response = requests.post(url=request_url, data=params, headers=headers, params=payload)
    content = response.json()
    return content


def customized_image(request_url, access_token, img=None, top_num=5):
    '''
    定制图像分类
    '''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    params = {"image": img, "top_num": top_num}

    payload = {'access_token': access_token}
    response = requests.post(url=request_url, data=params, headers=headers, params=payload)
    content = response.json()
    return content


def customized_object(request_url, access_token, img=None):
    '''
    定制图像分类
    '''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    params = {"image": img}

    payload = {'access_token': access_token}
    response = requests.post(url=request_url, data=params, headers=headers, params=payload)
    content = response.json()
    return content
