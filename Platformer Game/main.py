import time

import arcade
from player import Player
from ground import Ground, Box
from zombie import Zombie
from goal import Key, Lock, Coin

class Game(arcade.Window):
    def __init__(self):
        self.w = 1000
        self.h = 700
        self.gravity = 0.2
        super().__init__(self.w, self.h, 'keep Yourself Alive!')
        self.texture = arcade.load_texture('images/background.jpg')

        self.key = Key()
        self.lock = Lock(self.w)
        
        self.me = Player(self.w, self.h)
        self.ground_list = arcade.SpriteList()

        for i in range(0, 1000, 85):
            new_ground = Ground(i, 40)
            self.ground_list.append(new_ground)

        for i in range(600, 800, 85):
            new_box = Box(i, 250)
            self.ground_list.append(new_box)

        for i in range(100, 400, 85):
            new_box = Box(i, 450)
            self.ground_list.append(new_box)

        self.zombie_list = arcade.SpriteList()
        self.zombie_physics_engine_list = []

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.me, self.ground_list, self.gravity)

        self.start_time = time.time()

        self.flag = 0
        self.flag_for_game_over = 0
        self.game_over = GameOver(self.w, self.h)

    def on_draw(self):
        arcade.start_render()
        
        if len(self.me.life_list) == 0:
            self.flag_for_game_over = 1
            self.game_over.on_draw(self.me.score)
        
        else:
            arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.texture)
            self.me.draw()
            
            
            try:
                self.key.draw()
            except:
                pass

            try:
                self.lock.draw()
            except:
                pass

            try:
                if self.flag == 1:
                    self.coin.draw()
            except:
                pass
            
            for ground in self.ground_list:
                ground.draw()
            
            for zombie in self.zombie_list:
                zombie.draw()
            
            arcade.draw_text(f"Lives: {self.me.lives}", 10, 10, arcade.color.RED, 20, 20)
            arcade.draw_text(f"Score: {self.me.score}", self.w - 130, 10, arcade.color.WHITE, 20, 20)

    def on_update(self, delta_time: float):
        if self.flag_for_game_over == 1:
            arcade.finish_render()
        
        else:
        
            self.physics_engine.update()
            self.end_time = time.time()

            self.me.update_animation()
            
            for zombie in self.zombie_list:
                zombie.update_animation()

            for zombie in self.zombie_physics_engine_list:
                zombie.update()

            if self.end_time - self.start_time > 2:
                new_zombie = Zombie(self.w, self.h)
                self.zombie_list.append(new_zombie)
                self.zombie_physics_engine_list.append(arcade.PhysicsEnginePlatformer(new_zombie, self.ground_list, self.gravity))
                self.start_time = time.time()
            
            try:    
                if arcade.check_for_collision(self.me, self.key):
                    arcade.play_sound(self.key.sound)
                    self.me.pocket_list.append(self.key)
                    del self.key
            except:
                pass

            try:
                if arcade.check_for_collision(self.me, self.lock) and len(self.me.pocket_list) == 1:
                    self.flag = 1
                    arcade.play_sound(self.lock.sound)
                    self.coin = Coin(self.w)
                    del self.lock
            except:
                pass

            try:
                if arcade.check_for_collision(self.me, self.coin):
                    self.me.score += 1
                    arcade.play_sound(self.coin.sound, 50)
                    del self.coin
                    self.flag = 0
                    self.key = Key()
                    self.lock = Lock(self.w)
                    self.me.pocket_list.clear()
            except:
                pass
            
            for zombie in self.zombie_list:
                if arcade.check_for_collision(self.me, zombie):
                    arcade.play_sound(self.me.hit_sound, 50)
                    self.me.Check_for_lives()
                    self.zombie_list.remove(zombie)

            for zombie in self.zombie_list:
                if zombie.center_x < 0 or zombie.center_x > 1000:
                    self.zombie_list.remove(zombie)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.me.change_x = 1 * self.me.speed

        elif key == arcade.key.LEFT:
            self.me.change_x = -1 * self.me.speed

        elif key == arcade.key.SPACE:
            if self.physics_engine.can_jump():
                self.me.change_y = 10
                arcade.play_sound(self.me.jump_sound)

        elif key == arcade.key.ESCAPE:
            self.game_over.exit_game()


    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.me.change_x = 0

class GameOver(arcade.View):
    def __init__(self, w, h):
        super().__init__()
        self.w = w
        self.h = h
        arcade.set_viewport(0, self.w, 0, self.h)
        self.texture = arcade.load_texture("images/background.jpg")

    def on_draw(self, score = 0):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.texture)
        arcade.draw_text("Game Over", self.w // 2.3, self.h // 2, arcade.color.WHITE, 20, 20)
        arcade.draw_text(f"Score: {score}", self.w // 2.18, self.h // 2.2, arcade.color.WHITE, 16, 16)
        arcade.draw_text("Press 'ESC' to Exit", self.w // 2.3, self.h // 2.35, arcade.color.WHITE, 12, 12)

    def exit_game(self):
        arcade.finish_render()
        arcade.exit()

game = Game()
arcade.run()