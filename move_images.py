#If all files are in one directory 
import shutil
import sys
import os
import random
from tqdm import tqdm

TRAIN_PATH="C:/Users/drose/Documents/Thesis/Computer_Vision/dataset_AWS/PTA-AM/"
image_dir=TRAIN_PATH + "crops/"
mask_dir=TRAIN_PATH + "masks/"
train_ids = next(os.walk(TRAIN_PATH))[1]

if os.path.isdir(image_dir) is False:
    os.mkdir(image_dir)

for ids_ in tqdm(enumerate(train_ids), total=len(train_ids)):
    
    ids=ids_[1]
    FOLDER_PATH = TRAIN_PATH + ids + '/'
    folder_id = next(os.walk(FOLDER_PATH))[2]

    for image_ids_ in tqdm(enumerate(folder_id), total=len(folder_id)):
        im_id = image_ids_[1]
        
        if im_id.endswith(".jpg") and os.path.isfile(image_dir + im_id) is False:
            print (im_id)
            shutil.copyfile(FOLDER_PATH+im_id,image_dir+im_id)
        