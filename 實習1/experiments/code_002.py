import cv2
from matplotlib import pyplot as plt

image = cv2.imread('./test_P05.bmp')
grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, th1 = cv2.threshold(grayimage, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) 
th2 = cv2.adaptiveThreshold(grayimage, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2) 
th3 = cv2.adaptiveThreshold(grayimage, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2) 

titles = ['ORIGIN', 'OTSU THRESHOLD', 'ADAPTIVE MEAN THRESHOLD', 'ADAPTIVE GAUSSIAN THRESHOLD']
images = [grayimage, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()