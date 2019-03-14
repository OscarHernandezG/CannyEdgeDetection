import cv2
import numpy as np
import gaussianFilter as gauss
import sobelFiler as sobel

if __name__ == '__main__':

    sonic = cv2.imread("sonic.jpg", 0)
    cv2.imshow("Original", sonic)

    largeSonic = np.zeros((sonic.shape[0] + 2, sonic.shape[1] + 2))

    sonic = gauss.ApplyFilter(sonic)

    sobel.ApplyFilter(sonic)


    cv2.waitKey()
    
    
    