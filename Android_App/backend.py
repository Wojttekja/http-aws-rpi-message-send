import boto3
import botostubs

on_off = str(input("On?: "))
if (on_off == "True"):
    mode = str(input("Mode: "))
    if (mode == "Static"):
        colour = str(input("Colour: "))
    else:
        colour = ""
else:
    mode = ""
    colour = ""

s3 = boto3.resource("s3")
with open("Android_App/mode.txt", "w") as file:
    file.write(on_off + "\n" + mode + "\n" + colour)
    
s3.Object("light-control-app", "mode.txt").upload_file("Android_App/mode.txt")
