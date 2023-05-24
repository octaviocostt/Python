import cv2
import numpy as np
import matplotlib.pyplot as plt


octavio = cv2.imread('familia.jfif')
octavio_two = cv2.imread('octavioebia.jfif')

octavio = cv2.cvtColor(octavio,cv2.COLOR_BGR2RGB)

octavio_two = cv2.cvtColor(octavio_two,cv2.COLOR_BGR2RGB)

face_octavio = cv2.imread('face_octavio.jfif')
face_octavio = cv2.cvtColor(face_octavio,cv2.COLOR_BGR2RGB)

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']


for m in methods:
    #Create an image copy 
    copy_octavio = octavio.copy()
    method = eval(m)
    #Template Matching
    res = cv2.matchTemplate(copy_octavio,face_octavio,method)

    #Take min and max values and also min and max localization
    min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)

    #Check the brightness
    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        left_top = min_loc
    else:
        left_top = max_loc

    #Defining rectangle form
    height,width, channel =  face_octavio.shape
    right_base = (left_top[0] + width, left_top[1] + height)
    #Drawing the rectangle
    cv2.rectangle(octavio,left_top,right_base,(0,0,255), 10)


    #Showing the images
    plt.subplot(121)
    plt.imshow(res)
    plt.title("WarmMap")

    plt.subplot(122)
    plt.imshow(octavio)
    plt.title("Detection")

    #Method Name
    plt.suptitle(m)

    plt.show()
    print('\n')





