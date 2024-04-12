import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("image/shibas.jpg")
cv.imshow("Dog", img)

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# BGR to Lab
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB",lab)

# BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)

# HSV to BGR
hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow("HSV to BGR",hsv_bgr)

# LABto BGR
lab_bgr=cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow("LAB to BGR",lab_bgr)

plt.imshow(rgb)
plt.show()

while True:
    if cv.waitKey(20) & 0xFF == ord("q"):
        break
