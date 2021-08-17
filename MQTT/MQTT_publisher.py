import paho.mqtt.client as mqtt
import uuid
import threading
import random
import time




clientID= str(uuid.uuid4())
client=mqtt.Client(clientID)
client.connect('127.0.0.1')

while(True):
    r= random.randint(18,22)
    string=str(r)
    print('Sended: ',string)
    print('Acknowledged: ',client.publish('/classroom_A/temperature',string.encode('utf-8'), qos=1,retain=False))
    time.sleep(2)
