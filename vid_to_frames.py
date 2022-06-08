
import cv2
vidcap = cv2.VideoCapture('/mnt/mars-beta/tochukwu/maestro/maestro_code/Endo_video/Endoscope-Video2.avi')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("/mnt/mars-beta/tochukwu/maestro/maestro_code/frames/frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1