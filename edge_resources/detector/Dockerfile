FROM ubuntu:latest  ENV DEBIAN_FRONTEND noninteractive#ENV PYTHONUNBUFFERED=1
RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-opencv mosquitto-clients libopencv-dev
RUN pip3 install paho-mqtt
RUN pip install paho-mqtt
RUN pip3 install Cython
RUN pip3 install numpy
WORKDIR /app
# example from https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
COPY face_capture2.py face_capture2.py
COPY haarcascade_frontalface_default.xml haarcascade_frontalface_default.xml
CMD ["python3","face_capture2.py"]
