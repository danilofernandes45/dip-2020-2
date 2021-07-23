import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('original.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

rot_img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

plt.subplot(121)
plt.title("Original")
plt.imshow(img)
plt.subplot(122)
plt.title("Rotated 90 degrees")
plt.imshow(rot_img)
plt.show()