import arcade

class Ground(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.texture = arcade.load_texture("images/Other/Track.png")
        
        self.width = 2404
        self.height = 28
        
        self.center_x = x
        self.center_y = y
        self.change_x = -1

    def move(self, speed):
        self.center_x += self.change_x * speed