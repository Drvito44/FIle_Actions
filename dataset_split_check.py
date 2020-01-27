import os
import random
import sys

import json
import shutil

from skimage.io import imread, imshow, imread_collection, concatenate_images
from skimage.transform import resize
from tqdm import tqdm

import numpy as np 
import matplotlib.pyplot as plt 

#use if your using U_Net dataset
unet_train_dir = '/home/dylan/Documents/Computer_vision/UNet_Starter/dataset/train/'
unet_val_dir = '/home/dylan/Documents/Computer_vision/UNet_Starter/dataset/val/'
train_ids = next(os.walk(unet_train_dir))[1]
val_ids = next(os.walk(unet_val_dir))[1]
train_dataset = {}
val_dataset = {}
train_pixel = {}
val_pixel = {}
train_carbide_count = 0
val_total_carbide_count = 0
total_train_coverage = 0
total_val_coverage = 0

for ids_ in tqdm(enumerate(train_ids), total=len(train_ids)):
    json_dir = unet_train_dir + ids_[1]
    mask_dir = json_dir+ '/' + 'mask/' + ids_[1] + '_mask.jpg'
    file_ids = next(os.walk(json_dir))[2]
    for id in file_ids:
        if id.endswith(".json") and not id.endswith("via_region_data.json"):
            mask_path=json_dir + "/" + id
            id_split = id.split(".")
            id_name = id_split[0]    
            with open(mask_path, "r") as json_file:
                mask_json=json.load(json_file)
            tmp=mask_json['shapes']
            carbide_count = 0
            for shape in mask_json["shapes"]:
                if isinstance(shape['label'], str) is True:
                    carbide_count += 1
                    train_carbide_count +=1
            train_dataset[id_name] = carbide_count
            img = imread(mask_dir)
            mask = np.zeros((img.shape[0],img.shape[1],1),dtype=np.bool)
            img = resize(img,(img.shape[0],img.shape[1],1), mode= 'constant', preserve_range=True)  
            mask = np.maximum(mask,img)
            
            train_pixel_count = np.count_nonzero(mask)
            total_pixel = img.shape[0]*img.shape[1]
            mask_pixel_cover = train_pixel_count / total_pixel
            total_train_coverage += train_pixel_count
            train_pixel[id_name] = mask_pixel_cover 
            carbide_per_train_image = train_carbide_count / len(train_ids)
            pixel_per_train_image = total_train_coverage / len(train_ids)
            pixel_percent_train = pixel_per_train_image/(total_pixel)
            print(carbide_per_train_image,pixel_per_train_image, pixel_percent_train)
            
for ids_ in tqdm(enumerate(val_ids), total=len(val_ids)):
    val_json_dir = unet_val_dir + ids_[1]
    val_mask_dir = val_json_dir+ '/' + 'mask/' + ids_[1] + '_mask.jpg'
    val_file_ids = next(os.walk(val_json_dir))[2]
    for val_id in val_file_ids:
        if val_id.endswith(".json") and not val_id.endswith("via_region_data.json"):
            val_mask_path=val_json_dir + "/" + val_id
            val_id_split = val_id.split(".")
            val_id_name = val_id_split[0]    
            with open(val_mask_path, "r") as val_json_file:
                val_mask_json=json.load(val_json_file)
            tmp=val_mask_json['shapes']
            val_carbide_count = 0
            for shape in val_mask_json["shapes"]:
                if isinstance(shape['label'], str) is True:
                    val_carbide_count += 1
                    val_total_carbide_count +=1
            val_dataset[val_id_name] = val_carbide_count
            val_img = imread(val_mask_dir)
            val_mask = np.zeros((val_img.shape[0],val_img.shape[1],1),dtype=np.bool)
            val_img = resize(val_img,(val_img.shape[0],val_img.shape[1],1), mode= 'constant', preserve_range=True)  
            val_mask = np.maximum(val_mask,val_img)
            
            val_pixel_count = np.count_nonzero(val_mask)
            val_total_pixel = val_img.shape[0]*val_img.shape[1]
            val_mask_pixel_cover = val_pixel_count / val_total_pixel
            total_val_coverage += val_pixel_count
            val_pixel[val_id_name] = val_mask_pixel_cover     
            carbide_per_val_image = val_total_carbide_count / len(val_ids)
            pixel_per_val_image = total_val_coverage / len(val_ids)
            pixel_percent_val = pixel_per_val_image / val_total_pixel
            print(carbide_per_val_image,pixel_per_val_image, pixel_percent_val)            
        