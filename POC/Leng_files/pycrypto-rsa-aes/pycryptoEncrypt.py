from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

with open("testData.txt","r+b") as f:
	#import public key
	key = RSA.importKey(open("public.pem","r").read()) 
	#print pub key
	print(key)
	session_key = "1234567891011121"
	#put public key into correct format
	cipher_rsa = PKCS1_OAEP.new(key) 
	print(cipher_rsa)
	#enc key with the session key 
	enc_session_key = cipher_rsa.encrypt(session_key)
	print(enc_session_key)
	iv="this is a new !!"
	ses_key = open("ses_key.txt","r+b") 
	ses_key.seek(0)	
	ses_key.write(enc_session_key)
	fbytes = bytes(f.read())
	cipher_aes = AES.new(session_key, AES.MODE_CFB,iv) 
	encrypted = cipher_aes.encrypt(fbytes)
	f.seek(0)
	f.truncate()
	f.write(encrypted)

	


