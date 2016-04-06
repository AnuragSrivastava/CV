import cv2
import numpy as np

image1 = cv2.imread('face.tiff')
image2 = cv2.imread('normal.jpg')

# Resize

h, w = image1.shape[:2]

image = cv2.resize(image2, (w, h), interpolation= cv2.INTER_AREA)

sum_img = cv2.addWeighted(image1, 0.7, image, 0.3, 0)

cv2.imshow('sum_img', sum_img)

# Rotation

mat = cv2.getRotationMatrix2D((w/2, h/2), 90, 1)
rotated = cv2.warpAffine(sum_img, mat, (w, h))
cv2.imshow('Rotated', rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
