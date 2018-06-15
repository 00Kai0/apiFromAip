from django.http import HttpResponse, Http404, HttpResponseForbidden
from utils.baidu_ai import img_classify, ocr, face
from utils.baidu_ai.audio import text2audio
from utils.baidu_ai.token import get_access_token
from django.views.decorators.csrf import csrf_exempt
from .models import Token
import datetime
import json
from .config import client_id, client_secret
from .tools.data_filter import Img_classifyFilter, OcrFilter, FaceFilter


def get_useful_token():
    '''
    获取当前可用的access_token
    '''
    now = datetime.datetime.now()
    try:
        token = Token.objects.all()[0]
    except IndexError:
        # 当数据库没有access_token时，直接调用api获取新的token,并存入数据库
        # 失效时间为当前时间加上30天
        access_token = get_access_token(client_id=client_id,
                                        client_secret=client_secret)
        token = Token(access_token=access_token, end_time=now + datetime.timedelta(days=30))
        token.save()
    # 判断access_token是否失效,失效则删除旧的token，获取新token,并存入数据库
    if (token.end_time - now).days < 2:
        access_token = get_access_token(client_id=client_id,
                                        client_secret=client_secret)
        token.delete()
        token = Token(access_token=access_token, end_time=now + datetime.timedelta(days=30))
        token.save()
    return token.access_token


@csrf_exempt
def detect(request, ai_model):
    '''
    图像识别视图
    '''
    if request.method == 'POST':
        # 获取post过来的图片，以及获取当前时间
        img = request.POST.get('img', None)

        # 图片不存在，返回错误
        if not img:
            return HttpResponse(json.dumps({"error_msg": "images invalid", "error_code": "666666"}),
                                content_type="application/json")

        # 获取access_token
        access_token = get_useful_token()

        # 确定检测模型,并获取每种模型需要的参数，没有则赋值为默认值,并调用api获取结果回传到客户端
        if ai_model == 'object_detect':
            with_face = request.POST.get('with_face', 1)
            content = img_classify.object_detect(img=img, access_token=access_token, with_face=with_face)
        elif ai_model == 'car':
            top_num = request.POST.get('top_num', 5)
            content = img_classify.car(img=img, access_token=access_token, top_num=top_num)
        elif ai_model == 'dish':
            top_num = request.POST.get('top_num', 5)
            filter_threshold = request.POST.get('filter_threshold', 0.95)
            content = img_classify.dish(img=img, access_token=access_token, top_num=top_num, filter_threshold=filter_threshold)
        elif ai_model == 'logo':
            custom_lib = request.POST.get('custom_lib', False)
            content = img_classify.logo(img=img, access_token=access_token, custom_lib=custom_lib)
        elif ai_model == 'animal':
            top_num = request.POST.get('top_num', 6)
            content = img_classify.animal(img=img, access_token=access_token, top_num=top_num)
        elif ai_model == 'plant':
            content = img_classify.plant(img=img, access_token=access_token)
        elif ai_model == 'advanced_general':
            content = img_classify.advanced_general(img=img, access_token=access_token)
        elif ai_model == 'customized_image':
            request_url = request.POST.get('request_url', None)
            top_num = request.POST.get('top_num', 5)
            if not request_url:
                return HttpResponse(0)
            content = img_classify.customized_image(img=img, access_token=access_token, request_url=request_url, top_num=top_num)
        elif ai_model == 'customized_object':
            request_url = request.POST.get('request_url', None)
            if not request_url:
                return HttpResponse(0)
            content = img_classify.customized_object(img=img, access_token=access_token, request_url=request_url)
        else:
            # 非已知模型返回404
            return Http404()

        # 加载筛选器,对数据筛选
        imgfr = Img_classifyFilter(content, ai_model)
        content = imgfr.filter()

        # 结果以json格式返回给客户端
        return HttpResponse(json.dumps(content), content_type="application/json")
    else:
        # 其他请求禁止
        return HttpResponseForbidden()


@csrf_exempt
def speech_synthesise(request):
    '''
    语音合成视图
    '''
    if request.method == 'POST':
        tex = request.POST.get('tex', None)
        cuid = request.POST.get('cuid', None)
        if tex is None or cuid is None:
            # 没有给出必要参数 返回错误码
            return HttpResponse(json.dumps({"error_msg": "tex or cuid is None", "error_code": "666655"}),
                                content_type="application/json")
        ctp = request.POST.get('ctp', 1)
        lan = request.POST.get('lan', 'zh')
        spd = request.POST.get('spd', 5)
        pit = request.POST.get('pit', 5)
        vol = request.POST.get('vol', 5)
        per = request.POST.get('per', 0)

        # 获取 access_token
        access_token = get_useful_token()
        CType, content = text2audio(
            tok=access_token,
            tex=tex,
            cuid=cuid,
            ctp=ctp,
            lan=lan,
            spd=spd,
            pit=pit,
            vol=vol,
            per=per
        )
        if CType == 'audio/mp3':
            # 返回的是mp3格式内容时返回mp3内容
            return HttpResponse(content, content_type=CType)
        else:
            # 没返回mp3内容则认为是错误信息，并以json格式返回
            return HttpResponse(json.dumps(content), content_type=CType)
    else:
        # 其余访问禁止
        return HttpResponseForbidden()


@csrf_exempt
def char_recognize(request, ai_model):
    '''
    文字识别视图
    暂时不支持图片url参数
    '''
    if request.method == 'POST':
        # 取得必要参数，若没给返回错误
        image = request.POST.get('image', None)
        if image is None:
            return HttpResponse(json.dumps({"error_msg": "images invalid", "error_code": "666666"}),
                                content_type="application/json")

        # 获取 access_token
        access_token = get_useful_token()

        # 确定检测模型,同图像识别
        if ai_model == "general_basic":
            language_type = request.POST.get('language_type', 'CHN_ENG')
            detect_direction = request.POST.get('detect_direction', False)
            detect_language = request.POST.get('detect_language', 'false')
            probability = request.POST.get('probability', 'false')
            content = ocr.general_basic(access_token=access_token,
                                        image=image,
                                        language_type=language_type,
                                        detect_direction=detect_direction,
                                        detect_language=detect_language,
                                        probability=probability)
        elif ai_model == "accurate_basic":
            detect_direction = request.POST.get('detect_direction', False)
            probability = request.POST.get('probability', 'false')
            content = ocr.accurate_basic(access_token=access_token,
                                         image=image,
                                         detect_direction=detect_direction,
                                         probability=probability)
        elif ai_model == "general":
            recognize_granularity = request.POST.get('recognize_granularity', 'big')
            language_type = request.POST.get('language_type', 'CHN_ENG')
            detect_direction = request.POST.get('detect_direction', False)
            detect_language = request.POST.get('detect_language', 'false')
            vertexes_location = request.POST.get('vertexes_location', 'false')
            probability = request.POST.get('probability', 'false')
            content = ocr.general(access_token=access_token,
                                  image=image,
                                  recognize_granularity=recognize_granularity,
                                  language_type=language_type,
                                  detect_direction=detect_direction,
                                  detect_language=detect_language,
                                  vertexes_location=vertexes_location,
                                  probability=probability)
        elif ai_model == "accurate":
            recognize_granularity = request.POST.get('recognize_granularity', 'big')
            detect_direction = request.POST.get('detect_direction', False)
            vertexes_location = request.POST.get('vertexes_location', 'false')
            probability = request.POST.get('probability', 'false')
            content = ocr.accurate(access_token=access_token,
                                   image=image,
                                   recognize_granularity=recognize_granularity,
                                   detect_direction=detect_direction,
                                   vertexes_location=vertexes_location,
                                   probability=probability)
        elif ai_model == "general_enhanced":
            language_type = request.POST.get('language_type', 'CHN_ENG')
            detect_direction = request.POST.get('detect_direction', False)
            detect_language = request.POST.get('detect_language', 'false')
            probability = request.POST.get('probability', 'false')
            content = ocr.general_enhanced(access_token=access_token,
                                           image=image,
                                           language_type=language_type,
                                           detect_direction=detect_direction,
                                           detect_language=detect_language,
                                           probability=probability)
        else:
            return Http404()

        # 加载筛选器,筛选结果
        ocrfr = OcrFilter(content, ai_model)
        content = ocrfr.filter()

        # json格式返回结果
        return HttpResponse(json.dumps(content), content_type="application/json")
    else:
        # 其余访问禁止
        return HttpResponseForbidden()


@csrf_exempt
def human_face(request, ai_model):
    '''
    人脸识别视图
    '''
    if request.method == 'POST':
        # 取得必要参数，若没有返回错误,有单张图片或者多张图片
        image = request.POST.get('image', None)
        if image is None:
            return HttpResponse(json.dumps({"error_msg": "images invalid", "error_code": "666666"}),
                                content_type="application/json")

        # 获取access_token
        access_token = get_useful_token()

        # 确定检测模型
        if ai_model == "face_detect":
            image_type = request.POST.get('image_type', 'BASE64')
            face_field = request.POST.get('face_field', 'faceshape,facetype,age,gender,race')
            max_face_num = request.POST.get('max_face_num', 1)
            face_type = request.POST.get('face_type', 'LIVE')
            content = face.face_detect(access_token=access_token,
                                       image=image,
                                       image_type=image_type,
                                       face_field=face_field,
                                       max_face_num=max_face_num,
                                       face_type=face_type)
        elif ai_model == "face_match":
            # 多张图片用json格式传送，这里需要解码
            image_set = json.loads(image)
            images = list()
            image_types = list()
            face_types = list()
            quality_controls = list()
            liveness_controls = list()
            for temp in image_set:
                images.append(temp.get('image', None))
                image_types.append(temp.get('image_type', 'BASE64'))
                face_types.append(temp.get('face_type', 'LIVE'))
                quality_controls.append(temp.get('quality_control', 'NONE'))
                liveness_controls.append(temp.get('liveness_control', 'NONE'))
            content = face.face_match(access_token=access_token,
                                      images=images,
                                      image_types=image_types,
                                      face_types=face_types,
                                      quality_controls=quality_controls,
                                      liveness_controls=liveness_controls)
        elif ai_model == "face_faceverify":
            # 多张图片用json格式传送，这里需要解码
            image_set = json.loads(image)
            images = list()
            image_types = list()
            face_fields = list()
            for temp in image_set:
                images.append(temp.get('image', None))
                image_types.append(temp.get('image_type', 'BASE64'))
                face_fields.append(temp.get('face_field', 'faceshape,facetype,age,gender,race'))
            content = face.face_faceverify(access_token=access_token,
                                           images=images,
                                           image_types=image_types,
                                           face_fields=face_fields)
        else:
            return Http404()

        # 加载筛选器，筛选结果
        facefr = FaceFilter(content, ai_model)
        content = facefr.filter()

        # json格式返回结果
        return HttpResponse(json.dumps(content), content_type="application/json")

    else:
        # 其余访问禁止
        return HttpResponseForbidden()
