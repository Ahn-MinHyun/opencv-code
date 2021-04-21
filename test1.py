import numpy as np
import cv2

sv = cv2.VideoCapture('data/videos/lane_detection.avi')
if sv.isOpened() == False :
    print( "Error opening video stream or file" )

else :
    frame_width = int(sv.get(3))
    frame_height = int(sv.get(4))
    frame_fps = sv.get(5)
    print("frame_height",frame_height)
    # frame_fps = sv.get()
    print(frame_fps)
