import os
import requests
import datetime
import sys
from pathlib import Path
from collections import OrderedDict

f = open(r"C:\users\lengl\Desktop\sensor_data.txt","r")
print("Opened")

for line in f:
    colIndex=0
    linedata = OrderedDict()
    linedata["created_at"] = ""
    linedata["apikey"] = ""
    linedata["temperature"] = ""
    linedata["humidity"] = ""
    linedata["pressure"] = ""
    linedata["latitude"] = ""
    linedata["longitude"] = ""

line = line.rstrip('\n')
line = [col.strip() for col in line.split(',')]

for col in linedata:
    linedata[col] = line[colIndex]
    colIndex += 1
    

print(linedata)
f.close()

nf = open(r"C:\users\lengl\Desktop\sensor_test.txt","w")
nf.write(linedata["created_at"])
nf.write(linedata["apikey"])
nf.write(linedata["temperature"])
nf.write(linedata["humidity"])
nf.write(linedata["pressure"])
nf.write(linedata["latitude"])
nf.write(linedata["longitude"])
nf.close() 