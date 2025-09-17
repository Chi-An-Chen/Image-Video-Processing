import cv2
from matplotlib import pyplot as plt

image = cv2.imread('./test_P05.bmp')
grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, th1 = cv2.threshold(grayimage, 127, 255, cv2.THRESH_BINARY) 
ret, th2 = cv2.threshold(grayimage, 127, 255, cv2.THRESH_BINARY_INV) 
ret, th3 = cv2.threshold(grayimage, 127, 255, cv2.THRESH_TRUNC) 
ret, th4 = cv2.threshold(grayimage, 127, 255, cv2.THRESH_TOZERO) 
ret, th5 = cv2.threshold(grayimage, 127, 255, cv2.THRESH_TOZERO_INV) 

titles = ['Original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [grayimage, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
