import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils

theta = -30
mean_x = 0
mean_y = 0
sigma_x = 2
sigma_y = 1

range_axis = np.arange(-5, 5, 0.1)
x, y = np.meshgrid(range_axis, range_axis)

z = np.exp( - (x-mean_x)**2/(2*sigma_x**2) - (y-mean_y)**2/(2*sigma_y**2)) / (2 * np.pi * sigma_x * sigma_y)
z = imutils.rotate_bound(z, theta)

plt.title("theta: %.2fº\n mx: %.2f, my: %.2f\n sx: %.2f sy: %.2f"%(theta, mean_x, mean_y, sigma_x, sigma_y))
plt.imshow(z, cmap = 'gray')
plt.show()