import cv2
import matplotlib.pyplot as plt
import numpy as np


xadrez = cv2.imread('xadrez.jpeg')
xadrez = cv2.cvtColor(xadrez,cv2.COLOR_BGR2RGB)
gray_xadrez = cv2.cvtColor(xadrez,cv2.COLOR_RGB2GRAY)

xadrez_real = cv2.imread('xadrez_real.jpg')
xadrez_real = cv2.cvtColor(xadrez_real,cv2.COLOR_BGR2RGB)
gray_real_xadrez = cv2.cvtColor(xadrez_real,cv2.COLOR_RGB2GRAY)


edge = cv2.goodFeaturesToTrack(gray_xadrez,100,0.01,10)
edge2 = cv2.goodFeaturesToTrack(gray_real_xadrez,100,0.01,10)

edge = np.int0(edge)
edge2 = np.int0(edge2)

for i in edge2:
    x,y = i.ravel()

    cv2.circle(xadrez_real,(x,y),15,(255,0,0),-1)


plt.imshow(xadrez_real)