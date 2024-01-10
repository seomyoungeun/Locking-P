from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def encrypt(fil, key, filename): 
    key *= 16
    key = key[:16]
    iv = os.urandom(16)
    
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    padded_fil = pad(fil.encode('utf-8'), 16)
    
    ciphertext = cipher.encrypt(padded_fil)
    
    f = open(filename, 'wb')
    f.write(iv + ciphertext)
    f.close()

def decrypt(fil, key, filename):
    key *= 16
    key = key[:16]
    iv = fil[:16]
    ciphertext = fil[16:]
    
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    decrypted_fil = unpad(cipher.decrypt(ciphertext), 16)
        
    f = open(filename, 'w')
    f.write(decrypted_fil)
    f.close()
