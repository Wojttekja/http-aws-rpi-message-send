import sys
import board
import neopixel
from time import sleep

kolor = sys.argv[1]
kolor = kolor.split("-")
kolor = tuple([int(i) for i in kolor])

pixels = neopixel.NeoPixel(board.D18, 50)
for i in range(50):
    pixels[i] = (kolor)