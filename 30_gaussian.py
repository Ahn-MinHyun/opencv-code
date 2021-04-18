# 이미지를 부드럽게 해주는 필터의 끝판왕

import cv2 
import numpy as np

img = cv2.imread('data/images/gaussian-noise.png',1)


dst1 = cv2.GaussianBlur(img,(3,3),0)

dst2 = cv2.blur(img,(3,3),50)

#화면에 그리자 
combined =np.hstack([img,dst1,dst2])
cv2.imshow("combine",combined)

cv2.waitKey()
cv2.destroyAllWindows()