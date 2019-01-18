from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import paho.mqtt.client as mqtt
import os
import fileinput

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

# data = "secret message".encode("utf-8")
# print(data)
# fout = open("en.txt", "wb")

pub_key = RSA.import_key(open("public.pem").read())
session_key = get_random_bytes(16)

# Encrypt the session key with the public RSA key
cipher_rsa = PKCS1_OAEP.new(pub_key)
enc_session_key = cipher_rsa.encrypt(session_key)

# Encrypt the data with the AES session key
# cipher_aes = AES.new(session_key, AES.MODE_EAX)
# ciphertext, tag = cipher_aes.encrypt_and_digest(data)
# [ fout.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
# fout.close()

if os.path.exists("en.txt"):
    modified = os.stat("test.txt").st_mtime

    count = len(open("en.txt").readlines())
    print(count)
    with open("en.txt","r+") as fp:
        line = fp.readlines()
        i=0
        for i in range(count):
            lineNum = line[i].encode("utf-8")
            print(lineNum)
            cipher_aes = AES.new(session_key, AES.MODE_EAX)
            ciphertext, tag = cipher_aes.encrypt_and_digest(lineNum)
            # line[i] = (enc_session_key, cipher_aes.nonce, tag, ciphertext)
            # print(line[i])
            [fp.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
            # fp.write('\n')
        # while line:
        #     print(line[i])
        #     line[i] = line[i].encode("utf-8")
        #     cipher_aes = AES.new(session_key, AES.MODE_EAX)
        #     ciphertext, tag = cipher_aes.encrypt_and_digest(line[i])
        #     print(ciphertext)
        #     # [fp.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
        #     # print (lineToken)
        #     # decryptLine = f.decrypt(lineToken)
        #     # fp.seek(0)
        #     # fp.write(lineToken)
        #     # fp.truncate()
        #     line = fp.readline()
        #     i = i + 1
        # fp.close()

else:
    print ("File Does Not Exist")

# client.publish("test",ciphertext)

# print(ciphertext)

