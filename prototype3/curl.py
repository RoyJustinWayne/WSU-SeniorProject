import requests
import os
from getOldest import oldest
from pycryptoDecrypt import decrypt
from alert import alertSMS

#url = "https://cxdp3vrdt6.execute-api.us-east-2.amazonaws.com/dev/verifyKey"
#headers = {"X-API-Key":"7NYpat2DyO6yqh6EqXSah924XRzVeBi26TEPcwfx"}
#data = '{"key":"ffb97bc80462cbeca180"}'


#r = requests.post(url = url, headers = headers, data = data) 


#if (r.status_code == 200):
 #   print("Key Verified.")
    #f = open(str(keyFile), 'w')
    #f.write(key)
   # f.close()
    #verified = True
#elif (r.status_code == 400):
 #   print("Invalid API key. Please try again.")
#elif (r.status_code == 409):
 #   print("API key already taken. Please try again with an unused API key.")
#else:
#    print("Something went wrong with the server.")

urlP = "https://l4m03tep94.execute-api.us-east-2.amazonaws.com/post1/sensordata"
headersP = {"X-API-Key":"KIfI3IStxB6PgOXj014cN1DwoS2kpqRh5gsFlpjT"}
old = oldest()
dataP = decrypt(oldest())
print(dataP)

alertSMS(dataP)

post = requests.post(url = urlP, headers = headersP, data = dataP) 



if (post.status_code == 200):
    print("Data Sent.")
    os.remove(old)
    #f = open(str(keyFile), 'w')
    #f.write(key)
   # f.close()
    #verified = True
elif (post.status_code == 400):
    print("Invalid Please try again.")
elif (post.status_code == 409):
    print("Messed up.")
else:
    print("Something went wrong with the server.")

