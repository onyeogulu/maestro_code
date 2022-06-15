import json
import os
import shutil

anno_file  = os.path.join('Videotoframes.json')

with open(anno_file,'r') as fff:
    final_annots = json.load(fff)

for frame_name in final_annots['frames']:
    if len(final_annots['frames'][frame_name])>0:
        shutil.copyfile("input_folder/"+frame_name, "images/"+frame_name)
    


