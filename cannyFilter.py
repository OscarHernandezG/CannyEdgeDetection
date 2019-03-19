import cv2
import numpy as np


def ApplyFilter(scr, gradientX, gradientY, minT, maxT):
    filteredImage = scr.copy()
    rows, cols = gradientX.shape

    angleMatrix = np.zeros((rows, cols))

    # Calculate the angles
    for i in range(0, rows):
        for j in range(0, cols):
            angle = np.rad2deg(np.arctan2(gradientY[i, j], gradientX[i, j]))

            if (23 >= angle >= -23) or (158 <= angle <= 181) or (-180 <= angle <= -158):
                angleMatrix[i, j] = 0
            elif (23 <= angle <= 68) or (-113 >= angle >= -158):
                angleMatrix[i, j] = 45
            elif (68 <= angle <= 113) or (-68 >= angle >= -113):
                angleMatrix[i, j] = 90
            elif (113 <= angle <= 158) or (-23 >= angle >= -68):
                angleMatrix[i, j] = 135

    #angleMatrix = ang
    borderImage = filteredImage.copy()

    # Non-maximum Suppression
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):

            value = filteredImage[i, j]

            if angleMatrix[i, j] == 0:
                if borderImage[i, j - 1] > value or borderImage[i, j + 1] > value:
                    filteredImage[i, j] = 0

            elif angleMatrix[i, j] == 45:
                if borderImage[i + 1, j - 1] > value or borderImage[i - 1, j + 1] > value:
                    filteredImage[i, j] = 0

            elif angleMatrix[i, j] == 90:
                if borderImage[i - 1, j] > value or borderImage[i + 1, j] > value:
                    filteredImage[i, j] = 0

            elif angleMatrix[i, j] == 135:
                if borderImage[i + 1, j + 1] > value or borderImage[i - 1, j - 1] > value:
                    filteredImage[i, j] = 0

    # Decide max and min
    for i in range(0, rows):
        for j in range(0, cols):
            if filteredImage[i, j] > maxT:
                filteredImage[i, j] = 255

            elif filteredImage[i, j] < minT:
                filteredImage[i, j] = 0

    # Select borders
    borderImage = filteredImage.copy()
    for i in range(1, rows - 2):
        for j in range(1, cols - 2):

            if maxT > borderImage[i, j] > minT:
                localMat = borderImage[i - 1:i + 2, j - 1:j + 2]

                if localMat.max() == 255:
                    filteredImage[i, j] = 255
                else:
                    filteredImage[i, j] = 0


    # Show the image
    cv2.imshow("Canny Filter", np.uint8(filteredImage))

    return np.uint8(filteredImage)
