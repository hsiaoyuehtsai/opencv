import cv2 as cv
import numpy as np

img = cv.imread("image/shibas.jpg")

cv.imshow("Dog", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

# canny = cv.Canny(img, 125, 175)
# cv.imshow("Canny", canny)

ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Tresh',thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours(s) found!')

while True:
    if cv.waitKey(20) & 0xFF == ord("q"):
        break
