import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

def plot_channels(image, title):

    plt.figure(figsize = (20,20))

    plt.subplot(131), plt.imshow(image[:,:,0], cmap = "gray")
    plt.subplot(132), plt.imshow(image[:,:,1], cmap = "gray"), plt.title(title, fontsize = 25)
    plt.subplot(133), plt.imshow(image[:,:,2], cmap = "gray")

    plt.show()

def plot_channels_CMYK(image):

    # Create float
    bgr = image.astype(float)/255.

    # Extract channels
    with np.errstate(invalid='ignore', divide='ignore'):
        K = 1 - np.max(bgr, axis=2)
        C = (1-bgr[...,2] - K)/(1-K)
        M = (1-bgr[...,1] - K)/(1-K)
        Y = (1-bgr[...,0] - K)/(1-K)

    # Convert the input BGR image to CMYK colorspace
    CMYK = (np.dstack((C,M,Y,K)) * 255).astype(np.uint8)

    # Split CMYK channels
    Y, M, C, K = cv.split(CMYK)

    np.isfinite(C).all()
    np.isfinite(M).all()
    np.isfinite(K).all()
    np.isfinite(Y).all()

    plt.figure(figsize = (20,20))

    plt.subplot(141), plt.imshow(C, cmap = "gray"), plt.title("C", fontsize = 25)
    plt.subplot(142), plt.imshow(M, cmap = "gray"), plt.title("M", fontsize = 25)
    plt.subplot(143), plt.imshow(K, cmap = "gray"), plt.title("K", fontsize = 25)
    plt.subplot(144), plt.imshow(Y, cmap = "gray"), plt.title("Y", fontsize = 25)

    plt.show()

    

baboon = cv.imread("input_images/baboon.png")
chips = cv.imread("input_images/chips.png")
rgbcube = cv.imread("input_images/rgbcube_kBKG.png")

plot_channels( cv.cvtColor(baboon, cv.COLOR_BGR2YCrCb), "YCrCb")
plot_channels( cv.cvtColor(baboon, cv.COLOR_BGR2HSV), "HSV")
plot_channels_CMYK( baboon )

plot_channels( cv.cvtColor(chips, cv.COLOR_BGR2YCrCb), "YCrCb")
plot_channels( cv.cvtColor(chips, cv.COLOR_BGR2HSV), "HSV")
plot_channels_CMYK( chips )

plot_channels( cv.cvtColor(rgbcube, cv.COLOR_BGR2YCrCb), "YCrCb")
plot_channels( cv.cvtColor(rgbcube, cv.COLOR_BGR2HSV), "HSV")
plot_channels_CMYK( rgbcube )