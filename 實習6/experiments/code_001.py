import cv2
import numpy as np
from matplotlib import pyplot as plt


def ChannelSeparation(image):
    c1, c2, c3 = cv2.split(image)
    zeros = np.zeros(image.shape[:2], dtype=np.uint8)
    c1 = cv2.merge([c1, zeros, zeros])
    c2 = cv2.merge([zeros, c2, zeros])
    c3 = cv2.merge([zeros, zeros, c3])
    return c1, c2, c3

def GammaCorrection(src, gamma):
    normalized_image = src / 255.
    gamma_image = np.power(normalized_image, 1/gamma) * 255.
    return gamma_image.astype(np.uint8)

ImagePath = './lenna_RGB.bmp'
image = cv2.imread(ImagePath)

RGBimage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
HSVimage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
YCrCbimage = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

Y, Cr, Cb = ChannelSeparation(YCrCbimage)
H, S, V = ChannelSeparation(HSVimage)
R, G, B = ChannelSeparation(RGBimage)
gamma1 = GammaCorrection(RGBimage, gamma=2)
gamma2 = GammaCorrection(RGBimage, gamma=0.5)

images = [Y, Cr, Cb, H, S, V, R, G, B, gamma1, gamma2]
titles = ['CHANNEL_Y', 'CHANNEL_Cr', 'CHANNEL_Cb', 'CHANNEL_H', 'CHANNEL_S', 'CHANNEL_V', 'CHANNEL_R', 'CHANNEL_G', 'CHANNEL_B', 'GAMMA1', 'GAMMA2']

plt.figure() 
for i in range(len(images)):
    plt.subplot(4, 3, i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()


