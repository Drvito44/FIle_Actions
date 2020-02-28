import numpy as np
import cv2
from matplotlib import pyplot as plt

img_dir = '/home/dylan/Documents/Unet_trials/chocolate_valley/train_pred1.png'

img = cv2.imread(img_dir,cv2.IMREAD_GRAYSCALE)
open_kernel = np.ones((2,2), np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, open_kernel, iterations=3)
erosion = cv2.erode(closing,open_kernel,iterations=2)
closing_2 = cv2.morphologyEx(erosion, cv2.MORPH_CLOSE, open_kernel, iterations=5)
dilate = cv2.dilate(closing_2,open_kernel,iterations=5)
kernel = np.ones((2,2),np.uint8)
opening = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel, iterations = 3)
kernel = np.ones((1,1),np.uint8)
opening = cv2.morphologyEx(opening,cv2.MORPH_CLOSE,kernel, iterations = 3)

plt.subplot(2,2,1)
plt.imshow(img)
plt.subplot(2,2,2)
plt.imshow(erosion)
plt.subplot(2,2,3)
plt.imshow(closing_2)
plt.subplot(2,2,4)
plt.imshow(dilate)
plt.show()
plt.imshow(opening)
plt.show()