#If all files are in one directory 
import shutil
import sys
import os
import random
from tqdm import tqdm

TRAIN_PATH="/home/dylan/Documents/Computer_vision/UNet_Starter/dataset/val2/"
image_dir=TRAIN_PATH + "images/"
mask_dir=TRAIN_PATH + "masks/"
train_ids = next(os.walk(TRAIN_PATH))[2]

for ids_ in tqdm(enumerate(train_ids), total=len(train_ids)):
    
    ids=ids_[1]
    
    if ids.endswith(".PNG"):
        shutil.move(TRAIN_PATH+ids,image_dir)
    if ids.endswith(".json"):
        new_id = ids.split(".")
        file_name = new_id[0]
        shutil.move(TRAIN_PATH+ids,TRAIN_PATH+file_name)
