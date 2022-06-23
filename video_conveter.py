import sys
import argparse
import cv2

count = 0
vidcap = cv2.VideoCapture('/mnt/mars-beta/tochukwu/maestro/maestro_code/newData/eyetracker/world.mp4')
success,image = vidcap.read()
success = True
while success:
    vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000)) # added this line 
    success,image = vidcap.read()
    print ('Read a new frame: ', success)
    cv2.imwrite("/mnt/mars-beta/tochukwu/maestro/maestro_code/BodycamImage/frame%d.jpg" % count, image) # save frame as JPEG file
    count = count + 1