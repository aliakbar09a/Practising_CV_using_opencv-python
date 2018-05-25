import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('myself.jpg')
cv2.imshow('j', img)
template = img[130:370, 255:450]
cv2.imwrite('myface.jpg', template)
cv2.imshow('ali', template)
h, w, c = template.shape

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED',
           'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
i = 0
for meth in methods:
    img2 = img.copy()
    img3 = img.copy()
    method = eval(meth)
    res = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img3, top_left, bottom_right,255,2)
    cv2.imshow('img3 after rectangle', img3)
    plt.subplot(3,4,i+1), plt.imshow(res)
    plt.xticks([]),plt.yticks([])
    plt.subplot(3,4,i+2), plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
    plt.xticks([]), plt.yticks([])
    i = i + 2
plt.show()