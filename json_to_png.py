import os
import sys
import random
import PIL
from PIL import Image, ImageDraw
import json
import numpy as np
from tqdm import tqdm
import cv2 as cv
import matplotlib.pyplot as plt
import shutil

mask_dir = '/home/dylan/Documents/Computer_vision/aktwelve_Mask_RCNN/datasets/single_carbide_class/val2/' # Set the directory of the coco formatted json
mask_id = next(os.walk(mask_dir))[2]


for ids_ in tqdm(enumerate(mask_id), total = len(mask_id)):
    id = ids_[1]
    if id.endswith(".json") and not id.endswith("via_region_data.json"):
        mask_path = mask_dir+id
        file_id = id.split(".")
        file_name = file_id[0]
        new_path=mask_dir + "/" + str(file_name) + "/" + "mask/"
        if os.path.isdir(new_path) is True:
            pass
        else:    
            os.makedirs(new_path)
        with open(mask_path,"r") as json_file:
            mask_json = json.load(json_file)
        img=np.zeros((mask_json["imageHeight"],mask_json["imageWidth"],3), np.uint8)
        for shape in mask_json["shapes"]:
            pts=np.array([shape["points"]],np.int32)
            pts = pts.reshape((-1,1,2))
            cv.fillPoly(img,[pts],(255,255,255))
        img=cv.resize(img,(512,512))
        cv.imwrite(new_path + str(file_name) + '_mask.jpg',img)
    if id.endswith('.PNG'):
        file_id = id.split(".")
        file_name = file_id[0]
        current_image_path = mask_dir+id
        new_image_path = mask_dir + str(file_name) + "/" + id
        if os.path.isdir(mask_dir + str(file_name) + "/") is True:
            pass
        else:    
            os.mkdir(mask_dir + str(file_name) + "/")
        shutil.move(current_image_path,new_image_path)

