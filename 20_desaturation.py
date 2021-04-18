import cv2
import numpy as np

img = cv2.imread('data/images/capsicum.jpg',1)

cv2.imshow("original", img)

# 필터링 수치
saturationScale = 0.01

hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hsvImage = np.float32(hsvImage)

# 채널로 분리하는 함수.
H, S, V = cv2.split(hsvImage)

# 유용한 함수 cv2.clip 0보다 작으면, 0으로 255보다 크면 255로 맞추는 

np.clip( S * saturationScale, 0, 255)

# 나눈 채널을 하나로 합치는 함수
hsvImage = cv2.merge([H, S, V])

# 웨에서 float으로 작업을 했으므로, 다시 uint8로 변경해줘야한다.
hsvImage = np.uint8(hsvImage)

# BGR로 다시 변경해야, 우리가 눈으로 확인가능
imgBGR = cv2.cvtColor(hsvImage, cv2.COLOR_HSV2BGR)
cv2.imshow("cvt BGR",imgBGR)


cv2.waitKey()
cv2.destroyAllWindows()
