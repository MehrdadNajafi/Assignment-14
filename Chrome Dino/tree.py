import random
import arcade

class Tree(arcade.Sprite):
    def __init__(self, w):
        super().__init__()
        self.width = 48
        self.height = 95
        self.images = []
        for i in range(3):
            self.images.append(f"images/Cactus/LargeCactus{i+1}.png")
            self.images.append(f"images/Cactus/SmallCactus{i+1}.png")

        self.texture = arcade.load_texture(random.choice(self.images))
    
        self.center_x = w
        self.center_y = 140
        self.change_x = -1
        self.speed = 2
    def move(self, speed):
        self.center_x += self.change_x * speed