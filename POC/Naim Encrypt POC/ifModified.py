from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import time
import datetime

modified = os.stat("wholeFile.txt").st_mtime

while true:
    if datetime.datetime.now().minute % 5 == 0:
        #put function here
        #wait for file to get new data
        time.sleep(60)
        newModified = os.stat("wholeFile.txt").st_mtime
        if newModified > modified:
            #if modified time changed encrypt or decrypt here

        else:

    time.sleep(60)


with open('wholeFile.txt', 'r+') as out_file:
    recipient_key = RSA.import_key(
        open('public.pem').read())
    session_key = get_random_bytes(16)
         
    f = out_file.read()
    fbyte = f.encode('utf-8')

    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # out_file.write(cipher_rsa.encrypt(session_key))
 
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    # data = b'blah blah blah Python blah blah'
    ciphertext, tag = cipher_aes.encrypt_and_digest(fbyte)
    out_file.seek(0)
    out_file.truncate()
    # out_file.write(cipher_aes.nonce)
    # out_file.write(tag)
    # out_file.write(ciphertext)
    [out_file.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]