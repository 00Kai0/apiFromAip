import requests
import json
from . import config

headers = {
    "Content-Type": "application/json",
}


def face_detect(access_token,
                image=None,
                image_type="BASE64",
                face_field="faceshape,facetype",
                max_face_num=1,
                face_type="LIVE"):
    '''
    人脸检测
    '''
    # 检测接收的图片,和参数错误
    if image is None:
        return {"error_msg": "images invalid", "error_code": "666666"}
    request_url = config.face_detect_url
    params = {'image': image,
              'image_type': image_type,
              'face_field': face_field,
              'max_face_num': max_face_num,
              'face_type': face_type}
    payload = {'access_token': access_token}

    response = requests.post(url=request_url, data=params, params=payload, headers=headers)
    return response.json()


def face_match(access_token,
               images=None,
               image_types=["BASE64", "BASE64"],
               face_types=["LIVE", "LIVE"],
               quality_controls=["NONE", "NONE"],
               liveness_controls=["NONE", "NONE"]):
    '''
    人脸对比
    '''

    # 检测接收的图片是否符合规范
    if images is None or len(images) != 2:
        return {"error_msg": "images invalid", "error_code": "666666"}
    request_url = config.face_match_url
    params = list()

    try:
        for i in range(2):
            temp = dict()
            temp['image'] = images[i]
            temp['image_type'] = image_types[i]
            temp['face_type'] = face_types[i]
            temp['quality_control'] = quality_controls[i]
            temp['liveness_control'] = liveness_controls[i]
            params.append(temp)
    except Exception:
        return {"error_msg": "params invalid", "error_code": "666665"}
    payload = {'access_token': access_token}

    response = requests.post(url=request_url, data=json.dumps(params), params=payload, headers=headers)
    return response.json()


def face_faceverify(access_token,
                    images=None,
                    image_types=None,
                    face_fields=None):
    '''
    在线活体检测
    '''

    # 检测接收的图片,和参数错误
    if images is None:
        return {"error_msg": "images invalid", "error_code": "666666"}

    num = len(images)
    if image_types is not None and len(image_types) != num:
        return {"error_msg": "image_type invalid", "error_code": "666667"}
    elif image_types is None:
        image_types = ["BASE64" * num]

    if face_fields is not None and len(image_types) != num:
        return {"error_meg": "face_fields invalid", "error_code": "666668"}
    elif face_fields is None:
        face_field = "faceshape,age,beauty"
        face_fields = [face_field * num]

    request_url = config.face_faceverify_url
    params = list()
    for i in range(num):
        temp = dict()
        temp['image'] = images[i]
        temp['image_type'] = image_types[i]
        temp['face_field'] = face_fields[i]
        params.append(temp)
    payload = {'access_token': access_token}

    response = requests.post(url=request_url, data=json.dumps(params), params=payload, headers=headers)
    return response.json()
