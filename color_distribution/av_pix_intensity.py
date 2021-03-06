import shutil
import sys
import os
import random
import math
from tqdm import tqdm
import cv2
import numpy as np
from matplotlib import pyplot as plt

#Each pixel is 3.821 micron (3.821micron/pixel), the particle sie is -180 +44 micron or -47 +12 pixels

DIR_PATH = '/home/labuser/Documents/Computer_vision/color_distribution/'
KERNEL_SIZE = 8
AV_PARTICLE_SIZE_IN_PIXELS = math.floor(((63*0.175/3.821)+((180+125)/2*0.525/3.821))) #63 micron is the average particle size of the angular WC that made up 17.5% of the sample
#The particle size range for spherical WC is 125-180 micron making up 52.5% of the sample
LINE_LENGTH = math.floor(AV_PARTICLE_SIZE_IN_PIXELS*(1/2))

file_ids = next(os.walk(DIR_PATH))[2]

for ids_ in tqdm(enumerate(file_ids), total=len(file_ids)):
    ids = ids_[1]

    if ids.endswith('.jpg') or ids.endswith('.JPG') or ids.endswith('.png') or ids.endswith('.PNG'):
        im_dir = DIR_PATH + ids
        img = cv2.imread(im_dir,1)
        im_len = img.shape[1]
        im_hei = img.shape[0]

        #kernel setup
        hor_tran = math.floor(im_len/KERNEL_SIZE)
        ver_tran = math.floor(im_hei/KERNEL_SIZE)
        av_RGB_int = []
        av_red_int = []
        av_blue_int = []
        av_green_int = []
        sum_RGB = []

        #Horizontal Line setup
        hor_line = math.floor(im_len/LINE_LENGTH)
        av_RGB_hor_line = []
        av_red_hor_line = []
        av_blue_hor_line = []
        av_green_hor_line = []
        sum_RGB_hor_line = []

        #Verticle line setup
        ver_line = math.floor(im_hei/LINE_LENGTH)
        av_RGB_ver_line = []
        av_red_ver_line = []
        av_blue_ver_line = []
        av_green_ver_line = []
        sum_RGB_ver_line = []        

        for hor_stride in range(hor_tran):
            for ver_stride in range(ver_tran):
                kern_im = img[ver_stride*KERNEL_SIZE:(ver_stride + 1)*KERNEL_SIZE, hor_stride*KERNEL_SIZE:(hor_stride+1)*KERNEL_SIZE,:]
                # print(kern_im, kern_im.shape)
                av_pix_int = np.mean(kern_im,axis=tuple(range(kern_im.ndim-1)))
                av_red_int.append(av_pix_int[0])
                av_green_int.append(av_pix_int[1])
                av_blue_int.append(av_pix_int[2])
                av_RGB_int.append(np.mean(kern_im))
                sum_RGB.append(np.sum(kern_im))
                # print(kern_im, np.sum(kern_im))
                # print(av_pix_int, av_red_int, av_green_int, av_blue_int, av_RGB_int)
        
        #Horizontal line
        for hor_lin_ver_str in range(im_hei):
            for hor_line_str in range(hor_line):
                hor_line_im = img[hor_lin_ver_str,hor_line_str*LINE_LENGTH:(hor_line_str+1)*LINE_LENGTH,:]
                hor_line_av_pix_int = np.mean(hor_line_im,axis=tuple(range(hor_line_im.ndim-1)))
                av_red_hor_line.append(hor_line_av_pix_int[0])
                av_green_hor_line.append(hor_line_av_pix_int[1])
                av_blue_hor_line.append(hor_line_av_pix_int[2])
                av_RGB_hor_line.append(np.mean(hor_line_av_pix_int))
                sum_RGB_hor_line.append(np.sum(hor_line_im))

        #Verticle line
        for ver_lin_ver_str in range(im_len):
            for ver_line_str in range(ver_line):
                ver_line_im = img[ver_line_str*LINE_LENGTH:(ver_line_str+1)*LINE_LENGTH,ver_lin_ver_str,:]
                ver_line_av_pix_int = np.mean(ver_line_im,axis=tuple(range(ver_line_im.ndim-1)))
                av_red_ver_line.append(ver_line_av_pix_int[0])
                av_green_ver_line.append(ver_line_av_pix_int[1])
                av_blue_ver_line.append(ver_line_av_pix_int[2])
                av_RGB_ver_line.append(np.mean(ver_line_av_pix_int))
                sum_RGB_ver_line.append(np.sum(ver_line_im))

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
        plt.hist(av_RGB_int,bins=128)
        plt.xlim([0,256])
        plt.xlabel('Pixel_Value')
        plt.ylabel('Count')
        plt.title('Average Pixel Distribution for RGB Channels using' + str(KERNEL_SIZE) + 'x' + str(KERNEL_SIZE) + 'Kernel')
        plt.gcf()
        plt.savefig(KERNEL_DIR + 'pixel_distribution.png', dpi=600)
        plt.close()

        plt.hist(av_RGB_int,bins=128)
        plt.xlim([0,256])
        plt.xlabel('Pixel_Value')
        plt.ylabel('Count')
        plt.title('Average Pixel Distribution for RGB Channels using' + str(KERNEL_SIZE) + 'x' + str(KERNEL_SIZE) + 'Kernel')
        plt.gcf()
        plt.savefig(KERNEL_DIR + 'average_RGB_pix_intensity.png')
        plt.close()       

        plt.hist(sum_RGB,bins=384)
        plt.xlim([0,768])
        plt.xlabel('Pixel_Value')
        plt.ylabel('Count')
        plt.title('Sum of the Pixel Values for RGB Channels using' + str(KERNEL_SIZE) + 'x' + str(KERNEL_SIZE) + 'Kernel')
        plt.gcf()
        plt.savefig(KERNEL_DIR + 'Sum_RGB_pix_intensity.png')
        plt.close()  

        plt.subplot(221)
        plt.hist(av_red_hor_line, bins=128)
        plt.xlabel('Pixel_Value')
        plt.ylabel('Count')
        plt.xlim([0,256])
        plt.title('Average Pixel Distribution for Red Channel using' + str(LINE_LENGTH) + 'Length Line')
        plt.subplot(222)
        plt.hist(av_green_hor_line, bins=128)
        plt.xlabel('Pixel_Value')
        plt.ylabel('Count')
        plt.xlim([0,256])
        plt.title('Average Pixel Distribution for Green Channel using' +  str(LINE_LENGTH) + 'Length Line')
        plt.subplot(223)
        plt.hist(av_blue_hor_line,bins=128)
        plt.xlabel('Pixel_Value')
        plt.ylabel('Count')
        plt.xlim([0,256])
        plt.title('Average Pixel Distribution for Blue Channel using' + str(LINE_LENGTH) + 'Length Line')
        plt.subplot(224)
        plt.hist(av_RGB_hor_line,bins=128)
        plt.xlim([0,256])
        plt.xlabel('Pixel_Value')
        plt.ylabel('Count')
        plt.title('Average Pixel Distribution for RGB Channels using' + str(LINE_LENGTH) + 'Length Line')
        plt.gcf()
        plt.savefig(KERNEL_DIR + 'pixel_distribution_hor_line.png', dpi=600)
        plt.close()

        # plt.hist(av_RGB_int,bins=128)
        # plt.xlim([0,256])
        # plt.xlabel('Pixel_Value')
        # plt.ylabel('Count')
        # plt.title('Average Pixel Distribution for RGB Channels using' + str(KERNEL_SIZE) + 'x' + str(KERNEL_SIZE) + 'Kernel')
        # plt.savefig(KERNEL_DIR + 'average_RGB_pix_intensity.png')
        # plt.show()       

        plt.hist(sum_RGB_hor_line,bins=384)
        plt.xlim([0,768])
        plt.xlabel('Pixel_Value')
        plt.ylabel('Count')
        plt.title('Sum of the Pixel Values for RGB Channels using' + str(LINE_LENGTH) + 'Length Line')
        plt.gcf()
        plt.savefig(KERNEL_DIR + 'Sum_RGB_pix_intensity_hor_line.png')
        plt.close()  

        plt.subplot(221)
        plt.hist(av_red_ver_line, bins=128)
        plt.xlabel('Pixel_Value')
        plt.ylabel('Count')
        plt.xlim([0,256])
        plt.title('Average Pixel Distribution for Red Channel using' + str(LINE_LENGTH) + 'Length Line')
        plt.subplot(222)
        plt.hist(av_green_ver_line, bins=128)
        plt.xlabel('Pixel_Value')
        plt.ylabel('Count')
        plt.xlim([0,256])
        plt.title('Average Pixel Distribution for Green Channel using' +  str(LINE_LENGTH) + 'Length Line')
        plt.subplot(223)
        plt.hist(av_blue_ver_line,bins=128)
        plt.xlabel('Pixel_Value')
        plt.ylabel('Count')
        plt.xlim([0,256])
        plt.title('Average Pixel Distribution for Blue Channel using' + str(LINE_LENGTH) + 'Length Line')
        plt.subplot(224)
        plt.hist(av_RGB_ver_line,bins=128)
        plt.xlim([0,256])
        plt.xlabel('Pixel_Value')
        plt.ylabel('Count')
        plt.title('Average Pixel Distribution for RGB Channels using' + str(LINE_LENGTH) + 'Length Line')
        plt.gcf()
        plt.savefig(KERNEL_DIR + 'pixel_distribution_ver_line.png', dpi=600)
        plt.close()

        # plt.hist(av_RGB_int,bins=128)
        # plt.xlim([0,256])
        # plt.xlabel('Pixel_Value')
        # plt.ylabel('Count')
        # plt.title('Average Pixel Distribution for RGB Channels using' + str(KERNEL_SIZE) + 'x' + str(KERNEL_SIZE) + 'Kernel')
        # plt.savefig(KERNEL_DIR + 'average_RGB_pix_intensity.png')
        # plt.show()       

        plt.hist(sum_RGB_ver_line,bins=384)
        plt.xlim([0,768])
        plt.xlabel('Pixel_Value')
        plt.ylabel('Count')
        plt.title('Sum of the Pixel Values for RGB Channels using' + str(LINE_LENGTH) + 'Length Line')
        plt.gcf()
        plt.savefig(KERNEL_DIR + 'Sum_RGB_pix_intensity_ver_line.png')
        plt.close() 