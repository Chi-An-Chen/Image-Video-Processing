import cv2
import numpy as np
from matplotlib import pyplot as plt


def HE(grayimage):
    return cv2.equalizeHist(grayimage)

def CLAHE(grayimage, clipLimit=4.0, tileGridSize=(8, 8)):
    clahe = cv2.createCLAHE(clipLimit, tileGridSize)
    return clahe.apply(grayimage)

image = cv2.imread('./pout.bmp')
grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
he_image = HE(grayimage)
clahe_image = CLAHE(grayimage)

images = [grayimage, he_image, clahe_image]
titles = ['GRAY', 'HE', 'CLAHE']
plt.figure() 
for i in range(3):
    plt.subplot(1, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

