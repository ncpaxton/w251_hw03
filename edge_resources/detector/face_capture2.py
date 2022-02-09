import numpy as np
import cv2 as cv
import paho.mqtt.client as mqtt

LOCAL_MQTT_HOST='10.43.235.231'
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="mypub"

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

# Load face cascade. My cascade is in the current folder
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# Alternative face detect

# Read the video stream
cap = cv.VideoCapture(0)
if not cap.isOpened:
    print(' ..(!)Error opening video capture')
    exit(0)
while True:
    #Capture frame by frame
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    # Get the gray frame from the camera capture
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        # Cut out the faces
        face = gray[y:y+h, x:x+w]
	#cv.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 2)
        #roi_color = frame[y:y + h, x:x + w]
        print("[INFO] Object found")
    
        # encode as png
        rc, png = cv.imencode('.png', face)
        cv.imwrite('/image.png/',png) 
        msg = png.tobytes()

        # publish the encoded image to broker
        local_mqttclient.publish(LOCAL_MQTT_TOPIC, msg)
    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.rlease()
cv.destroyAllWindows()


