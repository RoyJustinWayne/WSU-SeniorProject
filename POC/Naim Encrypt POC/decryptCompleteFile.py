from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

 
fobj = open('wholeFile.txt', 'r+')
    
private_key = RSA.import_key(open('private.pem').read())
 
enc_session_key, nonce, tag, ciphertext = [ fobj.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]
print(len(ciphertext))
cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(enc_session_key)
    
cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
data = cipher_aes.decrypt_and_verify(ciphertext, tag)

#test
print(data.decode("utf-8"))

#clear and write
fobj.seek(0)
fobj.truncate()
fobj.write(data)
 
