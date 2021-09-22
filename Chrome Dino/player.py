import arcade
from arcade.texture import load_texture

class Player(arcade.AnimatedWalkingSprite):
    def __init__(self):
        super().__init__()
        self.width = 88
        self.height = 90
        
        self.stand_right_textures = []
        for i in range(2):
            self.stand_right_textures.append(load_texture(f"images/Dino/DinoRun{i+1}.png"))

        self.walk_right_textures = []
        for i in range(2):
            self.walk_right_textures.append(load_texture(f"images/Dino/DinoRun{i+1}.png"))
        
        self.center_x = 100
        self.center_y = 90
        self.change_x = 0
        self.change_y = 0
        self.jump_sound = arcade.load_sound(":resources:sounds/jump3.wav")

        self.score = 0
        self.speed = 0

    def move(self): 
        if self.center_x > 100 or self.center_x < 100:
            self.center_x = 100

    # def dino_duck(self):
    #     self.walk_right_textures.clear()
    #     for i in range(2):
    #         self.walk_right_textures.append(load_texture(f"images/Dino/DinoDuck{i+1}.png"))
    #     # self.width = 120
    #     # self.height = 80
        
    # def dino_stand(self):
    #     self.walk_right_textures.clear()
    #     for i in range(2):
    #         self.walk_right_textures.append(load_texture(f"images/Dino/DinoRun{i+1}.png"))
    #     # self.width = 88
    #     # self.height = 90