import cv2 as cv
import sys

img = cv.imread("starry_night.jpg")
print(img)


cv.imshow('test', img)
