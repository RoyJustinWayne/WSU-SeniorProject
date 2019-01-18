from Crypto.Cipher import PKCS1_OAEP 
from Crypto.PublicKey import RSA

#Used to decrypt the encrypted Weather Data File. Decryption will be using RSA 1024

def decrypt(fileName): 
	try:
		encrypted = open("/home/pi/Desktop/2018-12-09 19:14:55.txt","r+b")
		blankFile = open("/home/pi/Desktop/Blank.txt",'r').read()
		decKey = RSA.importKey(open("/home/pi/Desktop/weather-station-master/client/1024private.pem",'r').read())
		decrypted = PKCS1_OAEP.new(decKey)
		dec_rsa = decrypted.decrypt(encrypted.read()) 
		print(dec_rsa)

		encrypted.seek(0)
		encrypted.truncate()
		encrypted.write(dec_rsa)
		encrypted.close()

	except ValueError as e:
		print ("Decryption Error")
		print ("Returning Blank.")
		dec_rsa = blankFile
		print(dec_rsa)	
	
	return dec_rsa