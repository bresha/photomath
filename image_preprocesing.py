import numpy as np
import cv2
import os


dataDir = "data_copy/"

dirList = os.listdir(dataDir)

for directory in dirList:
    path = os.path.join(dataDir, directory)
    for fileName in os.listdir(path):
        imagePath = os.path.join(path, fileName)

        image = cv2.imread(imagePath)
        kernel = np.ones((3, 3), np.uint8)

        erodedImage = cv2.erode(image, kernel, iterations=1)

        folder = os.path.join(dataDir, directory)

        imagePath = folder + "/" + fileName
        cv2.imwrite(imagePath, erodedImage)
