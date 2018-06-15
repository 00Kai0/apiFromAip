from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^img-classify/([a-zA-Z_]+)/$', views.detect, name='detect'),
    url(r'^text2audio/$', views.speech_synthesise, name='speech_synthesise'),
    url(r'^ocr/([a-zA-Z_]+)/$', views.char_recognize, name='char_recognize'),
    url(r'^face/([a-zA-Z_]+)/$', views.human_face, name='human_face'),
]
