
import cv2 
import numpy as np

highThreshold = 100
lowThreshold = 50

maxThreshold = 1000

apertureSizes = [3, 5, 7]
maxapertureIndex = 2
apertureIndex = 0

blurAmount = 0
maxBlurAmount = 20

# 트랙바용 함수 
# 캐니 에지 적용하는 함수
def applyCanny():
    if blurAmount > 0 :
        blurredSrc = cv2.GaussianBlur(src, (2*blurAmount +1, 2*blurAmount+1), 0  )
    else :
        blurredSrc = src.copy()
    
    apertureSize = apertureSizes[apertureIndex]

    edges = cv2.Canny(blurredSrc, lowThreshold, highThreshold, apertureSize = apertureSize)

    cv2.imshow("Edges", edges)

# 로우 쓰레숄드 적용하는 함수
def updateLowThreshold(*args) :
    global lowThreshold
    lowThreshold = args[0]
    applyCanny()

# 하이 쓰레숄드 적용하는 함수
def updateHighThreshold(*args):
    global highThreshold
    highThreshold = args[0]
    applyCanny()

# 블러 적용하는 함수
def updateBlurAmout(*args) :
    global blurAmount 
    blurAmount = args[0]
    applyCanny()

# aperture 적용하는 함수
def updateApertureIndex(*args) :
    global apertureIndex
    apertureIndex = args[0]
    applyCanny()


src = cv2.imread('data/images/sample.jpg', 0)

edges = src.copy()

cv2.imshow('Edges', src)

cv2.namedWindow('Edges', cv2.WINDOW_AUTOSIZE)

# 로우 쓰레숄드에 대한 컨트롤러를 트랙바에 붙인다.
cv2.createTrackbar("Low Threshold", "Edges", lowThreshold, maxThreshold, updateLowThreshold)
# 하이 쓰레숄드에 대한 컨트롤러를 트랙배에 붙인다.
cv2.createTrackbar("High Threshold", "Edges", highThreshold, maxThreshold, updateHighThreshold)
# aperture 를 트랙바에 붙인다.
cv2.createTrackbar("Aperture Size", "Edges", apertureIndex, maxapertureIndex, updateApertureIndex)
# 블러 컨트롤러를 트랙바에 붙인다.
cv2.createTrackbar("Blur", "Edges", blurAmount, maxBlurAmount, updateBlurAmout)

cv2.waitKey()
cv2.destroyAllWindows()

