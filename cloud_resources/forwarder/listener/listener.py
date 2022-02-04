import paho.mqtt.client as mqtt
import boto3
from botocore.exceptions import ClientError
import os


#s3client = boto3.client('s3', region_name='us-east-1')
#bucketname = 'nphw3'

LOCAL_MQTT_HOST="localhost"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="mypub"

#first_file_name = create_temp_file(msg)
#first_object = s3_resource.Object(bucket_name=first_bucket_name, key=first_file_name)

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)

def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)
        s3_client = boto3.client('s3',aws_access_key_id="AKIAXFMHW5EMQG5FYNA5",
                aws_secret_access_key="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")
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def on_message(client, userdata, msg):
    try:
        id = str(uuid.uuid4())
        print("messae received: ",str(msg.paylode.decode))
        f = open("images" + id + ".png", "wb")
        f.write(msg.payload)
        #msg = msg.payload
        f.close()
        upload_file("images" + id + ".png", "nphw3")
       #file_to_read = msg

       # fileobj = s3client.get_object(
       #         Bucket=bucketname,
       #         Key=file_to_read
       #         )
    except:
        print("Unexpected error:", sys.exc_info()[0])
    # return msg



local_mqttclient = mqtt.Client()

local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

#s3_client = boto3.client('s3')
#with open(msg, "rb") as f:
#    s3.upload_fileobj(f, "nphw3")


local_mqttclient.loop_forever()
