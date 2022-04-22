import numpy as np
import cv2
import tensorflow as tf
from tensorflow import keras


CLASSES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '(', ')']

class Classifier:
    @classmethod
    def clasify(cls, image):
        '''Clasifies symbol of image'''

        squaredImage = cls.__squareImage(image)

        resizedImage = cv2.resize(squaredImage, (45, 45), interpolation=cv2.INTER_CUBIC)

        imageBatch = tf.expand_dims(resizedImage, 0)

        model = keras.models.load_model("model2")

        predictions = model.predict(imageBatch)

        index = np.argmax(predictions)

        symbol = CLASSES[index]

        return symbol


    @classmethod
    def __squareImage(cls, image):
        height, width, _ = image.shape

        dimension = height if height > width else width

        square = np.full((dimension,dimension,3), 255, np.uint8)

        square[int((dimension-height)/2):int(dimension-(dimension-height)/2), int((dimension-width)/2):int(dimension-(dimension-width)/2)] = image

        return square