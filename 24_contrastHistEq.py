import cv2
import numpy as np

img = cv2.imread("data/images/candle.jpg")

scaleFactor = 2.5

ycbImage  = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

Ychannel, Cr, Cb = cv2.split(ycbImage)

cv2.equalizeHist(Ychannel)

ycbImage = cv2.merge([Ychannel, Cr, Cb])

ycbImage = cv2.cvtColor(ycbImage, cv2.COLOR_YCrCb2BGR)

combined = np.hstack([img, ycbImage])

cv2.imshow("combine", combined)

cv2.waitKey()
cv2.destroyAllWindows()

