import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('erosion.png',0)
kernel = np.ones((3,3), np.uint8)
kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

erosion = cv2.erode(img, kernel, iterations = 1)
dilation = cv2.dilate(img, kernel, iterations = 1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN,kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

titles = ['erosion', 'dilation', 'opening', 'closing', 'gradient', 'tophat', 'blackhat']
images = [erosion, dilation, opening, closing, gradient, tophat, blackhat]

for i in range(7):
    plt.subplot(4,2,i+ 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i]), plt.xticks([]), plt.yticks([])
plt.show()

erosion = cv2.erode(img, kernel2, iterations = 1)
dilation = cv2.dilate(img, kernel2, iterations = 1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN,kernel2)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel2)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel2)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel2)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel2)

for i in range(7):
    plt.subplot(4,2,i+ 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i]), plt.xticks([]), plt.yticks([])
plt.show()