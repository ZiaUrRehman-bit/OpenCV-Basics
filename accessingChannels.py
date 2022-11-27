import cv2 as cv
import numpy as np

path = "C:\\Users\\hp\\Google Drive\\Fiverr Work\\2022\\15. Teaching OpenCV to Client\\pictures"

img = cv.imread(path + "\\eyes.jpg")
imgResized = cv.resize(img, (400, 400))

dimension = imgResized.shape
print(f"\nDimension of image {dimension}\n")

# Blue channel 0 represents blue, 1 for green, and 2 for red channel
b = imgResized[:,:,0]
print(f"{b} \n\n Dimension of blue Channel is: {b.shape}")

g = imgResized[:,:,1]
print(f"{g} \n\n Dimension of green Channel is: {g.shape}")

r = imgResized[:,:,2]
print(f"{r} \n\n Dimension of red Channel is: {r.shape}")

# we can do same thing by using split function of opencv
# but this function is costly in terms of time so taht's why above methods prefered to split
blue, green, red = cv.split(imgResized)
print(f"{blue} \n {green} \n {red}")

cv.imshow("image", img)
cv.imshow("Resized Image", imgResized)

cv.imshow("blue channel image", b)
cv.imshow("green channel image", g)
cv.imshow("red channel image", r)

# you can also merge these channel to make orignal image

mergedImage = cv.merge([b, g, r])

cv.imshow("Merged Image", mergedImage)

# for accessing actual blue, green, and red you have to merge blue and with zero matrics of same size
# as green and red

# create an array of same length as blue or green contain with data type mentioned also
zeroChannel = np.zeros((dimension[0], dimension[1]), "uint8")

blueImage = cv.merge([b, zeroChannel, zeroChannel])
greenImage = cv.merge([zeroChannel, g, zeroChannel])
redImage = cv.merge([zeroChannel, zeroChannel, r])

cv.imshow("actual blue channel", blueImage)
cv.imshow("actual green channel", greenImage)
cv.imshow("actual red channel", redImage)

cv.waitKey()
cv.destroyAllWindows()