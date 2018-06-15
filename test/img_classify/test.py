import requests
import base64
from json.decoder import JSONDecodeError


def main():
    '''
    图像识别测试
    '''
    source = {"http://127.0.0.1:8000/img-classify/car/": "car2.jpg",
              #"http://127.0.0.1:8000/img-classify/object_detect/": "face.jpeg",
              #"http://127.0.0.1:8000/img-classify/dish/": "dish.jpeg",
              #"http://127.0.0.1:8000/img-classify/logo/": "logo.jpg",
              #"http://127.0.0.1:8000/img-classify/animal/": "animal.jpeg",
              #"http://127.0.0.1:8000/img-classify/plant/": "plant.jpg",
              #"http://127.0.0.1:8000/img-classify/advanced_general/": "view.jpg"
              }
    for request_url, img_path in source.items():
        f = open(img_path, 'rb')
        img = base64.b64encode(f.read())
        params = {"img": str(img,'utf-8')}
        response = requests.post(url=request_url, data=params)
        try:
            print(response.json())
        except JSONDecodeError:
            print(response.content)


if __name__ == '__main__':
    main()
