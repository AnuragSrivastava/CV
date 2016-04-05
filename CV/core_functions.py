import cv2
import numpy as np

image = cv2.imread('face.tiff')

# (Rows, Columns, Channels)
r, c, ch = image.shape

# getting regions of interest (roi)

roi1 = image[:, c/4:c/2]
roi2 = image[:, c/2:(3*c/4)]

image[:, (3*c/4):c] = roi1
image[:, 0:c/4] = roi2

cv2.imshow("Image", image)

# add images

img = cv2.imread('normal.jpg')

roi = image[:, :]
bw_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(bw_image, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

foreground = cv2.bitwise_and(roi, roi, mask = mask)
background = cv2.bitwise_and(roi, roi, mask = mask_inv)

img_sum = cv2.add(foreground, background)
img[0:r, 0:c] = img_sum

cv2.imshow('Sum', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
