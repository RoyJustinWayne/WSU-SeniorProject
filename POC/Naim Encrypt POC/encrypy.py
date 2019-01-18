import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import paho.mqtt.client as mqtt

broker_address = "10.0.2.15"
client = mqtt.Client("Pi-1")
client.connect(broker_address)

# print(os.stat("vera.txt").st_mtime)
# filepwd = open('.pwdkey.txt','r').read()
# print(filepwd)

# if os.path.exists(".pwdkey.txt"):
#     os.remove(".pwdkey.txt")
# else:
#     print("File does not exist")

# password = filepwd.encode() #converts to bytes utf-8
# print(password)
# password = b"password"
key = Fernet.generate_key()
print("before     " + key)
salt = os.urandom(16)
kdf = PBKDF2HMAC(
     algorithm=hashes.SHA256(),
     length=32,
     salt=salt,
     iterations=100000,
     backend=default_backend()
 )
key2 = base64.urlsafe_b64encode(kdf.derive(key))
print("After      " + key2)

f = Fernet(key2)

message = b" This is secret"
print(message)

token = f.encrypt(message)
print(token)

client.publish("test",token)

decrypt = f.decrypt(token)
print(decrypt)

if os.path.exists("test.txt"):
    modified = os.stat("test.txt").st_mtime

    
    with open("test.txt","r+") as fp:
        line = fp.readline()
        lineToken = []
        i = 0
        while line:
            print(line)
            lineToken.append(f.encrypt(line)) 
            # print (lineToken)
            # decryptLine = f.decrypt(lineToken)
            # print(decryptLine)
            # fp.seek(0)
            # fp.write(lineToken)
            # fp.truncate()
            line = fp.readline()
            i = i + 1
        fp.write("\n".join(lineToken))
        fp.close()

else:
    print ("File Does Not Exist")

