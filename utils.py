import os
import boto3
from dotenv import load_dotenv


load_dotenv()


def fetch_model_from_s3_bucket(model_name):
    destination_path = os.path.join("models", model_name)
    if os.path.isfile(destination_path):
        return
    s3 = boto3.client('s3', aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                      aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"))
    s3.download_file('url-phishing-models', model_name, destination_path)


if __name__ == "__main__":
    fetch_model_from_s3_bucket("model.h5")
