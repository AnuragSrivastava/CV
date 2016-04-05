import cv2
import numpy as np

image = cv2.imread('face.tiff')

# (Rows, Columns, Channels)
r, c, _ = image.shape

# getting regions of interest (roi)

roi1 = image[:, c/4:c/2]
roi2 = image[:, c/2:(3*c/4)]

image[:, (3*c/4):c] = roi1
image[:, 0:c/4] = roi2

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
