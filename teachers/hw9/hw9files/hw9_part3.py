'''
Author: Aaron Taylor Email:tayloa5@rpi.edu

    Purpose:This program asks the user for a battleship board then
    runs a simulation of the game.
'''
class Boat(object):
    def __init__(self,boat): ##initializing the object, dictionary is one of the inputs
        self.name = boat['name']
        self.x = boat['x']
        self.y = boat['y']
        self.length = boat['length']
        self.height = boat['height']
        self.health = boat['health']
    def __str__(self):  ##string representation of the object
        return "%s: (%s,%s,%s,%s) Health: %s" %(self.name.rjust(12),self.x,self.y,self.length,self.height,self.health)
    def check_hit(self,coordinates):  ##checking to see if a player chosen coordinate set is inside the rectangle created with the battlesip's information
        if (coordinates[1] in range(self.x,(self.x+self.length)+1)) and (coordinates[2] in range(self.y,(self.y+self.height)+1)):
            self.health = self.health -1
            print "%s fires (%s, %s) hits" %(coordinates[0],coordinates[1],coordinates[2]),"%s: (%s,%s,%s,%s) Health: %s" %(self.name.rjust(12),self.x,self.y,self.length,self.height,self.health)
        if self.health <= 0:
            print "%s is sinking!" %(self.name)
        else:
            return 
    def check_health(self):
        if self.health == 0:
            return "%s is sinking!" %(self.name)
        else:
            return self.health
            

if __name__ == '__main__':
    fname = raw_input("Enter file name => ")
    print fname
    fname = open(fname)
    allships = [] ##list of dictionaries of ships and their information
    pmoves = [] ## lists of player coordinate choices
    number_of_ships = 0 ##number of ships from file
    for ship in fname: ##for every line in the file
        ships = {}  ##new dictionary
        ship = ship.strip().split("|")  ##splitting the line,"ship" is now a list
        if len(ship) > 3: ##lines with this length are ones with battleship information
            ships['name'] = ship[0]  ##each element of the list is now turned into a dictionary key
            ships['x'] = int(ship[1])
            ships['y'] = int(ship[2])
            ships['length'] = int(ship[3])
            ships['height'] = int(ship[4])
            ships['health'] = int(ship[5])
            allships.append(ships)  ##adding the new dictionary to "allships"
        elif 1 < len(ship) < 4:  ## lines with this length are player moves
            coordinates = [ship[0],int(ship[1]),int(ship[2])] ##[player,x,y]
            pmoves.append(coordinates)  ##adding each list ot the list "pmoves"
        else:
            number_of_ships = int(ship[0])
    shipobjects = [] ##list of ship objects
    for i in range(len(allships)): ##looking at every battleship dictionary
        boat = Boat(allships[i])  ##turning the dictionary into an object
        shipobjects.append(boat)
    for battleship in shipobjects:  ##printing the battleships
        print battleship
    player = " " ##will be used when simulation is over and winner needs to be displayed
    fallen_ships = []  ##list of ships whose health have reached 0
    for move in pmoves:  ##looping through the list of moves
        player = move[0]          
        for n in range(number_of_ships): 
            if shipobjects[n].health < 0: ##if ships' health is negative,skip it
                continue
            elif shipobjects[n].health > 0:
                shipobjects[n].check_hit(move)  ##checking if a ship has been hit
                shipobjects[n].check_health()   ##checking the ship's health 
            elif shipobjects[n].health == 0: ##if a ship's health reaches 0,it will be added to the list "fallen_ships"
                fallen_ships.append(shipobjects[n]) 
    if len(fallen_ships) == 0:  ##printing "No winners" if no ships have fallen after the simulation has finished
        print "No player won!."
    else:
        print player,"wins!"  ##printing the winner of the simulation