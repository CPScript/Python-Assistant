print("Would you like to set up your assistant?")
print ("Yes/No")
choice = input("")

if choice == "yes":
    print("Set up started")
   from subprocess import call
  call(["python", "Setup2.py"])

if choice == "no":
    print("OK...")
    print("Booting Down")
