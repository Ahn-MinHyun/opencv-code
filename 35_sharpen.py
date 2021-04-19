import cv2 
import numpy as np

img = cv2.imread('data/images/mountain.jpeg',1)

sharpen = np.array(
    [
        [0,-1,0],
        [-1,5,-1],
        [0,-1,0]
    ], dtype = 'int'
)

result = cv2.filter2D(img, -1, sharpen)

#화면에 그리자 
combined =np.hstack([img,result])
cv2.imshow("combine",combined)

cv2.waitKey()
cv2.destroyAllWindows()