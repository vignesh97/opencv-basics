import numpy as np 
import cv2 
color = cv2.imread("butterfly.jpg",1)
cv2.imshow("Image",color)
cv2.moveWindow("Image",0,0)
print(color.shape)
height,width,channels = color.shape
cv2.waitKey(0)
cv2.destroyAllWindows()
