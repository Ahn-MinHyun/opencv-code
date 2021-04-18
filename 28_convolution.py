import cv2 
import numpy as np

img = cv2.imread('data/images/gaussian-noise.png',1)

# img = original.copy()

cv2.imshow("img",img)

kernnel_size = 5

kernnel = np.ones( ( kernnel_size , kernnel_size ) ) / kernnel**2
print(kernnel)

#컨볼루션! cv2.filter2D 함수
result = cv2.filer2D(img, -1,kernel)
print(result)

#화면에 그리자 
combined =np.hstack([img,result])
cv2.imshow("combine",combined)

cv2.waitKey()
cv2.destroyAllWindows()