import cv2
import numpy as np
import gaussianFilter as gauss
import sobelFiler as sobel
import cannyFilter as canny

if __name__ == '__main__':

    sonic = cv2.imread("sonic.jpg", 0)
    cv2.imshow("Original", sonic)
    #cv2.imshow("Result", cv2.Canny(sonic, 150, 200))

    gaussSonic = gauss.ApplyFilter(sonic)

    sobelSonic, gradientX, gradientY = sobel.ApplyFilter(gaussSonic)

    gx = cv2.Sobel(sonic, cv2.CV_32F, 1, 0)
    gy = cv2.Sobel(sonic, cv2.CV_32F, 0, 1)

    mag, ang = cv2.cartToPolar(gx, gy)

    canny.ApplyFilter(mag, gradientX, gradientY, 110, 175)

    cv2.waitKey()
