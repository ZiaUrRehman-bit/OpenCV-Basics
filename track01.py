import cv2 as cv
import numpy as np



img1 = np.zeros((300, 400, 3), "uint8")
img2= np.ones((300, 400, 3), "uint8")*255


resultant = cv.bitwise_and(img1, img2)
resultant2 = cv.bitwise_or(img1, img2)
resultant3 = cv.bitwise_not(img1)

cv.imshow("image33", img1)
cv.imshow("imagewww", img2)

cv.imshow("image", resultant)
cv.imshow("image1", resultant2)
cv.imshow("image2", resultant3)

cv.waitKey()

# img = cv.VideoCapture(0)

# path = "C:\\Users\\hp\\Google Drive\\Fiverr Work\\2022\\15. Teaching OpenCV to Client\\pictures"

# # as this is required by createTrackbar function
# def nothing(x):
#     pass

# # create a window
# cv.namedWindow('TrackBar')

# # create trackbar for lower hue values, by default at 0
# cv.createTrackbar('LH', 'TrackBar', 0, 180, nothing)
# # create trackbar for upper hue values, by default at 255
# cv.createTrackbar('UH', 'TrackBar', 180, 180, nothing)
# # create trackbar for lower saturation values, by default at 0
# cv.createTrackbar('LS', 'TrackBar', 0, 255, nothing)
# cv.createTrackbar('US', 'TrackBar', 255, 255, nothing)
# cv.createTrackbar('LV', 'TrackBar', 0, 255, nothing)
# cv.createTrackbar('UV', 'TrackBar', 255, 255, nothing)


# while True:
#     # read an image
#     # img = cv.imread(path + "\\coloredChips.png")
#     success, frame = img.read()

#     # convert it to hsv
#     hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

#     # get the values of trackbar using getTrackbarPos function
#     lh = cv.getTrackbarPos('LH', 'TrackBar')
#     uh = cv.getTrackbarPos('UH', 'TrackBar')
#     ls = cv.getTrackbarPos('LS', 'TrackBar')
#     us = cv.getTrackbarPos('US', 'TrackBar')
#     lv = cv.getTrackbarPos('LV', 'TrackBar')
#     uv = cv.getTrackbarPos('UV', 'TrackBar')

#     # create an array of lower bound and upper bound

#     lowerRegion = np.array([lh, ls, lv])
#     upperRegion = np.array([uh, us, uv])

#     # creating a mask
#     mask = cv.inRange(hsv, lowerRegion, upperRegion)

#     # now apply the mask
#     resultantImage = cv.bitwise_and(frame, frame, mask = mask)

#     cv.imshow('input image', frame)
#     cv.imshow('mask', mask)
#     cv.imshow('output', resultantImage)
    
#     k = cv.waitKey(1)

#     if k == ord('q'):
#         cv.destroyAllWindows()
