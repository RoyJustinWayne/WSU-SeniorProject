from Cryptodome.Cipher import AES, PKCS1_OAEP  
from Cryptodome.PublicKey import RSA 
from Cryptodome.Random import get_random_bytes

key = RSA.generate(2048)

def privateKey(): 
    private_key = key.export_key()
    f = open(r"C:\\Users\lengl\Desktop\Crypto\private.pem","wb")
    f.write(private_key)

def publicKey():
    public_Key = key.publickey().export_key()
    j = open(r"C:\\Users\lengl\Desktop\Crypto\public.pem","wb")
    j.write(public_Key)

#open a blank file for writing encrypted data
f = open(r"C:\\Users\lengl\Desktop\Crypto\secret.txt","wb")

#Data to encrypt
data = "Hello this is my test Crypto".encode("utf-8")

#Read Public Key
pubKey = RSA.import_key(open(r"C:\\Users\lengl\Desktop\Crypto\public.pem").read())

#Generate Session Identifier
session_identifier = get_random_bytes(16)

#Create the Encrypted Public Key With the Session Identifier
cipher_rsa = PKCS1_OAEP.new(pubKey)
enc_session_identifier = cipher_rsa.encrypt(session_identifier)

#Encrypt Using AES and the identifier
cipher_aes = AES.new(session_identifier, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(data)
#Make sure file is empty
f.truncate()
#Write the encrypted data into the file
[f.write(x) for x in (enc_session_identifier, cipher_aes.nonce,tag,ciphertext) ]

f = open(r"C:\\Users\lengl\Desktop\Crypto\secret.txt","rb")

#Get the private Key
privateKey = RSA.import_key(open(r"C:\\Users\lengl\Desktop\Crypto\private.pem").read())

#Write the key
enc_session_identifier, nonce, tag, ciphertext = [ f.read(x) for x in (privateKey.size_in_bytes(), 16, 16, -1) ]
#Decrypt with the session identifier
cipher_rsa= PKCS1_OAEP.new(privateKey)
session_identifier = cipher_rsa.decrypt(enc_session_identifier)
#Decrypt using privateKey AES
cipher_aes = AES.new(session_identifier,AES.MODE_EAX,nonce)
data = cipher_aes.decrypt_and_verify(ciphertext, tag)
print(data.decode("utf-8"))