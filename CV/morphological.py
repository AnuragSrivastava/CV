import cv2
import numpy as np

image = cv2.imread('j.png')
kernal = np.ones((5,5))

# Erosion
eroded = cv2.erode(image, kernal, iterations=1)
cv2.imshow('eroded J', eroded)

# Dilation
dilated = cv2.dilate(image, kernal, iterations=2)
cv2.imshow('dilated J', dilated)


cv2.waitKey(0)
cv2.destroyAllWindows()
