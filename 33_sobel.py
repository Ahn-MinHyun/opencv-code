import cv2 
import numpy as np

img = cv2.imread('data/images/truth.png',1)

sobelx = cv2.Sobel(img, cv2.CV_32F,1,0)
sobely = cv2.Sobel(img, cv2.CV_32F,0,1)

#화면에 그리자 
combined =np.hstack([img,sobelx, sobely])
cv2.imshow("combine",combined)

cv2.waitKey()
cv2.destroyAllWindows()