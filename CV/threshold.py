import cv2

img = cv2.imread('normal.jpg', 0)

# Global thresholding sets one threshold for full image
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)

# Adaptive thresholding to get different thresholds for different regions
adpt_thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
adpt_thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('Original', img)
cv2.imshow('thresh1', thresh)
cv2.imshow('Adaptive thresh gaussian', adpt_thresh)
cv2.imshow('Adaptive threshold mean', adpt_thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()