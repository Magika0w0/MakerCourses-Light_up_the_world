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
    pixels.fill((0, 0, 255))
    pixels.show()
    stay(2)
    print("team: blue")


def show_green():
    pixels.fill((0, 255, 0))
    pixels.show()
    stay(2)
    print("team: green")


def shut_off():
    pixels.fill((0, 0, 0))
    pixels.show()
    stay(2)


if __name__ == '__main__':

    print("What's the number of players:")
    count = int(input())
    for i in range(count):
        shut_off()
        number = random.randint(1, 90)
        print("Player", i, "will be in ", end='')
        if number > 60:
            show_red()
        elif 30 < number < 60:
            show_green()
        else:
            show_blue()

    shut_off()
