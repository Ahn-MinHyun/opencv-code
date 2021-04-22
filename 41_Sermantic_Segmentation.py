import numpy as np
import argparse
import imutils
import time
import cv2
import os
import matplotlib.pyplot as plt

SET_WIDTH = int(600)
normalize_image = 1 / 255.0
resize_image_shape = (1024, 512)
sample_img = cv2.imread('data4/images/example_04.png')

print(sample_img.shape)
sample_img = imutils.resize(sample_img, width=SET_WIDTH)
# opencv 의 pre trained model 을 통해서, 예측하기 위해서는
# (opencv의 DNN라이브러리를 이용하기 위해서)
# 입력이미지를 blob 으로 바꿔줘야 한다.
blob_img = cv2.dnn.blobFromImage(sample_img, normalize_image, 
                                resize_image_shape, 0, 
                                swapRB = True, crop=False)
# Enet 모델 가져오기.
cv_enet_model = cv2.dnn.readNet('data4/enet-cityscapes/enet-model.net')
print( cv_enet_model)

# blob된 이미지를 모델에 맞게 세팅해주는 함수 
cv_enet_model.setInput(blob_img)

# 클라스의 갯수 많큼 아웃풋이 나온다. 
cv_enet_model_output = cv_enet_model.forward()

# 1 : 1개의 이미지를 넣었으므로
# 20 : 클래스의 갯수
# 512 : 행렬의 행의 갯수
# 1024 : 행렬의 열의 갯수
print(cv_enet_model_output.shape)

# 레이블 이름을 로딩
label_values = open('data4/enet-cityscapes/enet-classes.txt').read().split('\n')
print(label_values)
# 더미 데이타 제거
label_values = label_values[ : -2+1]

# 원래의 모양인 (1, 20, 512, 1024) 에 있는 값을, 변수로 저장.
# 20은 클래스의 갯수, 512는 높이 1024는 너비로 저장.
IMG_OUTPUT_SHAPE_START = 1 
IMG_OUTPUT_SHAPE_END = 4
classes_num, h, w = cv_enet_model_output.shape[IMG_OUTPUT_SHAPE_START : IMG_OUTPUT_SHAPE_END]

# 중요 2 모델의 아웃풋 20개 행렬을 하나의 행렬로 만든다.(1장에서 비교할 곳은 (20,514,1024)중 20이니깐 
class_map = np.argmax(cv_enet_model_output[0], axis = 0)

# 색정보를 로딩
CV_ENET_SHAPE_IMG_COLORS = open('data4/enet-cityscapes/enet-colors.txt').read().split('\n')
# 더미 데이타 제거
CV_ENET_SHAPE_IMG_COLORS = CV_ENET_SHAPE_IMG_COLORS[ : -2+1]
CV_ENET_SHAPE_IMG_COLORS = np.array([np.array(color.split(',')).astype('int')  for color in CV_ENET_SHAPE_IMG_COLORS  ])

## 중요 3 하나의 행렬을 => 이미지로 만든다.
# 각 픽셀별로, 클래스에 해당하는 숫자가 적힌 class_map을
# 각 숫자에 매핑되는 색깔로 셋팅해 준것이다.
# 따라서 각 픽셀별 색깔 정보가 들어가게 되었다.
# 2차원 행렬을, 3차원 채널이 있는 RGB 행렬로 만든다.
mask_class_map = CV_ENET_SHAPE_IMG_COLORS[class_map]

# 리사이즈 한다.
# 인터폴레이션을 INTER_NEAREST 로 한 이유는?? 
# 레이블 정보(0~19) 와 컬러정보 (23,100,243) 는 둘다 int 이므로, 
# 가장 가까운 픽셀 정보와 동일하게 셋팅해주기 위해서.
mask_class_map = cv2.resize(mask_class_map, (sample_img.shape[1], sample_img.shape[0]) , 
           interpolation = cv2.INTER_NEAREST )
class_map = cv2.resize(class_map, (sample_img.shape[1], sample_img.shape[0]) , 
                       interpolation=cv2.INTER_NEAREST)

# 원본이미지랑, 색마스크 이미지를 합쳐서 보여준다.
# 가중치 비율을 줘서 보여준다. ()
cv_enet_model_output = ( ( 0.6 * sample_img ) + (0.4 * mask_class_map) ).astype('uint8')

# 라벨 가져오기
my_legend = np.zeros( ( len(label_values) * 25 ,  300 , 3  )   , dtype='uint8' )
for ( i, (class_name, img_color)) in enumerate( zip(label_values , CV_ENET_SHAPE_IMG_COLORS)) :
  color_info = [  int(color) for color in img_color  ] 
  cv2.putText(my_legend, class_name, (5, (i*25) + 17) , 
              cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0) , 2 )
  cv2.rectangle(my_legend, (100, (i*25)), (300, (i*25) + 25) , tuple(color_info), -1)


# cv2.imshow('color',mask_class_map)
cv2.imshow('legend', my_legend)


img_all= np.hstack([sample_img, cv_enet_model_output])
cv2.imshow("combined", img_all)

cv2.waitKey()
cv2.destroyAllWindows()



