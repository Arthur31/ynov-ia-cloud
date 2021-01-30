from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


from keras.models import Sequential, load_model
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# from IPython.display import display
from PIL import Image
import cv2
from pathlib import Path




import numpy as np
from keras.preprocessing import image



BASE_DIR = Path(__file__).resolve().parent.parent

staticPath = BASE_DIR.as_posix() + "/staticfiles/"

@login_required(login_url='register')
def home(request):
    return render(request, 'imgClassif/index.html', locals())

@csrf_exempt
def classifierCatDog(request):

    img_str = request.FILES['image'].read()

    nparr = np.fromstring(img_str, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)


    imageSize = cv2.resize(img,(128, 128))

    # print(BASE_DIR + "/staticfiles/model/")

    print("load model from $staticPath")
    loaded_model = load_model(staticPath + "/modelClassif")
    # x = tf.random.uniform((10, 3))
    # assert np.allclose(model.predict(imageSize), loaded_model.predict(imageSize))


    test_image = imageSize

    # test_image = image.load_img(staticPath + 'cat.4808.jpg', target_size = (128, 128))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = loaded_model.predict(test_image)

    # print(result)

    # prediction = result[0][0]


    # if result [0][0] >=0.5:
    #     prediction = 'Chacha'
    # else :
    #     prediction = 'Doggo'
    # print(prediction)

    prediction = {
        'cat': str(result[0][0]),
        'dog': str(result[0][1]),
    }

    print(prediction)

    return JsonResponse(prediction)


    # test_image = image.load_img(staticPath + 'dog.5000.jpg', target_size = (128, 128))
    # test_image = image.img_to_array(test_image)
    # test_image = np.expand_dims(test_image, axis = 0)
    # result = loaded_model.predict(test_image)


    # print(result)

    # prediction = result[0][0]


    # if result [0][0] >=0.5:
    #     prediction = 'Chacha'
    # else :
    #     prediction = 'Doggo'
    # print(prediction)


    # # prediction = loaded_model.predict(imageSize)
    # print(prediction)

    # return HttpResponse("it's all good, prediction : " + str(prediction))




    # classifier = keras.models.load_model('./model.pb')

    # result = classifier.predict(imageSize)
    # training_set.class_indices
    # if result [0][0] >=0.5:
    #     prediction = 'Chacha'
    # else :
    #     prediction = 'Doggo'
    # print(prediction)
    # return HttpResponse("it's all good, prediction : "+prediction)