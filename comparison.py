import cv2
import numpy as np

image1 = cv2.imread("spot1.png")
image2 = cv2.imread("spot2.png")

original = image1

difference = cv2.subtract(image1, image2)

imgGray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgGray, 127,255,0)
contours, hierrarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow("Comparison 2", original)
cv2.imshow("Comparison 1", image2)
cv2.drawContours(image1, contours, -1, (0,0,0), 3)
cv2.imshow("Result", image1)

cv2.waitKey(0)

cv2.destroyAllWindows()

