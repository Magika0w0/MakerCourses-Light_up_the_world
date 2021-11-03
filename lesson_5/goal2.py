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


def wheel(pos):
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)


def chase_rainbow(led_number, pixels):
    for j in range(256):
        for q in range(3):
            for i in range(0, led_number, 3):
                pixels[i + q] = wheel((i + j) % 255)
            pixels.show()
            time.sleep(0.05)
            for i in range(0, led_number, 3):
                pixels[i + q] = (0, 0, 0)


def rainbow_flow(led_number, pixels):
    for j in range(256):
        for i in range(led_number):
            pixels[i] = wheel((i + j) % 255)
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
    white = (255, 255, 255)
    rainbow = (red, orange, yellow, green, cyan, blue, magenta, white)

    while True:
        for r in range(0, 255, 1):
            pixels.fill((r, 0 ,0))
            pixels.show()
            stay(0.001)

        for g in range(0, 255, 1):
            pixels.fill((255, g ,0))
            pixels.show()
            stay(0.001)

        for r in range(255, 0, -1):
            pixels.fill((r, 255, 0))
            pixels.show()
            stay(0.001)

        for r in range(255, 0, -1):
            pixels.fill((0, r, 0))
            pixels.show()
            stay(0.001)

