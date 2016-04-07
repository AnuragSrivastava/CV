import cv2

image = cv2.imread('face.tiff', 0)

# Sobel's filter

sobel = cv2.Sobel(image, cv2.CV_64F, 1, 1, ksize= 5)
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize= 5)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize= 5)


cv2.imshow('Sobel', sobel)
# cv2.imshow('SobelX', sobelX)
# cv2.imshow('SobelY', sobelY)


# Using Scharr's filter
scharr = cv2.Sobel(image, cv2.CV_64F, 1, 1, ksize= 1)
scharrX = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize= -1)
scharrY = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize= -1)
scharrXX = cv2.Scharr(image, cv2.CV_64F, 1, 0)

# cv2.imshow('Scharr', scharr)
cv2.imshow('ScharrX', scharrX)
# cv2.imshow('ScharrY', scharrY)
cv2.imshow('Scharr Complete on X', scharrXX)
cv2.imshow('Scharr Complete on X', scharrXX)
# Laplacian Filter

laplace = cv2.Laplacian(image, cv2.CV_64F)

cv2.imshow('Laplacian', laplace)

cv2.waitKey(0)
cv2.destroyAllWindows()
