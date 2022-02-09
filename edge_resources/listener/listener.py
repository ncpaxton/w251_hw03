import paho.mqtt.client as mqtt

LOCAL_MQTT_HOST="10.43.235.231"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="mypub"
REMOTE_MQTT_HOST="3.238.68.160"
REMOTE_MQTT_PORT=1883
REMOTE_MQTT_TOPIC="mypub"


def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)

def on_message(client, userdata, msg):
  try:
    print("message received: ",str(msg.payload.decode))
    # if we wanted to re-publish this message, something like this should work
    msg = msg.payload
    remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()

local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

remote_mqttclient = mqtt.Client()

remote_mqttclient.connect(REMOTE_MQTT_HOST, REMOTE_MQTT_PORT, 60)
#time.sleep(5)
remote_mqttclient.loop_start()
# go into a loop

local_mqttclient.loop_forever()

