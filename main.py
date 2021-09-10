import cv2 as cv

img = cv.imread('opencv-course/Resources/Photos/cat.jpg')




def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    demension = (width, height)

    return cv.resize(frame, demension, interpolation=cv.INTER_AREA)
resized_image = rescaleFrame(img)
cv.imshow('Cat', resized_image)
cv.waitKey(0)

cap = cv.VideoCapture('opencv-course/Resources/Videos/dog.mp4')
while True:
    isTrue, frame = cap.read()

    frame_resize = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resize', frame_resize)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

cap.release()
cv.destroyAllWindows()