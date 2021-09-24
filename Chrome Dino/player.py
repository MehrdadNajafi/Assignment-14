import arcade

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()
        
        self.texture = arcade.load_texture("images/Dino/DinoStand.png")

        self.width = 88
        self.height = 94
        
        self.center_x = 100
        self.center_y = 150
        self.change_y = 0
        
        self.jump_sound = arcade.load_sound(":resources:sounds/jump3.wav")
        
        self.score = 0

        try:
            myfile = open('Score.txt', 'r')
            self.high_score = float(myfile.read())
            myfile.close()

        except:
            self.high_score = 0

    def move(self):
        if self.center_x < 100 or self.center_x > 100:
            self.center_x = 100
    
    def write_high_score(self):
        myfile = open('Score.txt', 'w')
        myfile.write(str(self.score))
        myfile.close()

    def reset_high_score(self):
        myfile = open('Score.txt', 'w')
        myfile.write('0')
        myfile.close()