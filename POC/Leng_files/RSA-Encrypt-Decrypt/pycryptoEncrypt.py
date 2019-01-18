from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import time
import os

if os.path.isfile("/home/lenglee/WSU-RaspberryPi-WeatherStation/POC/Leng_files/RSA-Encrypt-Decrypt/testData.txt") :
	pass 
else : 
	f = open("testData.txt","w+")
	f.close()

with open("testData.txt","r+b") as f:
	#import public key
	key = RSA.importKey(open("public.pem","r").read()) 
	#print pub key
	print(key)
	#put public key into correct format
	cipher_rsa = PKCS1_OAEP.new(key) 
	print(cipher_rsa)
	#enc key with the session key 
	enc_file = cipher_rsa.encrypt(f.read())
	
	print("Encrypted file is: " , enc_file) 
	f.seek(0)
	f.truncate()
	f.write(enc_file)
	f.close()

time.sleep(2)
os.remove("testData.txt")
time.sleep(2)

#Generate the new file with timestamp
ts = time.gmtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", ts))
t = time.strftime("%Y-%m-%d %H:%M:%S", ts)
f2 = open( t + ".txt", "w")
f2.write (enc_file)
f2.close()
	
	
	


