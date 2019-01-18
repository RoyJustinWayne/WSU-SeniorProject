import os
import requests
import datetime
import sys
from pathlib import Path
from collections import OrderedDict

def parseServant(f):
    
    #print("Opened")

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
    
    #print(linedata)
    f.close()

    return linedata 