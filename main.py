import cv2
import numpy as np
import gaussianFilter as gauss
import sobelFiler as sobel
import cannyFilter as canny

if __name__ == '__main__':

    sonic = cv2.imread("test.jpg", 0)
    cv2.imshow("Original", sonic)

    gaussSonic = gauss.ApplyFilter(sonic)

    sobelSonic, gradientX, gradientY = sobel.ApplyFilter(gaussSonic)

    canny.ApplyFilter(sobelSonic, gradientX, gradientY, 60, 150)


    cv2.imshow("Result", cv2.Canny(sonic, 150, 200))
    cv2.waitKey()
    
    
    