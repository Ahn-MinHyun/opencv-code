import cv2
import numpy as np

# 칼라이미지
image_color = cv2.imread('data2/image.jpg')
# cv2.imshow('ori',image_color)

# 그레이 스케일
image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray',image_gray)

# 이미지 카피
image_copy = image_gray.copy()

# 값이 195 미만인 것들은 0으로 셋팅.
image_copy[ image_copy[ : , :] <195 ] = 0
# cv2.imshow('copy',image_copy)

image = cv2.imread('data2/test_image.jpg')
print('Height = ', int(image.shape[0]),'pixels')
print('Width = ', int(image.shape[1]), 'pixels')
# cv2.imshow('self Driving car',image)

gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('SDC Gray',gray_img)

# HSV 칼라 스페이스로 변경  
hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
# cv2.imshow('HSV', hsv_image)

# Hue 채널만 표시!
H, S, V = cv2.split(hsv_image) # H = hsv_image[ : , : , 0 ]
# cv2.imshow( "Hue", H )

# 이미지 커널
sharp_kenel_1 = np.array( [ 
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])
sharpend_img_1 = cv2.filter2D(gray_img,-1, sharp_kenel_1)
# cv2.imshow('Gray',gray_img)
# cv2.imshow('Sharpen',sharpend_img_1)
sharp_kenel_2 = np.array( [ 
    [0,-1,0],
    [-1,11,-1],
    [0,-1,0]
])
sharpend_img_2 = cv2.filter2D(gray_img,-1, sharp_kenel_2)
# cv2.imshow('Sharpen',sharpend_img_2)

# 블러링
blur_img = cv2.GaussianBlur(gray_img, (5,5), 1)
# cv2.imshow("blur", blur_img)

# Sobel 이용한 edge detection
x_sobel = cv2.Sobel(gray_img, cv2.CV_64F, 0,1, ksize = 7)
# cv2.imshow("sobel x",x_sobel)
y_sobel = cv2.Sobel(gray_img, cv2.CV_64F,1,0, ksize = 7)
# cv2.imshow("sobel y",y_sobel)

# 라플라시안은 한번에 수직수평을 다 잡는다.
laplacian = cv2.Laplacian(gray_img, cv2.CV_64F)
# cv2.imshow('lapl', laplacian)

# Canny edge detection
threshold_1 = 100
threshold_2 = 200
canny_img = cv2.Canny(gray_img, threshold_1, threshold_2)
# cv2.imshow('canny',canny_img)

# transformation
image = cv2.imread('data2/test_image2.jpg')
cv2.imshow('ori',image)
print(image.shape)
M_rotation = cv2.getRotationMatrix2D( (image.shape[1]/2, image.shape[0]/2 ), 90, 0.5 )
rotation_img= cv2.warpAffine(image, M_rotation, (image.shape[1], image.shape[0]))
# cv2.imshow('rotated',rotation_img)

# translation
image = cv2.imread('data2/test_image3.jpg')
cv2.imshow('ori', image)
height = image.shape[0]
width = image.shape[1]
T_matrix = np.array([
    [1, 0, 120],
    [0,1,-150] ],dtype = 'float32')
print( T_matrix)
translation_image = cv2.warpAffine(image, T_matrix, (width, height))
# cv2.imshow("tran", translation_image)

# Resizing
resized_image= cv2.resize(image, None, fx =0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
cv2.imshow("resized", resized_image)

cv2.waitKey()
cv2.destroyAllWindows()

