import cv2 as cv
import cv2
import numpy as np
#camera = cv.VideoCapture(0)
frameWidth = 480
frameHeight = 300

originalImage = cv.imread("Resources/fasteners.jpg")
originalImage = cv2.resize(originalImage, (frameWidth, frameHeight))
grayImage = cv.cvtColor(originalImage, cv.COLOR_BGR2GRAY)

(thresh, blackAndWhiteImage) = cv.threshold(grayImage, 180, 255, cv.THRESH_BINARY)

cv.imshow('Black white image', blackAndWhiteImage)
cv.imshow('Original image', originalImage)
cv.imshow('Gray image', grayImage)
edges = cv.Canny(blackAndWhiteImage, 150, 150)
cv.imshow('Canny', edges)

cv.waitKey(0)
cv.destroyAllWindows()






