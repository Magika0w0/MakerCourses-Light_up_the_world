import time
import board
import neopixel

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


if __name__ == '__main__':
    red = (255, 0, 0)
    orange = (255, 175, 0)
    yellow = (255, 255, 0)
    green = (0, 255, 0)
    cyan = (0, 255, 255)
    blue = (0, 0, 255)
    magenta = (255, 0, 255)
    white = (255, 255, 255)
    black = (0, 0, 0)
    rainbow = (red, orange, yellow, green, cyan, blue, magenta, white,black)

    while True:
        for color in rainbow:
            pixels.fill(color)
            pixels.show()
            stay(0.5)

