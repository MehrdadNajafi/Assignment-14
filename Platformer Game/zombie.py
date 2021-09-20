import random
import arcade

class Zombie(arcade.AnimatedWalkingSprite):
    def __init__(self, w, h):
        super().__init__()
        self.width = 50
        self.height = 46
        
        self.stand_right_textures = [arcade.load_texture(':resources:images/animated_characters/zombie/zombie_idle.png')]
        self.stand_left_textures = [arcade.load_texture(':resources:images/animated_characters/zombie/zombie_idle.png', mirrored= True)]

        self.walk_right_textures = []
        for i in range(8):
            self.walk_right_textures.append(arcade.load_texture(f":resources:images/animated_characters/zombie/zombie_walk{i}.png"))
        
        self.walk_left_textures = []
        for i in range(8):
            self.walk_left_textures.append(arcade.load_texture(f":resources:images/animated_characters/zombie/zombie_walk{i}.png", mirrored= True))

        
        self.center_x = random.randint((w*1)//5, (w*4)//5)
        self.center_y = h
        self.change_y = 0

        self.speed = 3

        self.change_x = random.choice([-1, 1]) * self.speed