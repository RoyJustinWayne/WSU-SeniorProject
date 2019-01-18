from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

######### Decrypt ###############
file_in = open("test.txt", "r+")

private_key = RSA.import_key(open("private.pem").read())

enc_session_key, nonce, tag, ciphertext = \
   [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]

# Decrypt the session key with the private RSA key
cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(enc_session_key)

# Decrypt the data with the AES session key
cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
data = cipher_aes.decrypt_and_verify(ciphertext, tag)
print(data.decode("utf-8"))

#write decrypted back to file
#get rid of these lines to keep encrypted data in file
file_in.seek(0)
file_in.truncate()
file_in.write(data)