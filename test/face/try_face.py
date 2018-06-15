import requests
import base64
import json

headers = {
    "Content-Type": "application/json",
}
access_token = "24.46a179f08cc86620cd7bf4b09e5e57ac.2592000.1528250089.282335-11200882"


def face_detect():
    '''
    人脸检测
    '''
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"

    with open('face1.jpeg', 'rb') as f:
        image = base64.b64encode(f.read())
    image_type = 'BASE64'

    face_field = 'faceshape,facetype'

    params = {'image': image, 'image_type': image_type, 'face_field': face_field}
    payload = {'access_token': access_token}

    response = requests.post(url=request_url, data=params, params=payload, headers=headers)
    print(response.json())


def face_match():
    '''
    人脸对比
    '''
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"

    with open('face1.jpeg', 'rb') as f:
        image1 = base64.b64encode(f.read()).decode("utf-8")
    image_type1 = "BASE64"

    with open('face2.jpeg', 'rb') as f:
        image2 = base64.b64encode(f.read()).decode("utf-8")
    image_type2 = "BASE64"
    params = json.dumps([{'image': image1, 'image_type': image_type1}, {'image': image2, 'image_type': image_type2}])
    payload = {'access_token': access_token}

    response = requests.post(url=request_url, data=params, params=payload, headers=headers)
    print(response.json())


def face_faceverify():
    '''
    在线活体检测
    '''
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceverify"

    with open('face1.jpeg', 'rb') as f:
        image1 = base64.b64encode(f.read()).decode("utf-8")
    image_type1 = "BASE64"

    with open('face2.jpeg', 'rb') as f:
        image2 = base64.b64encode(f.read()).decode("utf-8")
    image_type2 = "BASE64"
    params = json.dumps([{'image': image1, 'image_type': image_type1}, {'image': image2, 'image_type': image_type2}])
    payload = {'access_token': access_token}

    response = requests.post(url=request_url, data=params, params=payload, headers=headers)
    print(response.json())


if __name__ == '__main__':
    face_faceverify()
