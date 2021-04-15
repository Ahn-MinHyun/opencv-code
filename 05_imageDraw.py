import cv2
import numpy as np
image = cv2.imread("data/images/sample.jpg")

cv2.imshow("img", image)


# 선 그리기
imageLine = image.copy()
#                  선의 시작   선의 끝점    색깔       두께 
cv2.line(imageLine,(322,179),(400,183), (0,0,255),thickness =2, lineType=cv2.LINE_AA)

cv2.imshow("imageLine",imageLine)

# 원 그리기 
imageCircle = image.copy()
#                      원의 중심  반지름  색깔      두께                 
cv2.circle(imageCircle,(350,200),150,(255,0,0),thickness = 3)

cv2.imshow("imageCircle",imageCircle)

# 타원 그리기
imageEllipse = image.copy()
                        #  타원중심                        색깔
cv2.ellipse(imageEllipse,(360,200),(100,170),45,0,360,(0,255,0),thickness=3)
cv2.ellipse(imageEllipse,(360,200),(100,170),135,0,360,(0,0,255),thickness=3)

cv2.imshow("ellipse", imageEllipse)

# 사각형그리기
imageRectangle = image.copy()
cv2.rectangle(imageRectangle,(200,55),(450,355),(255,0,0), thickness=3)

cv2.imshow("imageRectangle", imageRectangle)

# 글자 넣기 
imageText = image.copy()
cv2.putText(imageText, "Mark Zukerberg", (200, 55), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0))
cv2.imshow("text",imageText)

cv2.waitKey(0)
cv2.destroyAllWindows()