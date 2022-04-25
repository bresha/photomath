import numpy as np
import cv2
from detector import Detector
from classifier import Classifier
from calculator import Calculator


expresion = "-((-(20+10)*(-10+20)*(10-20))/2)" #  -1500

calc = Calculator()
print(calc.calculate(expresion))


# img = cv2.imread("samples/onetimestwo.jpg")

# detector = Detector()
# cropedImages = detector.detect(img)

# classifier = Classifier()

# for c in cropedImages:
#     print(c["coordinates"])
#     cv2.imshow("crop", c["image"])
#     cv2.waitKey(0)
#     image = c["image"]
#     print(classifier.clasify(c["image"]))

# cv2.destroyAllWindows()