import numpy as np
import cv2
from matplotlib import pyplot as plt
from skimage.io import imshow

img_dir = '/home/dylan/Documents/Unet_trials/breazy_dream/train_img.png'
img_dir2 = '/home/dylan/Documents/Unet_trials/chocolate_valley/train_img.png'


img = cv2.imread(img_dir)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

imshow(thresh)
plt.show()

# noise removal
kernel = np.ones((10,10),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
erosion = cv2.erode(opening,kernel,iterations=1)

plt.subplot(1,2,1)
plt.imshow(opening)
plt.subplot(1,2,2)
plt.imshow(erosion)
plt.show()

# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)

# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,3)
ret, sure_fg = cv2.threshold(dist_transform,0.4*dist_transform.max(),255,0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)
plt.subplot(2,2,1)
plt.imshow(sure_bg)
plt.subplot(2,2,2)
plt.imshow(dist_transform)
plt.subplot(2,2,3)
plt.imshow(sure_fg)
plt.subplot(2,2,4)
plt.imshow(unknown)
plt.show()

plt.subplot(1,2,1)
plt.imshow(img)
plt.subplot(1,2,2)
plt.imshow(dist_transform)
plt.show()

# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)

# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

# Now, mark the region of unknown with zero
markers[unknown==255] = 0

markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]
