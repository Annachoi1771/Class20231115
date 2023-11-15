import numpy as np
import cv2 as cv

video = cv.VideoCapture(0)
print(video)




while True:
    captured, frame = video.read()
    print(captured)
    cv.imshow('title', frame)







