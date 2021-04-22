import numpy as np
import cv2
import imutils

# 불러오기
# lanelines_image = cv2.imread('data3/test_image.jpg')
# cv2.imshow('ori',lanelines_image)

# # gray scale
# gray_conversion = cv2.cvtColor(lanelines_image,cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray',gray_conversion)

# # smoothing
# blur_conversion = cv2.GaussianBlur(gray_conversion,(5,5), 0)
# cv2.imshow('smooth',blur_conversion)

# # Canny
# canny_conversion = cv2.Canny(blur_conversion, 50, 155)
# cv2.imshow('canny',canny_conversion)

#  위의 과정을 Canny 함수 만들기
def canny_edge(image):
    gray_conversion = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur_conversion = cv2.GaussianBlur(gray_conversion,(5,5), 0)
    canny_conversion = cv2.Canny(blur_conversion, 50, 150)
    return canny_conversion

# Masking the region of interest (RoI)함수만들기
def reg_of_interest(image):
    image_height = image.shape[0]
    polygons =np.array( [[ (200, image_height),(1100, image_height), (550,250)  ]])
    image_mask = np.zeros_like(image)
    cv2.fillPoly(image_mask, polygons, 255)
    masking_image = cv2.bitwise_and(image,image_mask)
    
    return masking_image

# line을 표시하는 함수
def show_lines(image, lines):
    lines_image = np.zeros_like(image)
    if lines is not None :
        for i in range(len(lines)):
            for x1,y1,x2,y2 in lines[i]:
                cv2.line(lines_image,(x1,y1),(x2,y2),(255,0,0),10)
    return lines_image

# 여러 선을, 하나의 선으로 만들어 주는 함수.
# optimizing 기울기와 y절편을 평균으로 해서 하나의 기울기와 y절편을 갖도록 만드는 방법.
def make_coordinates(image, line_parameters):
    slope, intercept = line_parameters
    y1 = image.shape[0]
    y2 = int(y1*(3/5))
    x1 = int ( (y1 - intercept) / slope )
    x2 = int ( (y2 - intercept) / slope )
    return np.array( [x1, y1 ,x2, y2] )

def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    for line in lines :
        x1, y1, x2, y2 = line.reshape(4)
        # 기울기와 y절편을 가져올 수 있다. 
        parameter = np.polyfit( (x1, x2),(y1,y2), 1 )
        slope = parameter[0]
        intercept = parameter[1]
        if slope < 0 :
            left_fit.append( (slope, intercept))
        else :
            right_fit.append( (slope, intercept))
    left_fit_avg =np.average(left_fit, axis= 0)
    right_fit_avg = np.average(right_fit, axis=0)
    left_line = make_coordinates(image, left_fit_avg)
    right_line = make_coordinates(image, right_fit_avg)

    return np.array( [[left_line, right_line]] )

# 사진 가져오기 
# image = cv2.imread('data3/test_image.jpg')
# lanelines_image = image.copy()

# canny_conversion = canny_edge(lanelines_image)
# roi_conversion = reg_of_interest(canny_conversion)

# # cv2.imshow("canny",roi_conversion)
# lines = cv2.HoughLinesP(roi_conversion, 1, np.pi/180, 100, minLineLength=40,maxLineGap=5)
# print(lines)
# lines_image = show_lines(lanelines_image, lines)

# averaged_lines = average_slope_intercept(lanelines_image,lines)
# lines_image = show_lines(lanelines_image, averaged_lines)
# # cv2.imshow("canny",lines_image)

# combine_image = cv2.addWeighted(lanelines_image, 0.8, lines_image,1,1)


# # lines_image = show_lines(lanelines_image,lines)

# # cv2.imshow("ori",image)

# # cv2.imshow("RoI", lines_image)
# cv2.imshow("combined",combine_image)


# cv2.waitKey()
# cv2.destroyAllWindows()


# 비디오 가져오기 
sv = cv2.VideoCapture('data3/test2.mp4')
if sv.isOpened() == False :
    print( "Error opening video stream or file" )

else :
    # frame_width = int(sv.get(3)/2)
    # frame_height = int(sv.get(4)/2)
    # frame_fps = sv.get(5)
    # print("frame_height",frame_height)
    # print(frame_fps)
    # out = cv2.VideoWriter('data/videos/lane_detection.avi',cv2.VideoWriter_fourcc(*'MJPG'),10,(frame_width,frame_height))
    while sv.isOpened() :
        # 사진을 1장씩 가져와서.
        ret, frame = sv.read()
        # canny
        canny_image = canny_edge(frame)
        # RoI
        roi_image = reg_of_interest(canny_image)
        # houghline
        lines = cv2.HoughLinesP(roi_image, 1, np.pi/180, 100, minLineLength=40, maxLineGap=5)
        # 라인 합치기
        average_lines = average_slope_intercept(frame, lines)
        # 라인 가져오기
        line_image = show_lines(frame, average_lines)
        # 원본과 라인 합치기 
        combine_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
        
        # 리사이즈
        # combine_image = imutils.resize(combine_image, width=frame_width, height=frame_height)


        # 제대로 사진 가져왔으면, 화면에 표시
        if ret == True :
            # out.write(combine_image)
            cv2.imshow("Frame", combine_image)

            # 키보드에서 esc키를 누르면 exit하라는 것
            if cv2.waitKey(25)&0xFF == 27 :
                break
            
        else :
            break
sv.release()

cv2.destroyAllWindows()