from email import message
from turtle import screensize
import pygame
from dino_runner.components.dinosaurs import Dinosaurs
from dino_runner.components.obstacles.obstacles_manager import ObstcacleManager
from dino_runner.components.power_ups.powe_up_manager import PowerUpManager
from dino_runner.utils.constants import BG, ICON, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.utils.text_utils import  draw_message_componet


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Dinosaurs()
        self.obstacle_manager = ObstcacleManager()
        self.power_up_manager = PowerUpManager()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        
        self.points= 0
        self.death_count = 0

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
            
        pygame.display.quit()
        pygame.quit()

        

    def run(self):
        # Game loop: events - update - draw
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.playing = True
        self.game_speed = 20
        self.points = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.update_score()
        user_input = pygame.key.get_pressed()
        ##user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.player.check_invencibility(self.screen)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)
    
    #def update_score(self):
        #self.points.reset.update_score()
     #   number_of_points = True
      #  while self.death_count > 0 :
       #     self.draw_score()


     
        #self.points += 1
        #if self.points % 100 == 0:
          #  self.game_speed += 20

      

        
    def update_death(self):
        self.death_count += 1
        if self.death_count > 0:
            self.death_count()
        
    ##def new_score(self):
      #  if self.death_count > 0:
       #     self.points += 1
        #if self.points % 100 == 0:
         #   self.game_speed += 20
    
       # pass
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_score()
        self.draw_background()
        self.player.draw(self.screen)
        self.player.check_invencibility(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed


    def draw_score(self):
        draw_message_componet(
            f'POINTS: {self.points}'
            self.screen,
            font_size = 22,
            pos_x_center = 1000,
            pos_y_center = 50

        )
           # font = pygame.font.Font(FONT_STYLE, 22)
            #text = font.render(f'Points : {self.points}', True, (0,0,0))
            #text_rect = text.get_rect()
            #text_rect.center = (1000, 50)
            #self.screen.blit(text, text_rect)  

    def new_text(self, font,size, message, widht, height):
            font = pygame.font.Font( 22)#FONT STYLE
            text = font.render(message, True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (widht, height)
            self.screen.blit(text, text_rect)


    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                
            if event.type == pygame.KEYDOWN:
                self.run()


    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT //2
        half_screen_width = SCREEN_WIDTH //2
        

        if self.death_count == 0:
           draw_message_componet('Press any key to start', self.screen)
        elif self.death_count > 0:
            draw_message_componet('Press any key to splay again', self.screen)
            draw_message_componet(
                f'POINTS: {self.points}'
                self.screen,
                pos_y_center = half_screen_height + 50
            
            ):
            draw_message_componet(
                f'NUMBER DEATHS: {self.death_count}'
                self.screen,
                pos_y_center = half_screen_height + 100
            
            ):
            # puntos actuales y numero de muertes
        self.screen.blit(RUNNING[0], (half_screen_width - 20, half_screen_height -140))

        pygame.display.update()
        self.handle_key_events_on_menu()
        


