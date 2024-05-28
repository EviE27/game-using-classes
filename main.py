#if case and gold key in inventory = victory
import map
import player

Dora = player.Player(0, 0)
port = map.Map('map.txt', map.port_map, 4, 3)
object = objects.Keys(location)

def play():
   victory = False 
   while not victory:
       print(Dora.x, Dora.y)
       print(port.map[Dora.x][Dora.y].description)
       #find_available_action(x, y)
       player_action(Dora, port)



def action_saver(key, name):
    print("{}: {}".format(key, name))
    

def find_available_action(Char, Map):
    if Char.x < Map.map_width:
        action_saver("F", "forward")
    if Char.x > 0:
        action_saver("B", "backward")
    if Char.y < 2:
        action_saver("D",  "down")
    if Char.y >= 1:
        action_saver("U", "up")
    
      
def player_action(Char, Map):
    print("chose action:")
    action = True
    while action:
        find_available_action(Char, Map)
        action_input = input("action: ").upper()
        if action_input == 'F':
            if Char.x < 3:
                    Char.move(Char.x+1, Char.y)
                    action = False
        elif action_input == 'B':
            if Char.x > 0:
                Char.move(Char.x-1, Char.y)
                action = False
        elif action_input == 'D':
            if Char.y < 2:
                Char.move(Char.x, Char.y + 1)
                action = False
        elif action_input == 'U':
            if Char.y >= 1:
                Char.move(Char.x, Char.y-1)
                action = False


def seach(Char):
    if Dora = 
    
    
    
play()
port.open_map()
port.read_map()



