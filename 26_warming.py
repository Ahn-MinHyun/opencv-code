import cv2 
import numpy as np

original = cv2.imread('data/images/girl.jpg')

img = original.copy()

# x 축 피봇 포인트
originalValue = np.array([0,50,100,150,200,255])

# y 축 포인트 : 빨간쪽, 파란쪽 두 부분의 포인트
rCurve = np.array([0,80,150,190,220,255])
bCurve = np.array([0,20,40,75,150,255])

# Lookup 테이블 만들기
fullRange = np.arange(0, 255+1)
rLUT = np.interp(fullRange, originalValue, rCurve)
bLUT = np.interp(fullRange, originalValue, bCurve)

print(rLUT)
print(rLUT.shape)

rChannel = img[:,:,2] # B,G,rChannel = cv2.split(img)과 동일
rChannel = cv2.LUT(rChannel,rLUT)
img[:,:,2] = rChannel

bChannel = img[:,:,0]
bChannel = cv2.LUT(bChannel, bLUT)
img[:,:,0] = bChannel

#화면에 그리자 
combined =np.hstack([original,img])
cv2.imshow("combine",combined)

cv2.waitKey()
cv2.destroyAllWindows()