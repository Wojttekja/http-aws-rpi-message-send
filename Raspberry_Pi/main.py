import boto3
import botostubs
from datetime import datetime
from time import sleep


def check ():
    s3 = boto3.resource("s3")
    with open("Raspberry_Pi/last_modified.txt", "r") as file:
        last = file.read()
    last = last.replace("-", "/")
    last = datetime.strptime(last, "%Y/%m/%d %H:%M:%S%z")
    now = s3.Object("light-control-app", "mode.txt").__getattribute__("last_modified")
    if (now > last):
        with open("Raspberry_Pi/last_modified.txt", "w") as file:
            file.write(str(now))
        return True
    return False
    

if (check()):
    s3 = boto3.resource("s3")
    s3.meta.client.download_file("light-control-app", "mode.txt", "Raspberry_Pi/mode.txt")
    print("pobralem")
else:
    print("Nie ma nic nowego")
