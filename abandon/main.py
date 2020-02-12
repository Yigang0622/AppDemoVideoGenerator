# AppDemoVideoGenerator
# main 
# Created by Yigang Zhou on 2020-02-12.
# Copyright © 2020 Yigang Zhou. All rights reserved.

import numpy as np
import cv2

img = cv2.imread('iPhone 11 Pro.png')
x, y = img.shape[0:2]
img = cv2.resize(img, (int(y / 2), int(x / 2)))

x, y = img.shape[0:2]
print(x,y)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(imgray, 127, 255, 0)
ret, thresh = cv2.threshold(imgray, 250, 255, cv2.THRESH_TOZERO)

cv2.imshow("",thresh)
k_w  = int(max([x,y])/55)
if k_w % 2 == 0:
    k_w += 1
print(k_w)
img_blur = cv2.GaussianBlur(thresh, (k_w, k_w), 0)
cv2.imshow("blur",img_blur)
canny = cv2.Canny(img_blur, 50, 150)
cv2.imshow("canny",canny)

contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

if len(contours) >= 4:
    contours = sorted(contours,  key=len, reverse=True)

cv2.drawContours(img, contours[2], -1, (0,255,0), 3)

for each in contours:
    print(len(each))

cv2.namedWindow("11", cv2.WINDOW_NORMAL)
cv2.imshow("11",img)
cv2.waitKey()