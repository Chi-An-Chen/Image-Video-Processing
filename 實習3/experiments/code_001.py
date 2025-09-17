import cv2
import numpy as np
from matplotlib import pyplot as plt

def average_filter(grayimage, kernel_size=3):
    return cv2.blur(image, (kernel_size, kernel_size))

def median_filter(grayimage, kernel_size=3):
    return cv2.medianBlur(image, kernel_size)     

def gaussian_filter(grayimage, kernel_size=3):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)     

image = cv2.imread('./Lena_noise.bmp')
grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

average = average_filter(grayimage)
median = median_filter(grayimage)
gaussian = gaussian_filter(grayimage)

titles = ['GRAY', 'AVERAGE', 'MEDIAN', 'GAUSSIAN']
images = [grayimage, average, median, gaussian]
for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

