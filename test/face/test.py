import requests
import base64
import json
from json.decoder import JSONDecodeError


def main():
    '''
    人脸识别测试
    '''
    source = {"http://127.0.0.1:8000/face/face_detect/": ["face1.jpeg"],
              "http://127.0.0.1:8000/face/face_match/": ["face1.jpeg", "face2.jpeg"],
              "http://127.0.0.1:8000/face/face_faceverify/": ["face1.jpeg", "face2.jpeg"],
              }
    for request_url, img_path in source.items():
        if len(img_path) == 1:
            # 仅上传一张图片
            with open(img_path[0], 'rb') as f:
                image = base64.b64encode(f.read())
            # 指定各种人脸特征
            # params = {"image": image, "face_field": "age,beauty,expression,faceshape,gender,glasses,landmark,race,quality,facetype,parsing"}
            params = {"image": image}
            response = requests.post(url=request_url, data=params)
            try:
                print(response.json())
            except JSONDecodeError:
                print(response.content)
        else:
            # 上传多张图片
            params = list()
            for each_path in img_path:
                temp = dict()
                with open(each_path, 'rb') as f:
                    image = base64.b64encode(f.read()).decode('utf-8')
                temp['image'] = image
                params.append(temp)
            '''
            这里
            params = [
                {
                    "image": "face1.jpeg的base64编码"
                    其他参数
                },
                {
                    "image": "face2.jpeg的base64编码"
                    其他参数
                }

            ]
            '''

            # 多图片重新以json格式封装在image里,便于服务器读取
            image = json.dumps(params)
            params = {'image': image}
            response = requests.post(url=request_url, data=params)
            try:
                print(response.json())
            except JSONDecodeError:
                print(response.content)


if __name__ == '__main__':
    main()
