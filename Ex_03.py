
# Exercise 03: Binarization, image stacking, trackbars

import cv2 
import numpy as np

# as this is required by createTrackbar function
def nothing(x):
    pass

path ="C:\\Users\\hp\\Google Drive\\Fiverr Work\\2022\\15. Teaching OpenCV to Client\\Pics+scripts\\Pictures"

img = cv2.imread(path +"\\piece03.png")
img = cv2.resize(img, (220, 500))

cv2.namedWindow("stack", cv2.WINDOW_NORMAL)

cv2.createTrackbar('LB', 'stack', 0, 255, nothing)
cv2.createTrackbar('UB', 'stack', 255, 255, nothing)

while True:

    lb = cv2.getTrackbarPos('LB', 'stack')
    ub = cv2.getTrackbarPos('UB', 'stack')

    ret, thresh1 = cv2.threshold(img, lb, ub, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img, lb, ub, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(img, lb, ub, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(img, lb, ub, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(img, lb, ub, cv2.THRESH_TOZERO_INV)
    
    # the window showing output images
    # with the corresponding thresholding
    # techniques applied to the input images

    hstackw = np.hstack((img,thresh1,thresh2,thresh3,thresh4,thresh5))
    cv2.imshow("stack", hstackw)
    # cv2.imshow('Binary Threshold', thresh1)
    # cv2.imshow('Binary Threshold Inverted', thresh2)
    # cv2.imshow('Truncated Threshold', thresh3)
    # cv2.imshow('Set to 0', thresh4)
    # cv2.imshow('Set to 0 Inverted', thresh5)

    # cv2.imshow("image", img)
    cv2.waitKey(1)
    