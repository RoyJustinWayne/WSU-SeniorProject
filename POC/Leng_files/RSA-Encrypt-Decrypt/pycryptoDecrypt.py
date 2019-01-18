from Crypto.Cipher import AES, PKCS1_OAEP 
from Crypto.PublicKey import RSA 

encrypted = open("testData.txt","r+b") 

decKey = RSA.importKey(open("private.pem",'r').read())
decrypted = PKCS1_OAEP.new(decKey)
dec_rsa = decrypted.decrypt(encrypted.read()) 
print(dec_rsa)

encrypted.seek(0)
encrypted.truncate()
encrypted.write(dec_rsa)
encrypted.close()



