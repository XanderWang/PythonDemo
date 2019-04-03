
import os
import sys
import cv2

current_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
video_path = "{0}{1}video{1}my_video.mp4".format(current_dir, os.sep)
print("video_path", video_path)
images_path = "{0}{1}image".format(current_dir, os.sep)
os.makedirs(images_path,exist_ok=True)
vidcap = cv2.VideoCapture(video_path)
success, image = vidcap.read()
count = 0
while success:
  cv2.imwrite("{0}{1}frame_{2}.jpg".format(images_path, os.sep, count), image)     # save frame as JPEG file
  success, image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
