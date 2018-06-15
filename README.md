# 代理服务器开发

#### 项目介绍
百度ai应用代理服务器,在代理服务器更新access_token

#### 目录结构
pry_server/-------------(django项目源码)<br>
&nbsp;&nbsp;pry_server/---------- (djangoproject目录，存放配置文件)<br>
&nbsp;&nbsp;proxy_baidu/-------- (代理服务app目录,代理服务的源码)<br>
&nbsp;&nbsp;utils/-------------------       (存放百度ai_api)<br>
test/----------------------(测试脚本) <br>

#### 环境
<ul>
    <li>python3.5</li>
    <li>django1.8.2</li>
    <li>requesets</li>
</ul>

#### 安装教程

1. xxxx
2. xxxx
3. xxxx

#### 使用说明
1. 使用前

第一次运行参考django官方文档<br>
在proxy_baidu目录下的config.py中加入client_id=(API Key),client_secret=(Secret Key)
可部署到服务器 或者 运行./short_cat_runserver.sh启动内置测试服务器(linux下)<br>

2. 各类ai调用(待进一步扩展能调用的ai接口) 


##### 图像识别
url格式为:http://(服务器ip或域名):(端口)/baidu/ai/img-classify/(检测类型) 加上post参数<br>
检测类型包括:(可参考百度ai文档)<br>
<ul>
    <li>car(车辆识别),&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;参数：img,top_num(默认值为5)</li>
    <li>object_detect(图像主体识别),&nbsp;&nbsp;&nbsp;参数:img,with_face(默认值为1)</li>
    <li>dish(菜品识别),&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;参考:img,top_num(默认值为5),filter_threshold(默认值为0.95)</li>
    <li>logo(logo识别),&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;参数:img,custom_lib(默认值为False)</li>
    <li>animal(动物识别),&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;参数:img,top_num(默认值为6)</li>
    <li>plant(植物识别),&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;参数:img</li>
    <li>advanced_general(通用物体及场景识别)&nbsp;参数:img</li>
    <li>customized_image(定制图像分类)&nbsp;&nbsp;&nbsp;参数:img,request_url,top_num(默认值为5)</li>
    <li>customized_object(定制图像分类)&nbsp;&nbsp;&nbsp;参数:img,request_url</li>
</ul>

测试脚本:<br>
```
import requests
import base64


def main():
    source = {"http://127.0.0.1:8000/baidu/ai/img-classify/car/": "car.jpg",               # 车辆识别
              "http://127.0.0.1:8000/baidu/ai/img-classify/object_detect/": "face.jpeg",   # 图像主体识别 
              "http://127.0.0.1:8000/baidu/ai/img-classify/dish/": "dish.jpeg",            # 菜品识别
              "http://127.0.0.1:8000/baidu/ai/img-classify/logo/": "logo.jpg",             # logo识别
              "http://127.0.0.1:8000/baidu/ai/img-classify/animal/": "animal.jpeg",        # 动物识别
              "http://127.0.0.1:8000/baidu/ai/img-classify/plant/": "plant.jpg",           # 植物识别
              "http://127.0.0.1:8000/baidu/ai/img-classify/advanced_general/": "view.jpg"} # 通用物体及场景识别
    for request_url, img_path in source.items():
        f = open(img_path, 'rb')
        img = base64.b64encode(f.read())
        params = {"img": img}
        response = requests.post(url=request_url, data=params)
        print(response.json())


if __name__ == '__main__':
    main()

```


##### 语音合成

url格式:http://(服务器ip或域名):(端口)/baidu/ai/text2audio/ 加上get参数<br>
测试脚本:<br>
```
import requests


def main():
    tex = "寥落古行宫 宫花寂寞红 白头宫女在 闲坐说玄宗 ".encode("utf-8")
    cuid = "00:0c:29:53:5f:2f"
    payloads = {'tex': tex, 'cuid': cuid}
    request_url = "http://localhost:8000/baidu/ai/text2audio/"

    response = requests.get(url=request_url, params=payloads)
    if response.headers['Content-Type'] == 'audio/mp3':
        with open("123.mp3", 'wb') as f:
            f.write(response.content)
            f.flush()
        print('download:' + '123.mp3')
    else:
        print(response.json())


if __name__ == '__main__':
    main()
```

##### 文字识别

url格式:http://(服务器ip或域名):(端口)/baidu/ai/ocr/(检测类型)/ 加上post参数<br>
类型包括:general_basic(通用文字识别),accurate_basic(通用文字识别高精度),general(通用文字识别位置信息),<br>
accurate(通用文字识别位置高精度),general_enhanced(通用文字识别含生僻字)<br>
参数参照百度文档，测试实例参照test测试目录下的文字识别<br>





