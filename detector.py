import cv2
import numpy as np


class Detector:
    @classmethod
    def detect(cls, inputImage):
        '''Detects digits and math symbols from input image and returns croped images.
        Expects image to be clean of noise and on white paper'''

        grayscaleImage = cls.__createGrayscaleImage(inputImage)

        boundingBoxes = cls.__getBoundingBoxes(grayscaleImage)

        boundingBoxes = cls.__sortBoundingBoxes(boundingBoxes)

        cropedImages = cls.__cropImages(inputImage, boundingBoxes)

        return cropedImages


    @classmethod
    def __createGrayscaleImage(cls, inputImage):
        grayscaleImage = cv2.cvtColor(inputImage, cv2.COLOR_BGR2GRAY)

        return grayscaleImage


    @classmethod
    def __getBoundingBoxes(cls, image):
        

        threshValue, binaryImage = cv2.threshold(
            image, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

        contours, hierarchy = cv2.findContours(
            binaryImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        boundingBoxes = []

        for c in contours:
            boundRect = cv2.boundingRect(c)
            boundingBoxes.append(boundRect)

        return boundingBoxes


    @classmethod
    def __sortBoundingBoxes(cls, boundingBoxes):
        return sorted(boundingBoxes, key=lambda x: x[0])


    @classmethod
    def __cropImages(cls, image, boundingBoxes):
        cropedImages = []
        
        for box in boundingBoxes:
            rectX = box[0]
            rectY = box[1]
            rectWidth = box[2]
            rectHeight = box[3]

            rectArea = rectWidth * rectHeight

            minArea = 10

            if rectArea > minArea:
                currentCrop = image[rectY : rectY + rectHeight, rectX : rectX + rectWidth]
                cropedImages.append(currentCrop)

        return cropedImages
