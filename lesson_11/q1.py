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

def two_color_rotate(color1, color2):

    for i in range(num_pixels):
        pixels.fill(color1)
        for j in range(num_pixels // 2):
            if i + j < num_pixels:
                pixels[i + j] = color2
            else:
                pixels[i + j - num_pixels] = color2

        pixels.show()
        stay(0.05)
if __name__ == '__main__':

    red = (255, 0, 0)
    orange = (255, 175, 0)
    yellow = (255, 255, 0)
    green = (0, 255, 0)
    cyan = (0, 255, 255)
    blue = (0, 0, 255)
    magenta = (255, 0, 255)
    rainbow = (red, orange, yellow, green, cyan, blue, magenta)

    while True:
        for i in range(144):
            pixels[i] = (i, i ,0)
            pixels.show()
            stay(0.05)
        for i in range(144):
            pixels[i] = (0, 0 ,0)
            pixels.show()
            stay(0.05)