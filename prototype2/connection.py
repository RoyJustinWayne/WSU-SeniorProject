#define mqtt as the library
import paho.mqtt.client as mqtt

#define broker address
broker_address = "192.168.1.131";

#define the client name 
client = mqtt.Client("Pi-1");

#connect to the broker
client.connect(broker_address);

#publish to the broker
client.publish("dev/test","Hello World");

