import requests
from . import config
import json

'''
语音相关api
参数设置参考百度文档
'''


def text2audio(tok, tex, cuid, ctp=1, lan='zh', spd=5, pit=5, vol=5, per=0):
    '''
    语音合成
    返回值为列表:[返回类型，返回内容]
    '''
    request_url = config.text2audio_url
    payloads = {'tok': tok,
                'tex': tex,
                'cuid': cuid,
                'ctp': ctp,
                'lan': lan,
                'spd': spd,
                'pit': pit,
                'vol': vol,
                'per': per, }
    response = requests.get(url=request_url, params=payloads)
    if response.headers['Content-Type'] == 'audio/mp3':
        return ['audio/mp3', response.content]
    else:
        return ['application/json', response.json()]


def speech_recognize(token, format, cuid, speech, len, dev_pid=1537):
    '''
    语音识别
    返回值为百度ai返回的原始json数据
    '''
    rate = 16000
    channel = 1
    headers = {
        "Content-Type": "application/json",
    }
    request_url = config.speech_recognize_url
    payloads = {"token": token,
                "format": format,
                "cuid": cuid,
                "speech": speech,
                "len": len,
                "dev_pid": dev_pid,
                "rate": rate,
                "channel": channel, }
    response = requests.post(url=request_url, data=json.dumps(payloads), headers=headers)
    return response.json()
