import cv2

def nothing(x):
    pass

# read the image in gray scale
image = cv2.imread('normal.jpg', 0)
'''
# best way to find a satisfactory image measure ;)

cv2.namedWindow('Threshold', cv2.WINDOW_AUTOSIZE)

cv2.createTrackbar('threshValue', 'Threshold', 0, 255, nothing)
cv2.createTrackbar('maxValue', 'Threshold', 0, 255, nothing)

while 1:
    k = cv2.waitKey(1)
    if k == 27:
        cv2.destroyWindow('Threshold')
        break
    threshVal = cv2.getTrackbarPos('threshValue', 'Threshold')
    maxVal = cv2.getTrackbarPos('maxValue', 'Threshold')
# the object that needs to be found has to be white, while the background has to black
    ret, thresh = cv2.threshold(image, threshVal, maxVal, cv2.THRESH_TOZERO_INV)
    cv2.imshow('Threshold', thresh)
'''

# the object that needs to be found has to be white, while the background has to black
ret, thresh = cv2.threshold(image, 226, 0, cv2.THRESH_TOZERO_INV)


# find the contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(image, contours, -1, (0, 0, 255), 3)

print hierarchy

# display the contours
cv2.imshow('found_contours', image)




cv2.waitKey(0)
cv2.destroyAllWindows()