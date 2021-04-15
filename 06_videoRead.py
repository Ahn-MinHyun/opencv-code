import cv2
import numpy as np

# FPS : Frame per Second : 1초당 몇장의 사진으로 구성되어 있다.
cap = cv2.VideoCapture('data/videos/chaplin.mp4')

if cap.isOpened() == False :
    print( "Error opening video stream or file" )

else :
    while cap.isOpened() :
        # 사진을 1장씩 가져와서.
        ret, frame = cap.read()

        # 제대로 사진 가져왔으면, 화면에 표시
        if ret == True :
            cv2.imshow("Frame", frame)

            # 키보드에서 esc키를 누르면 exit하라는 것
            if cv2.waitKey(25)&0xFF == 27 :
                break
            
        else :
            break
    cap.release()

    cv2.destroyAllWindows()