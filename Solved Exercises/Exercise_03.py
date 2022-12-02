import cv2
import numpy as np

#for tackbars
def nothing(x):
    pass

path ="C:\\Users\\hp\\Google Drive\\Fiverr Work\\2022\\15. Teaching OpenCV to Client\\Pics+scripts\\Pictures"

cv2.namedWindow("stack")
cv2.createTrackbar('LB', 'stack', 0, 255, nothing)
cv2.createTrackbar('UB', 'stack', 255, 255, nothing)

while True:
    img=cv2.imread(path +"\\piece03.png")
    img=cv2.resize(img, (100, 100))
    img_copy=img.copy()

    gray=cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)

    LowerBound=cv2.getTrackbarPos('LB', 'stack')
    UpperBound = cv2.getTrackbarPos('UB', 'stack')
    
    ret, thresh2 = cv2.threshold(gray, LowerBound, UpperBound, cv2.THRESH_BINARY_INV)
    ret, thresh1 = cv2.threshold(gray, LowerBound, UpperBound, cv2.THRESH_BINARY)
    ret, thresh3 = cv2.threshold(gray, LowerBound, UpperBound, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(gray, LowerBound, UpperBound, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(gray, LowerBound, UpperBound, cv2.THRESH_TOZERO_INV)


    images=[thresh1,thresh2,thresh3,thresh4,thresh5]
    img_stack=np.hstack(images)

    cv2.imshow("stack",img_stack)
    cv2.waitKey(1)
    
    