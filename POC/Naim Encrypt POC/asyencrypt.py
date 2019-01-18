from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import paho.mqtt.client as mqtt

#Change Adress
broker_address = "10.0.2.15"
client = mqtt.Client("Pi-1")
client.connect(broker_address)

key = RSA.generate(2048)
private_key = key.export_key()
fout = open("private.pem", "wb")
fout.write(private_key)
fout.close()

public_key = key.publickey().export_key()
fout = open("public.pem", "wb")
fout.write(public_key)
fout.close()

#Message to be encrypted
data = "secret message ".encode('utf-8')
print(data)
fout = open("test.txt", "wb")

pub_key = RSA.import_key(open("public.pem").read())
session_key = get_random_bytes(16)

# Encrypt the session key with the public RSA key
cipher_rsa = PKCS1_OAEP.new(pub_key)
enc_session_key = cipher_rsa.encrypt(session_key)

# Encrypt the data with the AES session key
# fout.write('\n')
cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(data)

# [ fout.write(x) for x in (tag, ciphertext) ]
[fout.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]

fout.close()
# enc_session_key, cipher_aes.nonce,
client.publish("test",ciphertext)

print(ciphertext)

