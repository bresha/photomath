import numpy as np
import cv2
from detector import Detector


img = cv2.imread("samples/oneminustwo.jpg")

cropedImages = Detector.detect(img)

for c in cropedImages:
    cv2.imshow("crop", c)
    cv2.waitKey(0)

cv2.destroyAllWindows()