
from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('ocr/', include('OCR.urls')),
    path('tts/', include('TTS.urls')),
    path('removeBg/', include('BGRemover.urls')),
    path('cnn/', include('imgClassif.urls')),
]
