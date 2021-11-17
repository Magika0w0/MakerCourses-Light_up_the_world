import random

def two_color_rotate(team1, team2):
    print(team1, team2)

if __name__ == '__main__':

    team_red_color = (255, 0, 0)
    team_green_color = (0, 255, 0)
    team_blue_color = (0, 0, 255)

    teams = [team_red_color, team_blue_color, team_green_color]
    random.shuffle(teams)

    for team1 in teams:
        for team2 in teams:
            if not team1 == team2:
                two_color_rotate(team1, team2)
                temp = input()
                print(temp)
