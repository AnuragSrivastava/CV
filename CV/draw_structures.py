import numpy as np
import cv2

image = np.zeros((512, 512, 3))

cv2.namedWindow("figures")

mode = True
draw = False
ix, iy = -1, -1


def draw_figures(event, x, y, flags, param):
    global mode, draw, ix, iy

    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
        if mode:
            cv2.rectangle(image, (ix, iy), (x, y), (0, 125, 125), -1)
        else:
            cv2.circle(image, (x, y), 5, (125, 125, 0), -1)

    elif event == cv2.EVENT_LBUTTONDBLCLK:
        mode = not mode


cv2.setMouseCallback('figures', draw_figures)

while 1:
    cv2.imshow('figures',image)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()