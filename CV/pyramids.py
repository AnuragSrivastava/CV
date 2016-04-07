import cv2
import numpy as np

img_color = cv2.imread('face.tiff')
img_gray = cv2.imread('face.tiff, 0')

# Gaussian for colored

gpC = [img_color]
for i in xrange(6):
    GP = cv2.pyrDown(img_color)
    gpC.append(GP)

# Laplacian for grayscaled
lpG = [gpC[5]]
for i in xrange(6):
    LP = cv2.pyrDown(img_color)
    lpG.append(LP)

# combine the twi images
ls = []
for la, lb in zip(gpC, lpG):
    rows, cols, depth = la.shape
    lss = np.hstack((la[:, 0:cols/2], lb[:, cols/2:]))
    ls.append(ls)


# reconstruct the images
comb = LS[0]
for i in xrange(1,6):
    comb = cv2.pyrUp(comb)
    comb = cv2.add(comb, LS)


# image with direct connecting each half
real, rest = np.hstack((img_color[:,:cols/2],img_gray[:,cols/2:]))

cv2.imshow('Hello world!!!', comb)
cv2.imshow('Real', real)

cv2.waitKey(0)
cv2.destroyAllWindows()