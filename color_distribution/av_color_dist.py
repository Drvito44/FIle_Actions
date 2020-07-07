import shutil
import sys
import os
import random
import math
from tqdm import tqdm
import cv2
import numpy as np
from matplotlib import pyplot as plt


DIR_PATH = '/home/dylan/Documents/Computer_vision/color_distribution/'
KERNEL_SIZE = 10

file_ids = next(os.walk(DIR_PATH))[2]

for ids_ in tqdm(enumerate(file_ids), total=len(file_ids)):
    ids = ids_[1]

    if ids.endswith('.jpg') or ids.endswith('.JPG') or ids.endswith('.png') or ids.endswith('.PNG'):
        im_dir = DIR_PATH + ids
        img = cv2.imread(im_dir,1)
        im_len = img.shape[1]
        im_hei = img.shape[0]
        hor_tran = math.floor(im_len/KERNEL_SIZE)
        ver_tran = math.floor(im_hei/KERNEL_SIZE)
        # print(hor_tran, ver_tran)
        av_RGB_int = []
        av_red_int = []
        av_blue_int = []
        av_green_int = []

        for hor_stride in range(hor_tran):
            for ver_stride in range(ver_tran):
                kern_im = img[ver_stride*KERNEL_SIZE:(ver_stride + 1)*KERNEL_SIZE, hor_stride*KERNEL_SIZE:(hor_stride+1)*KERNEL_SIZE,:]
                # print(kern_im, kern_im.shape)
                av_pix_int = np.mean(kern_im,axis=tuple(range(kern_im.ndim-1)))
                av_red_int.append(av_pix_int[0])
                av_green_int.append(av_pix_int[1])
                av_blue_int.append(av_pix_int[2])
                av_RGB_int.append(np.mean(kern_im))
                # print(av_pix_int, av_red_int, av_green_int, av_blue_int, av_RGB_int)
        im_id = ids.split('.')[0]    
        PLOT_DIR = DIR_PATH + 'plots/' + im_id + '/'
        KERNEL_DIR = PLOT_DIR + im_id + '_kernel_size_' + str(KERNEL_SIZE) + '/'
        if  os.path.isdir(KERNEL_DIR) is False:
            os.makedirs(KERNEL_DIR)
        plt.subplot(221)
        plt.hist(av_red_int, bins=128)
        plt.xlabel('Pixel_Value')
        plt.ylabel('Count')
        plt.xlim([0,256])
        plt.title('Average Pixel Distribution for Red Channel using' + str(KERNEL_SIZE) + 'x' + str(KERNEL_SIZE) + 'Kernel')
        plt.subplot(222)
        plt.hist(av_green_int, bins=128)
        plt.xlabel('Pixel_Value')
        plt.ylabel('Count')
        plt.xlim([0,256])
        plt.title('Average Pixel Distribution for Green Channel using' + str(KERNEL_SIZE) + 'x'+ str(KERNEL_SIZE) + 'Kernel')
        plt.subplot(223)
        plt.hist(av_blue_int,bins=128)
        plt.xlabel('Pixel_Value')
        plt.ylabel('Count')
        plt.xlim([0,256])
        plt.title('Average Pixel Distribution for Blue Channel using' + str(KERNEL_SIZE) + 'x '+ str(KERNEL_SIZE) + 'Kernel')
        plt.subplot(224)
        plt.plot(av_red_int,'r', label='Red_dist')
        plt.plot(av_green_int, 'b--', label='Green_dist')
        plt.plot(av_blue_int, 'g:', label='Blue_dist')
        plt.legend()
        plt.xlim([0,256])
        plt.xlabel('Pixel_Value')
        plt.ylabel('Count')
        plt.title('Average Pixel Distribution for All Channels using' + str(KERNEL_SIZE) + 'x '+ str(KERNEL_SIZE) + 'Kernel')
        plt.savefig(KERNEL_DIR + 'pixel_distribution.png', dpi=600)
        plt.show()

        plt.hist(av_RGB_int,bins=128)
        plt.xlim([0,256])
        plt.xlabel('Pixel_Value')
        plt.ylabel('Count')
        plt.title('Average Pixel Distribution for RGB Channels using' + str(KERNEL_SIZE) + 'x' + str(KERNEL_SIZE) + 'Kernel')
        plt.savefig(KERNEL_DIR + 'average_RGB_pix_intensity.png')
        plt.show()        



       
              




