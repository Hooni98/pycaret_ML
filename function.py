import cv2 as cv
import numpy as np

img = cv.imread('opencv-course/Resources/Photos/cat.jpg')
cv.imshow('cat', img)

cv.waitKey(0)