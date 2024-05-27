#if case and gold key in inventory = victory
import map
import player

position = player.Player.charactor_position
x, y = position
position = x, y
#player_ = player.Player()
map_ = map.Map_tile(x, y, description="")
 
   #while not player_.victory: 

def play():
   victory = False 
   while not victory:
       print(player.Player.charactor_position)
       print(map.functional_map[x][y].description)
       #find_available_action(x, y)
       player_action()



def action_saver(action_dic, key, action, name):
    action_dic[key.lower()] = action
    print("{}: {}".format(key, name))
    

def find_available_action(x, y):
    x, y = position
    #map_ = map.Map_tile(x, y, description="")
    actions = {}
    
    if player.Player.charactor_position[x] < 3:
        action_saver(actions, "F", map_.forward, "forwards")
       
    if player.Player.charactor_position[x] > 0:
        action_saver(actions, "B", map_.backward, "backward")
    
    if player.Player.charactor_position[y] < 2:
        action_saver(actions, "D", map_.down, "down")
       
    if player.Player.charactor_position[y] >= 1:
        action_saver(actions, "U", map_.up, "up")

    return actions

    
      
def player_action():
    print("chose action:")
    action = None
    while action is None:
        available_action = find_available_action(x, y)
        action_input = input("action: ").upper()
        action = available_action.get(action_input)
        if action is not None:
            if action_input == 'f':
                map_.forward(dx=1 , dy=0)
            elif action_input == 'b':
                map_.backward()
            elif action_input == 'd':
                map_.down()
            elif action_input == 'u':
                map_.up()
        return action
        #else:
           # print("not Valid")


    
    
play()
map.map_f.open_map()
map.map_f.read_map()



