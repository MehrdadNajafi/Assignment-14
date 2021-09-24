import arcade

class Bird(arcade.AnimatedWalkingSprite):
    def __init__(self, x):
        super().__init__()
        
        self.walk_left_textures = []
        for i in range(2):
            self.walk_left_textures.append(arcade.load_texture(f"images/Bird/Bird{i+1}.png"))

        self.width = 97
        self.height = 68
        
        self.center_x = x
        self.center_y = 222
        self.change_x = -1
        self.speed = 3
    def move(self, speed):
        self.center_x += self.change_x * self.speed