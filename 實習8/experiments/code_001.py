import cv2
import numpy as np
from matplotlib import pyplot as plt

def Scale(src):
  H, W, C = src.shape
  N_Image = cv2.resize(src, (H//2, W//2), interpolation=cv2.INTER_NEAREST)
  L_Image = cv2.resize(src, (H//2, W//2), interpolation=cv2.INTER_LINEAR)
  C_Image = cv2.resize(src, (H//2, W//2), interpolation=cv2.INTER_CUBIC)
  return N_Image, L_Image, C_Image

def Rotation(src):
  H, W, C = src.shape
  M_rotation = cv2.getRotationMatrix2D([(H-1)/2, (W-1)/2], 45, 1)
  rotationImage = cv2.warpAffine(src, M_rotation, (H, W))
  return rotationImage

def Affine(src):
  H, W, C = src.shape
  pts1 = np.array([[160, 165], [240, 390], [270, 125]], dtype=np.float32) 
  pts2 = np.array([[190, 140], [190, 375], [310, 140]], dtype=np.float32)
  M_affine = cv2.getAffineTransform(pts1, pts2)
  affineImage = cv2.warpAffine(src, M_affine, (H, W))
  return affineImage


def Perspective(src):
  pts1 = np.array([[795, 350], [795, 690], [1090, 720], [1090, 250]], dtype=np.float32) 
  pts2 = np.array([[0, 0], [0, 500], [650, 500], [650, 0]], dtype=np.float32)
  M = cv2.getPerspectiveTransform(pts1, pts2)
  perspectiveImage = cv2.warpPerspective(src, M, (650, 500))
  return perspectiveImage
  

image = cv2.imread('./Baboon.bmp')
N_Image, L_Image, C_Image = Scale(image)

image = cv2.imread('./Baboon.bmp')
rotationImage = Rotation(image)

image = cv2.imread('./Poker.bmp')
affineImage = Affine(image)

image = cv2.imread('./Gallery.bmp')
perspectiveImage = Perspective(image)


images = [N_Image, L_Image, C_Image, rotationImage, affineImage, perspectiveImage]
titles = ['NEAREST', 'LINEAR', 'CUBIC', 'ROTATION', 'AFFINE', 'PERSPECTIVE']

plt.figure() 
for i in range(len(images)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i][..., ::-1])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()


