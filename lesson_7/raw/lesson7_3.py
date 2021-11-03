import time
import board
import neopixel
import random

# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21

# The number of NeoPixels
num_pixels = 144

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


def stay(number):
    time.sleep(number)


def show_red():
    pixels.fill((255, 0, 0))
    pixels.show()
    stay(2)
    print("team: red")

def show_blue():
    print("team: blue")

if __name__ == '__main__':

    print("What's the number of players:")
    count = int(input())
    for i in range(count):
        number = random.randint(1,100)
        print("Player",i, "will be in", end='')
        if number > 50:
            show_red()

