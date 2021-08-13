import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

def plot_channels(image):

    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    red = image.copy()
    red[:,:,1] = 0
    red[:,:,2] = 0

    green = image.copy()
    green[:,:,0] = 0
    green[:,:,2] = 0

    blue = image.copy()
    blue[:,:,0] = 0
    blue[:,:,1] = 0

    plt.figure(figsize = (20,20))

    plt.subplot(231), plt.imshow(red)
    plt.subplot(234), plt.hist(red[:,:,0].reshape(-1), color = "red", bins = 25)

    plt.subplot(232), plt.imshow(green)
    plt.subplot(235), plt.hist(green[:,:,1].reshape(-1), color = "green", bins = 25)

    plt.subplot(233), plt.imshow(blue)
    plt.subplot(236), plt.hist(blue[:,:,2].reshape(-1), color = "blue", bins = 25)

    plt.show()

baboon = cv.imread("input_images/baboon.png")
chips = cv.imread("input_images/chips.png")
rgbcube = cv.imread("input_images/rgbcube_kBKG.png")

plot_channels(baboon)
plot_channels(chips)
plot_channels(rgbcube)