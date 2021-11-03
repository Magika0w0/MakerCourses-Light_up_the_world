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
    while True:
        for i in range(0,72, 1):
            pixels[i] = (255,0,255)
            pixels[143-i] = (255, 0, 255)
            pixels.show()
            stay(0.01)

        for i in range(0,72, 1):
            pixels[i+72] = (0,0,0)
            pixels[72-i] = (0,0,0)
            pixels.show()
            stay(0.01)


