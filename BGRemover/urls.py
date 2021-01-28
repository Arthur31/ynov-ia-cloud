from django.contrib import admin
from django.urls import path
from BGRemover import views


urlpatterns = [
    path('', views.home, name="removeBgHome"),
    path('removeBgProcess', views.removeBgProcess, name="removeBgProcessEndpoint"),
    # path('register', views.ocr, name="register"),
    # path('logout', views.ocr, name="logout"),
]