from Crypto.PublicKey import RSA 
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

rsa_key = RSA.generate(2048) 
private_key = rsa_key.exportKey()
public_key = rsa_key.publickey().exportKey()
fPub = open("public.pem","wb")
fPub.write(public_key)
fPub.close()
fPriv = open("private.pem","wb")
fPriv.write(private_key)
#f = fPriv.read() 
fPriv.close()
#f = RSA.importKey(open("private.pem","r+"))
#print(f.size())


