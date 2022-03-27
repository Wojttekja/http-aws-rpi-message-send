import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 50)
pixels.fill((0, 0, 0))