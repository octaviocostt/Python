import cv2
import time

def desenha_retangulo(event,x,y,flags,params):
    global pt1,pt2,topo,base

    if event == cv2.EVENT_LBUTTONDOWN:

        #apagar retangulo apresentado na tela
        if topo == True and base == True:
            pt1 = (0,0)
            pt2 = (0,0)
            topo = False
            base = False

        if topo == False:
            pt1 = (x,y)
            topo = True
        
        elif base == False:
            pt2 = (x,y)
            base = True

#Global Variables
pt1 = (0,0)
pt2 = (0,0)
topo = False
base = False



video = cv2.VideoCapture(0)

cv2.namedWindow('frame')
cv2.setMouseCallback('frame', desenha_retangulo)


while True:

    ret, frame = video.read()

    if topo:
        cv2.circle(frame,pt1,6,(0,0,255), -1)

    if topo and base:
        cv2.rectangle(frame, pt1,pt2,(0,255,0), 3)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

video.release()

cv2.destroyAllWindows()
        
