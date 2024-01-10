import crypto_m as cr
import save_m as sa
import zip_m as zi
import check_m as ch
import os

order = input("order : ")

filename = input("filename : ")
if filename.find('.') == -1:
    filename = zi.zip(filename)

f = open(filename, 'rb')
fil = f.read()
f.close()

if order == 'enc':
    key = input("password : ")
    cr.encrypt(fil, key, filename)
    sa.save(fil, key)
    print('Encrypt success')

elif order == 'dec':
    key = input("password : ")
    if ch.check(fil, key):
        cr.decrypt(fil, key, filename)
        print('Decrypt success')
    else:
        print('password wrong')

dir_name = os.getcwd()
test = os.listdir(dir_name)

for item in test:
    if item.endswith(".pyc"):
        os.remove(os.path.join(dir_name, item))