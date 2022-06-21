"""
Python MQTT Subscription client - No Username/Password
Thomas Varnish (https://github.com/tvarnish), (https://www.instructables.com/member/Tango172)
Written for my Instructable - "How to use MQTT with the Raspberry Pi and ESP8266"
"""
import paho.mqtt.client as mqtt
import json
import time

# Don't forget to change the variables for the MQTT broker!
mqtt_topic = "garden"
mqtt_broker_ip = "127.0.0.1" # 
LOG_PATH = "C:/Users/chaav/Projects/log.txt"

client = mqtt.Client()

mostureBuffer = []

# These functions handle what happens when the MQTT client connects
# to the broker, and what happens then the topic receives a message
def on_connect(client, userdata, flags, rc):
    # rc is the error code returned when connecting to the broker
    print ("Connected!", str(rc))
    
    # Once the client has connected to the broker, subscribe to the topic
    client.subscribe(mqtt_topic)
    
def on_message(client, userdata, msg):
    # Every time we get a message, we will log it to a predefined file for now.
    #

    print ("Topic: ", msg.topic + "\nMessage: " + str(msg.payload))
    with open(LOG_PATH, "a") as fi:
        fi.writelines(str(msg.topic) + "\t" + str(msg.payload) + "\n")
    
    # The message itself is stored in the msg variable
    # and details about who sent it are stored in userdata
    print ("user data: ", userdata, "\tclient: ", client)

# Here, we are telling the client which functions are to be run
# on connecting, and on receiving a message
client.on_connect = on_connect
client.on_message = on_message

# Once everything has been set up, we can (finally) connect to the broker
# 1883 is the listener port that the MQTT broker is using
client.connect(mqtt_broker_ip, 1883)

# Once we have told the client to connect, let the client object run itself
client.loop_forever()
client.disconnect()
