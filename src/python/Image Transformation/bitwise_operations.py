import numpy as np
import cv2
import matplotlib.pyplot as plt

# draw a rectangle
rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (50, 50), (250, 250), 255, -1)

plt.subplot(231)
plt.imshow(rectangle, cmap = "gray")

# draw a semicircle
semicircle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(semicircle, (50, 50), 150, 255, -1)

plt.subplot(232)
plt.imshow(semicircle, cmap = "gray")

img_and = cv2.bitwise_and(rectangle, semicircle)
plt.subplot(234)
plt.title("AND")
plt.imshow(img_and, cmap = "gray")

plt.subplot(235)
img_or = cv2.bitwise_or(rectangle, semicircle)
plt.title("OR")
plt.imshow(img_or, cmap = "gray")


plt.subplot(236)
img_xor = cv2.bitwise_xor(rectangle, semicircle)
plt.title("XOR")
plt.imshow(img_xor, cmap = "gray")

plt.show()