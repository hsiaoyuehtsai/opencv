import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
cv.imshow("Blank", blank)

img = cv.imread("image/shiba.jpg")
cv.imshow("dog", img)

# 1. Paint the image a certain colour
blank[200:300, 300:400] = 0, 0, 255
cv.imshow("Red", blank)

# 2. Draw a Rectangle
cv.rectangle(
    blank,
    (10, 10),
    (blank.shape[1] // 2, blank.shape[0] // 2),
    (0, 255, 0),
    thickness=-1,
)
cv.imshow("Rectangle", blank)

# 3. Draw a circle
cv.circle(blank, (250, 250), 40, (0, 0, 255), thickness=-1)
cv.imshow("Circle", blank)

# 4. Draw a line
cv.line(
    blank,
    (500, 250),
    (blank.shape[1] // 3, blank.shape[0] // 3),
    (255, 255, 255),
    thickness=3,
)
cv.imshow("Line", blank)

# 5. Write text
cv.putText(blank, "Hello", (255, 255), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), 2)
cv.imshow("Text", blank)

while True:
    if cv.waitKey(20) & 0xFF == ord("q"):
        break
