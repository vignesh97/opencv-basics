import numpy as np
import cv2

# Global variables
canvas = np.ones([500,500,3],'uint8')*255

radius=3
color=(0,255,0)

# click callback
def click(event, x, y, flags, param):
	global canvas
	if event == cv2.EVENT_LBUTTONDOWN:
		cv2.circle(canvas,(x,y),radius,color, -1)
	elif event == cv2.EVENT_MOUSEMOVE:
		print("Mousemove")
	elif event == cv2.EVENT_LBUTTONUP:
		print("LButton Up")

# window initialization and callback assignment
cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas", click)
# Forever draw loop
while True:

	cv2.imshow("canvas",canvas)

	# key capture every 1ms
	ch = cv2.waitKey(1)
	if ch & 0xFF == ord('q'):
		break
	

cv2.destroyAllWindows()