import shutil
import sys
import os
import random
import math
import cv2
from tqdm import tqdm

image_folder_path="/home/dylan/Documents/Computer_vision/UNet_Starter/dataset/mult_val/"
new_crops_dir='/home/dylan/Documents/Computer_vision/UNet_Starter/dataset/crops/'

crop_size = 128

if  os.path.isdir(new_crops_dir) is False:
    os.mkdir(new_crops_dir)

im_ids = next(os.walk(image_folder_path))[2]



for ids_ in tqdm(enumerate(im_ids), total=len(im_ids)):
     
    ids = ids_[1]
    img = cv2.imread(image_folder_path + ids)
    im_length = img.shape[0]
    im_height = img.shape[1]
    num_crop_length = math.floor(im_length / crop_size)
    num_crop_height = math.floor(im_height / crop_size)
    print(num_crop_height,num_crop_length)
    
    total_crops = 0
    crop_count = 0
    for crop_count_length in range(num_crop_length):
        for crop_count_height in range(num_crop_height):
            crop_im = img[crop_count_height*crop_size:(crop_count_height + 1)*crop_size, crop_count_length*crop_size:(crop_count_length+1)*crop_size]
            if ids.endswith('mask.jpg'):               
                crop_path = new_crops_dir + ids.split('_mask')[0] + '_crop' + str(crop_count) + '/' + 'mask/'
                if  os.path.isdir(crop_path) is False:
                    os.makedirs(crop_path) 
                im_dir = crop_path + ids.split('.')[0] + '_crop' + str(crop_count) + '_mask' + '.jpg'
                cv2.imwrite(im_dir,crop_im)
                crop_count = crop_count + 1
                total_crops = total_crops + 1
                
            if ids.endswith('PNG'):               
                crop_path = new_crops_dir + ids.split('.')[0] + '_crop' + str(crop_count) + '/' 
                if  os.path.isdir(crop_path) is False:
                    os.mkdir(crop_path) 
                im_dir = crop_path + ids.split('.')[0] + '_crop' + str(crop_count) + '.PNG'
                cv2.imwrite(im_dir,crop_im)
                crop_count = crop_count + 1
                total_crops = total_crops + 1
        print(crop_count)