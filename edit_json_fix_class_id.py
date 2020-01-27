import os
import random
import sys
from tqdm import tqdm
import json

mask_dir ='/home/dylan/Documents/Computer_vision/'
train_ids = next(os.walk(mask_dir))[2]

for ids_ in tqdm(enumerate(train_ids), total=len(train_ids)): # why enumerate? is it possibly used for tqdm?
    id=ids_[1]
    if id.endswith(".json") and not id.endswith("via_region_data.json"): # ... and not id.endswith("via_region_data.json") should work
        mask_path = mask_dir + id # spacing between "...h = m..."
        with open(mask_path, "r") as json_file:
            mask_json = json.load(json_file) # nitpicky, but I would just call it "mask" to avoid confusion or "mask_dict" as it isn't json until you ".dump()"
             
        tmp=mask_json['categories']
        for category in mask_json["categories"]:
            category['id']=category['id']-1
        for annotations in mask_json["annotations"]:
            annotations['category_id']=annotations['category_id']-1
	# these should be indented to lie in the if loop should it be restructured to not use the preceding continue
        with open(mask_path, "w") as json_file:
        # don't need the "+" I don't think as you are not reading
            json.dump(mask_json,json_file, indent=4) # I THINK you can just use "json.dump(mask_json, json_file)"; should use the same patter here as above to be consistent (eg. with open...)
        
