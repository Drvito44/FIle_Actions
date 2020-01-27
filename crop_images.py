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

image_dir = 'C:/Users/drose/Documents/Thesis/Computer_Vision/dataset_AWS/PTA-AM/crops/'
im_file = next(os.walk(image_dir))[1]

for ids_ in tqdm(enumerate(im_file), total=len(im_file)):
    print (ids_)

    