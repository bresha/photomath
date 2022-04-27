import numpy as np
import cv2
import tensorflow as tf
from tensorflow import keras




class Classifier:
    def __init__(self):
        self.CLASSES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '(', ')']
        self.model = keras.models.load_model("models/model2")


    def clasify(self, image):
        '''Clasifies symbol of image'''

        image[image < 150] = 0

        cv2.imshow("image", image)
        cv2.waitKey(0)

        squaredImage = self.__squareImage(image)

        resizedImage = cv2.resize(squaredImage, (45, 45), interpolation=cv2.INTER_CUBIC)

        imageBatch = tf.expand_dims(resizedImage, 0)     

        predictions = self.model.predict(imageBatch)

        index = np.argmax(predictions)

        symbol = self.CLASSES[index]
        print(symbol)
        return symbol


    def __squareImage(self, image):
        height, width = image.shape

        dimension = height if height > width else width

        square = np.zeros((dimension,dimension), np.uint8)

        square[int((dimension-height)/2):int(dimension-(dimension-height)/2), int((dimension-width)/2):int(dimension-(dimension-width)/2)] = image

        return square