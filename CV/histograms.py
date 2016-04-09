import cv2
import numpy as np

image_c = cv2.imread('face.tiff')
image_g = cv2.imread('face.tiff', 0)

# using CV
hist_cv = cv2.calcHist([image_g], [0], mask=None, histSize=[256], ranges=[0,256])

# using np
hist_c, bins = np.histogram(image_c)
hist_g, bins = np.histogram(image_g)

cv2.imshow("CV_HIST", hist_cv)
cv2.imshow('NP_HIST Color', hist_c)
cv2.imshow('NP_HIST GRAY', hist_g)

# equalization

image = cv2.equalizeHist(image_g)
res_u = np.hstack((image_g, image))

# adaptive equalization

clahe = cv2.createCLAHE()
adapted = clahe.apply(image_g)
res_l = np.hstack((image_g, adapted))

res = np.vstack((res_u, res_l))
cv2.imshow('after equalization', res)


cv2.waitKey(0)
cv2.destroyAllWindows()