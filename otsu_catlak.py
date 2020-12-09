import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math


img_color = cv.imread('Hot-crack.jpg')
#img_color=cv.resize(img_color,(500,500))
cv.imshow("org", img_color)
img = cv.imread('Hot-crack.jpg',0)


otsu_threshold, treshold = cv.threshold(img, 200, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)



cv.imshow("treshold",treshold)
blur = cv.GaussianBlur(img, (5, 5), 0)
#cv.imshow("blur",blur)
edges = cv.Canny(blur, 50, 200)
#cv.imshow("canny",edges)
lines = cv.HoughLinesP(edges, 1, np.pi/180, 200, minLineLength=1, maxLineGap=10)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(img_color, (x1, y1), (x2, y2), (255, 0, 0), 3)


img_color=cv.resize(img_color,(500,500))
cv.imshow("resultt",img_color)

cv.waitKey()
