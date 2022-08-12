from cgitb import text
import pygame
import random
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_power_ups(self, points):
        if len(self.power_ups) == 0:
            if self.when_appears == points:
                self.when_appears = random.randint(self.when_appears + 200, self.when_appears + 300)
                self.power_ups.append(Shield())
   # else: 
        # self.power_ups.append(Hammer())

        if len(self.power_ups) == 1:
            if self.when_appears == points:
                self.when_appears = random.randint(self.when_appears + 300, self.when_appears + 400)
                self.power_ups.append(Hammer())


    def update(self, points, game_speed, player):
        self.generate_power_ups(points)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.shield = True
                player.show_text = True
                player.type = power_up.type
                time_random = random.randint(5, 8)
                player.shield_time_up = power_up.start_time +(time_random *1000)
                self.power_ups.remove( power_up)

    def update_new(self, points, game_speed, player):
        self.generate_power_ups(points)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.hammer = True
                player.show_text = True
                player.type = power_up.type
                time_random = random.randint(5, 8)
                player.hammer_time_up = power_up.start_time +(time_random *1000)
                self.power_ups.remove( power_up)


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)

    
