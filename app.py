from flask import Flask, request
from tensorflow.keras.models import load_model
from flask_swagger_ui import get_swaggerui_blueprint
from lib_ml.preprocessing import TextPreprocessor

from utils import fetch_model_from_s3_bucket

app = Flask(__name__)

# Define the Swagger UI blueprint
SWAGGER_URL = '/swagger'
API_URL = '/api/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Phishing Detection App"
    }
)

# Register the Swagger UI blueprint with the app
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

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

    return str(y_pred)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
