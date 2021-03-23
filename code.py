# importing the required packages for cryptographt(enc and dec) from Crypto import Random
from Crypto.Cipher import AES
# importing the os package for specifying the file path and directory import os
import os.path
from os import listdir
from os.path import isfile, join import time
# importing boto3 for connecting this jupyter to AWS cloud import boto3
from botocore.client import Config # creating a class for enc
class Encryptor:
def	init	(self, key): self.key = key



# creating a definition for padding, encryption and encrypting file def pad(self, s):
return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encrypt(self, message, key, key_size=256): message = self.pad(message)
iv = Random.new().read(AES.block_size) cipher = AES.new(key, AES.MODE_CBC, iv) return iv + cipher.encrypt(message)
def encrypt_file(self, file_name): with open(file_name, 'rb') as fo:
plaintext = to.read()
enc = self.encrypt(plaintext, self.key) with open(file_name + ".enc", 'wb') as fo:
fo.write(enc) os.remove(file_name)
 
#automatically uploading the enc file into the AWS cloud

ACCESS_KEY_ID = 'AKIAI6MEGNRDGR5Y3Q3Q' ACCESS_SECRET_KEY =
'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'
BUCKET_NAME = 'sudhir1266'
data = open(file_name+'.enc', 'rb') s3 = boto3.resource(
's3',
aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=ACCESS_SECRET_KEY, config=Config(signature_version='s3v4')
)
s3.Bucket(BUCKET_NAME).put_object(Key=file_name+'.enc', Body=data)
# creating def for dec and dec the file def decrypt(self, ciphertext, key):
iv = ciphertext[:AES.block_size]
cipher = AES.new(key, AES.MODE_CBC, iv) plaintext = cipher.decrypt(ciphertext[AES.block_size:]) return plaintext.rstrip(b"\0")

def decrypt_file(self, file_name): with open(file_name, 'rb') as fo:
ciphertext = fo.read()
dec = self.decrypt(ciphertext, self.key) with open(file_name[:-4], 'wb') as fo:
fo.write(dec) os.remove(file_name)

# automatically uploading the dec file in the AWS cloud

ACCESS_KEY_ID = 'AKIAI6MEGNRDGR5Y3Q3Q' ACCESS_SECRET_KEY =
'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'
BUCKET_NAME = 'sudhir1266'

data = open(file_name[:-4], 'rb')
 
s3 = boto3.resource( 's3',
aws_access_key_id=ACCESS_KEY_ID,
aws_secret_access_key=ACCESS_SECRET_KEY, config=Config(signature_version='s3v4')
)
s3.Bucket(BUCKET_NAME).put_object(Key=file_name[:-4], Body=data) #assigning the key
key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\ xc4\x94\x9d(\x9e'

enc = Encryptor(key)
clear = lambda: os.system('cls')

# have to enter the password for the crypto process and that pwd will stored in the data.txt and it will be always in the enc format

if os.path.isfile('data.txt.enc'): while True:
password = str(input("Enter password: ")) enc.decrypt_file("data.txt.enc")
p = ''
with open("data.txt", "r") as f: p = f.readlines()
if p[0] == password: enc.encrypt_file("data.txt")
break
# user have to enter the choice for the operation while True:
clear()
choice = int(input(
"1. Press '1' to encrypt file.\n2. Press '2' to decrypt file.\n3. Press '3' to exit.\n"))
clear()
if choice == 1:
enc.encrypt_file(str(input("Enter name of file to encrypt: "))) elif choice == 2:
enc.decrypt_file(str(input("Enter name of file to decrypt: ")))
elif choice == 3: exit()
 
else:
print("Please select a valid option!")

else:
while True: clear()
password = str(input("Setting up stuff. Enter a password that will be used
for decryption: "))
repassword = str(input("Confirm password: ")) if password == repassword:
break
else:
print("Passwords Mismatched!") f = open("data.txt", "w+") f.write(password)
f.close() enc.encrypt_file("data.txt")
print("Please restart the program to complete the setup")
time.sleep(15)
