#defining mqtt as the library
import paho.mqtt.client as mqtt
import os
from pi_parser import pi_parser

#when its connected, display the message 
def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc));
  client.subscribe("dev/test");

#if the message is equal to this string then print 
def on_message(client, userdata, msg):
    #check if file exists, if so then delete
    if os.path.exists("dataFiles.txt") :
        os.remove("dataFiles.txt");
    #creates the file to write received data in
    f = open("dataFiles.txt","a");
    #set message = payload received
    message = msg.payload;
    decoded_message = message.decode("utf-8") 
    #write the message into the document
    f.write(decoded_message);
    #close the document
    f.close();
    client.disconnect();
    print("Calling --> Pi_Parser")
    pi_parser()

#broker address
broker_address = "192.168.1.2";

#Name of the pi    
client = mqtt.Client("Pi-2");

#connect to broker
client.connect(broker_address);

client.on_connect = on_connect;
client.on_message = on_message;

client.loop_forever();

