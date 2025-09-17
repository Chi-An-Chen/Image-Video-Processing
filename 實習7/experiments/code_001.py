import cv2
import numpy as np
from matplotlib import pyplot as plt


def Percentage2Intensity(thres_hsv):
    thres_hsv[0] = thres_hsv[0] / 2
    thres_hsv[1] = thres_hsv[1] // 100 * 255
    thres_hsv[2] = thres_hsv[2] // 100 * 255
    return thres_hsv


def HSVColorSegmentation(**kwargs):
    src, LowerHSV, UpperHSV = kwargs['src'], kwargs['LowerHSV'], kwargs['UpperHSV']
    image = src.copy()
    image_hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    LowerHSV = Percentage2Intensity(LowerHSV)
    UpperHSV = Percentage2Intensity(UpperHSV)
    mask = cv2.inRange(image_hsv, lowerb=LowerHSV, upperb=UpperHSV)
    seg = cv2.bitwise_and(image, image, mask=mask)
    return seg


def BGRColorSegmentation(**kwargs):
    src, thresh = kwargs['src'], kwargs['thresh']
    seg = src.copy()
    for h in range(src.shape[0]):
        for w in range(src.shape[1]):
            R, G, B = src[h, w, :]
            chroma = (int(B) + int(R)) / 2 - int(G)
            if chroma < thresh and chroma != 0:
                seg[h, w, :] = 255
            else:
                seg[h, w, :] = 0
    return seg


ChartPath = './RGB_Chart.bmp'
ChartImage = cv2.imread(ChartPath)
ChartImage = cv2.cvtColor(ChartImage, cv2.COLOR_BGR2RGB)
BGRSeg = BGRColorSegmentation(src=ChartImage, thresh=100)

FlowerPath = './Flower.bmp'
FlowerImage = cv2.imread(FlowerPath)
FlowerImage = cv2.cvtColor(FlowerImage, cv2.COLOR_BGR2RGB)
LowerHSV = np.array([30, 30, 30])
UpperHSV = np.array([70, 100, 100])
HSVSeg = HSVColorSegmentation(src=FlowerImage, LowerHSV=LowerHSV, UpperHSV=UpperHSV)

images = [ChartImage, BGRSeg, FlowerImage, HSVSeg]
titles = ['CHART', 'BGR_SEGMENTATION', 'FLOWER', 'HSV_SEGMENTATION']

plt.figure() 
for i in range(len(images)):
    plt.subplot(2, 2, i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()


