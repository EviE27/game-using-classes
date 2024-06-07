#####################################################################
# Title: Break in game with classes
# Class: CS 30
# Assignemt: game
# Coder: Eve Olson
# version: 1
#####################################################################


#class Keys():

# holds players items they colect in the game
Inventory = []

class Keys():
    """make keys and lock for the game, that the player needs to use to comple
the game."""
    
    def __init__(self, name, type, x, y, key):
        self.name = name
        self.type = type
        self.key = key
        self.x = x
        self.y = y


#Made keys, assigned location, 
silver_key = Keys('silver_key', 'key', 1, 1, None)
golden_key = Keys('gold_key', 'key', 3, 1, None)


# this is the location of the objects

class Locks(Keys):

    
    def __init__(self, name, type, x, y, key, room_open):
        
        self.room_open = room_open
        self.name = name
        self.type = type
        self.key = key
        self.x = x
        self.y = y
    
   
    

#silver_lock = Keys('silver_lock', 'lock', 1, 2, silver_key)
golden_lock = Locks('gold_lock', 'lock', 3, 2, golden_key, False)
silver_lock = Locks('silver_lock', 'lock', 1, 2, silver_key, None)



key_lock_map = [["Nothing", "Nothing", "Nothing", "Nothing"],
                ["Nothing", 'silver_key', "Nothing", 'golden_key'],
                ["Nothing", "silver_lock", "Nothing", "golden_lock"]
    ]

key_map = [["Nothing", "Nothing", "Nothing", "Nothing"],
            ["Nothing", silver_key, "Nothing", golden_key],
            ["Nothing", "silver_lock", "Nothing", "golden_lock"]
]
    
lock_map = [["Nothing", "Nothing", "Nothing", "Nothing"],
            ["Nothing", "Nothing", "Nothing", "Nothing"],
            ["Nothing", 'silver_lock', "Nothing",'golden_lock']
]

        
lock_map1 = [["Nothing", "Nothing", "Nothing", "Nothing"],
            ["Nothing", "Nothing", "Nothing", "Nothing"],
            ["Nothing", silver_lock, "Nothing", golden_lock]
]

 



    
        




    
     


        
    