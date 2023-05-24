import cv2
import time

video = cv2.VideoCapture('videogravado.avi')

if video.isOpened() ==  False:
    print("Error opening the video!")

while video.isOpened():

    ret, frame = video.read()

    if ret == True:
        time.sleep(1/30)
        cv2.imshow('frame', frame)

        if cv2.waitKey(10) & 0xFF == ord('s'):
            break

    else:
        break

video.release()
cv2.destroyAllWindows()