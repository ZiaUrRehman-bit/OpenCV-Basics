import cv2 as cv

path = "C:\\Users\\hp\\Google Drive\\Fiverr Work\\2022\\15. Teaching OpenCV to Client\\pictures"

img = cv.imread(path + "\\eyes.jpg")
imgResized = cv.resize(img, (1200, 700))

# each color code hase integer value
colorName = [cv.COLOR_BGR2RGB, cv.COLOR_BGR2RGBA, cv.COLOR_BGR2BGRA, cv.COLOR_BGR2GRAY,
            cv.COLOR_BGR2HSV, cv.COLOR_BGR2HLS_FULL,cv.COLOR_BGR2HSV_FULL, 
            cv.COLOR_BGR2YCrCb, cv.COLOR_BGR2LAB, cv.COLOR_BGR2XYZ, 
            cv.COLOR_BGR2LUV]

for colorNumber in colorName:
    
    colorImage = cv.cvtColor(imgResized, colorNumber)


    cv.imshow(f"Image of color number {colorNumber}", colorImage)
    cv.waitKey(2000)

    cv.destroyAllWindows()