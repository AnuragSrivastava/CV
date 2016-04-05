import cv2
import numpy as np


def nothing(x):
    pass


img = np.zeros((512, 512, 3))
'''
# create a window to which the trackbars would be attached
cv2.namedWindow('TrackBar')

# cereat trackbars
cv2.createTrackbar('R', 'TrackBar', 0, 255, nothing)
cv2.createTrackbar('G', 'TrackBar', 0, 255, nothing)
cv2.createTrackbar('B', 'TrackBar', 0, 255, nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'TrackBar', 0, 1, nothing)

while (1):
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
'''
# Simple Paint Application using trackbars


mode = ''
ix, iy = -1, -1
# b, g, r, s = 0, 0, 0, 0


def draw_shape(event, x, y, flags, param):
    global mode, ix, iy, b, g, r, s

    if event == cv2.EVENT_LBUTTONDOWN:
        ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        if mode == 'Rectangle':
            cv2.rectangle(img, (ix, iy), (x, y), (b, g, r), -1)
            print cv2.getTrackbarPos('B', 'Paint')
        elif mode == 'Circle':
            xc = abs(ix+x)/2
            yc = abs(iy+y)/2
            radius = abs(x-xc)
            cv2.circle(img, (xc, yc), radius, (b, g, r), -1)

cv2.namedWindow('Paint')

cv2.setMouseCallback('Paint', draw_shape)
paint = np.ones((800, 1024, 3))


cv2.createTrackbar('R', 'Paint', 0, 255, nothing)
cv2.createTrackbar('G', 'Paint', 0, 255, nothing)
cv2.createTrackbar('B', 'Paint', 0, 255, nothing)
shape = '0 -> Circle \n 1 -> Rectangle'
cv2.createTrackbar(shape, 'Paint', 0, 1, nothing)

while True:
    cv2.imshow('Paint', paint)
    k = cv2.waitKey(1) & 0xFF

    if k == 27:
        break

    r = cv2.getTrackbarPos('R', 'Paint')
    g = cv2.getTrackbarPos('G', 'Paint')
    b = cv2.getTrackbarPos('B', 'Paint')
    s = cv2.getTrackbarPos(shape, 'Paint')

    if s == 0:
        mode = 'Circle'
    elif s == 0:
        mode = 'Rectangle'

cv2.destroyAllWindows()
