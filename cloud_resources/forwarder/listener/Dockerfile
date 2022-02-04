FROM alpine:latest
ENV PYTHONUNBUFFERED=1
RUN apk update && apk add -y python3 python3-pip
RUN sudo apt install -y mosquitto-clients

COPY listener.py listener.py

CMD ["python3","listener.py"]
