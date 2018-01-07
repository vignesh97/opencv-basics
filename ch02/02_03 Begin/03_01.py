import numpy as np 
import cv2
bw = cv2.imread('detect_blob.png',0)
height,width = bw.shape[0:2]
cv2.imshow("Original BW",bw)
binary = np.zeros([height, width,1],'uint8')

threshold_value = 85

for row in range(0,height):
	for col in range(0, width):
		if bw[row][col]>threshold_value:
			binary[row][col]=255

#cv2.imshow("Slow Binary",binary)
ret, thresh = cv2.threshold(bw,threshold_value,255,cv2.THRESH_BINARY)
cv2.imshow("CV Threshold",thresh)


thresh_adapt = cv2.adaptiveThreshold(bw,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 115, 1)

cv2.imshow("CV AdaptiveThreshold",thresh_adapt)





cv2.waitKey(0)
cv2.destroyAllWindows()



