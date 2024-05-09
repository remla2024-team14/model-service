from flask import Flask, request
from tensorflow.keras.models import load_model
import numpy as np

from utils import fetch_model_from_s3_bucket

app = Flask(__name__)


@app.route("/predict", methods=['POST'])
def run_inference():
    content = request.json
    model_name = content['model_name']
    input_url = content['input_url']
    input_url = np.ndarray(input_url)

    model_path = fetch_model_from_s3_bucket(model_name)
    model = load_model(model_path)

    y_pred = model.predict([[input_url]])
    print(y_pred)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
