import cv2
import numpy as np

img = cv2.imread('data/images/candle.jpg',1)





# 컬러 스페이스 변경
ycbImage = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

# 가공을 위해서 uint8을 float으로 변경
ycbImage = np.float32(ycbImage)

# 채널 분리
Ychannel, Cr, Cb = cv2.split(ycbImage)

# 밝기 조절
beta = 100
Ychannel = np.clip( Ychannel +beta, 0,255)

# 다시 합치기 
ycbImage = cv2.merge([Ychannel,Cr,Cb])

# 다시 uint8로 변경(정수)
ycbImage = np.uint8(ycbImage)

# 화면 표시를 위해서 컬러 스페이스 BGR로 변경
ycbImage = cv2.cvtColor(ycbImage, cv2.COLOR_YCrCb2BGR)

# 이미지를 각각의 윈도우에 표시한것
cv2.imshow("dst",ycbImage)
cv2.imshow("src",img)

# # 하나의 윈도위에 2개의 이미지를 수평으로 붙임
img_all= np.hstack([img, ycbImage])
cv2.imshow("combined", img_all)

cv2.waitKey()
cv2.destroyAllWindows()