import shutil
import sys
import os
import random
from tqdm import tqdm

import numpy as np
import cv2


from skimage.io import imread, imshow, imread_collection, concatenate_images
from skimage.transform import resize

TRAIN_PATH='/content/drive/My Drive/Computer_Vision_Dataset/unzipped/dataset/train_axondeepseg/'

train_ids = next(os.walk(TRAIN_PATH))[2]

file_ids = next(os.walk(TRAIN_PATH))[2]
for txt_file in file_ids:
  if txt_file.endswith('.txt'):
    txt_id = txt_file
ii=0
jj=0
for ids_ in tqdm(enumerate(train_ids), total=len(train_ids)):
  
  
    
    if ids_[1].endswith('.xml'):
      ids = ids_[1].split(".")[0]
    else:
      ids=ids_[1]
    
    if ids.endswith(".PNG"):
      im = cv2.imread(TRAIN_PATH+ids)
      print(ids,im.shape)
      new_dir = '/content/drive/My Drive/Computer_Vision_Dataset/unzipped/dataset/axon_dataset/data/Train/' + 'image_' + str(ii) + '.png'
      #im_array = np.zeros(im.shape[0],im.shape[1],3)
      # im_array = im[:,:,3]
      cv2.imwrite(new_dir,im)
      ii = ii + 1