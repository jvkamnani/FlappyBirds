import pygame 
import random
PIPE_SCROLL = -60

class Pipe:
    def __init__(self, display_width, display_height):
        self.image = pygame.image.load('D:/Flappy Birds/assets/sprites/pipe.png')
        self.width, self.height = self.image.get_size()
        self.x = display_width
    
    def set_y(self, y):
        self.y = y 
    
    def flip_vertically(self):
        
        self.image = pygame.transform.flip(self.image, False, True)
     
    def render(self, gameDisplay):
        gameDisplay.blit(self.image, (self.x, self.y))
    def update(self, dt):
        self.x = self.x + dt * PIPE_SCROLL
    def check_out_of_bounds(self):
        if self.x + self.width < 0:
            return True