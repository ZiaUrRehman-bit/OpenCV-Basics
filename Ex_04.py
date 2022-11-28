# Exercise 04: Extracting the color channels

import cv2 as cv
import numpy as np

def getGrayscaleImages(image):

    b = image[:,:,0]
    g = image[:,:,1]
    r = image[:,:,0]

    return b, g, r

def colorChannelImages(image):

    dimension = image.shape
    height, width = dimension[0], dimension[1]

    zeroChannel = np.zeros((height, width), "uint8")

    b, g, r = getGrayscaleImages(image)

    blueImage = cv.merge([b, zeroChannel, zeroChannel])
    greenImage = cv.merge([zeroChannel, g, zeroChannel])
    redImage = cv.merge([zeroChannel, zeroChannel, r])

    return blueImage, greenImage, redImage

path ="C:\\Users\\hp\\Google Drive\\Fiverr Work\\2022\\15. Teaching OpenCV to Client\\Pics+scripts\\Pictures"

img = cv.imread(path + "\\colorStripe.png")
imgResized = cv.resize(img, (200, 400))

print(imgResized.shape)

b, g, r = getGrayscaleImages(imgResized)
blue, green, red = colorChannelImages(imgResized)

grayscalResult = np.hstack((b, g, r))
colorResult = np.hstack((blue, green, red))

cv.imshow("image", imgResized)
cv.imshow("grayScale channel Images", grayscalResult)
cv.imshow("color channel Images", colorResult)

cv.waitKey()
cv.destroyAllWindows()