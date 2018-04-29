import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images.jpg')

ret, thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original image', 'Binary','Binary_inv','Trunc', 'Tozero', 'Tozero_inv']
images = [img, thresh1,thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(3,2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()