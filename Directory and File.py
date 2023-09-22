import os
import time
os.mkdir("CS")
time.sleep(5)
with open("CS/homework.txt","w") as file:
    time.sleep(5)
    file.write("4112029029_吳起維")
    time.sleep(5)
with open("CS/homework.txt","r") as file:
    print(file.read())
    time.sleep(5)
print(f"文件大小:{os.path.getsize('CS/homework.txt')}個位元組")
if os.path.exists("CS/homework.txt"):
    os.remove("CS/homework.txt")
    time.sleep(5)
os.rmdir("CS")