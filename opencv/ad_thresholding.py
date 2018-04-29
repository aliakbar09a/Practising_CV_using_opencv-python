from matplotlib import pyplot as plt
import cv2
import numpy as np

img = cv2.imread('sudoku.jpg',0 )
#img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
img = cv2.GaussianBlur(img, (5,5),0)
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
thresh3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

titles = ['original', 'global', 'mean c', 'gaussian c']
images = [img , thresh1, thresh2, thresh3]

for i in range(4):
    plt.subplot(2,2,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()