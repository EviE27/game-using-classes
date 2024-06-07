#if case and gold key in inventory = victory
import sys
from os import name
import map
import objects
import player

# tempary inventory
inventory = []
room_True = []
# reasigning imported code to use it in main
key_map = objects.key_lock_map
key_map1 = objects.key_map
lock_map = objects.lock_map
lock_map1 = objects.lock_map1
Dora = player.Player(0, 0)
port = map.Map('map.txt', map.port_map, 4, 3)
key_locks = objects.Keys('key_lock','key', 0, 0, objects.key_lock_map)
locks_ = objects.Locks('key_lock','lock', 0, 0, objects.lock_map, room_True)


def play():
    """main code that keeps runing until the player finds the plans"""
    victory = False
    while not victory:
        # prints player location
        #print(Dora.x, Dora.y)
        #orint the description of the players location
        print(port.map[Dora.x][Dora.y].description)
        #move_inventory()
        #asks player what action they want to complete
        player_action(Dora, port)
# can do if room loction  = whatever print map
        
# organizie the actions and how they print
def action_saver(key, name):
    print("{}: {}".format(key, name))


def find_available_action(Char, Map):
    """ decides what option the player gets. if the conditions are met then
that option is maded and avaliable option """
    #temp is a value that will be chaged when a task is compledted
    # this lets the player move to a new part of the map
    
    temp = 2
    if  room_True == ['good']:
        temp =+ 3
    if Char.x >= 0 and Char.x < temp:
        action_saver("F", "forward")
    if Char.x > 0:
        action_saver("B", "backward")
    if Char.y < 2:
        action_saver("D",  "down")
    if Char.y > 0:
        action_saver("U", "up") 
    # if the lock map says there is a lock the unlock function will be added
    if lock_map[Char.x][Char.y] == 'silver_lock':
            action_saver("L", "unlock")
    if lock_map[Char.x][Char.y] == 'golden_lock':
        action_saver("L", "unlock")
    # if the key map says there is a key the search function will be added
    if key_map[Char.x][Char.y] == 'silver_key':
        action_saver("S", "Search")
    if  key_map[Char.x][Char.y] == 'golden_key':
        action_saver("S", "Search")
    #always gives inventory opption and quit
    action_saver("I", "Inventory")
    action_saver("Q", "Quit")
    

def player_action(Char, Map):
    """This askes what the player wants to do for an action"""
    print("chose action:")
    # aslong as action = true this loop will contiue
    action = True
    while action:
        # finds the action the player can complete
        find_available_action(Char, Map)
        action_input = input("action: ").upper()
        # if statments to compleate the actions and action movement
        if action_input == 'F':
            if Char.x != 2:
                Char.move(Char.x + 1 , Char.y)
                action = False
            else:
                pass
        elif action_input == 'B':
            if Char.x > 0:
                Char.move(Char.x - 1, Char.y)
                action = False
        elif action_input == 'D':
            if Char.y < 2 :
                Char.move(Char.x, Char.y + 1)
                action = False
        elif action_input == 'U':
            if Char.y >= 0 and Char.x >= 0 :
                Char.move(Char.x, Char.y - 1)
                action = False
        #opens inventory
        elif action_input == 'I':
            print(inventory)
        #if player wants to quit then they can quit
        elif action_input == 'Q':
            sys.exit("Thank you for playing")
        elif action_input == 'S':
       #if the map says theres nothing, then search will not be a option
            if key_map[Char.x][Char.y] != 'Nothing':
                print("")
                search(Dora)
        elif action_input == 'L':
        #if the map says theres nothing, then unlock will not be a option
            if lock_map1[Char.x][Char.y] != 'Nothing':
                unlock(Dora)
            else:
                pass
                

def search(Char):
    """prints object if there is one in the room and allows player to pick it up"""
    try:
        if inventory == []:
            if key_map1[Char.x][Char.y].type == 'key':
                print("there is a ")
                print(key_map1[Dora.x][Dora.y].name)
                print("do you want to pick this up, type yes or no:")
                pickup = input(":")
                if pickup == "yes":
                    inventory.append(key_map1[Dora.x][Dora.y].name)
                    move_inventory()
                else:
                    pass
            else:
                print("nothing here to seach")
        else:
            print("you have found everything")
    except ValueError:
        print("nothing to seach")
        pass
    finally:
        print("keep up the good work!")
    

def unlock(Char):
    if inventory == ['silver_key']:
        print(lock_map1[Char.x][Char.y].name)
        unlock_ = input("Do you want to unlock this, type yes or no:")
        if unlock_ == 'yes':
            print("you have disabled the lazors you can now get the plans")
            room_True.append('good')
            inventory.remove('silver_key')
    elif inventory == ['golden_key']:
        print(lock_map1[Char.x][Char.y].name)
        unlock__ = input("Do you want to unlock this, type yes or no:")
        if unlock__ == 'yes':
            print("You got the plans!!! mission accomplished!")
            sys.exit("Thank you for playing")
            
    else:
        print("you found",  lock_map1[Char.x][Char.y].name )
        print("you cant unlock this yet")
            


def move_inventory():
    objects.Inventory = inventory
    print(objects.Inventory)


play()
port.open_map()
port.read_map()



