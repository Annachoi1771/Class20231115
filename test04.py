import numpy as np
import cv2 as cv

video = cv.VideoCapture(0)
print(video)




while True:
    captured, frame = video.read()
    print(captured)
    grayimage = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('title', frame)
    if cv.waitKey(1) == ord('q'):
        break
