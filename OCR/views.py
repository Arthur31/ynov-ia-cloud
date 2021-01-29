from django.shortcuts import render
from django.contrib.auth.decorators import login_required


BASE_DIR = Path(__file__).resolve().parent.parent

staticPath = BASE_DIR.as_posix() + "/staticfiles/"


@login_required(login_url='register')
def home(request):
    return render(request, 'ocr/index.html', locals())



    loaded_model = load_model(staticPath + "/modelocr")