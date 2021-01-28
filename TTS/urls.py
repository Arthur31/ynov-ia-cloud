from django.contrib import admin
from django.urls import path
from TTS import views


urlpatterns = [
    path('', views.home, name="ttsHome"),
    path('speech', views.readSentence, name="textToSpeechEndpoint"),
    # path('register', views.ocr, name="register"),
    # path('logout', views.ocr, name="logout"),
]