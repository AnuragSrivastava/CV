import cv2
import numpy as np

image = cv2.imread('face.tiff')

# Creating own filter
kernel = np.ones((10, 10))/100
filtered1 = cv2.filter2D(image, -1, kernel)

# Blurring (box filter
blurred = cv2.blur(image, (5,5))

# Gaussian filter
gauss_blurred = cv2.GaussianBlur(image, (5, 5), 0)


cv2.imshow('original', image)
cv2.imshow('global', filtered1)
cv2.imshow('blurred', blurred)
cv2.imshow('guass_blur', gauss_blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()
