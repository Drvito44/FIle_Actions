import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/dylan/Documents/Computer_vision/color_distribution/img_1.jpg',1)
color = ('b','g','r')
for i,col in enumerate(color):  
    histr = cv2.calcHist([img],[2],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
    plt.xlabel('Pixel_Value')
    plt.ylabel('Count')
    plt.ylim(0,100000)
    plt.title('Per Pixel Distribution for Red Channels')
plt.show()