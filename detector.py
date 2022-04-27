import cv2
import numpy as np


class Detector:
    def detect(self, inputImage):
        '''Detects digits and math symbols from input image and returns croped images.
        Expects image to be clean of noise and on white paper'''

        grayscaleInversedImage = self.__createGrayscaleInversedImage(inputImage)

        boundingBoxes = self.__getBoundingBoxes(grayscaleInversedImage)

        cropedImages = self.__cropImages(grayscaleInversedImage, boundingBoxes)

        return cropedImages


    def __createGrayscaleInversedImage(self, inputImage):
        grayscaleImage = cv2.cvtColor(inputImage, cv2.COLOR_BGR2GRAY)

        inversedImage = cv2.bitwise_not(grayscaleImage)

        return inversedImage


    def __getBoundingBoxes(self, image):
        

        threshValue, binaryImage = cv2.threshold(
            image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        contours, hierarchy = cv2.findContours(
            binaryImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        boundingBoxes = []

        for c in contours:
            boundRect = cv2.boundingRect(c)
            boundingBoxes.append(boundRect)

        return boundingBoxes


    def __cropImages(self, image, boundingBoxes):
        cropedImages = []
        
        for box in boundingBoxes:
            rectX = box[0]
            rectY = box[1]
            rectWidth = box[2]
            rectHeight = box[3]

            rectArea = rectWidth * rectHeight

            minArea = 10

            if rectArea > minArea:
                cropedImageWithCoordinates = {}

                coordinates = (rectX, rectY, rectWidth, rectHeight)

                cropedImageWithCoordinates["coordinates"] = coordinates

                currentCrop = image[rectY : rectY + rectHeight, rectX : rectX + rectWidth]

                cropedImageWithCoordinates["image"] = currentCrop
                
                cropedImages.append(cropedImageWithCoordinates)

        return cropedImages
