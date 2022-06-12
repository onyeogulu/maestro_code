
import cv2
vidcap = cv2.VideoCapture('world.mp4')
success,image = vidcap.read()
count = 1
skip = 30
success = True
while success:
  if count%skip == 0:
    cv2.imwrite("frames/frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1