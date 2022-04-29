import numpy as np
import cv2
import base64
from io import BytesIO
from detector import Detector
from classifier import Classifier
from calculator import Calculator
from flask import Flask, render_template, request
import os


detector = Detector()
classifier = Classifier()
calculator = Calculator()

def decodeImage(name):
    imStr = request.form[name]
    imStr = imStr.split(",")[1]
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
        symbol = classifier.clasify(data["image"])
        symbols.append(symbol)
    
    expresion = ''.join(symbols)

    try:
        result = { "result": calculator.calculate(expresion) }
    except:
        result = { "result": "Unable to calculate" }

    return result


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
