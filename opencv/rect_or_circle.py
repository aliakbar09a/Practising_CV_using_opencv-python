import cv2
import numpy as np

drawing = False
mode = True
ix,iy = -1,-1

def draw(event,x,y,flags ,param):
    global ix, iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing =True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(255,0,0),1)
            else:
                cv2.circle(img,(x,y),5,(255,0,0),1,cv2.LINE_AA)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(255,0,0),1)
        else:
            cv2.circle(img,(x,y),5,(255,0,0),1,cv2.LINE_AA)

img = np.zeros((512,700,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == ord('r'):
        img = np.zeros((512,700,3),np.uint8)
    elif k == ord('q'):
        break
cv2.destroyAllWindows()
