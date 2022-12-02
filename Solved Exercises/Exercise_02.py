
from PIL import Image
import cv2

path ="C:\\Users\\hp\\Google Drive\\Fiverr Work\\2022\\15. Teaching OpenCV to Client\\Pics+scripts\\Pictures"

x= 1046
y= 1676

Flowerimg = path + "\\flower.png"
Eagleimg = path + "\\eagle.png"
Carimg = path + "\\car.png"

##EX1
# kontrollera att bilden läses in
img_1 = Image.open(Flowerimg)
img_11 = cv2.imread(Flowerimg)

img_2 = Image.open(Eagleimg)
img_22 = cv2.imread(Eagleimg)

img_3 = cv2.imread(Carimg)

dimensions = img_1.size
# height, width, number of channels in image
height = img_1.height
width = img_1.width
channel = img_1.getchannel



print('\nImage1 Dimension    : ' + str(dimensions))
print('\nImage1 Height       : ' + str(height))
print('\nImage1 Width        : ' + str(width))
print('\nImage1 channgels are: ' + str(channel))
print('\nImage1 Typ is       : ' + img_1.mode)
print("\n1data type is       : " + str(img_11.dtype))
print('\n1pixel value is     : ' + str(img_11))

dimensions = img_2.size
# height, width, number of channels in image
height = img_2.height
width = img_2.width
channel = img_2.getchannel



print('\nImage2 Dimension    : ' + str(dimensions))
print('\nImage2 Height       : ' + str(height))
print('\nImage2 Width        : ' + str(width))
print('\nImage2 channgels are: ' + str(channel))
print('\nImage2 Typ is       : ' + img_2.mode)
print("\n2data type is       : " + str(img_22.dtype))
print('\n2pixel value is     : ' + str(img_22))
'''
for .mode these type can be shown.
1 (1-bit pixels, black and white, stored with one pixel per byte)

L (8-bit pixels, black and white)

P (8-bit pixels, mapped to any other mode using a color palette)

RGB (3x8-bit pixels, true color)

RGBA (4x8-bit pixels, true color with transparency mask)

CMYK (4x8-bit pixels, color separation)

YCbCr (3x8-bit pixels, color video format)

Note that this refers to the JPEG, and not the ITU-R BT.2020, standard

LAB (3x8-bit pixels, the L*a*b color space)

HSV (3x8-bit pixels, Hue, Saturation, Value color space)

I (32-bit signed integer pixels)

F (32-bit floating point pixels)
'''

print("\nvalues for the pixel located at (Y,X)=(1676,1046):" + str(img_3[y, x]) + "\n")

