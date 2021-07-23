import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("original.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.subplot(131)
plt.title("Original")

plt.imshow(img)

# draw a circle
circle = np.zeros(np.shape(img)[:2], dtype = "uint8")
cv2.circle(circle, (750, 512), 500, 255, -1)

plt.subplot(132)
plt.title("Mask")
plt.imshow(circle, cmap = 'gray')

masked = cv2.bitwise_and(img, img, mask=circle)
plt.subplot(133)
plt.title("Region of Interest")
plt.imshow(masked)

plt.show()