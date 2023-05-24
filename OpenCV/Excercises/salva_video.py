import numpy as np
import matplotlib.pyplot as plt 
from PIL import Image
import cv2

captura_imagem = cv2.VideoCapture(0)

largura = int(captura_imagem.get(cv2.CAP_PROP_FRAME_WIDTH))
altura = int(captura_imagem.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
saida = cv2.VideoWriter('videogravado.avi',fourcc,15.0,(largura,altura))





while (captura_imagem.isOpened()):

    ret, frame = captura_imagem.read()
    
    if ret == True:
        frame = cv2.flip(frame,1)
        saida.write(frame)
    
        cv2.imshow('frame', frame)

        if cv2.waitKey(10) & 0xFF == ord('s'):
            break
    else:
        break

captura_imagem.release()
saida.release()
cv2.destroyAllWindows()






