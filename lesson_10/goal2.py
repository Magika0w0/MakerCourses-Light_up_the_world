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


def initial_strip():
    pixels.fill((0, 0, 0))
    pixels.show()
    stay(1)

def two_color_rotate(color1, color2):
    while True:
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
    team_red_color = (255, 0, 0)
    team_green_color = (0, 255, 0)
    team_blue_color = (0,0,255)

    teams = [team_red_color, team_blue_color, team_green_color]

    team1 = random.choice(teams)
    teams.remove(team1)
    team2 = random.choice(teams)
    two_color_rotate(team1, team2)


