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


block = int(144/4)
if __name__ == '__main__':
    while True:
        for q in range(0, 3, 1): # q = 1
            for i in range(0, 144, 3):
                pixels[i+q] = (255, 0, 255) # A
                pixels.show()
                stay(0.1)

            for i in range(1, 142, 3):
                pixels[i+q] = (0, 255, 255) # B
                pixels.show()
                stay(0.1)

            for i in range(2, 141, 3):
                pixels[i+q] = (0, 255, 0) # C
                pixels.show()
                stay(0.1)

            for i in range(0, 144, 3):
                pixels[i + q] = (0, 0, 0)
                pixels.show()
                stay(0.1)
