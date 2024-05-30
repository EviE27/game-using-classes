#####################################################################
# Title: Break in game with classes
# Class: CS 30
# Assignemt: game
# Coder: Eve Olson
# version: 1
#####################################################################


#class Keys():
#from map import Celler_entrence
import map


class Keys():
    #port_map = map.Map()
    def __init__(self, name, type, x, key):
        self.name = name
        self.type = type
        self.key = key
        self.x = x
        

    def take(self):
        if self.type == 'key':
            self.location = None
            #my_bag.append(self.name)

#add where house and ofice location
#silver_key = Keys('silver_key', 'key', [map.Ware_house], None )
#golden_key = Keys('gold_key', 'key', [map.Office], None)
gray_key = Keys('gray_key', 'key', (0, 1), None)
#silver_lock = Keys('silver_lock', 'lock', [map.Celler], silver_key)
#golden_lock = Keys('gold_lock', 'lock', [map.Celler], golden_key)
#gray_lock = Keys('gray_lock', 'lock', [map.Celler_entrence], gray_key)

    




class Locks(Keys):
    
    
    def unlocked(self,):
        unlock = False
       # if self.type == lock:
            #if self.key in player.my_bag():
               # unlock = True

        
        

 



    
        




    
     


        
    