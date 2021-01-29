from django.contrib import admin
from django.urls import path
from imgClassif import views


urlpatterns = [
    path('', views.home, name="cnnHome"),
    path('classifierCatDog', views.classifierCatDog, name="classifierCatDogEndpoint"),
]