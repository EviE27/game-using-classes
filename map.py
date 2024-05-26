from tabulate import tabulate

import player


class Map_tile:
    
    def __init__(self, x, y, description):
        self.x = x
        self.y = y
        self.description = description 


    def move(self, dx, dy):
        self.x =+ dx
        self.y =- dy
    
    def forward(self):
        self.move(dx=+1, dy=+0)
    
    def backward(self):
        self.move(dx=-1, dy=+0)
    
    def up(self):
        self.move(dx=+0, dy=-1)
    
    def down(self):
        self.move(dx=+0, dy=+1)

    def location_(self):
        player.charactor_posiion.append([self.x][self.y])
        


        
    
Start_tile = Map_tile(0, 0,"""You have been hierd to break into the the enemy base.
Your goal is to steal their plans on how they are going to take over the city.
Get the plans and excape on the boat at the docs without triping any allarms
or getting caught. You will be given action option type the corosponing letter 
and hit enter to compleat the action 

                 You have arived at the enemys base.
                 The base is a lager whear house by the docks """ )


Side_tile = Map_tile(1, 0, """You have made your way down the side of the building.
                There are wooden shiping crates scaderd around.
        On the side of the building there is the entrenc door that has adirty window.
                On the ground there is a gray key. 
                """)

Celler_entrence = Map_tile(0, 2, """You are at the front of the whear house.
You see somthing stiking out from under a tarp.
You pull the taro off the revel trap door with a number lock on it""")

Celler = Map_tile(1, 2, """You found the Celler. 
              The cold stone walls and dim lighting make it look like a dungen. 
              There is a table with a case on it that has the PLANS writen on it.
              The table is on the other side of a lazor wall.
              If you touch the lazor you will set of the allarm.
              You see a braker box. Maybe thats what is powering
              the lazors, the lock is silver.""")

#silver key
Ware_house = Map_tile(1, 1,"""The ware house is dim and full of wooden crates.""")

Office = Map_tile(2, 1, """You enter the office. 
There is a large wooden desk and lots of filling cabnets in the room.""")

empty = Map_tile(None, None, "There is nothing here" )



functional_map = [[Start_tile, Side_tile, empty, empty],
      [empty, Ware_house, empty, Office ],
      [Celler_entrence, Celler, empty, empty]  
      ]


map = [['Start_tile', 'Side_tile', 'empty', 'empty'],
      ['empty', 'Ware_house', 'empty', 'Office' ],
      ['Celler_entrence', 'Celler', 'empty', 'empty']   
      ]
"""
def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return map[x,y]
    except:
        return None

"""
class Map:
   
    def __init__(self, map_file):
        self.map_file = map_file
    def open_map(self):
        try:
            with open(self.map_file, 'w') as file:
                file.write(tabulate(map, tablefmt = "mixed_grid"))
        except:
            print("somthing went wrong")
        else:
            print("you have a map of the wear house")


    def read_map(self):
        try:
            with open(self.map_file, 'r') as file:
                print(file.read())
        except:
            print("somthing went wrong")

map_f = Map('map.txt')





