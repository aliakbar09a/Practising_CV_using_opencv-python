import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
template = cv2.imread('myface.jpg')
h, w, c = template.shape
while(1):
    ret, frame = cap.read()
    img = frame.copy()
    cv2.imshow('image', frame)
    res = cv2.matchTemplate(img, template, cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = min_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img, top_left, bottom_right,(0,255,255),2)
    cv2.imshow('img after rectangle', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()