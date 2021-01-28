from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from gtts import gTTS 
from io import BytesIO
import os

@login_required(login_url='register')
def home(request):
    return render(request, 'tts/index.html', locals())


@csrf_exempt
def readSentence(request):

    #La methode get retourne le dernier message lu, on as pas tourver comment l'enlever sans casser l'autre route de demo ( si on l'enleve on ne peut pulus utiliser la route post dans le navigateur, uniquement dans postman)
    if request.method == 'GET':
        fname="result.mp3"
        f = open(fname,"rb") 
        response = HttpResponse()
        response.write(f.read())
        response['Content-Type'] ='audio/mp3'
        response['Content-Length'] =os.path.getsize(fname )
        return response

    if request.method == 'POST':
        text = request.POST['sentense']
        language = 'fr'
        speech = gTTS(text = text, lang = language, slow = False)
        speech.save("result.mp3")


        fname="result.mp3"
        f = open(fname,"rb") 
        response = HttpResponse()
        response.write(f.read())
        response['Content-Type'] ='audio/mp3'
        response['Content-Length'] =os.path.getsize(fname )
        return response
