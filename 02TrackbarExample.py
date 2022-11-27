
# convert the color (cvtColor) using Trackbar

import cv2 as cv

def nothing(x):
    pass

path = "C:\\Users\\hp\\Google Drive\\Fiverr Work\\2022\\15. Teaching OpenCV to Client\\pictures"

img = cv.imread(path + "\\eyes.jpg")
imgResized = cv.resize(img, (1000, 600))

# create a window
cv.namedWindow("image", cv.WINDOW_NORMAL)

# [4, 2, 0, 6, 40, 68, 66, 36, 44, 32, 50]
# each color code hase integer value
colorName = [cv.COLOR_BGR2RGB, cv.COLOR_BGR2RGBA, cv.COLOR_BGR2BGRA, cv.COLOR_BGR2GRAY,
            cv.COLOR_BGR2HSV, cv.COLOR_BGR2HLS_FULL,cv.COLOR_BGR2HSV_FULL, 
            cv.COLOR_BGR2YCrCb, cv.COLOR_BGR2LAB, cv.COLOR_BGR2XYZ, 
            cv.COLOR_BGR2LUV]

# create Trackbar
cv.createTrackbar('color', 'image', 0, 10, nothing)

while True:

    # get value from trackbar
    colorNumber = cv.getTrackbarPos('color', 'image')

    # assign the value to convert color
    colorImage = cv.cvtColor(imgResized, colorName[colorNumber])

    cv.imshow("image", colorImage)
    k = cv.waitKey(1)

    if k == ord('q'):
        cv.destroyAllWindows()