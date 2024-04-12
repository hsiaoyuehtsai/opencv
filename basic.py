import cv2 as cv

img = cv.imread("image/shiba.jpg")

cv.imshow("Dog", img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Dog", gray)

# Blur
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow("Blur Dog", blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny", canny)

# Dilating the image
dilated = cv.dilate(canny, (3, 3), iterations=5)
cv.imshow("Dilated", dilated)

# Eroding
eroded = cv.erode(dilated, (3, 3), iterations=3)
cv.imshow("Eroded", eroded)

# Resized
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized image", resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

while True:
    if cv.waitKey(20) & 0xFF == ord("q"):
        break
