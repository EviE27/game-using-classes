#####################################################################
# Title: Break in game with classes
# Class: CS 30
# Assignemt: game
# Coder: Eve Olson
# version: 1
#####################################################################
# move and seach



#location = map.tile_at(x, y)

class Player():
   
    
    
    def __init__(self):
        self.y = 0
        self.x = 0
        self.inventory = []
        self.victory = False
    

    def move(self, dx, dy):
        self.x += dx
        self.y -= dy

    charactor_position = [0, 0]
    """

    def forward(self):
        self.move(dx=+1, dy=+0)

    def backward(self):
        self.move(dx=-1, dy=+0)

    def up(self):
        self.move(dx=+0, dy=-1)

    def down(self):
        self.move(dx=+0, dy=+1)


    

#if location = object location print object when seached.
#class Search(Player):
    
    
    """
    
    
    
        
        
    


