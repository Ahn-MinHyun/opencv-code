import cv2
import numpy as np

source = cv2.imread('data/images/sample.jpg',1)

warpMat = np.float32([1.2,0.2,2,-0.3,1.3,1])
warpMat = warpMat.reshape(2,3)

result = cv2.warpAffine(source, warpMat, 
            (int(source.shape[1]*1.5),int(source.shape[0]*1.5)))


warpMat2 =np.float32([1.2,0.3,2,-0.3,1.3,1])
warpMat2 = warpMat2.reshape(2,3)

result2 = cv2.warpAffine(source, warpMat2, 
            (int(source.shape[1]*1.5),int(source.shape[0]*1.5)))

cv2.imshow("Original",source)
cv2.imshow("rotated",result)
cv2.imshow("rotated2",result2)

cv2.waitKey()
cv2.destroyAllWindows()