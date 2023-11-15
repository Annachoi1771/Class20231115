import cv2 as cv
import numpy as np

# Read the image
img = cv.imread('data/starry_night.jpg')

# Display the image
cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()


