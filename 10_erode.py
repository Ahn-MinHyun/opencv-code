import cv2


# 경계선 축소
imageName = "data/images/truth.png"

image = cv2.imread(imageName, cv2.IMREAD_COLOR)

cv2.imshow("original",image)

# 이미지 침식
erosionSize = 2
element = cv2.getStructuringElement(cv2.MORPH_RECT, # 어떻게 확장할 것인지?
                        (2*erosionSize+1,2*erosionSize+1), # 얼만큼 확장할 것인지?
                        ) 

imageEroded = cv2.erode(image, element)

cv2.imshow("Erosion",imageEroded)

cv2.waitKey()
cv2.destroyAllWindows()