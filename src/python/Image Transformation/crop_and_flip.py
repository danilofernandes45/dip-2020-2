import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('original.jpg')

cropped_img = img[:1250, :1000, :]

flipped_img = img[:, ::-1, :]

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cropped_img = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB)
flipped_img = cv2.cvtColor(flipped_img, cv2.COLOR_BGR2RGB)

plt.subplot(131)
plt.title("Original\n Shape: %s"%str(np.shape(img)))
plt.imshow(img)
plt.subplot(132)
plt.title("Cropped\n Shape: %s"%str(np.shape(cropped_img)))
plt.imshow(cropped_img)
plt.subplot(133)
plt.title("Flipped")
plt.imshow(flipped_img)
plt.show()