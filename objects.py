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
    def __init__(self, name, type, location, key):
        self.name = name
        self.type = type
        self.location = [None] #idk about his might change back to[x,y]
        self.key = key

    def take(self):
        if self.type == key:
            self.location = None
            my_bag.append(self.name)

#add where house and ofice location 
silver_key = Keys(silver_key, key, [map.Ware_house], None )
gold_key = Keys(gold_key, key, [map.Office], None)
gray_key = Keys(gray_key, key, [map.Side_tile], None)
silver_lock = Keys(silver_lock, lock, [map.Celler], silver_key)
gold_lock = Keys(gold_lock, lock, [map.Celler], gold_key)
gray_lock = Keys(gray_lock, lock, [map.Celler_entrence], gray_key)




class Locks(Keys):
    
    
    def unlocked(self,):
        unlock = False
        if self.type == lock:
            if self.key in player.my_bag():
                unlock = True

        
        

 



    
        




    
     


        
    