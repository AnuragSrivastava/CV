import cv2
import numpy as np

def nothing(x):
    pass

img = np.zeros((512, 512, 3))

# create a window to which the trackbars would be attached
cv2.namedWindow('TrackBar')

# cereat trackbars
cv2.createTrackbar('R', 'TrackBar', 0, 255, nothing)
cv2.createTrackbar('G', 'TrackBar', 0, 255, nothing)
cv2.createTrackbar('B', 'TrackBar', 0, 255, nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'TrackBar', 0, 1, nothing)

while(1):
    cv2.imshow('TrackBar', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R', 'TrackBar')
    g = cv2.getTrackbarPos('G', 'TrackBar')
    b = cv2.getTrackbarPos('B', 'TrackBar')
    s = cv2.getTrackbarPos(switch, 'TrackBar')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv2.destroyAllWindows()