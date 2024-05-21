#####################################################################
# Title: Break in game with classes
# Class: CS 30
# Assignemt: game
# Coder: Eve Olson
# version: 1
#####################################################################
# move and seach
class Movement():
    #player_position = []
    movement_options = ['f', 'b', 'u', 'd']
    def __init__(self, y, x  ):
        self.y = y
        self.x = x
        self.min_h = 0
        self.max_h = 2
        self.min_w = 0
        self.max_w = 3
        self.victory = False

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
    
        
        
    


