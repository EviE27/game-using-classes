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
    
    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.inventory = []
        self.victory = False

    
    def move(self, newx, newy):
        self.x = newx
        self.y = newy
        
'''
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def forward(self):
        self.move(dx=+1, dy=+0)

    def backward(self):
        self.move(dx=-1, dy=+0)

    def up(self):
        self.move(dx=+0, dy=-1)

    def down(self):
        self.move(dx=+0, dy=+1)
'''

    

#if location = object location print object when seached.
#class Search(Player):
    
    
    
    
    
    
        
        
    


