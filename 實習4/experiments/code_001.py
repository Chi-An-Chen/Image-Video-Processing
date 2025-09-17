import cv2
import numpy as np
from matplotlib import pyplot as plt


def calc_histogram(image, use_bgr=False):
    c = 3 if use_bgr else 1
    hist = [cv2.calcHist([image], [i], None, [256], [0, 255]) for i in range(c)]
    return hist

def plot_pic(hist, use_bgr=False):
    color = ['b','g','r'] if use_bgr else ['gray']
    for i, col in enumerate(color):
        plt.plot(hist[i], color=col)
        plt.xlim([0, 255])
    plt.show()

image = cv2.imread('./pout.bmp')
grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

bgr_hist = calc_histogram(image, use_bgr=True)
plot_pic(bgr_hist, use_bgr=True)
gray_hist = calc_histogram(grayimage, use_bgr=False)
plot_pic(gray_hist, use_bgr=False)