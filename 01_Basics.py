import cv2 as cv
import numpy as np

# path = "C:\\Users\\hp\\Google Drive\\Fiverr Work\\2022\\15. Teaching OpenCV to Client\\pictures"

img = cv.imread("zia.png")
imgResized = cv.resize(img, (500,500))

print(img.shape)

cv.imshow("zia image", img)
cv.imshow("resized iamge", imgResized)
k = cv.waitKey()

if k == ord('q'):
    cv.destroyAllWindows()

