from django.contrib import admin
from django.urls import path
from OCR import views


urlpatterns = [
    path('', views.home, name="ocrHome"),
    path('proceedOcr', views.proceedOcr, name="proceedOcr"),
    # path('register', views.ocr, name="register"),
    # path('logout', views.ocr, name="logout"),
]
