import sys
import argparse
import cv2

count = 0
vidcap = cv2.VideoCapture('/mnt/mars-beta/tochukwu/maestro/maestro_code/Endo_video/Endoscope-Video.avi')
success,image = vidcap.read()
success = True
while success:
    vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))    # added this line 
    success,image = vidcap.read()
    print ('Read a new frame: ', success)
    cv2.imwrite("/mnt/mars-beta/tochukwu/maestro/maestro_code/newframe2/frame%d.jpg" % count, image)     # save frame as JPEG file
    count = count + 1