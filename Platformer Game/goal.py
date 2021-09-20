import random
import arcade


class Key(arcade.Sprite):
    def __init__(self):
        super().__init__(':resources:images/items/keyYellow.png')
        self.width = 100
        self.height = 80
        self.center_x = 160
        self.center_y = 560
        self.sound = arcade.load_sound(":resources:sounds/coin1.wav")

class Lock(arcade.Sprite):
    def __init__(self, w):
        super().__init__(":resources:images/tiles/lockYellow.png")
        self.width = 70
        self.height = 70
        self.center_x = random.randint(50, w - 50)
        self.center_y = 145
        self.sound = arcade.load_sound(":resources:sounds/secret2.wav")

class Coin(arcade.Sprite):
    def __init__(self, w):
        super().__init__(":resources:images/items/gold_1.png")
        self.width = 50
        self.height = 50
        self.center_x = random.randint(50, w - 50)
        self.center_y = 145
        self.coin_flag = 0
        self.sound = arcade.load_sound(":resources:sounds/coin5.wav")