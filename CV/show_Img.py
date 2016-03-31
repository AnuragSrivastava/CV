import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('normal.jpg')

# show image using cv2

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# show image using matplotlib
b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])
plt.subplot(121)
plt.imshow(img2)
plt.show()





# line
# cv2.line(image, (0, 0), (255, 255), (255, 255, 255), 3)

# rectangle
# cv2.rectangle(image, (120, 120), (200, 200), (255, 255, 255), 5)


