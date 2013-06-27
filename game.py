
import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
SAVED_BOARDS = []
DEBUG = False
KEYBOARD = None
PLAYER = None
######################

GAME_WIDTH = 10
GAME_HEIGHT = 10

#### Put class definitions here ####

class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = True

    def interact(self,player):
        position = (self.x, self.y)
        GAME_BOARD.del_el(self.x, self.y)
        gem = Gem()
        GAME_BOARD.register(gem)
        GAME_BOARD.set_el(position[0],position[1], gem)


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
        self.game_level = []

#       GAME_BOARD.draw_msg(str(self.inventory))  make it print the inventory
class Catgirl(Character):           #creating catgirl w character attributes
    IMAGE = "Cat"
    SOLID = True
    def interact(self, player):
        GAME_BOARD.draw_msg("Catgirl says find the key to open the door!")

class Heart(GameElement):
    IMAGE = "Heart"
    SOLID = True
    def interact(self, player):
        counter = 0
        
        GAME_BOARD.draw_msg("heartz n starz")
        position = (self.x, self.y)
        GAME_BOARD.del_el(self.x, self.y)
        heart = Heart()
        GAME_BOARD.register(heart)
        GAME_BOARD.set_el(self.x, (self.y-1), heart)
        counter = counter + 1
        
        while counter < 2: 
            SOLID = True
     #   def interact(self,player):
            # position = (self.x, self.y)
            GAME_BOARD.del_el(self.x, self.y)
            key = Key()
            GAME_BOARD.register(key)
            GAME_BOARD.set_el(position[0],position[1], key)   
            counter += 1


class Gem1(GameElement):
    IMAGE = "OrangeGem"
    SOLID = True
    def interact(self, player):
        GAME_BOARD.draw_msg("Nothing here!")

    def interact(self,player):
            position = (self.x, self.y)
            GAME_BOARD.del_el(self.x, self.y)
            key = Key()
            GAME_BOARD.register(key)
            GAME_BOARD.set_el(position[0],position[1], key)

class Boy(Character):
    IMAGE = "Boy"
    SOLID = True
    def interact(self, player):
        GAME_BOARD.draw_msg("I love you Baby! Muah!!")
        print chr(7) * 2

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
        GAME_BOARD.draw_msg("You just aquired a key! Use it to open the door and get the treasure!")

class Tall_Tree(GameElement):
    IMAGE = "TallTree"
    SOLID = True

class Short_Tree(GameElement):
    IMAGE = "ShortTree"
    SOLID = True


class Closeddoor(GameElement):
    IMAGE = "DoorClosed"
    SOLID = True
    def interact(self, player):
        for item in player.inventory:
            if isinstance(item, Key):
                GAME_BOARD.draw_msg("You have a key!  Open the door!")
                position = (self.x, self.y)
                GAME_BOARD.del_el(self.x, self.y)
                opendoor = Opendoor()
                GAME_BOARD.register(opendoor)
                GAME_BOARD.set_el(position[0],position[1], opendoor)
   

class Opendoor(GameElement):
    IMAGE = "DoorOpen"
    SOLID = False
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just aquired a key! You have %d items!"%(len(player.inventory)))

    # when she goes through the door, gets to a new level.
    #save the old board to Saved Boards list.

class Wall(GameElement):
    IMAGE = "Wall"
    SOLID = True

class Treasure(GameElement):
    IMAGE = "Chest"

    def __init__(self, level):
        GameElement.__init__(self)
        self.level = level

    # Treasures are our portals to new levels
    def interact(self, player):
        # Get the current board
        global SAVED_BOARDS
        #global LEVEL_1
        current_board = GAME_BOARD.save_board(GAME_WIDTH, GAME_HEIGHT)

        # Save the current_board dictionary to our saved boards list
        SAVED_BOARDS.append(current_board)

        # Clear the board display
        GAME_BOARD.clear_board(GAME_WIDTH, GAME_HEIGHT)

        # Populate the board display with the new level
        GAME_BOARD.write_board(SAVED_BOARDS[1])



####   End class definitions    ####

def initialize():
    global PLAYER
    PLAYER = Character()

    GAME_BOARD.draw_msg("Let's have an adventure! Catgirl knows the way!")

    level_0 = {}
    level_0["PLAYER_START"] = 2,2
    level_0[(5,5)] = Rock()
    level_0[(8,6)] = Rock()
    level_0[(2,4)] = Rock()
    level_0[(8,4)] = Rock()

    level_0[(5,2)] = Catgirl()

    #level_0[(4,4)] = Key()

    level_0[(7,3)] = Closeddoor()

    level_0[(3,5)] = Heart()

    level_0[(6,2)] = Wall()
    level_0[(6,3)] = Wall()
    level_0[(6,1)] = Wall()
    level_0[(8,3)] = Wall()

    level_0[(3,7)] = Short_Tree()
    level_0[(4,8)] = Tall_Tree()
    level_0[(5,1)] = Tall_Tree()

    level_0[(8,8)] = Gem1()

    level_0[(8,1)] = Treasure(1)

    level_1 = {}
    level_1["PLAYER_START"] = 2,2

    level_1[(3,1)] = Gem()
    level_1[(5,2)] = Gem()
    level_1[(6,7)] = Gem()

    level_1[(4,4)] = Boy()

    level_1[(2,7)] = Tall_Tree()
    level_1[(3,5)] = Tall_Tree()
    level_1[(8,3)] = Tall_Tree()
#    level_1[(6,7)] = "Green"




    ##TODO:
    Level0 = SAVED_BOARDS.append(level_0)
    Level1 = SAVED_BOARDS.append(level_1)

    print SAVED_BOARDS

    GAME_BOARD.clear_board(GAME_WIDTH, GAME_HEIGHT)
    GAME_BOARD.write_board(SAVED_BOARDS[0])


    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(2, 2, PLAYER)


    ## Save level_0 in saved_boards (here)
    ## Write the board, using GAME_BOARD.write_board() (which looks in the saved_boards array) (here)
    ## Make level 1, store it in a dict the way we did level_0, then store THAT in SAVED_BOARDS (somewhere.)
    

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



