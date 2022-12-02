
import cv2

path ="C:\\Users\\hp\\Google Drive\\Fiverr Work\\2022\\15. Teaching OpenCV to Client\\Pics+scripts\\Pictures"

colorStripe= path + "\\piece03.png"
image = cv2.imread(colorStripe)#pass correct object
image =cv2.resize(image, (200,290))
bw,gw,rw=cv2.split(image)#pass correct object

b = image.copy()
# set green and red channels to 0
b[:,:,1] = 0
b[:,:,2] = 0
g = image.copy()
# set blue and red channels to 0
g[:,:,0] = 0
g[:,:,2] = 0
r = image.copy()
# set blue and green channels to 0
r[:,:,0] = 0
r[:,:,1] = 0


# RGB - Blue
cv2.imshow('B-RGB', b)
cv2.imshow('BW B-RGB', bw)
# RGB - Green
cv2.imshow('G-RGB', g)
cv2.imshow('Gw-RGB', gw)
# RGB - Red
cv2.imshow('R-RGB', r)
cv2.imshow('w-RGB', rw)

cv2.waitKey(0)
