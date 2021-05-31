import boto3
import botostubs
from datetime import datetime
from time import sleep
import RPi.GPIO as GPIO

def toggle ():
    with open ("mode.txt", "r") as file:
        mode = file.read()
    if (mode == "True"):
        GPIO.output(21, GPIO.HIGH)
    else:
        GPIO.output(21, GPIO.LOW)
    
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

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

while True:
    if (check()):
        s3 = boto3.resource("s3")
        print("Zmienilo sie\t", datetime.now())
        s3.meta.client.download_file("light-control-app", "mode.txt", "mode.txt")
        toggle()
    else:
        print("Nie ma nic nowego", datetime.now())
    sleep(5)