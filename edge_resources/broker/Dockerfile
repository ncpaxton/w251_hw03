FROM alpine:latest
RUN apk update
RUN apk add mosquitto
RUN echo "allow_anonymous true" > /etc/mosquitto/mosquitto.conf
RUN echo "listener 1883 0.0.0.0" >> /etc/mosquitto/mosquitto.conf
# Configure to allow remote access
CMD ["mosquitto", "-v","-c","/etc/mosquitto/mosquitto.conf"]
