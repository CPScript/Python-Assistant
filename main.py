import time
time.sleep(5)
print("Assistant powering on...")
time.sleep(2)
print("Loading...")
time.sleep(5)
print(" ")
print(" ")
print("Done")
print("<3")
from subprocess import call
call(["python", "python-helper"])
time.sleep(1)
## REMENDER add another FailSafe if the Main FailSafe doesn't work.
