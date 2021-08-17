import paho.mqtt.client as mqtt
import uuid
import threading
import random
import time

def on_message(client, userdata, message):
    print("Received " ,str(message.payload.decode("utf-8")))
    

clientID= str(uuid.uuid4())
client=mqtt.Client(clientID)
client.on_message=on_message

client.connect('127.0.0.1')

client.loop_start()

client.subscribe('/classroom_A/temperature',qos=0)
