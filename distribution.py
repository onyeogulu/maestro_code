import json
import os
import pandas as pd
""" 
This python script provides the distrubution of the different classes of the annotated 
data set in the Videotoframes.json file.
"""
def coco_to_yolo():
    inputTags = ["Crocodilegrasper","Yohangrasper","HookDiathermy","Marylandgrasper","Clipper","Scissors","Bagholder","Trocar"]
    anno_file  = os.path.join('./Videotoframes.json')

    with open(anno_file,'r') as fff:
        final_annots = json.load(fff)
    mycount = []
    for frame_name in final_annots['frames']:
        if len(final_annots['frames'][frame_name])>0:
            for item in final_annots['frames'][frame_name]:
                mycount.append(item['tags'][0])
    print("The number of annottation is {}".format(len(mycount)))
    # Count the Number of Occurrences in a Python list using Pandas

    counts = pd.Series(mycount).value_counts()
    print(counts)           
coco_to_yolo()