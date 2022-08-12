import random
from xml.dom.expatbuilder import ElementInfo
import pygame

from ...utils.text_utils import FONT_STYLE
from .bird import Bird
from dino_runner.components.obstacles.cactus import  Cactus, Large_Cactus
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD

class ObstcacleManager:
    def __init__(self):
        self.obstacles = []
        self.choose_cactus =  0


    def update(self,game):
        if len(self.obstacles) == 0:
            self.choose_cactus = random.randint(1, 2)

            if self.choose_cactus == 1:
                self.obstacles.append(Cactus(SMALL_CACTUS)) 
                
            else:
             self.obstacles.append(Large_Cactus(LARGE_CACTUS))

            #else:
            #self.obstacles.append(Bird(BIRD))


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if  not game.player.shield:
                    if not game.player.hammer:
                        pygame.time.delay(500)
                        game.playing =False
                        game.death_count += 1
                else:
                    self.obstacles.remove(obstacle)
                   # game.points = 0
                break

    #def update(self,game):
     #   if len(self.obstacles) == 0:  
      #      self.obstacles.append(Cactus(LARGE_CACTUS))
        #for obstacle in self.obstacles:
       #     obstacle.update(game.game_speed, self.obstacles)
         #   if game.player.dino_rect.colliderect(obstacle.rect):
          #      pygame.time.delay(500)
           #     game.playing =False
            #    break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []


       

