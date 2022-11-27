
# I want to change the color of image R, G, and B by using OpenCV trackbar functions

import cv2 as cv
import numpy as np

# you have to create a function which simply do nothing and pass 
# because it is required as fifth arguement of createTracbar function
def nothing(x):
    pass

# Creating a black image using numpy, with following dimension 400x500x3 
img = np.zeros((200, 600, 3), "uint8")

# creating a display window with named "image"  
cv.namedWindow("image")

# creating trackbars for red color change, 
# R is name of trackbar, 
# image is name of window on which it will display
# 0 is by default value of trackbar when it start
# 255 is the maximum value of the trackbar 
# nothing is the function created above which simply do nothing and pass, 
# it is requirement of creatTrackbar function 
cv.createTrackbar('R', 'image', 0, 255, nothing)
 
# creating trackbars for Green color change
cv.createTrackbar('G', 'image', 0, 255, nothing)
 
# creating trackbars for Blue color change
cv.createTrackbar('B', 'image', 0, 255, nothing) 

# now i want to get the valuse of each trackbar 
# for that i need a loop which runs continuesly 

while True:

    # get current positions or value of all Three trackbars
    # R is the name of trackbar created above and 
    # image is the name of window 
    r = cv.getTrackbarPos('R', 'image')
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')

    # now assign these r, g, and b trackbar value to original image
    img[:] = [b, g, r]

    # Now show the created image (img) inside the above created window, 
    # you have to mention the name of window, in this case the name of window is "image"
    cv.imshow("image", img)
    cv.waitKey(1)

cv.destroyAllWindows()

