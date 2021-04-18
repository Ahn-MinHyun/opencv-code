import cv2
import numpy as np
from utils import get_four_points

img_src = cv2.imread("data/images/book1.jpg")

dst_size = (400, 300, 3)

img_dst = np.zeros(dst_size,np.uint8)

# cv2.imshow("dst",img_dst)

# 우리가 원본 이미지로부터는 마우스 클릭으로 4개의 점을 가져올거다. 
cv2.imshow("Image",img_src)
points_src = get_four_points(img_src)
# 새로만들 이미지에서는 위의 원본 이미지 4개의 점과 매핑할 점을 잡아줘야 한다. 

point_dst = np.array([0,0,
                    dst_size[1],0, 
                    dst_size[1],dst_size[0], 
                    0, dst_size[0] ], dtype= float)

points_dst = point_dst.reshape(4,2)
h, status = cv2.findHomography(points_src, points_dst)
img_dst = cv2.warpPerspective(img_src, h,(dst_size[1],dst_size[0]))

cv2.imshow("img dst", img_dst)

cv2.waitKey(0)
cv2.destroyAllWindows()