import cv2 as cv

img = cv.imread("image/shiba2.jpg")
cv.imshow("Dog", img)

# Averaging
average = cv.blur(img, (3, 3))
cv.imshow("Average Blur", average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow("Gaussian BLUR", gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow("Median Blur", median)

# Bilateral
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow("Bilatiral", bilateral)

while True:
    if cv.waitKey(20) & 0xFF == ord("q"):
        break
