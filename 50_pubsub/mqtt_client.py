#!/usr/bin/env python3

import paho.mqtt.client as mqtt
from datetime import datetime
import time
import getpass

BROKER = "broker.mqttdashboard.com"  # "mqtt.eclipse.org"
PORT = 1883

TOPIC_BASE = "DIST_SYS"
TOPIC_PUB = TOPIC_BASE + "/ALL"
TOPIC_SUB = TOPIC_BASE + "/ALL"


def setup_mqtt():
    mqttc = mqtt.Client()  # Create a MQTT client object
    mqttc.on_connect = on_connect
    mqttc.on_disconnect = on_disconnect
    mqttc.on_message = on_message
    mqttc.connect(BROKER, PORT, 60)  # Connect to the test MQTT broker
    return mqttc


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Server with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    mqttc.subscribe(TOPIC_SUB, qos=1)

    # publish initial message to MQTT broker
    mqttc.publish(TOPIC_PUB, "Hi there!")


def on_disconnect(client, userdata, rc):
    print("Mqtt Client is now disconnected")
    # sys.exit(1)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Received " + msg.topic + " " + str(msg.payload))


try:
    print("Connecting to mqtt broker")
    mqttc = setup_mqtt()

    # subscription done in on_connect()

    # Start broker main loop in a non-blocking fashion in a separate thread.
    # Processes network traffic, dispatches callbacks and handles reconnecting.
    mqttc.loop_start()
    # Other loop*() functions are available, e.g., a blocking call: client.loop_forever()
    time.sleep(2)
    user = getpass.getuser()
    while True:
        print("Type a message to publish: ")
        msg = input()
        current_time = datetime.now().strftime("%H:%M:%S")
        # publish temp-message to MQTT broker
        mqttc.publish(TOPIC_PUB, current_time + " (" + user + "): " + msg)
        # looks like: '12:04:25 (username): Boom!'
        # time.sleep(5)  # snooze for a sec or 2

except KeyboardInterrupt:
    print("Keyboard interrupt.")
finally:
    print("Bye, bye.")
