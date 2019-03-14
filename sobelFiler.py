import cv2
import numpy as np


def ApplyFilter(img):

    filtered = img

    gx = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])

    gy = np.array([[-1, -2, -1],
                   [0, 0, 0],
                   [1, 2, 1]])


    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):

            localMat = img[i - 1:i + 2, j - 1:j + 2]

            if (localMat.shape[0] == 3 and localMat.shape[1] == 3):
                xMat = gx * localMat
                yMat = gy * localMat
                GX = xMat.sum()
                GY = yMat.sum()

                G = np.sqrt((GX * GX) + (GY * GY))

                filtered[i - 1, j - 1] = G

    cv2.imshow("Sobel Filter", filtered)

    return filtered