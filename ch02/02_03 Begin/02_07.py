import numpy as np 
import cv2
img = cv2.imread("butterfly.jpg",1)

img_half = cv2.resize(img, (0,0), fx=0.5,fy=0.5)
img_stretch = cv2.resize(img, (600,600))

img_stretch_near = cv2.resize(img, (600,600), interpolation=cv2.INTER_NEAREST)

cv2.imshow("img_half",img_half)
cv2.imshow("img_stretch",img_stretch)
cv2.imshow("img_stretch_near",img_stretch_near)

#Rotation
M = cv2.getRotationMatrix2D((0,0), -30, 1)
rotated = cv2.warpAffine(img,M,(img.shape[1], img.shape[0]))
cv2.imshow("rotated",rotated)



cv2.waitKey(0)
cv2.destroryAllWindows()



