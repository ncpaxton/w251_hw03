FROM ubuntu:latest
# this is needed to make sure we can see the log output
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install paho-mqtt 
COPY mylogger.py mylogger
CMD ["python3","mylogger.py"]
