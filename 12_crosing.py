import cv2
# 이미지 경계선 침식 후 확장 하여 작은 점을 제거할 수 있다.


imageName = "data/images/closing.png"

image = cv2.imread(imageName, 0)

cv2.imshow("original",image)

# 이미지 침식
closingSize = 3
element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, # 어떻게 확장할 것인지?
                        (2*closingSize+1,2*closingSize+1), # 얼만큼 확장할 것인지?
                        ) 

# 침식한 만큼 확장해주는 
imageclosed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, 
                            element, iterations= 4)# iterations 몇번 반복할 껀지 

cv2.imshow("closed",imageclosed)

cv2.waitKey()
cv2.destroyAllWindows()