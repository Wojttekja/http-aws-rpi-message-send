import boto3
from datetime import date, datetime
from time import sleep
import os
import subprocess
import neopixel
import board

def check():
    global nieudane_polaczenia, logi
    s3 = boto3.resource("s3")
    with open("swiatla/last_modified.txt", "r") as file:
        last = file.read()
    last = last.replace("-", "/")
    last = datetime.strptime(last, "%Y/%m/%d %H:%M:%S%z")

    print(datetime.now())
    with open(logi, "a") as file:
        file.write("\n" + str(datetime.now()))
    
    try:
        session = boto3.Session(
                aws_access_key_id='tu access key',
                aws_secret_access_key='tu secrey access key',
            )
        s3 = session.resource('s3')
        now = s3.Object("light-control-app", "mode.txt").__getattribute__("last_modified")
        if (now > last):
            with open("swiatla/last_modified.txt", "w") as file:
                file.write(str(now))
            return True
        nieudane_polaczenia = 0
    except:
        nieudane_polaczenia += 1
        print("Nie udalo sie polaczyc\tnieudane_polaczenia = ", nieudane_polaczenia, end='\t')
        with open(logi, "a") as file:
            file.write("\n" + str(datetime.now()) + "\tNie udalo sie polaczyc")

    return False


def download():
    global logi
    try:
        session = boto3.Session(
        aws_access_key_id='tu access key',
        aws_secret_access_key='tu secrey access key',
        )
        s3 = session.resource('s3')
        s3.Bucket('light-control-app').download_file('mode.txt', 'swiatla/last_mode.txt')
    except:
        print("Nie pobiera sie")
        with open(logi, "a") as file:
            file.write("\n" + str(datetime.now()) + "\tNie pobiera sie")


def which_mode():
    global mode, pixels, logi
    previous_mode = mode
    with open ("swiatla/last_mode.txt", "r") as file:
        mode = file.read().split()
    
    print(mode, previous_mode)
    with open(logi, "a") as file:
        file.write("\n" + str(mode) + " " + str(previous_mode))


    if previous_mode[0] != "static" and previous_mode[0] != "OFF":
        os.system(f"sudo pkill -f {previous_mode[0]}")
    if mode[0] == "OFF":
        pixels.fill((0, 0, 0))
        return
    if len(mode) == 2:
        subprocess.Popen(["sudo", "python", f"swiatla/{mode[0]}.py", mode[1]])
    else:
        subprocess.Popen(["sudo", "python", f"swiatla/{mode[0]}.py"])


# logi - swiatla/logs
logi = f"swiatla/logi/{date.today()}.txt"
with open(logi, "w") as file:
    file.write("nowy start " + str(datetime.now()) + "\n")

nieudane_polaczenia = 0

pixels = neopixel.NeoPixel(board.D18, 50)
with open ("swiatla/last_mode.txt", "r") as file:
    mode = file.read().split()
pixels[0:2] = [(255, 0, 69) for i in range(0, 2)]
sleep(5)
pixels.fill((0, 0, 0))
download()
which_mode()

while True:
    if datetime.now().hour == 21 and datetime.now().minute == 37:
        pixels.fill((255, 0, 63.5))
        sleep(60) 
    if check():
        download()
        which_mode()
    if nieudane_polaczenia == 15:
        print("5 nieudanych polaczen - ledy off")
        with open (logi, "a") as file:
            file.write("\n5 nieudanych polaczen - ledy off")
        with open ("swiatla/last_mode.txt", "w") as file:
            file.write("kolor 0-0-0 ") 
        which_mode()
    if nieudane_polaczenia == 60:
        print("10 nieudanych polaczen - reboot")
        with open (logi, "a") as file:
            file.write("\n10 nieudanych polaczen - reboot")
        os.system("sudo reboot")
    sleep(15)