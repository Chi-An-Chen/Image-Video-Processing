import cv2
import numpy as np
from matplotlib import pyplot as plt


def Binarization(image, threshold=55):
  grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  ret, binaryImage = cv2.threshold(grayImage, threshold, 255, cv2.THRESH_BINARY)
  return grayImage, binaryImage


def ImageLabeling(image, grayImage, binaryImage):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    binaryClose = cv2.dilate(binaryImage, kernel, iterations=2)
    numLabels, labels, stats, centers = cv2.connectedComponentsWithStats(binaryClose, connectivity=8, ltype=cv2.CV_32S)
    labelingImage = np.copy(image)
    segmentationImage = np.zeros(binaryImage.shape, dtype=np.uint8)
    contourImage = np.zeros(binaryImage.shape, dtype=np.uint8)
    for i in range(1, numLabels):
        x, y, w, h, area = stats[i]
        cx, cy = centers[i]
        if area <= 100:
            continue
        for row in range(image.shape[0]):
            for col in range(image.shape[1]):
                if labels[row, col] != i:
                    continue
                contourImage[row, col] = 255  
        contours, hierarchy = cv2.findContours(contourImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        labelingImage = cv2.drawContours(labelingImage, contours, -1, (255, 0, 0), 1)
        cnt = contours[0]
        perimeter = cv2.arcLength(cnt, True)
        e = 4 * np.pi * area / (perimeter ** 2) 
        cv2.circle(labelingImage, (int(cx), int(cy)), 2, (0, 255, 0), 2, 8, 0) 
        cv2.rectangle(labelingImage, (x, y), (x+w, y+h), (0, 0, 255), 1, 8, 0) 
        cv2.putText(labelingImage, f'No. {i}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        print(f'No. {i} 周長: {perimeter:.2f}, 面積: {area:.2f},真圓度: {e:.2f}')
        if e < 0.5:
            continue
        for row in range(image.shape[0]):
            for col in range(image.shape[1]):
                if labels[row, col] != i:
                    continue
                segmentationImage[row, col] = 255  
    return contourImage, segmentationImage, labelingImage


image = cv2.imread('./fruit.bmp')
grayImage, binaryImage = Binarization(image)
contourImage, segmentationImage, labelingImage = ImageLabeling(image, grayImage, binaryImage)

images = [image, binaryImage, contourImage, segmentationImage, labelingImage]
titles = ['ORIGINAL', 'BINARY', 'CONTOUR', 'SEGMENTATION', 'LABELING']
plt.figure() 
for i in range(len(images)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

