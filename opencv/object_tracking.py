import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while(1):
    ret, frame = cap.read()


    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    lower_red = np.array([-10,100,100])
    upper_red = np.array([10,255,255])
    lower_green = np.array([50,100,100])
    upper_green = np.array([70, 255, 255])

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#    blur = cv2.GaussianBlur(frame, (5,5), 0)
    mask1 = cv2.inRange(hsv, lower_blue, upper_blue)
    mask2 = cv2.inRange(hsv, lower_red,upper_red)
    mask3 = cv2.inRange(hsv,lower_green,upper_green)

    mask = cv2.bitwise_or(mask1, mask2, )
    masks = cv2.bitwise_or(mask,mask3,)
    res = cv2.bitwise_and(frame, frame, mask= masks)

    cv2.imshow('mask',mask)
    cv2.imshow('masks', masks)
    cv2.imshow('res',res)
    k = cv2.waitKey(1) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()
