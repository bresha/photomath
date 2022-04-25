import numpy as np
import cv2
import tensorflow as tf
from tensorflow import keras




class Classifier:
    def __init__(self):
        self.CLASSES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '(', ')']
        self.model = keras.models.load_model("model2")


    def clasify(self, image):
        '''Clasifies symbol of image'''

        squaredImage = self.__squareImage(image)

        resizedImage = cv2.resize(squaredImage, (45, 45), interpolation=cv2.INTER_CUBIC)

        imageBatch = tf.expand_dims(resizedImage, 0)     

        predictions = self.model.predict(imageBatch)

        index = np.argmax(predictions)

        symbol = self.CLASSES[index]

        return symbol


    def __squareImage(self, image):
        height, width, _ = image.shape

        dimension = height if height > width else width

        square = np.full((dimension,dimension,3), 255, np.uint8)

        square[int((dimension-height)/2):int(dimension-(dimension-height)/2), int((dimension-width)/2):int(dimension-(dimension-width)/2)] = image

        return square