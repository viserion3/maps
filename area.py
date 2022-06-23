import cv2 as cv
import numpy as np
import os
from PIL import Image

for file in os.listdir():
    filename, extension  = os.path.splitext(file)
    if extension == ".pgm":
        new_file = "{}.png".format(filename)
        with Image.open(file) as im:
            im.save(new_file)


for file in os.listdir():
    filename, extension  = os.path.splitext(file)
    if extension == ".png":

        img = cv.imread('map.png',0)
        _, th1 = cv.threshold(img, 220, 255, cv.THRESH_BINARY)
        cv.imwrite('map_thresh.png', th1)
            
img = cv.imread("map_thresh.png")
number_of_white_pix = np.sum(img == 255)

area = number_of_white_pix * 0.001

print(f'Map Area: {area:.3f} m2')

#area_round = round(area,3)
#print('Map Area:', area_round)
#cv.imshow("th1", th1)
