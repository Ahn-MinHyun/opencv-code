# 이미지를 부드럽게 해주는 필터

import cv2 
import numpy as np

img = cv2.imread('data/images/gaussian-noise.png',1)

# 3x3 커널 사용할 때
dst3 = cv2.blur(img,(3,3))

# 7x7 커널 사용할 때
dst7 = cv2.blur(img,(7,7))

#화면에 그리자 
combined =np.hstack([img,dst3,dst7])
cv2.imshow("combine",combined)

cv2.waitKey()
cv2.destroyAllWindows()