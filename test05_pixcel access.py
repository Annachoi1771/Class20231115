import cv2 as cv
import sys

img = cv.imread("starry_night.jpg")
print(img)
value = img[10][20]
print(value)
cv.imshow('test', img)
print(img.shape)
