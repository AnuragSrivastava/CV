import cv2


def nothing(x):
    pass


image = cv2.imread('normal.jpg', 0)

cv2.namedWindow('Canny', cv2.WINDOW_AUTOSIZE)

cv2.createTrackbar('minValue', 'Canny', 0, 255, nothing)
cv2.createTrackbar('maxValue', 'Canny', 0, 255, nothing)

while 1:

    k = cv2.waitKey(1)
    if k == 27:
        break
    minVal = cv2.getTrackbarPos('minValue', 'Canny')
    maxVal = cv2.getTrackbarPos('maxValue', 'Canny')
    edges2 = cv2.Canny(image, minVal, maxVal)
    cv2.imshow('Canny', edges2)

cv2.destroyAllWindows()
