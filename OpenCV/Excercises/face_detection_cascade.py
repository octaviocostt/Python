import cv2 
import numpy as np
import matplotlib.pyplot as plt

familia = cv2.imread('familia.jfif')
familia = cv2.cvtColor(familia,cv2.COLOR_BGR2GRAY)


face_cascade = cv2.CascadeClassifier('C:\\Users\\octav\\Desktop\\Octávio\\ProgrammingProject\\PythonLanguage\\OpenCV\\opencv-4.x\\data\\haarcascades')

def face_detector(image):
    face_image = image.copy()

    face_rectangle = face_cascade.detectMultiScale(face_image,scaleFactor = 1.2,minNeighbors = 5)

    for(x,y,w,h) in face_rectangle:
        cv2.rectangle(face_image,(x,y),(x+w,y+h),(255,0,0),10)
    
    return face_image

result = face_detector(familia)

plt.imshow(result, cmap ='gray')