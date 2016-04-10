import cv2
import numpy as np

image = cv2.imread('normal.jpg')
image_g = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_g = cv2.GaussianBlur(image_g, (5, 5), 0)

circles = cv2.HoughCircles(image_g, cv2.cv.CV_HOUGH_GRADIENT, 1, 20)

# convert to integers
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 255), 3)

cv2.imshow('Circles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()