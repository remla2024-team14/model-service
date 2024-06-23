import os
import urllib


def fetch_model_from_s3_bucket(model_name):
    destination_path = os.path.join("models", model_name)
    if os.path.isfile(destination_path):
        return destination_path
    bucket_path = 'https://team14awsbucket.s3.amazonaws.com/' + model_name
    urllib.request.urlretrieve(bucket_path, destination_path)
    return destination_path


if __name__ == "__main__":
    destination_path = fetch_model_from_s3_bucket("model.h5")
    print(destination_path)
