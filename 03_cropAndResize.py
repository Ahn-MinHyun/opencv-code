import cv2

source = cv2.imread("data/images/sample.jpg", 1 )

# Resize
# 숫자의 크기에 따라 확대/축소 가능
# interpolation 축소하거나 확대할 때 생기는 빈 공간 처리
scaleUp = cv2.resize(source, None, fx=1.8, fy=1.8, interpolation = cv2.INTER_LINEAR)


cv2.imshow("Original", source)
cv2.imshow("Scaled Up", scaleUp)

# 내가 원하는 부분의 이미지 가져오기
crop_img = source[ 50:150 , 20:200 ]

cv2.imshow("Croppen Img", crop_img)

cv2.waitKey(0)
cv2.destroyAllWindows()