import cv2
import numpy as np

img = cv2.imread('myself.jpg')
cv2.imshow('abs', img)
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()