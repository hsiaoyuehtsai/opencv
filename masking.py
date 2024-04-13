import cv2 as cv
import numpy as np

img = cv.imread("image/shiba2.jpg")
cv.imshow("Dog", img)

blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("Blank Image", blank)

circle = cv.circle(
    blank.copy(),
    (img.shape[1] // 2, img.shape[0] // 2),
    240,
    255,
    -1,
)
cv.imshow("Mask Circle", circle)

rectangle = cv.rectangle(
    blank.copy(),
    (50, 50),
    (679, 436),    
    255,
    -1,
)
cv.imshow("Mask Rectangle", rectangle)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow("Weird Shape", weird_shape)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow("Masked Image", masked)
while True:
    if cv.waitKey(20) & 0xFF == ord("q"):
        break
