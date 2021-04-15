import cv2
import numpy as np

source = cv2.imread('data/images/sample.jpg',1)

#파라미터 
center = (source.shape[1]/2,source.shape[0]/2)# 회전의 중심좌표
rotationAngle =90 #회전각도
scaleFactor = 1 #크기

rotationMatrix = cv2.getRotationMatrix2D(center, rotationAngle, scaleFactor)

print(rotationMatrix) #  6개가 나온다.

result=cv2.warpAffine(source, rotationMatrix,
                (source.shape[1], source.shape[0]))

cv2.imshow("Original",source)
cv2.imshow("rotated",result)

cv2.waitKey()
cv2.destroyAllWindows()