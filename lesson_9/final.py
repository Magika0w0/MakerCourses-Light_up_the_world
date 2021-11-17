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
    print("team: red")
    pixels.fill((255, 0, 0))
    pixels.show()
    stay(2)


def show_blue():
    print("team: blue")
    pixels.fill((0, 0, 255))
    pixels.show()
    stay(2)


def show_green():
    print("team: green")
    pixels.fill((0, 255, 0))
    pixels.show()
    stay(2)


def initial_strip():
    pixels.fill((0, 0, 0))
    pixels.show()
    stay(1)

if __name__ == '__main__':

    players = ["xiaohong", "xiaolan", "xiaoming"]
    team_red = []
    team_blue = []
    team_green = []
    saved_players = players.copy()

    while len(players) > 0:
        current_player = random.choice(players)
        players.remove(current_player)
        team_red.append(current_player)

        current_player = random.choice(players)
        players.remove(current_player)
        team_blue.append(current_player)

        current_player = random.choice(players)
        players.remove(current_player)
        team_green.append(current_player)

    for player in saved_players:
        if player in team_red:
            show_red()
            print("player", player, "is in team red")
        elif player in team_blue:
            show_blue()
            print("player", player, "is in team blue")
        else:
            show_green()
            print("player", player, "is in team green")

    print("now team red:", team_red)
    print("now team blue:", team_blue)
    print("now team green:", team_green)
    print("remaining people:", players)
    initial_strip()