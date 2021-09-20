import arcade

class Ground(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 85
        self.height = 85
        
        self.texture = arcade.load_texture(':resources:images/tiles/grassMid.png')
        
        self.center_x = x
        self.center_y = y

class Box(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 85
        self.height = 85

        self.texture =arcade.load_texture(":resources:images/tiles/grassHalf_mid.png")

        self.center_x = x
        self.center_y = y