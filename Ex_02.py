# Exercise 02

import tkinter as tk
from PIL import Image
import numpy as np
import cv2 as cv
import os

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

root = tk.Tk()

def findResolutionOfImage(image):

    # Image resolution is typically described in PPI, which refers to 
    # how many pixels are displayed per inch of an image

    # Screen Dimensions from Monitor (or Display) Control Panel	= 1024x768 pixels	
    # Viewable Width of Monitor	Screen Resolution = 12.5 inches	
    # Screen Resolution = 1024/12.5 = 82 ppi
    
    # find the width of your monitor or laptop 
    # it is in mm
    width_mm = root.winfo_screenmmwidth()
    # convert it to inches, To convert mm to inches, you must multiply the unit by 0.03937
    # because 1 mm = 0.03937 inches
    width_in = width_mm * 0.03937

    height = image.shape[0]
    width = image.shape[1]

    if height > width:
        resolution = round(height / width_in)
    else:
        resolution = round(width / width_in)

  
    return str(resolution) + " ppi"

def completeInformation(image, img, name):

    resolution_img_1 = findResolutionOfImage(image)
    dimension_img_1 = image.shape

    height_img_1 = dimension_img_1[0]
    width_img_1 = dimension_img_1[1]

    channels_img_1 = dimension_img_1[2]

    Type_img_1 = findTypeOfImage(img)
    dataType_img_1 = img_1.dtype


    print(f"\nThe resoltuion of {name} is " + resolution_img_1)
    print(f"The dimension {name} is {dimension_img_1}, height: {height_img_1}, width: {width_img_1}")
    print(f"Channels: {channels_img_1}\nData Type: {dataType_img_1}\nType: {Type_img_1}\n")


path ="C:\\Users\\hp\\Google Drive\\Fiverr Work\\2022\\15. Teaching OpenCV to Client\\Pics+scripts\\Pictures"


img_1 = cv.imread(path + "\\flower.png")
img1 = Image.open(path + "\\flower.png")
image_1_name = os.path.basename(path + "\\flower.png")

img_2 = cv.imread(path + "\\eagle.png")
img2 = Image.open(path + "\\eagle.png")
image_2_name = os.path.basename(path + "\\eagle.png")

completeInformation(img_1, img1, image_1_name)

completeInformation(img_2, img2, image_2_name)

