from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse
import random as rng

class Canny:
    def __init__(self):
        rng.seed(12345)
        
        self.src = cv.imread('HappyFish.jpg')

        # Convert image to gray and blur it
        self.src_gray = cv.cvtColor(self.src, cv.COLOR_BGR2GRAY)
        self.src_gray = cv.blur(self.src_gray, (3, 3))

        # Create Window
        self.source_window = 'Source'
        cv.namedWindow(self.source_window)
        cv.imshow(self.source_window, self.src)
        self.max_thresh = 255
        self.thresh = 100  # initial threshold
        cv.createTrackbar('Canny Thresh:', self.source_window, self.thresh, self.max_thresh, self.thresh_callback)
        self.thresh_callback(self.thresh)

        cv.waitKey()

    def thresh_callback(self, val):
        threshold = val

        # Detect edges using Canny
        canny_output = cv.Canny(self.src_gray, threshold, threshold * 2)

        # Find contours
        contours, hierarchy = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        # Draw contours
        drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
        for i in range(len(contours)):
            color = (rng.randint(0, 256), rng.randint(0, 256), rng.randint(0, 256))
            cv.drawContours(drawing, contours, i, color, 2, cv.LINE_8, hierarchy, 0)

        # Show in a window
        cv.imshow('Contours', drawing)

c = Canny()

   

class EdgeDetection():
    def __init__(self):
        pass

e =EdgeDetection()





























