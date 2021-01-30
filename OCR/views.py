from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from keras.models import Sequential, load_model


import cv2 
import numpy as np
from skimage.exposure import rescale_intensity
import numpy as np
# import pandas as pd
# import csv
# import string
# import random
# import matplotlib.pyplot as plt
# import tensorflow.compat.v1 as tf
#tf.disable_v2_behavior()
# import _pickle as pickle
import os.path

# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.utils import shuffle
# from skimage import img_as_float



from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

staticPath = BASE_DIR.as_posix() + "/staticfiles/"

alphabet = [
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z',
]

kernel = np.array(
    [
        [0.3, 0.5, 0.3],
        [0.5, 0.5, 0.5],
        [0.3, 0.5, 0.3]
    ]
)

@login_required(login_url='register')
def home(request):
    return render(request, 'ocr/index.html', locals())

@csrf_exempt
def proceedOcr(request):
    ocrProcess('image')
    return HttpResponse('Done')

def ocrProcess(imageInput):
    # print(staticPath + '2Dconvolved.png')
    image = cv2.imread(staticPath + '2Dconvolved.png')
    #image = cv2.imread('umbc_zipcode.png')
    #image = cv2.imread('hello_world.png')

    # print(image)
    # print("Convolve and Save Output")
    # Convolve and Save Output
    output = convolve2D(image.copy(), kernel, padding=0)

    # print("Output")

    img = rescale_intensity(output, out_range=(0, 200)).astype(np.uint8)

    gray = cv2.bilateralFilter(img, 11, 17, 17)

    gray = cv2.GaussianBlur(gray, (5, 5), 2)

    # cv2.imwrite('temp.png', gray)

    edged = cv2.Canny(gray, 30, 200)

    thresh_gray = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3)));

    cnts, hierarchy  = cv2.findContours(thresh_gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    print("Number of Contours found = " + str(len(cnts))) 
    print("Number of hierarchy found = " + str(len(hierarchy))) 

    imageProceed = image.copy()

    loaded_model = load_model(staticPath + "modelocr")

    print(staticPath + "modelocr")


    returnString = ""
    i = 0
    for cnt in cnts:
        x,y,w,h = cv2.boundingRect(cnt)
        
        imageResizeAndCrop = cv2.resize(imageProceed[y:y+h, x:x+w],(28,28))

        imageForModel = imageResizeAndCrop.reshape(-1,28,28,1)
        
        cv2.imwrite(staticPath + 'crop/output' + str(i) + '.png', imageForModel)


        predict = loaded_model.predict(imageForModel)

        # print(predict[0])

        m = np.where(predict[0] == max(predict[0]))
        print(alphabet[m[0][0]])
        
        
        cv2.rectangle(imageProceed,(x,y),(x+w,y+h),(0,255,0),2)

        i += 1

    cv2.imwrite('output.png', imageProceed)

    print("end")

    # imageToProceed = cv2.imread('output.jpg')

    # predict = loaded_model.predict(imageToProceed)




def processImage(image):
    image = cv2.imread(image) 
    image = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY) 
    return image

def convolve2D(image, kernel, padding=0, strides=1):
    # Cross Correlation
    kernel = np.flipud(np.fliplr(kernel))

    # Gather Shapes of Kernel + Image + Padding
    xKernShape = kernel.shape[0]
    yKernShape = kernel.shape[1]
    xImgShape = image.shape[0]
    yImgShape = image.shape[1]
    
    # Shape of Output Convolution
    xOutput = int(((xImgShape - xKernShape + 2 * padding) / strides) + 1)
    yOutput = int(((yImgShape - yKernShape + 2 * padding) / strides) + 1)
    
    output = np.zeros((xOutput, yOutput))

    # Apply Equal Padding to All Sides
    if padding != 0:
        imagePadded = np.zeros((image.shape[0] + padding*2, image.shape[1] + padding*2))
        imagePadded[int(padding):int(-1 * padding), int(padding):int(-1 * padding)] = image
        print(imagePadded)
    else:
        imagePadded = image

    # Iterate through image
    for y in range(image.shape[1]):
        # Exit Convolution
        if y > image.shape[1] - yKernShape:
            break
        # Only Convolve if y has gone down by the specified Strides
        if y % strides == 0:
            for x in range(image.shape[0]):
                # Go to next row once kernel is out of bounds
                if x > image.shape[0] - xKernShape:
                    break
                try:
                    # Only Convolve if x has moved by the specified Strides
                    if x % strides == 0:
                        output[x, y] = (kernel * imagePadded[x: x + xKernShape, y: y + yKernShape]).sum()
                except:
                    break

    return output

def load_az_dataset(datasetPath):
    data=[]
    labels=[]
    for row in open(datasethPath):
        row = row.split(",")
        label= int(row[0])
        image = np.array([int(x) for x in row[1:]], dtype="uint8")
        image = image.reshape((28,28))
        data.append(image)
        labels.append(label)
    data = np.array(data, dtype="float32")
    labels= np.array(labels, dtype="int")
    return data, labels


