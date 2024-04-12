import cv2 as cv

img = cv.imread("image/shiba2.jpg")
cv.imshow("Dog", img)


while True:
    if cv.waitKey(20) & 0xFF == ord("q"):
        break
