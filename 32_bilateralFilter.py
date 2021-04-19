import cv2 
import numpy as np

img = cv2.imread('data/images/gaussian-noise.png',1)

result = cv2.bilateralFilter(img, 15, 80, 80)

#화면에 그리자 
combined =np.hstack([img,result])
cv2.imshow("combine",combined)

cv2.waitKey()
cv2.destroyAllWindows()