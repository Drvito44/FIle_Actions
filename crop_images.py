import shutil
import sys
import os
import random
import math
import cv2
from tqdm import tqdm

image_folder_path="C:/Users/drose1/Documents/Thesis_Documents/Microscopy/Sample Photos/PTA-AM/114 ( 60A 52.5 HC Stark, 17.5% Scnc070, 30%6040)/"
new_crops_dir='C:/Users/drose1/Documents/Thesis_Documents/Computer_Vision/crops/'

crop_size = 128

if  os.path.isdir(new_crops_dir) is False:
    os.mkdir(new_crops_dir)

im_ids = next(os.walk(image_folder_path))[2]



for ids_ in tqdm(enumerate(im_ids), total=len(im_ids)):
     
    ids = ids_[1]
    img = cv2.imread(image_folder_path + ids)
    im_length = im.shape[0]
    im_height = im.shape[1]
    num_crop_length = math.floor(im_length / crop_size)
    num_crop_height = math.floor(im_height / crop_size)
    
    crop_count = 0

    for crop_count_length in range(num_crop_length):
        for crop_count_height in range(num_crop_height):
            crop_im = img[crop_count_height*crop_size:(crop_count_height + 1)*crop_size, crop_count_length*crop_size:(crop_count_length+1)*crop_size]
            crop_path = new_crops_dir + img.split('.')[0] + '_crop' + str(crop_count) + img.split('.')[1]
            cv2.imwrite(crop_path,crop_im)

    
    
