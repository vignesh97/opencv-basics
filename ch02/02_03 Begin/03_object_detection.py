import numpy as np
import cv2

img = cv2.imread("fuzzy.png",1)
cv2.imshow("Original",img)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (3,3),0)

thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,205,1)

cv2.imshow("Binary",thresh)






cv2.waitKey(0)
cv2.destroyAllWindows()