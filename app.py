import numpy as np
import cv2
import base64
from io import BytesIO
from detector import Detector
from classifier import Classifier
from calculator import Calculator
from flask import Flask, render_template, request


detector = Detector()
classifier = Classifier()
calculator = Calculator()

def decodeImage(name):
    imStr = request.form[name]
    imStr = imStr.split(",")[1] #drop prefix "data:image/jpeg;base64,"
    # data = BytesIO(base64.b64decode(imStr))
    nparr = np.fromstring(base64.b64decode(imStr), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img


app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    image = decodeImage("image")

    cropedImages = detector.detect(image)
    sortedImages = sorted(cropedImages, key=lambda x: x["coordinates"][0])

    symbols = []
    for data in sortedImages:
        cv2.imshow("image", data["image"])
        cv2.waitKey(0)
        symbol = classifier.clasify(data["image"])
        print(symbol)
        symbols.append(symbol)
    
    expresion = ''.join(symbols)
    print("Expresion: ", expresion)

    result = calculator.calculate(expresion)

    return result