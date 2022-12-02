
# Exercise 05: Preparing Image for edge detection

import cv2 as cv
import numpy as np

def nothing(x):
    pass

path ="C:\\Users\\hp\\Google Drive\\Fiverr Work\\2022\\15. Teaching OpenCV to Client\\Pics+scripts\\Pictures"

cv.namedWindow("output")

cv.createTrackbar("kernel1", "output", 0, 55, nothing)
cv.createTrackbar("kernel2", "output", 0, 55, nothing)
cv.createTrackbar("cannyLower", "output", 3, 255, nothing)
cv.createTrackbar("cannyUpper", "output", 255, 255, nothing)

while True:

    kernel1 = cv.getTrackbarPos("kernel1", "output")
    kernel2 = cv.getTrackbarPos("kernel2", "output")
    cannyLower = cv.getTrackbarPos("cannyLower", "output")
    cannyUpper = cv.getTrackbarPos("cannyUpper", "output")

    img = cv.imread(path + "\\piece05.png")
    imgResized = cv.resize(img, (200, 300))

    # # for dilation
    dilateKernel = np.ones((5,5), "uint8")

    imgGray = cv.cvtColor(imgResized, cv.COLOR_BGR2GRAY)
    
    # As kernel is size of odd dimension
    if (kernel1*kernel2)%2 == 1:
        dilateKernel = np.ones((kernel1,kernel2), "uint8")
        blurImg = cv.GaussianBlur(imgGray, (kernel1,kernel2), 0)
    else:
        blurImg = cv.GaussianBlur(imgGray, (3,3), 0)

    cannyImge = cv.Canny(blurImg, cannyLower, cannyUpper)

    imgDilation = cv.dilate(cannyImge, dilateKernel, iterations=1)

    contours, hierarchy = cv.findContours(imgDilation, 
        cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    
    Objects = 0
    print(len(contours))
    for i in contours:
        M = cv.moments(i) #moments is used for blob dectection, so to find edges use something else. M00 defines the area of found blobs
        
        if (M['m00'] != 0 ):#and M['m00'] <50000 and  M['m00'] <10 ):#filter out unreasaable big blobs for more help check out
                            #:https://pyimagesearch.com/2016/02/01/opencv-center-of-contour/
            Objects=Objects+1
            cx = int(M['m10'] / M['m00']) #insert centroid calculation
            cy = int(M['m01'] / M['m00']) #centroid calculation
            # cv.drawContours()#colors each pixel location in the array where a line has been detected
            cv.circle(imgResized, (cx, cy), 10, (0,0,255), -1)   #draw circle in center of blob  
    cv.drawContours(imgResized, contours, -1, (0, 255, 0), 3)
    cv.putText(imgResized, str(len(contours))+" objects", (20, 20), cv.FONT_HERSHEY_COMPLEX,
                0.5, (255, 255, 0), 1)

    result = np.hstack((imgGray, blurImg, cannyImge, imgDilation))

    cv.imshow("image", imgResized)
    cv.imshow("output", result)

    k = cv.waitKey(1)

    if k == ord("q"):
        cv.destroyAllWindows()