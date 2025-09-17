import cv2
import numpy as np
from matplotlib import pyplot as plt

def Sobel_edge_detection(grayimage):
    grad_x = cv2.Sobel(grayimage, cv2.CV_32F, 1, 0)  
    grad_y = cv2.Sobel(grayimage, cv2.CV_32F, 0, 1)  
    absX = cv2.convertScaleAbs(grad_x)
    absY = cv2.convertScaleAbs(grad_y)
    return absX, absY
    

def Laplacian_edge_detection(grayimage):
    lapimage = cv2.Laplacian(grayimage, cv2.CV_32F, ksize=3)
    lapimage = cv2.convertScaleAbs(lapimage)
    return lapimage

image = np.array([
    [10,  10,  10,  10, 10, 10],
    [10, 100, 100, 100, 10, 10],
    [10,  10, 100, 100, 10, 10],
    [10,  10, 100, 100, 10, 10],
    [10,  10, 100, 100, 10, 10],
    [10,  10,  10,  10, 10, 10],
    [10,  10,  10,  10, 10, 10],
])
print(image.shape)
image = cv2.convertScaleAbs(image)
absX, absY = Sobel_edge_detection(image)
lapimage = Laplacian_edge_detection(image)
print(absX)
print(absY)
print(lapimage)

"""
(7, 6)
[[  0 180   0 180 180   0]
 [  0 255  90 255 255   0]
 [  0 255 255 255 255   0]
 [  0 255 255 255 255   0]
 [  0 255 255 255 255   0]
 [  0  90  90  90  90   0]
 [  0   0   0   0   0   0]]
[[  0   0   0   0   0   0]
 [  0  90 255 255  90   0]
 [180 180  90   0   0   0]
 [  0   0   0   0   0   0]
 [  0  90 255 255  90   0]
 [  0  90 255 255  90   0]
 [  0   0   0   0   0   0]]
[[255 255 255 255 255   0]
 [  0 255 255 255 180   0]
 [255 255 180 255 255   0]
 [  0 255 255 255 255   0]
 [  0 180 255 255 180   0]
 [  0 180 180 180 180   0]
 [  0   0   0   0   0   0]]
"""
