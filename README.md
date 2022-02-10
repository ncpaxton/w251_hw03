# Homework 3 for Deep Learning at the Edge and in the Cloud
This repo contains the introductory pipeline from a jetson edge device to an AWS cloud instance. The message fabric used to provide communication between the edge and cloud components is MQTT which is a well-known fabric for IoT communications. Docker containers were used to package all the components and the slim version of Kubernetes (k3s) to orchastrate the containers.

## Commands used to run the project
To run this project, you first have to navigate to the folders that contain the dockerfiles used to build the containers used for the components. The solution given in this repo utilizes kubernettes for both the cloud and the edge components, so once the containers are built, they need to be tagged and pushed to the docker.hub registery. Once the containers have all been uploaded in the registery they should be launched in this mannor:
- Cloud Containers
  - Broker: kubectl apply -f mosquitto.yaml
  - Service: kubectl apply -f faceService.yaml
  - Forwarder: kubectl apply -f forwarder.yaml
  - Expose Port: kubectl expose deployment mosquitto-deployment --type=NodePort --port=1883 --name=cbroker
- Edge Containers
  - Broker: kubectl apply -f face_deploy.yaml
  - Service: kubectl apply -f faceService.yaml
  - Logger/forwarder/Capture: kubectl apply -f face_logger_deploy.yaml

## Edge Component Details
- Jetson SUB Mini PC-Blue, with Jetson Xavier NX module
- Container 1 (Alpine Base): MQTT Broker
- Container 2 (Ubuntu Base): MQTT Client which detects video and sends captured face images to a MQTT Broker that is local to the edge device and in the cloud
- Container 3 (Ubuntu Base): MQTT Client which logs details regarding the captured face images from the video stream

## Cloud Component Details
- AWS Virtual Machine Host (Ubuntu Base): T2.Small Instance
- Container 1 (Alpine Base): MQTT Broker
- Container 2 (Ubuntu Base): MQTT Client which detects bytes from the image stream sent from the edge and sends it to an S3 Bucket
- S3 Bucket: AWS Object storage which was created in the console and utilized for persistant storage of the captured images

## MQTT and QoS
This project uses a video camera for the sensor, the jetson nx for the edge and aws for the cloud components. In order to facilitate the movement through each component, we utilize MQTT. To facilitate communciation, the MQTT client running on the NX device publishes the real-time image captures in binary format to the MQTT Brokers on a topic channel. In this case we only utilize a video sensor. In our pipeline on the jetson, we have a logger that is subscribed to the local broker topic, so it will receive any messages published to that channel. This is the same for the forwarder that is located on the cloud based MQTT Broker. It is important to note that the topics on the local and remote sides do not have to match. 

For QoS which stands for Quality of Service, there are three options:
- 0 - at most once
- 1 - at least once
- 2 - Exactly one

QoS 0 provides a best effort delivery, meaning that it does not guarantee delivery
QoS 1 provides a guarantee of delivery of at least once to the reciever. Multiple deliveries are also possible.
QoS 2 guarantees that the message is received once. It is the safest, but the slowest QoS

In this pipeline we used the QoS 0 level which did not provide a guarantee.

## Links to S3 Bucket Images
Here are a few links to face images sent to S3
- https://nphw3.s3.amazonaws.com/imagesf4ff36af-94ed-497d-bb22-98fcac4c4645.png
- https://nphw3.s3.amazonaws.com/imagesf4715924-e505-4515-b918-9ed23da3b0ea.png
- https://nphw3.s3.amazonaws.com/imagese52471a3-b143-409e-bfc7-f4437584cf5d.png

