#if case and gold key in inventory = victory
import map
import player

position = player.charactor_posiion
x, y = position
#player_ = player.Player()
   #map_ = map.Map_tile(x=0, y=0, description="")
   #while not player_.victory: 

def play():
   print(player.charactor_posiion)
   print(map.functional_map[x][y].description)
   player_action()


def find_available_action(x, y):
    x, y = position
    x += 0
    y += 0
    map_ = map.Map_tile(x, y, description="")
    actions = {}
    try:
        if player.charactor_posiion[x] < 3:
            action_saver(actions, "F", map_.forward(), "forwards")
           
        if player.charactor_posiion[x] > 0:
            action_saver(actions, "B", map_.backward(), "backward")
        else:
            pass
        if player.charactor_posiion[y] < 2:
            action_saver(actions, "D", map_.down(), "down")
           
        if player.charactor_posiion[y] > 0:
            action_saver(actions, "U", map_.up(), "up")

        return actions
    except:
        pass
    
       
        
def action_saver(action_dic, key, action, name):
    action_dic[key.lower] = action
    print("{}: {}".format(key, name))
      
      
def player_action():
   print("chose action:")
   action = None
   while not action:
      available_action = find_available_action(x, y)
      action_input =input("action: ")
      action = available_action.get(action_input)
   return action
      
   
      
   


    
    
play()
map.map_f.open_map()
map.map_f.read_map()



