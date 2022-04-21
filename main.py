import numpy as np
import cv2
from detector import Detector


img = cv2.imread("samples/onetimestwo.jpg")

cropedImages = Detector.detect(img)

for c in cropedImages:
    print(c["coordinates"])
    cv2.imshow("crop", c["image"])
    cv2.waitKey(0)

cv2.destroyAllWindows()