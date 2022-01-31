import time
import boto3
from datetime import datetime
from time import sleep
import os
import subprocess
import board
import neopixel
    
def check():
    s3 = boto3.resource("s3")
    with open("sterowanie_swiatlem/last_modified.txt", "r") as file:
        last = file.read()
    last = last.replace("-", "/")
    last = datetime.strptime(last, "%Y/%m/%d %H:%M:%S%z")
    session = boto3.Session(
            aws_access_key_id='AKIAZPLFBF74LVKRVSMA',
            aws_secret_access_key='6hOGTaJcH0GGIjlB0HGB7WkA5iot2hkMPkIqzPpw',
        )
    s3 = session.resource('s3')
    now = s3.Object("light-control-app", "mode.txt").__getattribute__("last_modified")
    if (now > last):
        with open("sterowanie_swiatlem/last_modified.txt", "w") as file:
            file.write(str(now))
        return True
    return False


def rozpoznanie():
    with open ("sterowanie_swiatlem/last_mode.txt", "r") as file:
            mode = file.read().splitlines()[0]

    if mode == "rainbow":
        subprocess.Popen(["sudo", "python", "sterowanie_swiatlem/rainbow.py"])
    elif mode == "OFF":
        pixels.fill((0, 0, 0))
    elif mode == "wypelnianie":
        subprocess.Popen(["sudo", "python", "sterowanie_swiatlem/wypelnianie.py"])
    else:
        with open("sterowanie_swiatlem/last_mode.txt", "r") as file:
            kolor = file.read().splitlines()[1]
        static(pixels, kolor)


def static(pixels, kolor):

    if kolor == "red":
        pixels.fill((255, 0, 0))
    elif kolor == "violet":
        pixels.fill((255, 255, 0))
    elif kolor == "green":
        pixels.fill((0, 0, 255))
    elif kolor == "blue":
        pixels.fill((0, 255, 0))
    elif kolor == "white":
        pixels.fill((255, 255, 255))
    elif kolor == "orange":
        pixels.fill((255, 0, 140))
        


# Daj rozpoznawanie do funkcji, bo papiesz
# i zmień warunek, musi być poniżej 21.38
pixels = neopixel.NeoPixel(board.D18, 50)
mode = "es"
rozpoznanie()
while True:
    teura = datetime.now()
    if teura.hour == 21 and teura.minute == 37:
        pixels.fill((255, 0, 63.5))
        sleep(60)
        rozpoznanie()

    if check():
        print("Zmienilo sie\t", datetime.now())
        session = boto3.Session(
            aws_access_key_id='Oj nie nie B)',
            aws_secret_access_key='tym bardziej nie B))',
        )
        s3 = session.resource('s3')
        s3.Bucket('light-control-app').download_file('mode.txt', 'sterowanie_swiatlem/last_mode.txt')
        
        with open ("sterowanie_swiatlem/last_mode.txt", "r") as file:
            mode = file.read().splitlines()[0]
        if mode == "rainbow":
            os.system('sudo pkill -f rainbow')
        elif mode == "wypelnianie":
            os.system("sudo pkill -f wypelnianie")
        
        rozpoznanie()

    else:
        print("Nie ma nic nowego", datetime.now())
    sleep(3)
