
import cv2 
import numpy as np

img = cv2.imread('data/images/longborad.jpeg',0)

threshold_1 = 30 # high : 0~255중 설정

threshold_2 = 100 # low : 200

result = cv2.Canny(img, threshold_1, threshold_2)

#화면에 그리자 

combined =np.hstack([img,result])
cv2.imshow("combine",combined)

cv2.waitKey()
cv2.destroyAllWindows()