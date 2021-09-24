import time
import random

import arcade
from player import Player
from ground import Ground
from tree import Tree
from bird import Bird

class Game(arcade.Window):
    def __init__(self):
        self.w = 1100
        self.h = 600
        super().__init__(self.w, self.h, 'Chrome Dino')
        self.gravity = 0.5
        self.background = arcade.set_background_color(arcade.color.WHITE)
        self.speed = 5

        self.grounds_list = arcade.SpriteList()
        self.grounds_list.append(Ground(0, 85))

        self.me = Player()
        self.trees_list = arcade.SpriteList()
        self.sleep_for_tree = random.randint(1,4)
        self.bird_list = arcade.SpriteList()
        self.sleep_for_bird = random.choice([12, 18])
        self.flag_for_tree = 0

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.me, self.grounds_list, self.gravity)


        self.t1 = time.time()
        self.time_for_score = time.time()
        self.time_for_bird = time.time()

        self.time_for_day = time.time()
        self.count = 0
        self.flag_for_day = 0

        self.game_over = GameOver(self.w, self.h)
        self.flag_for_exit = 0
        self.flag_for_reset_score = False
        
    def on_draw(self):
        arcade.start_render()
        if self.flag_for_exit == 1:
            self.game_over.on_draw(self.me.score)
        
        else:
            self.t2 = time.time()
            
            if int(self.me.score % 20) == 0 and self.t2 - self.time_for_day > 20:
                self.flag_for_day = 1
                self.time_for_day = time.time()
            
            if self.flag_for_day == 1:
                if self.count % 2 == 0:
                    self.background = arcade.set_background_color(arcade.color.BLACK)
                else:
                    self.background = arcade.set_background_color(arcade.color.WHITE)
                self.count += 1
                self.flag_for_day = 0
            
            arcade.draw_text(f"Score: {self.me.score:.2f}", self.w - 120, self.h - 50, arcade.color.GREEN, 12, 12)
            arcade.draw_text(f" High Score: {self.me.high_score:.2f}", self.w - 300, self.h - 50, arcade.color.GREEN, 12, 12 )

            self.me.draw()

            for ground in self.grounds_list:
                ground.draw()

            for tree in self.trees_list:
                tree.draw()

            for bird in self.bird_list:
                bird.draw()

    def on_update(self, delta_time: float):
        if self.flag_for_exit == 1:
            if self.flag_for_reset_score:
                self.me.reset_high_score()
            else:    
                if self.me.score > self.me.high_score:
                    self.me.write_high_score()

            arcade.finish_render()
        
        else:
            self.t2 = time.time()
            self.physics_engine.update()
            self.me.move()

            for bird in self.bird_list:
                bird.update_animation()
            
            self.me.score = time.time() - self.time_for_score

            if len(self.bird_list) > 0:
                self.flag_for_tree = 1
            else:
                self.flag_for_tree = 0
                
            
            if self.flag_for_tree == 0:
                if self.t2 - self.t1 > self.sleep_for_tree:
                    new_tree = Tree(self.w)
                    self.trees_list.append(new_tree)
                    self.t1 = time.time()
                    self.sleep_for_tree = random.randint(1,4)
            else:
                pass

            if self.me.score > 30:
                if self.t2 - self.time_for_bird > self.sleep_for_bird:
                    new_bird = Bird(self.w)
                    self.bird_list.append(new_bird)
                    self.time_for_bird = time.time()
                    self.sleep_for_bird = random.choice([12, 18])

            for tree in self.trees_list:
                if arcade.check_for_collision(self.me, tree):
                    self.flag_for_exit = 1

            for bird in self.bird_list:
                if arcade.check_for_collision(self.me, bird):
                    self.flag_for_exit = 1

            for bird in self.bird_list:
                if bird.center_x < 0:
                    self.bird_list.remove(bird)


            for ground in self.grounds_list:
                if ground.center_x < 0 and len(self.grounds_list) < 2:
                    new_ground = Ground(2404, 85)
                    self.grounds_list.append(new_ground)


            for ground in self.grounds_list:
                if ground.center_x < (-2404):
                    self.grounds_list.remove(ground)

            self.speed += 0.005

            for tree in self.trees_list:
                tree.move(self.speed)

            for ground in self.grounds_list:
                ground.move(self.speed)

            for bird in self.bird_list:
                bird.move(self.speed)

            for tree in self.trees_list:
                if tree.center_x < 0:
                    self.trees_list.remove(tree)
            
    def on_key_press(self, key, modifiers: int):
        if key == arcade.key.SPACE:
            if self.physics_engine.can_jump():
                self.me.texture = arcade.load_texture("images/Dino/DinoRun1.png")
                self.me.change_y = 12
                arcade.play_sound(self.me.jump_sound, 5)

        elif key == arcade.key.DOWN:
            self.me.texture = arcade.load_texture('images/Dino/DinoDuck1.png')
            self.me.width = 118
            self.me.height = 60

        if key == arcade.key.R:
            self.flag_for_reset_score = True

        elif key == arcade.key.ESCAPE:
            self.game_over.exit_game()
            

    def on_key_release(self, key, modifiers: int):
        self.me.texture = arcade.load_texture('images/Dino/DinoStand.png')
        self.me.width = 88
        self.me.height = 94
class GameOver(arcade.View):
    def __init__(self, w, h):
        super().__init__()
        self.w = w
        self.h = h
        arcade.set_viewport(0, w, 0, h)

    def on_draw(self, score):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)
        arcade.draw_text("Game Over", self.w // 2.3, self.h // 2, arcade.color.BLACK, 20, 20)
        arcade.draw_text(f"Score: {score:.2f}", self.w // 2.25, self.h // 2.2, arcade.color.BLACK, 16, 16)
        arcade.draw_text("Press 'R' for reset the High Score", self.w // 2.3, self.h // 2.4, arcade.color.BLACK, 12, 12)
        arcade.draw_text("Press 'ESC' to Exit", self.w // 2.3, self.h // 2.6, arcade.color.BLACK, 12, 12)

    def exit_game(self):
        arcade.finish_render()
        arcade.exit()



game = Game()
arcade.run()