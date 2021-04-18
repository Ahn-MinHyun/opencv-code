import cv2 
import numpy as np

img = cv2.imread("data/images/saple.jpg",1)

cv2.imshow("color", img)
# 흑백으로 변환했다
gray_iimg = cvw.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray", gray_img)

# 컬러로 변환 (이상하게 나옴)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("hsv", hsv_img)

print(hsv_img)

#hue hsv_img[0]
hsv_img[2] = hsv_img[2] -100

bgr_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
cv2.imshow("BGR_img", bgr_img)

cv2.waitKey()
cv2.destroyAllWindows()
