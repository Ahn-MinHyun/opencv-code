import cv2
import numpy as np

img = cv2.imread("data/images/candle.jpg")

scaleFactor = 2.5

ycbImage  = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

ycbImage = ycbImage.astype('float')

Ychannel, Cr, Cb = cv2.split(ycbImage)

Ychannel = np.clip(Ychannel * scaleFactor,0, 255)

ycbImage = cv2.merge([Ychannel, Cr, Cb])

ycbImage = np.uint8(ycbImage)

ycbImage = cv2.cvtColor(ycbImage, cv2.COLOR_YCrCb2BGR)

combined = np.hstack([img, ycbImage])

cv2.imshow("combine", combined)

cv2.waitKey()
cv2.destroyAllWindows()

