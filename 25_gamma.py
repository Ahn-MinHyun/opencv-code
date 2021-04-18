import cv2 
import numpy as np

img = cv2.imread('data/images/candle.jpg')

gamma = 1.5

fullRange = np.arange(0,255+1)

IookupTable = np.unit8(255*np.power(fullRange /255.0),gamma))

output = cv2.LUT(img, lookupTable)

combined = np.hstack([img, output])

cv2.imshow("combined", combined)

cv2.waitKey()
cv2.destroyAllWindows()