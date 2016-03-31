import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('normal.jpg')

# show image
'''
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])
plt.subplot(121)
plt.imshow(img2)
plt.show()
'''
# camera capture
'''
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    cap.open
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1):
        break
cap.release()
cv2.destroyAllWindows()
'''

image = np.zeros((512, 512, 3))

# line
# cv2.line(image, (0, 0), (255, 255), (255, 255, 255), 3)

# rectangle
# cv2.rectangle(image, (120, 120), (200, 200), (255, 255, 255), 5)

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
