import os
import random
import sys
from tqdm import tqdm
import json

mask_dir='/home/dylan/Documents/Computer_vision/aktwelve_Mask_RCNN/datasets/carbide/train/'
train_ids = next(os.walk(mask_dir))[2]

for ids_ in tqdm(enumerate(train_ids), total=len(train_ids)):
    id=ids_[1]
#    if id.endswith("via_region_data.json"):
#        continue
    if id.endswith(".json") and not id.endswith("via_region_data.json"):
        mask_path=mask_dir + id
        with open(mask_path, "r") as json_file:
            mask_json=json.load(json_file)
 #           json_file.close()
        tmp=mask_json['shapes']
        for shape in mask_json["shapes"]:
            if shape['label'] == 'Angular_Carbide':
                print(shape['label'])
 #               shape['label'].replace('Angular_Carbide','Carbide')
                shape['label'] = 'Carbide'
            elif shape['label'] == 'Spherical_Carbide':
 #               shape['label'].replace('Spherical_Carbide','Carbide')
                shape['label'] = 'Carbide'
            elif shape['label'] == 'Degraded_Carbide':
 #               shape['label'].replace('Degraded_Carbide','Carbide')
                shape['label'] = 'Carbide'
        with open(mask_path, "w") as json_file:
            json.dump(mask_json,json_file, indent=4)
#            json_file.close()

