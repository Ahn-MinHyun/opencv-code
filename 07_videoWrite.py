import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if cap.isOpened() == False :
    print("Unable to read camera feed")

else :
    # 프레임 정보 가져오기 : 화면 크기(width,height)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # 저장
    out = cv2.VideoWriter('data/videos/output.avi',
                        cv2.VideoWriter_fourcc('M','J','P','G'),
                        10,
                        (frame_width,frame_height)
                        )
    # 캠으로 부터 사진을 계속 입력 받는다.
    while True :
        ret, frame = cap.read()

        if ret == True:
            out.write(frame)

            cv2.imshow('frame',frame)
            
            # 인공지능으로 동작을 시킬 코드가 들어간다.
            # code
            if cv2.waitKey(1) & 0xFf == 27:
                break
        else:
            break

    cap.release()
    out.release()

    cv2.destroyAllWindows()




                        