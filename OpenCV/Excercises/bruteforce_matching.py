import cv2
import numpy as np
import matplotlib.pyplot as plt


def showimage(image):
    img = plt.figure(figsize = (30,28))
    ax = img.add_subplot(111)
    ax.imshow(image,cmap='gray')

condensade_milk = cv2.imread('leite_condensado.png')
condensade_milk = cv2.cvtColor(condensade_milk,cv2.COLOR_BGR2GRAY)


shelf = cv2.imread('prateleira.jpg')
shelf = cv2.cvtColor(shelf,cv2.COLOR_BGR2GRAY)

#Brute force detection
orb = cv2.ORB_create()

#Return keypoints and where to
kp1, des1 = orb.detectAndCompute(condensade_milk,None)
kp2, des2 = orb.detectAndCompute(shelf,None)

bruteforce = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck= True)

matches = bruteforce.match(des1,des2)

matches = sorted(matches,key = lambda x:x.distance)

milk_matches = cv2.drawMatches(condensade_milk,kp1,shelf,kp2,matches[:50],None, flags =2)

showimage(milk_matches)