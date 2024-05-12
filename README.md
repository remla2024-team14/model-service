# model-service
A Flask server to serve model predictions

### Remote fetching of models

In order to avoid the model being added to the image and to make it interchangeable without re-building the image, the model is stored in an AWS bucket. The following environment variables are needed:

AWS_ACCESS_KEY_ID=`aws_access_key_id`
AWS_SECRET_ACCESS_KEY=`aws_secret_access_key`


## How to: Custom Docker Network
If you haven't already, you should make a docker network to make sure that the ip address stays the same when running the image. 
*Note: `app` and `model service` have to be on the same network*.
You can do this by executing this command in terminal: `docker network create --subnet=172.0.0.0/16 <yournetworkname>`.

To build your Docker image, execute the following command in your terminal: `docker build .`
To start a container from your image, use this command: `docker run -p 5000:5000 --net <yournetworkname> --ip <ip-arg> --name appcontainer <yourappimghash>`

- Replace `<yournetworkname>` with your chosen network name
- Replace `<ip-arg>` with some ip matching your subnet e.g. `172.0.0.4`. This argument serves as part of your `MODEL_SERVICE_URL`. *Note: It has to be different from the IP of the app.*
- Replace `<yourappimghash>` with the actual hash or tag of your Docker image.
