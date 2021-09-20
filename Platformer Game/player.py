import arcade

class Player(arcade.AnimatedWalkingSprite):
    def __init__(self, w, h):
        super().__init__()
        self.width = 50
        self.height = 46
        
        self.stand_right_textures = [arcade.load_texture(':resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png')]
        self.stand_left_textures = [arcade.load_texture(':resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png', mirrored= True)]

        self.walk_right_textures = []
        for i in range(8):
            self.walk_right_textures.append(arcade.load_texture(f':resources:images/animated_characters/male_adventurer/maleAdventurer_walk{i}.png'))

        self.walk_left_textures = []
        for i in range(8):
            self.walk_left_textures.append(arcade.load_texture(f":resources:images/animated_characters/male_adventurer/maleAdventurer_walk{i}.png", mirrored= True))

        self.center_x = w // 2
        self.center_y = h
        self.change_x = 0
        self.change_y = 0
        
        self.speed = 3.5

        self.life_list = ["❤"] * 3
        self.lives = '❤' * len(self.life_list)

        self.score = 0

        self.hit_sound = arcade.load_sound(':resources:sounds/hit5.wav')
        self.jump_sound = arcade.load_sound(":resources:sounds/jump3.wav")

        self.pocket_list = []

    def Check_for_lives(self):
        if len(self.life_list) > 0:
            del self.life_list[-1]
            self.lives = '❤' * len(self.life_list)