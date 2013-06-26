
import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
KEYBOARD = None
PLAYER = None
CATGIRL = None
######################

GAME_WIDTH = 10
GAME_HEIGHT = 10

#### Put class definitions here ####

class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = True

class Character(GameElement):
    IMAGE = "Horns"
    # IMAGE1 = "Cat"
    # IMAGE2 = "Horns"

    def next_pos(self, direction):
        if direction == "up":
            return (self.x, self.y-1)
        elif direction == "down":
            return (self.x, self.y+1)
        elif direction == "left":
            return (self.x-1, self.y)
        elif direction == "right":
            return (self.x+1, self.y)
        return None

    def __init__(self):
        GameElement.__init__(self)
        self.inventory = [] 
#       GAME_BOARD.draw_msg(str(self.inventory))  make it print the inventory
class Catgirl(Character):
    IMAGE = "Cat"
    SOLID = True
    def interact(self, player):
        GAME_BOARD.draw_msg("Catgirl says find the key to open the door!")

class Gem(GameElement):
    IMAGE = "BlueGem"
    SOLID = False       
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just aquired a gem! You have %d items!"%(len(player.inventory)))

class Key(GameElement):
    IMAGE = "Key"
    SOLID = False
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just aquired a key! You have %d items!"%(len(player.inventory)))


class Closeddoor(GameElement):
    IMAGE = "DoorClosed"
    SOLID = True
    def interact(self, player):
        for item in player.inventory:
            if isinstance(item, Key):
                GAME_BOARD.draw_msg("You have a key!")
                position = (self.x, self.y)
                GAME_BOARD.del_el(self.x, self.y)
                opendoor = Opendoor()
                GAME_BOARD.register(opendoor)
                GAME_BOARD.set_el(position[0],position[1], opendoor)

class Opendoor(GameElement):
    IMAGE = "DoorOpen"
    SOLID = False

class Wall(GameElement):
    IMAGE = "Wall"
    SOLID = True

class Treasure(GameElement):
    IMAGE = "Chest"


####   End class definitions    ####

def initialize():
    rock_positions = [
        (2,1),
        (1,2),
        (5,2),
        (2,3)
        ]

    rocks = []

    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

    rocks[-1].SOLID = False

    for rock in rocks:
        print rock

    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(2,2, PLAYER)
    print PLAYER

   # class Character(object):
    global CATGIRL
    CATGIRL = Catgirl()
    GAME_BOARD.register(CATGIRL)
    GAME_BOARD.set_el(5,2, CATGIRL)

    gem = Gem()
    GAME_BOARD.register(gem)
    GAME_BOARD.set_el(3,1,gem)

    key = Key()
    GAME_BOARD.register(key)
    GAME_BOARD.set_el(4,4,key)

    closeddoor1 = Closeddoor()
    GAME_BOARD.register(closeddoor1)
    GAME_BOARD.set_el(7,3, closeddoor1)

    wall_positions = [
        (6,2),
        (6,3),
        (6,1),
        (8,3)
        ]

    walls = []

    for pos in wall_positions:
        wall = Wall()
        GAME_BOARD.register(wall)
        GAME_BOARD.set_el(pos[0], pos[1], wall)
        #wall.append(wall)

    treasure = Treasure()
    GAME_BOARD.register(treasure)
    GAME_BOARD.set_el(8,1,treasure)



#we don't want to set this yet    

    # GAME_BOARD.draw_msg("This game is wicked awesome.")
    # GAME_BOARD.erase_msg()
    # GAME_BOARD.draw_msg("But it is only getting better from here.")


def keyboard_handler():
    direction = None

    if KEYBOARD[key.UP]:
        direction = "up"
    elif KEYBOARD[key.DOWN]:
        direction = "down"
    elif KEYBOARD[key.RIGHT]:
        direction = "right"
    elif KEYBOARD[key.LEFT]:
        direction = "left"
    # if KEYBOARD[key.SPACE]:
    #   GAME_BOARD.erase_msg
    # else:
    #   GAME_BOARD.draw_msg("Your move, my pretty.")
    if direction:
        next_location = PLAYER.next_pos(direction)
        next_x = next_location[0]
        next_y = next_location[1]

        existing_el = GAME_BOARD.get_el(next_x,next_y)

        if existing_el:
            existing_el.interact(PLAYER)
            
        if existing_el is None or not existing_el.SOLID:
            GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
            GAME_BOARD.set_el(next_x,next_y,PLAYER)



