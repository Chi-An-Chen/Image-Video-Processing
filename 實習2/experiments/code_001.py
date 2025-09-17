import cv2
import numpy as np
from matplotlib import pyplot as plt

def Sobel_edge_detection(grayimage):
    grad_x = cv2.Sobel(grayimage, cv2.CV_32F, 1, 0)  
    grad_y = cv2.Sobel(grayimage, cv2.CV_32F, 0, 1)  
    absX = cv2.convertScaleAbs(grad_x)
    absY = cv2.convertScaleAbs(grad_y)
    sobel = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
    # 對Sobel影像進行細線化
    ret, th = cv2.threshold(sobel, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return sobel, th

def Laplacian_edge_detection(grayimage):
    lapimage = cv2.Laplacian(grayimage, cv2.CV_32F, ksize=3)
    lapimage = cv2.convertScaleAbs(lapimage)
    return lapimage

def HoughLinesDetection(image, grayimage):
    canny = cv2.Canny(grayimage, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(canny, 1, np.pi/180, 150, None, 0, 0)
    lines = np.squeeze(lines)
    for rho, theta in lines:
        a, b = np.cos(theta), np.sin(theta)
        x0, y0 = a * rho, b * rho
        pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
        pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
        cv2.line(image, pt1, pt2, (0, 255, 0), 1)
    return canny, image

image = cv2.imread('./sudoku.jpg')
grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(grayimage.shape)
sobel, th = Sobel_edge_detection(grayimage)
lapimage = Laplacian_edge_detection(grayimage)
edges, hough = HoughLinesDetection(image, grayimage)

titles = ['GRAY', 'SOBEL', 'SOBEL THRESHOLD', 'LAPLACIAN', 'CANNY', 'HOUGH LINE']
images = [grayimage, sobel, th, lapimage, edges, hough]
for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
