import os 
import time 
from twilio.rest import Client

def pinging():
    pingCounter = 3
    for i in range(3): 
      ping = os.system("ping google.com")
      if ping == 0:
          pingCounter = pingCounter+1 
          if pingCounter != 0:
                print("Host reachable") 
      if ping != 0 :
          pingCounter = pingCounter-1
          if pingCounter == 0:
                print("Host unreachable")
                client = Client("AC103bb915a505ca4396131fd13083d65b","c1a2cee547aab1fb8340b838b5a3c2ce")
                client.messages.create(to="+13137595683",from_="+15862572867",body="A pi is down,please check") 
                
pinging(); 
