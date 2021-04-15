import cv2

# 경계선 확장
imageName = "data/images/truth.png"

image = cv2.imread(imageName, cv2.IMREAD_COLOR)

cv2.imshow("original",image)

# 이미지 확장 dilation
dilationSize = 6
element = cv2.getStructuringElement(cv2.MORPH_RECT, # 어떻게 확장할 것인지?
                        (2*dilationSize+1,2*dilationSize+1), # 얼만큼 확장할 것인지?
                        (dilationSize,dilationSize) ) 

imageDilate = cv2.dilate(image, element)

cv2.imshow("Dilation",imageDilate)

cv2.waitKey()
cv2.destroyAllWindows()