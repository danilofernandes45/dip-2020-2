import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('original.jpg')

img_resized = cv2.resize(img, dsize=(152, 190))


img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_resized = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
plt.subplot(121)
plt.title("Original shape: %s"%(str(np.shape(img))))
plt.imshow(img)
plt.subplot(122)
plt.title("Resized shape: %s"%(str(np.shape(img_resized))))
plt.imshow(img_resized)
plt.show()