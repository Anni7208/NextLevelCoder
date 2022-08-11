import random
from dino_runner.components.obstacles.obstacle import Obstacle
from ...utils.constants import LARGE_CACTUS



class Cactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 325
        #self.rect.y.append(Cactus(LARGE_CACTUS))
        #if super().__init__(image, self.type) == LARGE_CACTUS:
         #self.rect.y = 300
        #super().__init__(LARGE_CACTUS, self.type)
        #self.rect.y = 300
        
class Large_Cactus(Obstacle):   
    def __init__(self, image):
      self.type = random.randint(0,2)
      super().__init__(image, self.type)
      self.rect.y = 300
        