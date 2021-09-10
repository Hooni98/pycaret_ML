import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype ='uint8')
cv.imshow('Blank',blank)
img = cv.imread('opencv-course/Resources/Photos/cat.jpg')
cv.imshow('cat', img)


# 1. paint the image a certain color
blank[200:300, 300:400] = 255,0,0
cv.imshow('Green', blank)

# cv.rectangle(blank, (0,0),(blank.shape[1]//2), (0,255,0), thickness=cv.FILLED) # -1
# cv.imshow('Rectangle', blank)

# cv.waitKey(0)

cv.line(blank, (0,0),(blank.shape[1]//2, blank.shape[0]//2), (255,255,255),
        thickness=3)

cv.imshow('Line', blank)

# text
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0),2)
cv.imshow('text', blank)
cv.waitKey(0)