import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("image/shiba2.jpg")
cv.imshow("Dogs", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

circle = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)

masked = cv.bitwise_and(img, img, mask=circle)
cv.imshow("Mask", masked)

# Grayscale histogram
# gray_hist = cv.calcHist([gray], [0], circle, [256], [0, 256])

# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

# Color histogram

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
colors = ("b", "g", "r")
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

while True:
    if cv.waitKey(20) & 0xFF == ord("q"):
        break
