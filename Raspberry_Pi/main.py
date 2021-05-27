import boto3
# Before upload it to RPi you need to add "#", before import botostubs. It nothing changes, only needed to colour in VS Code :D
import botostubs
from datetime import datetime
from time import sleep
import RPi.GPIO as GPIO

def toggle ():
    with open ("last_mode.txt", "r") as last:
        last_str = last.read()
    with open ("last_mode.txt", "w") as last:
        if (last_str == "True"):
            GPIO.output(21, GPIO.LOW)
            last.write("False")
        else:
            GPIO.output(21, GPIO.HIGH)
            last.write("True")
        


def check ():
    s3 = boto3.resource("s3")
    with open("last_modified.txt", "r") as file:
        last = file.read()
    last = last.replace("-", "/")
    last = datetime.strptime(last, "%Y/%m/%d %H:%M:%S%z")
    now = s3.Object("light-control-app", "mode.txt").__getattribute__("last_modified")
    if (now > last):
        with open("last_modified.txt", "w") as file:
            file.write(str(now))
        return True
    return False


GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

while True:
    if (check()):
        s3 = boto3.resource("s3")
        print("Zmienilo sie", datetime.now())
        toggle()
    else:
        print("Nie ma nic nowego", datetime.now())
    sleep(5)
