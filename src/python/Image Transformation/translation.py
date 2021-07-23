import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('original.jpg')

trans_img = np.roll(img, shift=200, axis=1)
trans_img[:, 0:200, :] = 0

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
trans_img = cv2.cvtColor(trans_img, cv2.COLOR_BGR2RGB)

plt.subplot(121)
plt.title("Original")
plt.imshow(img)
plt.subplot(122)
plt.title("Translated to x = 200")
plt.imshow(trans_img)
plt.show()