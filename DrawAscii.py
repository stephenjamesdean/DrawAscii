import imgi as asc
import cv2
import numpy as np
from PIL import Image

drawing = False
ix,iy = -1,-1

def drawc(event,x,y,flags,param):
    global ix,iy,drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(img,(x,y),5,(0,0,255),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img, (x,y), 5,(0,0,255),-1)
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        asc.makeAsciiim(Image.fromarray(img2))


img = 255 * np.ones((512, 512, 3), np.uint8)

cv2.namedWindow("image")
cv2.setMouseCallback("image",drawc)

while(1):
    cv2.imshow("image",img)
    if cv2.waitKey(20) & 0xFF ==27:
        break
cv2.destroyWindow("image")


# asc.makeArtim("test.jpg")
