#defining mqtt as the library
import paho.mqtt.client as mqtt
import os

#when its connected, display the message 
def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc));
  client.subscribe("dev/test");

#if the message is equal to this string then print 
def on_message(client, userdata, msg):
    #check if file exists, if so then delete
    if os.path.exists("/home/pi/dataFiles.txt") :
        os.remove("/home/pi/dataFiles.txt");
    #creates the file to write received data in
    f = open("/home/pi/dataFiles.txt","a");
    #set message = payload received
    message = msg.payload;
    #write the message into the document
    f.write(message);
    #close the document
    f.close();
    
    client.disconnect();

#broker address
broker_address = "192.168.1.131";

#Name of the pi    
client = mqtt.Client("Pi-2");

#connect to broker
client.connect(broker_address);

client.on_connect = on_connect;
client.on_message = on_message;

client.loop_forever();
    