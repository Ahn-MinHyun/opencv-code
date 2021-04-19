
import cv2 
import numpy as np

img = cv2.imread('data/images/truth.png',1)

laplacian = cv2.Laplacian(img, cv2.CV_32F,ksize=3,scale=1)

#화면에 그리자 
combined =np.hstack([img,laplacian])
cv2.imshow("combine",combined)

cv2.waitKey()
cv2.destroyAllWindows()