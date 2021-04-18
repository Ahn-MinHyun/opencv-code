import cv2
import numpy as np

src = cv2.imread('data/images/image1.jpg')
dst = cv2.imread('data/images/image2.jpg')

cv2.imshow("src",src)
cv2.imshow("dst",dst)

output = dst.copy()

srcLab = cv2.cvtColor(src, cv2.COLOR_BGR2LAB)
dstLab = cv2.cvtColor(dst, cv2.COLOR_BGR2LAB)
outputLab = cv2.cvtColor(output, cv2.COLOR_BGR2LAB)

# srcLab =np.float32(srcLab)과 동일하게 float으로 숫자를 바꾼다.
scrcLab = srcLab.astype('float')
dstLab = dstLab.astype('float')
outputLab = outputLab.astype('float')

print(srcLab)
# 채널 분리
srcL, srcA, srcB = cv2.split(srcLab)
dstL, dstA, dstB = cv2.split(dstLab)
outL, outA, outB = cv2.split(outputLab)



# 얻고자 하는 이미지
outL = outL * ( srcL.std() / dstL.std() )
outA = outA * ( srcA.std() / dstA.std() )
outB = outB * ( srcB.std() / dstB.std() )


# 우리가 눈으로 보기 위해서 0~255 사이값으로 셋팅
outL = np.clip(outL, 0,255)
outA = np.clip(outA, 0,255)
outB = np.clip(outB, 0,255)

# 채널 합치기
outputLab = cv2.merge([outL, outA, outB])

# 이미지는 8비트 정수이므로,, 형변환
outputLab = np.uint8(outputLab)

outputLab = cv2.cvtColor(outputLab, cv2.COLOR_HSV2BGR)


cv2.imshow("output", outputLab)

cv2.waitKey()
cv2.destroyAllWindows()
