import cv2
import numpy as np
from matplotlib import pyplot as plt

def get_kernel(kernel_size=5, kernel_shape='rect'):
    assert kernel_shape in ['rect', 'cross', 'ellipse'], 'The kernel_size must be either rect, cross, or ellipse'
    if kernel_shape == 'rect':
        shape = cv2.MORPH_RECT
    elif kernel_shape == 'cross':
        shape = cv2.MORPH_CROSS
    elif kernel_shape == 'ellipse':
        shape = cv2.MORPH_ELLIPSE
    return cv2.getStructuringElement(shape, (kernel_size, kernel_size))


def morphology(grayimage, kernel_size=5, kernel_shape='rect', operation='open'):
    assert operation in ['open', 'close'], 'The operation must be either open or close.'
    if operation == 'open':
        op = cv2.MORPH_OPEN
    elif operation == 'close':
        op = cv2.MORPH_CLOSE
    kernel = get_kernel(kernel_size, kernel_shape)
    return cv2.morphologyEx(grayimage, op, kernel)


image = cv2.imread('./Number_noise.bmp')
grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
morph_open = morphology(grayimage, operation='open')
morph_close = morphology(grayimage, operation='close')

titles = ['OPEN', 'CLOSE']
images = [morph_open, morph_close]

plt.figure(figsize=(10, 10)) 
for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

