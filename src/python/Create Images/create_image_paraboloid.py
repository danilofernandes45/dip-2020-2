import numpy as np
import matplotlib.pyplot as plt

range_axis = np.arange(-5, 5, 0.1)
x, y = np.meshgrid(range_axis, range_axis)
z = x**2 + y**2

plt.imshow(z, cmap = "gray")
plt.show()