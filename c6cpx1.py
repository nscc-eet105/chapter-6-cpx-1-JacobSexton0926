import time
import board
import neopixel
import random

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5, auto_write=False)
#I like using this more than the from adafruit_circuitplayground command
pattern = [2, 7, 1, 9, 4, 0, 5, 8, 3, 6]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


while True:
    for pixel in pattern:
        color = random_color()
        pixels[pixel] = color
        pixels.show()
        time.sleep(0.2)
        pixels[pixel] = (0, 0, 0)
        pixels.show()
        time.sleep(0.05)# Write your code here :-)
