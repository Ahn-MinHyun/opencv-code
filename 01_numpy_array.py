import cv2
import numpy as np

imageName = "data/images/sample.jpg"

# open cv로 이미지 열기
image = cv2.imread(imageName, 1)

# 이미지가 정상인지 체크
if image is None:
    print('열수 없다.')

print(image)

print(image.shape)

# Gray Scale Image : 1개의 행렬로 만들고, 0~255 까지의 숫자로 채워진 
# 행렬로 변환한 이미지

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
 
# 이미지를 각각의 윈도우에 표시한것
cv2.imshow("image",image)
cv2.imshow("grayscale", grayImage)

'''
위의 이미지를 화면에 표시하는 코드는
실행되었다가 바로 종료된다.
왜냐하면, 이 파일 자체를 cpu가 실행해서, 끝냈기 때문에
위의 imshow 함수는 바로 종료가 된다. 

따라서, 위의 imshow 함수를 실행시켜서 우리가 눈으로 
화인하기 위해서는 다음처럼 코드 작성
'''


# # 하나의 윈도위에 2개의 이미지를 수평으로 붙임 수직 = vstack
# img_all= np.hstack([image, grayImage])
# cv2.imshow("combined", img_all)


cv2.waitKey(0)
cv2.destroyAllWindows()

