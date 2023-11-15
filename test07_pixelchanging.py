
#3:14

import cv2 as cv
import numpy as np

img = cv.imread('starry_night.jpg')

print(img)

#what's difference to add data/ or not

px = 300,300
value = img[300][400]
print(value)


px = 300,300
value = img[300][300]
print(value)

img[300,300] = 0,0,0

value = img[300][300]
print(value)

start = 300,300
rad = 20
color = 255,255, 255
th = 5 
cv.circle(img, start, rad, color, th)

cv.imshow('',img)
