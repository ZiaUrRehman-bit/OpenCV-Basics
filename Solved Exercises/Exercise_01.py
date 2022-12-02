# Exercise 1
# Part 1
from PIL import Image
import cv2

path ="C:\\Users\\hp\\Google Drive\\Fiverr Work\\2022\\15. Teaching OpenCV to Client\\Pics+scripts\\Pictures"

#The excersises will contain half-made functions and other half-finshed commands. 
#You are to fill them out with the correct commands in order to make the program work

img1=cv2.imread(path + "\\icons01.png")
dimensions = img1.shape
img11=Image.open(path + "\\icons01.png")
# RGB Image
print('GImage Typ is       : ', img11.mode)

img2=cv2.imread(path + "\\icons02.png")
dimensions = img2.shape
img22=Image.open(path + "\\icons02.png")
print('GImage Typ is       : ', img22.mode)


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


# Part 2
img1=cv2.imread(path + "\\rgb01.png")
img2=cv2.imread(path + "\\rgb02.png")
# img3=cv2.imread()
#check coords in paint, paint reads coords y=down x=side (img1[x, y])
b1,g1,r1 = img1[200, 200]
b2,g2,r2 = img1[51, 80]
b3,g3,r3 =img1[200, 94]

print("Geen",b1,g1,r1)
print("Red",b2,g2,r2)
print("Blue",b3,g3,r3)

#
image=Image.open(path + "\\rgb01.png")
#check type
print("IMG2", image.mode)
#convert to extract channels RGB
Coords=200, 200 #Green
print("green", image.getpixel(Coords))
Coords=51, 80 #red
print("red", image.getpixel(Coords))
Coords=200, 94 #Blue
print("Blue", image.getpixel(Coords))


#
image=Image.open(path + "\\rgb02.png")
#check type
print("IMG3", image.mode)
#convert to extract channels RGB
Coords=185, 200#Green
print("green",image.getpixel(Coords))
Coords=32, 154 #red
print("red",image.getpixel(Coords))
Coords=203, 37#Blue
print("Blue",image.getpixel(Coords))


