
import cv2
vidcap = cv2.VideoCapture('/mnt/mars-beta/tochukwu/maestro/maestro_code/newData/eyetracker/Endoscope-Video.avi')
success,image = vidcap.read()
count = 1
skip = 10000
success = True
while success:
  if count%skip == 0:
    cv2.imwrite("/mnt/mars-beta/tochukwu/maestro/maestro_code/Videotoframe2/frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1