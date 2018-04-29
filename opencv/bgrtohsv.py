import numpy as np
import cv2
green = np.uint8([[[0,255,0]]])
hsv = cv2.cvtColor(green, cv2.COLOR_BGR2GRAY)
print (hsv)