
# I want to put text using trackbar

import cv2 as cv
import numpy as np

# path = "C:\\Users\\hp\\Google Drive\\Fiverr Work\\2022\\15. Teaching OpenCV to Client\\pictures"

# img = cv.imread("zia.png")

# img = cv.putText(img, "hello", (50, 150), cv.FONT_HERSHEY_COMPLEX,
#                 2, (0,0,0), 3)

def nothing(x):
    pass

# Creating a black image using numpy, with following dimension 400x500x3 
img = np.zeros((300, 400, 3), "uint8")

# create a window 
cv.namedWindow("image", cv.WINDOW_NORMAL)

# create a trackbar
cv.createTrackbar("Value", "image", 0, 100, nothing)

while True:
    img = np.zeros((300, 400, 3), "uint8")

    number = cv.getTrackbarPos("Value", "image")

    img = cv.putText(img, str(number), (150, 150), cv.FONT_HERSHEY_COMPLEX,
                    2, (255,255,255), 3)
    
    img = cv.circle(img, (190, 150), number, (255, 255, 255), 3)

    cv.imshow("image", img)
    k = cv.waitKey(1)

    if k == ord('q'):
        cv.destroyAllWindows()