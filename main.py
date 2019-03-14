import cv2
import numpy as np
import gaussianFilter as gauss
import sobelFiler as sobel

if __name__ == '__main__':

    sonic = cv2.imread("sonic.jpg", 0)
    cv2.imshow("Original", sonic)

    largeSonic = np.zeros((sonic.shape[0] + 2, sonic.shape[1] + 2))

    gaussSonic = gauss.ApplyFilter(sonic)

    sobel.ApplyFilter(sonic)

    canny = cv2.Canny(sonic, 125,200)
    cv2.imshow("Canny", canny)


    cv2.waitKey()
    
    
    