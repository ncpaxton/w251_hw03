FROM ubuntu:latest
ENV DEBIAN_FRONTEND noninteractive

ENV PYTHONUNBUFFERED=1

RUN apt-get update
RUN apt-get install -y python3 python3-pip mosquitto-clients
RUN pip3 install paho-mqtt
RUN pip3 install numpy
RUN pip3 install boto3
WORKDIR /app


COPY listener.py listener.py

CMD ["python3","listener.py"]
