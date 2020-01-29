import shutil
import sys
import os
import random
from tqdm import tqdm

TRAIN_PATH="/content/drive/My Drive/Computer_Vision_Dataset/unzipped/dataset/val/"
image_dir=TRAIN_PATH + "crops/"

train_ids = next(os.walk(TRAIN_PATH))[1]

for ids_ in tqdm(enumerate(train_ids), total=len(train_ids)):
    
    ids=ids_[1]
    new_dir = '/content/drive/My Drive/Computer_Vision_Dataset/unzipped/dataset/val_axondeepseg/'
    FOLDER_PATH = TRAIN_PATH + ids + '/'
    folder_id = next(os.walk(FOLDER_PATH))[2]
    mask_dir=TRAIN_PATH + ids + '/' + "mask/"
    mask_id = next(os.walk(mask_dir))[2]
    for image_ids_ in tqdm(enumerate(folder_id), total=len(folder_id)):
        im_id = image_ids_[1]
        
        if im_id.endswith(".PNG") and os.path.isfile(new_dir + im_id) is False:
            
            shutil.copyfile(FOLDER_PATH+im_id,new_dir+im_id)
    for mask_ids_ in tqdm(enumerate(mask_id), total=len(mask_id)):
        mask_id = mask_ids_[1]
        
        if mask_id.endswith(".jpg") and os.path.isfile(new_dir + mask_id) is False:
            
            shutil.copyfile(mask_dir+mask_id,new_dir+mask_id)