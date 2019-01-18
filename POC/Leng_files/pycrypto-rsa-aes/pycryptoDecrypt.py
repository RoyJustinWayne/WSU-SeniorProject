from Crypto.Cipher import AES, PKCS1_OAEP 
from Crypto.PublicKey import RSA 

encrypted = open("testData.txt","r+b") 

decKey = RSA.importKey(open("private.pem",'r').read())
enc_session_key = open("ses_key.txt",'rb').read()
decrypted = PKCS1_OAEP.new(decKey)
dec_rsa = decrypted.decrypt(enc_session_key) 
print(dec_rsa)
iv="this is a new !!"
encBytes = bytes(encrypted.read())
cipher_aes = AES.new(dec_rsa,AES.MODE_CFB,iv)
dec_aes = cipher_aes.decrypt(encBytes)
print(dec_aes)
encrypted.seek(0)
encrypted.truncate()
encrypted.write(dec_aes)


