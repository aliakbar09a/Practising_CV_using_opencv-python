import cv2
import numpy as np
from  matplotlib import pyplot as plt
img = cv2.imread('colours.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print(image.shape)
imgr = cv2.drawContours(thresh, contours, -1, (0,255,0),3 )
plt.subplot(131), plt.imshow(imgr, 'gray')
plt.title('contours draw'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(thresh, 'gray')
plt.title('thresh'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(image, 'gray')
plt.title('contours'), plt.xticks([]), plt.yticks([])
plt.show()