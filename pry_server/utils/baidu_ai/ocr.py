import requests
from . import config


def general_basic(access_token,
                  image=None,
                  url=None,
                  language_type='CHN_ENG',
                  detect_direction=False,
                  detect_language='false',
                  probability='false'):
    '''
    通用文字识别
    '''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    request_url = config.general_basic_url
    access_token = access_token
    params = {"language_type": language_type,
              "detect_direction": detect_direction,
              "detect_language": detect_language,
              "probability": probability}
    if image is not None:
        params["image"] = image
    else:
        params["url"] = url
    payload = {"access_token": access_token}
    response = requests.post(url=request_url, data=params, headers=headers, params=payload)
    return response.json()


def accurate_basic(access_token, image=None, detect_direction=False, probability='false'):
    '''
    通用文字识别(高精度)
    '''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    request_url = config.accurate_basic_url
    access_token = access_token
    params = {"image": image,
              "detect_direction": detect_direction,
              "probability": probability}
    payload = {"access_token": access_token}
    response = requests.post(url=request_url, data=params, headers=headers, params=payload)
    return response.json()


def general(access_token,
            image=None,
            url=None,
            recognize_granularity='big',
            language_type='CHN_ENG',
            detect_direction=False,
            detect_language='false',
            vertexes_location='false',
            probability='false'):
    '''
    通用文字识别(含位置信息)
    '''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    request_url = config.general_url
    access_token = access_token
    params = {"detect_direction": detect_direction,
              "probability": probability,
              "recognize_granularity": recognize_granularity,
              "language_type": language_type,
              "detect_language": detect_language,
              "vertexes_location": vertexes_location}
    if image is not None:
        params["image"] = image
    else:
        params["url"] = url
    payload = {"access_token": access_token}
    response = requests.post(url=request_url, data=params, headers=headers, params=payload)
    return response.json()


def accurate(access_token,
             image=None,
             recognize_granularity='big',
             vertexes_location='false',
             detect_direction=False,
             probability='false'):
    '''
    通用文字识别(含位置高精度)
    '''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    request_url = config.accurate_url
    access_token = access_token
    params = {"image": image,
              "recognize_granularity": recognize_granularity,
              "vertexes_location": vertexes_location,
              "detect_direction": detect_direction,
              "probability": probability}
    payload = {"access_token": access_token}
    response = requests.post(url=request_url, data=params, headers=headers, params=payload)
    return response.json()


def general_enhanced(access_token,
                     image=None,
                     url=None,
                     language_type='CHN_ENG',
                     detect_direction=False,
                     detect_language='false',
                     probability='false'):
    '''
    通用文字识别(含生僻字)(不免费)
    '''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    request_url = config.general_enhanced_url
    access_token = access_token
    params = {"detect_direction": detect_direction,
              "probability": probability,
              "language_type": language_type,
              "detect_language": detect_language}
    if image is not None:
        params["image"] = image
    else:
        params["url"] = url
    payload = {"access_token": access_token}
    response = requests.post(url=request_url, data=params, headers=headers, params=payload)
    return response.json()
