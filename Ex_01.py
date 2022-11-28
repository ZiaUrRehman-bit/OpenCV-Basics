
# Exercise 01

from PIL import Image
import cv2 as cv

def findTypeOfImage(image):

    if image.mode == "1":
        imageType = "1-bit pixels, black and white, stored with one pixel per byte"
    elif image.mode == "L":
        imageType = "8-bit pixels, black and white"
    elif image.mode == "P":
        imageType = "8-bit pixels, mapped to any other mode using a color palette"
    elif image.mode == "RGB":
        imageType = "3x8-bit pixels, true color"
    elif image.mode == "CMYK":
        imageType = "4x8-bit pixels, color separation"
    elif image.mode == "YCbCr":
        imageType = "3x8-bit pixels, color video format"
    elif image.mode == "LAB":
        imageType = "3x8-bit pixels, the L*a*b color space"
    elif image.mode == "HSV":
        imageType ="3x8-bit pixels, Hue, Saturation, Value color space"
    elif image.mode == "I":
        imageType = "32-bit signed integer pixels"
    elif image.mode == "F":
        imageType = "32-bit floating point pixels"

    return imageType

def findRGBValuesByOpenCV(image):
    blue = image[:,:,0]
    green = image[:,:,1]
    red = image[:,:,2]

    print(f"Blue color values: {blue} \nGreen Color Values: {green}\nRed Color Values: {red}")

def findRGBValuesByPIL(image, x, y):
    img = Image.open(image).convert("RGB")
    r, g, b = img.getpixel((x, y))

    value = (r, g, b)

    return value

path ="C:\\Users\\hp\\Google Drive\\Fiverr Work\\2022\\15. Teaching OpenCV to Client\\Pics+scripts\\Pictures"

### Part 01 open the images icons01.png ....................#####

img1 = Image.open(path + "\\icons01.png")
img2 = Image.open(path + "\\icons02.png")

img1Type = findTypeOfImage(img1)
img2Type = findTypeOfImage(img2)

print(f"The Type of icons01.png is "+img1Type)
print(f"The Type of icons02.png is " +img2Type)

####### Answer Justification ################

# The mode of an image is a string which defines the type and depth of a pixel in the image. 
# Each pixel uses the full range of the bit depth. So a 1-bit pixel has a range of 0-1, 
# an 8-bit pixel has a range of 0-255 and so on.

# L (8-bit pixels, black and white)

# P (8-bit pixels, mapped to any other mode using a color palette)


# The mode of icons01.png image is P, it is 8-bit black and white image
# The mode of icon02.png image is L, it is also 8-bit black and white


########### Part 02 List RGB values of colors ....................... #############

img3 = cv.imread(path + "\\rgb01.png")
img03 = path + "\\rgb01.png"

img4 = cv.imread(path + "\\rgb02.png")
img04 = path + "\\rgb02.png"

findRGBValuesByOpenCV(img3)
findRGBValuesByOpenCV(img4)

rgbValue = findRGBValuesByPIL(img03, 200, 200)
print(rgbValue)

cv.imshow("imgae3", img3)
cv.imshow("image4", img4)
cv.waitKey()
cv.destroyAllWindows()