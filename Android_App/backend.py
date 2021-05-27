import boto3
import botostubs
while True:
    on_off = str(input("On?: "))
    if (on_off == "True"):
        on_off = True
    else:
        on_off = False

    s3 = boto3.resource("s3")
    with open("Android_App/mode.txt", "w") as file:
        file.write(str(on_off))
        
    s3.Object("light-control-app", "mode.txt").upload_file("Android_App/mode.txt")
