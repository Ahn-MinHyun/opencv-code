import cv2
import numpy as np
import random 

threshold = 0

maxThreshold = 300*2

random.seed(12345)


def callback():
    # 케니 엣지로, 엣지 검출하고,
    imCanny = cv2.Canny(img, threshold, threshold*2, apertureSize=3)

    # 컨투어스 연결시킨다. 엣지를 연결
    contours, heirarchy = cv2.findContours(imCanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # 연결시켜서 그린다. 
    display = np.zeros( ( imCanny.shape[0], imCanny.shape[1] ) )

    for i in range(0, len(contours)):
        lineColor = (255,0,0)
        cnt = contours[i]
        cv2.drawContours(display, [cnt], -1, lineColor, 2)

    cv2.imshow("Contours",display/255.0)

def updateThreshold(*args) :
    global threshold
    threshold = args[0]
    callback()

img = cv2.imread('data/images/longborad.png',0)

cv2.namedWindow("Contours", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Contours",img)

cv2.createTrackbar("Canny and Contours","Contours", threshold, maxThreshold, updateThreshold)

callback()

cv2.waitKey()
cv2.destroyAllWindows()

