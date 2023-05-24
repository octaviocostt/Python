import cv2

def desenha_tela(event, x , y, flags, param):
    global centro, clique

    if event == cv2.EVENT_LBUTTONDOWN:
        centro = (x,y)
        clique = False
    
    if event == cv2.EVENT_LBUTTONUP:
        clique = True
    
centro = (0,0)
clique = False

#captura video
cap = cv2.VideoCapture(0)
#Criar uma janela para o video
cv2.namedWindow('janela')

#Juntar janela a funcao desenha_circulo
cv2.setMouseCallback('janela', desenha_tela)

while True:
    #capturar frame
    ret, frame = cap.read()

    #verificar se ja foi clicado
    if clique:
        #desenha circulo
        cv2.circle(frame,centro,80, (0,255,0), 10)

    #apresentar o frame
    cv2.imshow('janela', frame)

    #comando de saida
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

cap.release()
cv2.destroyAllWindows()

