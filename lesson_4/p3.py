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


red = (255, 0, 0)
orange = (255, 175, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
magenta = (255, 0, 255)
rainbow = (red, orange, yellow, green, cyan, blue, magenta)

if __name__ == '__main__':
    red = (255, 0, 0)
    blue = (0, 0, 255)

    while True:
        pixels.fill(red)
        # pixels.fill((255, 0, 0))
        pixels.show()
        stay(0.5)
        pixels.fill(blue)
        pixels.show()
        stay(0.5)


        # for i in range(9, 144, 1):
        #     pixels[i] = red
        #     pixels.show()
        #     stay(0.05)
        #
        # for i in range(144 - 3 - 1, 3, -1):
        #     pixels[i] = red
        #     pixels[i - 3] = green
        #     pixels[i - 6] = blue
        #     pixels[i + 3] = (0, 0, 0)
        #     pixels.show()
        #     stay(0.05)
