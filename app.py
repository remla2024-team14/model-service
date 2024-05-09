from flask import Flask, request
from tensorflow.keras.models import load_model
import numpy as np
from lib_ml.preprocessing import TextPreprocessor

from utils import fetch_model_from_s3_bucket

app = Flask(__name__)


@app.route("/predict", methods=['POST'])
def run_inference():
    content = request.json
    model_name = content['model_name']
    input_url = [content['input_url']]

    preprocessor = TextPreprocessor()
    preprocessor.fit_text(input_url)
    processed_texts = preprocessor.transform_text(input_url)

    model_path = fetch_model_from_s3_bucket(model_name)
    model = load_model(model_path)

    y_pred = model.predict(processed_texts)
    y_pred = 0 if y_pred < 0.5 else 1

    if y_pred == 1:
        return "Phishing"
    else:
        return "Valid"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
