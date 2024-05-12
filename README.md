# model-service
A Flask server to serve model predictions

### Remote fetching of models

In order to avoid the model being added to the image and to make it interchangeable without re-building the image, the model is stored in an AWS bucket. The following environment variables are needed:

AWS_ACCESS_KEY_ID=`aws_access_key_id`
AWS_SECRET_ACCESS_KEY=`aws_secret_access_key`