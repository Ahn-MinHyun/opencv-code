import numpy as np
import argparse
import imutils
import time
import cv2
import os
import matplotlib.pyplot as plts

DEFAULT_FRAME = 1
sv = cv2.VideoCapture('data4/video/dashcam2.mp4')
sample_video_writer = None
cv_enet_model = cv2.dnn.readNet('data4/enet-cityscapes/enet-model.net')
CV_ENET_SHAPE_IMG_COLORS = open('data4/enet-cityscapes/enet-colors.txt').read().split('\n')
# 더미 데이타 제거
CV_ENET_SHAPE_IMG_COLORS = CV_ENET_SHAPE_IMG_COLORS[ : -2+1]
CV_ENET_SHAPE_IMG_COLORS = np.array([np.array(color.split(',')).astype('int')  for color in CV_ENET_SHAPE_IMG_COLORS  ])

# 레이블 이름을 로딩
label_values = open('data4/enet-cityscapes/enet-classes.txt').read().split('\n')
print(label_values)
# 더미 데이타 제거
label_values = label_values[ : -2+1]

# 라벨 가져오기
my_legend = np.zeros( ( len(label_values) * 25 ,  300 , 3  )   , dtype='uint8' )
for ( i, (class_name, img_color)) in enumerate( zip(label_values , CV_ENET_SHAPE_IMG_COLORS)) :
  color_info = [  int(color) for color in img_color  ] 
  cv2.putText(my_legend, class_name, (5, (i*25) + 17) , 
              cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0) , 2 )
  cv2.rectangle(my_legend, (100, (i*25)), (300, (i*25) + 25) , tuple(color_info), -1)


# cv2.imshow('color',mask_class_map)
cv2.imshow('legend', my_legend)


if sv.isOpened() == False :
    print( "Error opening video stream or file" )

else :
    try :
        prop = cv2.cv.CV_CAP_PROP_FRAME_COUNT if imutils.is_cv2() else cv2.CAP_PROP_FRAME_COUNT
        total = sv.get(prop)
        print("[INFO] {} total frames in video.".format(total))
    except :
        print("[INFO] could not determine number of frames in video")
        total = -1

    while True :
        grabbed, frame = sv.read()

        normalize_image = 1 / 255.0
        resize_image_shape = (1024, 512)
        SET_WIDTH = int(600)
        video_frame = imutils.resize(frame, width=SET_WIDTH)
        blob_img = cv2.dnn.blobFromImage(frame, normalize_image, resize_image_shape, 0, 
                                        swapRB = True, crop = False)
        cv_enet_model.setInput(blob_img)
        # 모델이, 세그멘테이션 추론(예측)하는데 얼마나 걸렸는지 측정.
        start_time = time.time()
        cv_enet_model_output = cv_enet_model.forward()
        end_time = time.time()

        (classes_num, height, width) = cv_enet_model_output.shape[1:4]

        class_map = np.argmax(cv_enet_model_output[0], axis=0)

        mask_class_map = CV_ENET_SHAPE_IMG_COLORS[class_map]

        mask_class_map = cv2.resize(mask_class_map, (video_frame.shape[1], video_frame.shape[0]) ,
                    interpolation = cv2.INTER_NEAREST)
        
        cv_enet_model_output = ( (0.5 * video_frame) + (0.5 * mask_class_map) ).astype('uint8')
        combined = np.hstack([video_frame, cv_enet_model_output])

        # 제대로 사진 가져왔으면, 화면에 표시
        if grabbed == True :
            cv2.imshow("Frame", combined)
            print("loading_time", end_time - start_time)            
            # 키보드에서 esc키를 누르면 exit하라는 것
            if cv2.waitKey(25)&0xFF == 27 :
                break

        else :
            break
    sv.release()

cv2.waitKey()
cv2.destroyAllWindows()



