import cv2
import numpy as np


def ApplyFilter(img):

    filtered = img
    gradientX = img
    gradientY = img

    gx = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])

    gy = np.array([[-1, -2, -1],
                   [0, 0, 0],
                   [1, 2, 1]])


    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):

            localMat = img[i - 1:i + 2, j - 1:j + 2]

            if (localMat.shape[0] == 3 and localMat.shape[1] == 3 and localMat.any()):
                xMat = localMat * gx
                yMat = localMat * gy
                GX = xMat.sum()
                GY = yMat.sum()

                gradientX[i -1, j -1] = GX
                gradientY[i -1, j -1] = GY

                G = np.sqrt((GX * GX) + (GY * GY))

                filtered[i - 1, j - 1] = G


    # Show the image
    #cv2.imshow("Sobel Filter", filtered)


    return filtered, gradientX, gradientY