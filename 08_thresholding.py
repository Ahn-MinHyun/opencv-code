import cv2

# 이미지 색구분하여 똑같이 맞춰 선명하게 만들기
src = cv2.imread('data/images/threshold.png',0)

#파라미터
thresh = 0 # 변경을 위한 기준 값 설정
maxValue = 255 # 위에서 설정한 값보다 큰 값의 변경 값 

# 원본파일에서 숫자들이 너무 어두운 색이여서 보이지 않았을때 
# 색을 모두바꿔준다.
cv2.imshow("Origianl",src)

th,dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY)

cv2.imshow("Thresholded Image", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()