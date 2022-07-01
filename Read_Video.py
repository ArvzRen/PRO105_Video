import cv2

# Usar "0" para la cámara web
#vid = cv2.VideoCapture(0)

vid = cv2.VideoCapture("AnthonyShkraba.mp4")

if(vid.isOpened()==False):
    print("No es posible leer la entrada.")


