import paho.mqtt.client as mqtt
import boto3
from botocore.exceptions import ClientError
import os
import cv2
import numpy as np
from datetime import datetime


LOCAL_MQTT_HOST="localhost"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="mypub"

# S3 connection
s3 = boto3.resource('s3')

#data = open('Nvidia_Cloud_EULA.pdf', 'rb')
#s3.Bucket('nphw3').put_object(Key='Nvidia_Cloud_EULA.pdf', Body=data)

#count = 0
#def save_img(img_bytes):
#    global count
#    response = s3client.put_object( 
#    Bucket='nphw3',
#    Body=img_bytes,

#Key='face{:d}.png'.format(count),
#    ACL='public-read',
#    ContentType='image/png'
  )

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)


def on_message(client, userdata, msg):
    try:
        # File Name
        date_t = datetime.now().strftime('%m-%d-%Y-%H-%M-%S')
        image_name = str(date_t) + '_image.png'

        # Save image
        msd = np.frombuffer(msg, np.uint8)
        msg = cv2.imdecode(msd, cv2.IMREAD_COLOR)
        cv2.imwrite(image_name, msg)
        data = msg
        s3.Bucket('nphw3').put_object(Key='image_name', Body=data)

    except:
        print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()

local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message


local_mqttclient.loop_forever()
