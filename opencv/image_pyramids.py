import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('roi.jpg')

lower_res = cv2.pyrDown(img)
more_lower = cv2.pyrDown(lower_res)
blurred = cv2.pyrUp(more_lower)

plt.imshow(img, 'gray')
plt.title('original'), plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(lower_res, 'gray')
plt.title('lower resolution'), plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(more_lower, 'gray')
plt.title('more_lower'), plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(blurred, 'gray')
plt.title('blurred'), plt.xticks([]), plt.yticks([])
plt.show()