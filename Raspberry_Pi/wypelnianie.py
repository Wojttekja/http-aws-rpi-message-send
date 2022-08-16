import board
import neopixel
import statistics
from time import sleep
#kolory = [[148, 211, 0], [75, 130, 0], [0, 255, 0],[255, 255, 255], [0, 0, 255], [255, 0, 255], [255, 0, 127], [255, 0, 0]]
kolory = [[148, 211, 0], [111.5, 170.5, 0], [75, 130, 0], [37.5, 192.5, 0], [0, 255, 0], [127.5, 255, 127.5], [255, 255, 255], [127.5, 127.5, 255], [0, 0, 255], [127.5, 0, 255], [255, 0, 255], [255, 0, 191], [255, 0, 127], [255, 0, 63.5], [255, 0, 0]]
pixels = neopixel.NeoPixel(board.D18, 50)

while True:
    for i in kolory:
        for j in range(50):
            pixels[j] = i
            sleep(0.1)

"""kolory2 = []
for i in range(len(kolory)-1):
    kolory2.append([statistics.mean([kolory[i][0], kolory[i+1][0]]), statistics.mean([kolory[i][1], kolory[i+1][1]]), statistics.mean([kolory[i][2], kolory[i+1][2]])])

#print(kolory2)
nowe = []
for i in range(len(kolory2)):
    nowe.append(kolory[i])
    nowe.append(kolory2[i])

nowe.append(kolory[len(kolory)-1])
print(nowe)"""