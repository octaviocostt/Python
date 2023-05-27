import cv2
import numpy as np
import matplotlib.pyplot as plt

xadrez = cv2.imread('xadrez.jpeg')

xadrez = cv2.cvtColor(xadrez,cv2.COLOR_BGR2RGB)


gray_xadrez = cv2.cvtColor(xadrez,cv2.COLOR_RGB2GRAY)

xadrez_real = cv2.imread('xadrez_real.jpg')
xadrez_real = cv2.cvtColor(xadrez_real,cv2.COLOR_BGR2RGB)

gray_real_xadrez = cv2.cvtColor(xadrez_real,cv2.COLOR_RGB2GRAY)

gray = np.float32(gray_xadrez)

destino = cv2.cornerHarris(src=gray_xadrez,blockSize=25,ksize=3,k=0.04)

destino = cv2.dilate(destino,None)

xadrez[destino > 0.01*destino.max()] = [255,0,0]

gray2 = np.float32(gray_real_xadrez)

destiny = cv2.cornerHarris(gray_real_xadrez,10,3,0.04)
destiny = cv2.dilate(destiny,None)
xadrez_real[destiny > 0.01*destiny.max()] = [0,255,0]


plt.imshow(xadrez_real)



